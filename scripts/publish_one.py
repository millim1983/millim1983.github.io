"""검토 완료된 초안 1편을 _posts/로 이동.

- 대상 폴더: _drafts/light 또는 _drafts/deep (인자로 지정)
- 선정 규칙: front matter에 `status: ready`가 있는 파일 중 mtime 가장 오래된 1개
- 이동 시 파일명에 오늘 날짜 prefix (YYYY-MM-DD-슬러그.md), front matter에 date 필드 삽입, status: published로 변경

사용:
    python scripts/publish_one.py light
    python scripts/publish_one.py deep
    python scripts/publish_one.py --slug 슬러그명   # 특정 글 강제 발행

종료 코드:
    0 — 1편 발행 성공
    2 — 발행할 ready 글 없음 (Actions에서 정상 처리)
    1 — 오류
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
DRAFTS = ROOT / "_drafts"
KST = ZoneInfo("Asia/Seoul")


def parse_front_matter(text: str) -> tuple[dict, str, str]:
    """front matter(YAML) 파싱. (메타 dict, raw_fm, body) 반환."""
    if not text.startswith("---"):
        return {}, "", text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, "", text
    raw_fm = text[3:end].lstrip("\n")
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in raw_fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            # 인라인 주석 제거
            val = re.sub(r"\s+#.*$", "", val).strip()
            meta[key] = val
    return meta, raw_fm, body


def find_ready(pool_dir: Path) -> Path | None:
    """status: ready 인 글 중 mtime 가장 오래된 1편."""
    candidates: list[tuple[float, Path]] = []
    if not pool_dir.exists():
        return None
    for p in pool_dir.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        meta, _, _ = parse_front_matter(text)
        if meta.get("status", "").strip().lower() == "ready":
            candidates.append((p.stat().st_mtime, p))
    if not candidates:
        return None
    candidates.sort()
    return candidates[0][1]


def find_by_slug(slug: str) -> Path | None:
    for pool in ("light", "deep"):
        p = DRAFTS / pool / f"{slug}.md"
        if p.exists():
            return p
    return None


def publish(src: Path) -> Path:
    text = src.read_text(encoding="utf-8")
    meta, raw_fm, body = parse_front_matter(text)
    now = datetime.now(KST)
    date_str = now.strftime("%Y-%m-%d %H:%M:%S %z")
    date_str = date_str[:-2] + ":" + date_str[-2:]  # +0900 → +09:00
    # front matter 갱신: date 추가/교체, status: published
    fm_lines = []
    seen_date = seen_status = False
    for line in raw_fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:", line)
        key = m.group(1) if m else None
        if key == "date":
            fm_lines.append(f"date: {date_str}")
            seen_date = True
        elif key == "status":
            fm_lines.append("status: published")
            seen_status = True
        else:
            fm_lines.append(line)
    if not seen_date:
        fm_lines.append(f"date: {date_str}")
    if not seen_status:
        fm_lines.append("status: published")

    new_text = "---\n" + "\n".join(fm_lines) + "\n---\n\n" + body
    slug = src.stem
    dest_name = f"{now.strftime('%Y-%m-%d')}-{slug}.md"
    dest = POSTS / dest_name
    POSTS.mkdir(parents=True, exist_ok=True)
    dest.write_text(new_text, encoding="utf-8")
    src.unlink()
    return dest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pool", nargs="?", choices=["light", "deep"], help="발행할 풀")
    ap.add_argument("--slug", help="특정 슬러그를 강제 발행 (status 무관)")
    args = ap.parse_args()

    if args.slug:
        src = find_by_slug(args.slug)
        if not src:
            print(f"[publish] slug '{args.slug}' 을 _drafts/ 어디에서도 찾지 못함", file=sys.stderr)
            return 1
    elif args.pool:
        src = find_ready(DRAFTS / args.pool)
        if not src:
            print(f"[publish] _drafts/{args.pool}/ 에 status:ready 글이 없음 — 발행 스킵", flush=True)
            return 2
    else:
        ap.print_help()
        return 1

    dest = publish(src)
    print(f"[publish] OK: {src.name} → _posts/{dest.name}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
