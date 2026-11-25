# evidence - sol-01-solutionizing-my-work-tools

열람일: 2026-10-22

## A. 외부 출처 (직접 열람)

### A1. The Twelve-Factor App: III. Config
- 저자: Adam Wiggins (사이트 하단 "Written by Adam Wiggins • Last updated 2017")
- URL: https://12factor.net/config (저자 표기는 https://12factor.net/ 하단)
- 읽은 위치: III. Config 본문 전체

| 본문 요지 | 원문 발췌 |
|---|---|
| 설정 = 배포마다 달라질 가능성이 있는 모든 것 | "An app's config is everything that is likely to vary between deploys (staging, production, developer environments, etc)." |
| 설정과 코드의 엄격한 분리 요구 | "...is a violation of twelve-factor, which requires strict separation of config from code." |
| 검사 방법: 지금 공개해도 자격 증명이 새지 않는가 | "...whether the codebase could be made open source at any moment, without compromising any credentials." |
| (참고) 환경변수 저장 | "The twelve-factor app stores config in environment variables." |

### A2. The Twelve-Factor App: IV. Backing services
- URL: https://12factor.net/backing-services, 읽은 위치: IV 본문

| 본문 요지 | 원문 발췌 |
|---|---|
| 로컬 DB를 외부 관리형으로 바꿔도 앱 코드 불변 | "...should be able to swap out a local MySQL database with one managed by a third party ... without any changes to the app's code." |

### A3. The Twelve-Factor App: 서문
- URL: https://12factor.net/, 읽은 위치: Introduction 첫 문장

| 본문 요지 | 원문 발췌 |
|---|---|
| SaaS 형태로 배포되는 앱을 위한 원칙 | "In the modern era, software is commonly delivered as a service: called web apps, or software-as-a-service." |

## B. 로컬 근거 (읽기만, 수정 없음)

| 본문 사실 | 근거 파일 |
|---|---|
| 스킬 35개 | `~/.claude/skills/` 폴더 목록(_past·synced 제외) |
| 서브에이전트 10개, 선정 기준(노이즈 흡수·독립 심판) | `~/.claude/agents/*.md`, `agents/README.md`, 운영체계_마스터 1-1절, memory subagent-layer-design.md |
| 훅 8개, 공용 스크립트 13개, 공유 지식자산 9폴더 | `~/.claude/hooks/`, `~/.claude/scripts/`, 공유 자산 루트 폴더 목록 |
| 절대경로 포함: 스킬 17/35, 파일 23/137 | 스킬 폴더 grep(사용자 홈·작업 드라이브·클라우드 드라이브 경로 패턴), 2026-10-22 실측 |
| 대시보드 6개 + 허브, 허브 레지스트리 절대경로·포트 | 대시보드허브 README·NOTES·registry.json(8개 항목, 구버전 2개 포함) |
| 포트 수동 배정 | memory dashboard-saas-standard.md |
| L1~L4 계층, 자산 배치표 판단 기준 | 운영체계_마스터 0절, 1-3절 |
| 게이트 G0~G6, PROJECT.yaml | gate-runner-kr/SKILL.md 2절 |
| 조직 분장 규칙(정량·정성 담당 부서) | bid-master-sheet-kr SKILL.md description |
| 정기회의 요일·시각 전제, 구글 인증 | meeting-minutes-kr description, scripts/google_auth.py; bid-calendar-kr scripts/gcal_auth.py |
| 사내 우수 제안서를 기준 문서로 | rnd-dev-content-kr description |
| storage.json root, 환경변수 우선, Storage 상속 | 사업관리대시보드 README.md, memory pm-dashboard.md |
| 제안관리 storage.json 작업 폴더·숨김 폴더 목록 | 제안관리대시보드 storage.json |
| 폴더 관례로 선정·미선정 판정 | 제안관리대시보드 NOTES.md, memory proposal-dashboard.md |
| SQLite DELETE 저널, WAL 금지(동기화 드라이브) | memory proposal-dashboard.md, 제안관리대시보드 README.md |
| PMO 코드 사본("고친 뒤 복사한다") | 사업관리대시보드 README.md |
| 사업 목록 5곳, git 1/10 | memory workos-integration-platform.md |
| workos: 경로는 설정 한 곳, 도구 14개 계약·writes 필수, 적합도 15종·래칫, 교정 장부 | workos README.md, tools.yaml |
| 세션 보관소·업무일지가 내 세션 기록을 읽음 | 세션보관소 README.md, daily-worklog-kr description |
| 공유 저장소 쓰기 조건과 훅 강제 | 전역 CLAUDE.md 「외부 저장소 취급」, hooks/block_shared_drive_write.py |
| 진척률 같은 기준일 비교 | memory pm-progress-skill.md |
