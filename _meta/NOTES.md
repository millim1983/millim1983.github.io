# 블로그 작업 노트

> 세션 간 연속성용 노트. 새 세션 시작 시 가장 먼저 확인할 파일.
> "현재 상태 / 다음 할 일 / 막힌 부분"이 항상 최신이어야 한다.

---

## 현재 상태 (2026-05-27)

### 인프라 — 완료
- 폴더 구조: `_posts/`, `_drafts/light/`, `_drafts/deep/`, `assets/images/`, `scripts/`, `.github/workflows/`
- Jekyll 설정(`_config.yml`), Gemfile, `.gitignore`, `index.md` 초안 — 모두 작성 완료.
- 자동 발행 인프라(`scripts/publish_one.py`, `publish-light.yml`, `publish-deep.yml`) — 완료.

### 글쓰기 원칙 — 갱신 완료
- `PERSONA.md` — 핵심 메시지·화자·독자·문체·표기 규칙·퇴고 체크리스트.
- **핵심 메시지** (모든 글의 결론으로 수렴):
  > "Claude Code는 엑셀이 함수에 한 일을 코드에 한다. 도구가 코드를 대신 짤 때, 사용자가 잘해야 하는 일은 — 무엇을 만들지 정의하는 능력과, 도구가 만든 결과를 검증하는 능력이다."
- 톤 원칙: "개발자/비개발자" 이항 구도 회피, 코드 폄하 표현 회피, 독자에게 시비조 표현 회피, "~이 아닌/아니라" 반박조 패턴 회피.

### 카테고리 구조 — 신설 (2026-05-27)
`CATEGORIES.md`에 9개 카테고리 정의서 작성. 모든 새 글은 다음 중 하나에 속한다.

| # | 표시명 | 슬러그 | 톤 | 풀 |
|---|---|---|---|---|
| 1 | 내 생각 | `thoughts` | 가벼운 의견 | light 주로 |
| 2 | AI와 개발하기 | `building-with-ai` | 기록·진지 | deep |
| 3 | 소프트웨어 디자인·아키텍처 | `design-architecture` | 바이블 + 실전 | deep |
| 4 | 클린 코드 | `clean-code` | 처방·학습 | light/deep |
| 5 | 알고리즘 | `algorithms` | 학습 | light/deep |
| 6 | 운영 일지 | `ops-log` | 일기스러움 | light |
| 7 | 도구 사용기 | `tool-reviews` | 가벼운 후기 | light |
| 8 | 질문 노트 | `questions` | 매우 짧음 | light |
| 9 | 정보/코딩 교육 | `coding-education` | 학습 친화 | deep 주로 |
| 10 | AX (AI Transformation) | `ax` | 스터디 노트 | deep 주로 |

### 작성된 글 — 1편 (검토 대기)
- `_drafts/light/a-year-with-claude-code.md`
  - 제목: "1년 동안 Claude Code를 쓴 사람으로서"
  - 부제: "그거 진짜 네가 만든 거 맞아?"
  - 카테고리: `thoughts`
  - status: **draft** — 검토 후 `ready`로 바꾸면 다음 cron(매일 09:00·17:00 KST 중 가장 가까운 시각)에 자동 발행.
  - 이전에 있던 `_drafts/deep/series-intro-ai-pair-development.md`(시리즈 서문, 진지·웅장 톤)는 톤 재정렬 과정에서 폐기. 본 글이 그 자리를 가벼운 의견 글로 대체.

### 시리즈 인덱스 — 보존
- `SERIES_OUTLINE.md` — 9편짜리 시리즈 회차 매핑(인용 코드 위치·"사용자가 결정한 일"·결론 한 줄). 이 시리즈는 새 카테고리 체계에서 **"AI와 개발하기"(`building-with-ai`)** 카테고리에 속한다.
- 본문은 미작성. 본격 착수 시 `_drafts/deep/`에 회차별 파일 생성.

### git — 부분 완료
- `git init` 완료. **아직 안 됨**: 첫 commit, GitHub 원격 저장소 생성, push.

---

## 다음 할 일 (재개 시)

### 즉시 (사용자 액션 필요)
1. **GitHub public 저장소 생성** (예: `blog`). URL 받으면 Claude가 commit + remote + push 명령 안내.
2. GitHub 저장소 설정 두 가지:
   - Settings → Pages: Source = `Deploy from a branch / main / / (root)`
   - Settings → Actions → General: Workflow permissions = **Read and write permissions**

### 그 다음 (콘텐츠)
3. `_drafts/light/a-year-with-claude-code.md` 검토 → `status: ready` → commit & push → 가까운 cron에 자동 발행.
4. **"AI와 개발하기"** 시리즈 본격 착수 — `SERIES_OUTLINE.md`의 회차 매핑대로 1편부터 본문 작성.
   - 작성 우선순위 권장: **1편 → 8편 → 7편 → 5·6편 → 2·3·4편 → 9편**.
   - 위치: `_drafts/deep/01-<슬러그>.md` 형식.
5. 다른 카테고리에도 글 채우기 시작 — 운영 일지·질문 노트·도구 사용기 같은 light 풀 글을 일주일에 몇 편씩 누적.

### 보류 / 미결정
- 테마 변경(minima → 다른 테마 또는 커스텀)·댓글 시스템(utterances·giscus 등)·분석 도구(GA 등)는 발행 시작 후 트래픽 보면서 결정.
- 카테고리별 인덱스 페이지(`/categories/<slug>/`) 자동 생성 — 필요해지면 jekyll-archives 플러그인 또는 수동 `category-<slug>.md` 페이지 추가.

---

## 막힌 부분 (없음)

현재 막힌 부분 없음. GitHub 저장소 생성 후 push만 진행하면 자동 발행 인프라가 즉시 가동된다.

---

## 빠른 참조

| 파일/폴더 | 역할 |
|---|---|
| `PERSONA.md` | 글쓰기 원칙. 새 글 쓰기 전 반드시 확인. |
| `REVIEW.md` | 검토 대기 큐. |
| `_drafts/light/` | 가벼운 글 풀. cron 매일 2회. |
| `_drafts/deep/` | 깊이 있는 글 풀. cron 주 1회 (월요일). |
| `_posts/` | 발행된 글. 자동 이동되는 위치(직접 손대지 않음). |
| `scripts/publish_one.py` | 발행 스크립트. cron이 호출. 로컬 수동 발행도 가능. |
| `.github/workflows/` | cron 정의. |
| `README.md` | 폴더 구조·발행 절차 요약. |

---

## 분리된 다른 프로젝트

이 블로그 프로젝트는 **콘텐츠 작성·발행 인프라**에 집중한다.

블로그의 분석 대상이 되는 실제 시스템 코드는 별도 프로젝트:
- 경로: `C:\Users\kbj\OneDrive\바탕 화면\biz-announcement-monitor`
- 그 프로젝트의 진행 상황은 그쪽 `NOTES.md` 참조.

두 프로젝트는 독립적으로 관리한다. 블로그 글이 그쪽 코드를 인용할 때만 참고한다.
