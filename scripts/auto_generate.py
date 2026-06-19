"""IDEAS.md 큐에서 글감 1개를 추출해 Claude API로 본문을 생성, _drafts/auto/에 status:ready로 저장.

전제:
    - 환경변수 ANTHROPIC_API_KEY 설정됨
    - pip install anthropic

추출 우선순위 (IDEAS.md의 운영 규칙과 동일):
    1. 트랙 B(트렌드) — 신선도 보존
    2. 트랙 D(논문) — 매일 1건
    3. 트랙 A(자료 모인 것)
    4. 트랙 C(기초)

선정된 글감의 상태가 pending인지 확인 후 작성. 작성 후 IDEAS.md의 해당 행 상태를 "auto-draft 생성됨"으로 갱신하는 것은 후속 hook이 처리(여기선 파일 작성까지만).

사용:
    python scripts/auto_generate.py            # 우선순위에 따라 자동 추출
    python scripts/auto_generate.py --track D  # 특정 트랙 강제
    python scripts/auto_generate.py --slug ... # 특정 슬러그 강제

종료 코드:
    0 — 1편 생성 성공
    2 — 추출할 글감 없음
    1 — 오류 (API 호출 실패 등)
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from anthropic import Anthropic
except ImportError:
    print("[auto_generate] anthropic 패키지가 필요합니다. pip install anthropic", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DRAFTS_AUTO = ROOT / "_drafts" / "auto"
IDEAS = ROOT / "_meta" / "IDEAS.md"
PERSONA = ROOT / "_meta" / "PERSONA.md"
CATEGORIES = ROOT / "_meta" / "CATEGORIES.md"
KST = ZoneInfo("Asia/Seoul")

MODEL = "claude-opus-4-7"


def read_meta() -> tuple[str, str, str]:
    """IDEAS·PERSONA·CATEGORIES 본문을 읽어 반환."""
    return (
        IDEAS.read_text(encoding="utf-8"),
        PERSONA.read_text(encoding="utf-8"),
        CATEGORIES.read_text(encoding="utf-8"),
    )


def build_prompt(ideas: str, persona: str, categories: str, track_hint: str | None, slug_hint: str | None) -> str:
    """Claude에게 보낼 프롬프트. 자기가 큐에서 다음 글감을 골라 글을 쓰도록."""
    extra = ""
    if track_hint:
        extra += f"\n반드시 트랙 {track_hint} 안에서 글감을 골라라.\n"
    if slug_hint:
        extra += f"\n반드시 슬러그 `{slug_hint}` 글감으로 작성하라.\n"

    return f"""너는 이 블로그의 작성자다. 아래 운영 문서를 모두 읽고, **글감 큐(IDEAS.md)에서 다음에 작성할 글 1편을 골라 본문을 완성하라.**

선택 우선순위 (IDEAS.md 운영 규칙과 동일):
1. 트랙 B(트렌드) — 신선도 보존
2. 트랙 D(논문) — 매일 1건
3. 트랙 A(자료 모인 것)
4. 트랙 C(기초)

다음 행은 건너뛴다:
- 이미 "초안 작성됨" / "발행됨" 상태인 행
- 트랙 A 중 자료가 아직 안 모인 행
{extra}

출력 형식 — 정확히 다음 두 블록만 출력하라. 다른 설명 금지.

```slug
<선택한 글감의 슬러그>
```

```markdown
---
layout: post
title: "..."
subtitle: "..."   # 선택
categories: [<카테고리 슬러그>]
tags: [...]
toc: true
status: ready
---

<본문>
```

작성 규칙(PERSONA.md 준수):
- 평어체(-다 종결), 1인칭 "나"
- 식별 단서 노출 금지(직업·소속·도메인)
- 트랙 D 논문 리뷰면 6축(모델/파인튜닝/학습/데이터/성능평가/실무 활용) 모두 다룬다
- 분량: 트랙 C 800~2000자, 트랙 B 1500~3500자, 트랙 D 1500~3500자, 트랙 A 2500~5000자

운영 문서:

===== IDEAS.md =====
{ideas}

===== PERSONA.md =====
{persona}

===== CATEGORIES.md =====
{categories}
"""


def call_claude(prompt: str) -> str:
    client = Anthropic()
    msg = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in msg.content if hasattr(b, "text"))


def extract_blocks(text: str) -> tuple[str, str]:
    slug_m = re.search(r"```slug\s*\n(.+?)\n```", text, re.DOTALL)
    md_m = re.search(r"```markdown\s*\n(.+?)\n```", text, re.DOTALL)
    if not slug_m or not md_m:
        raise ValueError(f"응답에서 slug/markdown 블록을 못 찾았다. 응답 앞 500자:\n{text[:500]}")
    return slug_m.group(1).strip(), md_m.group(1).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", choices=["A", "B", "C", "D"], help="특정 트랙 강제")
    ap.add_argument("--slug", help="특정 슬러그 강제")
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("[auto_generate] ANTHROPIC_API_KEY 환경변수가 없다.", file=sys.stderr)
        return 1

    ideas, persona, categories = read_meta()
    prompt = build_prompt(ideas, persona, categories, args.track, args.slug)

    print("[auto_generate] Claude API 호출 중...", flush=True)
    response = call_claude(prompt)

    try:
        slug, markdown = extract_blocks(response)
    except ValueError as e:
        print(f"[auto_generate] 파싱 실패: {e}", file=sys.stderr)
        return 1

    DRAFTS_AUTO.mkdir(parents=True, exist_ok=True)
    dest = DRAFTS_AUTO / f"{slug}.md"
    if dest.exists():
        print(f"[auto_generate] 같은 슬러그({slug})가 이미 _drafts/auto/에 있다. 스킵.", flush=True)
        return 2
    dest.write_text(markdown + "\n", encoding="utf-8")
    print(f"[auto_generate] OK: _drafts/auto/{slug}.md (status: ready)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
