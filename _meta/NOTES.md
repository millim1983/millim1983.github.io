# 블로그 작업 노트

> 세션 간 연속성용 노트. 새 세션 시작 시 가장 먼저 확인할 파일.
> "현재 상태 / 다음 할 일 / 막힌 부분"이 항상 최신이어야 한다.

---

## 한 줄 요약 (2026-05-27 종료 시점)

블로그 인프라(Chirpy + GitHub Actions) 안정, 첫 글 1편 발행, 시리즈 1편 ready 상태 (2026-06-01 월요일 09:00 KST 자동 발행 예약), 참고자료 폴더 인프라 신설.

---

## 사이트·인프라 상태

- **사이트 URL**: https://millim1983.github.io/
- **저장소**: https://github.com/millim1983/millim1983.github.io
- **테마**: jekyll-theme-chirpy 7.x (한국어 lang, Asia/Seoul timezone)
- **빌드 방식**: GitHub Actions (`pages-deploy.yml`). Pages Source = "GitHub Actions" 설정 완료.
- **자동 발행 cron**: `publish-light.yml`(매일 09:00·17:00 KST), `publish-deep.yml`(매주 월요일 09:00 KST). 둘 다 정상 동작 확인됨.

## 폴더 구조 (현재)

```
blog/
├── _config.yml             # Chirpy 설정 + 사용자 정보
├── Gemfile                 # jekyll-theme-chirpy gem
├── index.html              # Chirpy home layout
├── README.md
├── _data/                  # Chirpy 데이터 (contact, share)
├── _plugins/               # Chirpy posts-lastmod-hook
├── _tabs/                  # 사이트 탭 (about, archives, categories, tags)
├── _drafts/
│   ├── light/              # 매일 cron 발행 풀
│   └── deep/               # 매주 월 cron 발행 풀
├── _posts/                 # 발행 완료
├── _meta/                  # ★ 운영 문서·참고자료 (Jekyll 빌드 자동 제외)
│   ├── NOTES.md            # 이 파일
│   ├── PERSONA.md
│   ├── CATEGORIES.md
│   ├── REVIEW.md
│   ├── SERIES_OUTLINE.md
│   ├── USER_MANUAL.md
│   └── references/         # 주제별 글감 자료
├── .github/workflows/
│   ├── pages-deploy.yml    # Chirpy 빌드·배포
│   ├── publish-light.yml   # _drafts/light → _posts (매일 2회)
│   └── publish-deep.yml    # _drafts/deep → _posts (매주 월)
├── assets/
├── scripts/
└── tools/                  # Chirpy 보조 (run.sh, test.sh)
```

## 발행 상태

| 파일 | 풀 | 카테고리 | 상태 | 발행 시점 |
|---|---|---|---|---|
| `_posts/2026-05-27-a-year-with-claude-code.md` | light | thoughts | **published** | 2026-05-27 |
| `_drafts/deep/01-three-layers-of-data-source.md` | deep | building-with-ai | **ready** | 2026-06-01 09:00 KST 자동 또는 수동 즉시 |

## 카테고리 (10개, 확정)

`_meta/CATEGORIES.md` 참고. 슬러그·풀·예시 글감까지 정의돼 있음.

| # | 표시명 | 슬러그 | 풀 |
|---|---|---|---|
| 1 | 내 생각 | `thoughts` | light 주로 |
| 2 | AI와 개발하기 | `building-with-ai` | deep |
| 3 | 소프트웨어 디자인·아키텍처 | `design-architecture` | deep |
| 4 | 클린 코드 | `clean-code` | light/deep |
| 5 | 알고리즘 | `algorithms` | light/deep |
| 6 | 운영 일지 | `ops-log` | light |
| 7 | 도구 사용기 | `tool-reviews` | light |
| 8 | 질문 노트 | `questions` | light |
| 9 | 정보/코딩 교육 | `coding-education` | deep 주로 |
| 10 | AX (AI Transformation) | `ax` | deep 주로 |

---

## 참고자료 폴더 (2026-05-27 신설)

사용자가 글감별 자료를 올리는 자리. 사이트에 노출되지 않음. `_meta/references/README.md` 참고.

```
_meta/references/
├── README.md                                  # 사용법 안내
├── ax-01-manufacturing-multi-agent/           ★ 사용자 자료 업로드 대기
│   └── notes.md
├── ax-02-physical-training-agent/             # 제안서 완성 후 진행
├── series-08-double-click-ux/                 # 시리즈 8편 (자료 없어도 작성 가능)
├── ops-log/                                   # 운영 일지 자료 필요시
└── coding-education/                          # 정보/코딩 교육 단계별 자료
```

새 글감 생기면 `<카테고리>-<순번>-<주제>/` 형식으로 폴더 추가.

---

## 다음 할 일 (재개 시)

### 사용자가 직접 해야 할 일

1. **AX 첫 글 자료 업로드** — `_meta/references/ax-01-manufacturing-multi-agent/` 폴더에 제조 분야 멀티 에이전트 관련 자료(PDF·기사·발췌·메모 등) 자유 형식으로 넣기. 끝나면 *"AX 첫 글 자료 올렸어"* 라고만 알려주면 Claude가 본문 작성.

2. **정보/코딩 교육 첫 글 시작 단계 선택** — 다음 중 어디서 시작할지 결정:
   - 입문: 블록 코딩 (Scratch/엔트리)
   - 초급: 어린이 바이브 코딩 (자기 의도 → AI에게 말로 부탁 → 게임·사이트 만들기)
   - 중급: AI 비전 인식 (웹캠·객체 탐지)
   - 하드웨어: 아두이노 입문

3. **시리즈 1편 즉시 발행할지 결정 (선택)** — 자동 발행은 6/1(월) 09:00 KST. 지금 즉시 발행하려면 GitHub Actions 탭 → `publish-deep` 워크플로 → `Run workflow` 클릭.

4. **(보류) 익명화 진행 결정** — GitHub username 변경 + 저장소 이름 변경. 새 username 후보(`pair-notes`, `vibe-coder-kr`, `claude-runner` 등) 중 결정하거나 새로 제시.

### Claude가 다음 세션에 진행할 작업

사용자가 *"이어서 작업하자"* 또는 *"AX 첫 글 자료 올렸어"* 류로 시작하면 다음 순서로:

1. **시리즈 8편 본문 작성** — `_drafts/deep/08-double-click-ux.md`. `SERIES_OUTLINE.md`의 8편 매핑(`run.bat`, `run_all.py`, ledger.xlsx, 메타 자동화 — settings.local.json 권한)을 따른다. 자료(`biz-announcement-monitor`)는 이미 다 있음.

2. **운영 일지 첫 편 작성** — `_drafts/light/<슬러그>.md`, 카테고리 `ops-log`. 짧고 가벼운 첫 운영 기록. 300~1000자.

3. **AX 첫 글 본문 작성** — 사용자 자료 받은 후. `_drafts/deep/ax-01-manufacturing-multi-agent.md`.

4. **정보/코딩 교육 첫 글 작성** — 사용자가 단계 결정한 후. `_drafts/deep/coding-education-01-<주제>.md`.

5. **익명화 작업** — 사용자가 새 username 결정한 후 진행 (`_config.yml`·remote URL·저장소 이름 갱신).

### 진행 중 task (TaskList 상태 참고)

- #4 시리즈 1편 ready+push: **completed**
- #5 다음 글 한 편 더: **in_progress** — 인프라(참고자료 폴더) 완료, 본문 작성 대기
- #6 익명화: **pending**
- #7 운영 문서 동기화: **in_progress** — 본 NOTES 갱신으로 마무리

---

## 글쓰기 원칙 (반드시 확인)

- `_meta/PERSONA.md` — 핵심 메시지·화자 정체성·문체·도구/사용자 구분 표기·퇴고 체크리스트.
- `_meta/CATEGORIES.md` — 카테고리 정의·예시 글감·분량·풀 매핑.
- `_meta/SERIES_OUTLINE.md` — AI와 개발하기 시리즈 9편 회차 매핑.
- `_meta/REVIEW.md` — 검토 대기 큐.

새 글 쓰기 전에 위 4개 문서 한 번 훑고 시작.

## 톤 원칙 (사용자 누적 피드백 요약)

- "개발자/비개발자" 이항 구도 회피 — "실무자" 또는 "코딩이 본업이 아닌 사람"
- 코드 폄하 표현(`코드는 희소 자원이 아니다` 류) 사용 금지
- "도구(Claude Code)/사용자" 구도로 표기
- "~이 아닌/아니라" 반박조 표현 회피
- 독자에게 시비·도전조 표현 회피, 전문가 톤
- 도입은 가볍게(거창한 "서문" 표제 회피), 마무리는 SNS 훅 가능 (평어체 유지)
- 카드 추출 가능한 굵은 1줄 인용구(`> **...**`)를 섹션 시작·끝에 박기
- 긴 주어("본업이 다른 영역인 내가 동시에 운영 중인 자동화는...") 회피, 한국어 자연스러운 호흡

---

## 막힌 부분

없음. 사용자 자료 업로드와 정보/코딩 교육 단계 결정이 다음 액션의 트리거.
