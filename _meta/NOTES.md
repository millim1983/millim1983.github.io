# 블로그 작업 노트

> 세션 간 연속성용 노트. 새 세션 시작 시 가장 먼저 확인할 파일.
> "현재 상태 / 다음 할 일 / 막힌 부분"이 항상 최신이어야 한다.

---

## 한 줄 요약 (2026-06-19 갱신)

2026-06-19 작업: ① 검토 게이트 제거(`publish_one.py`가 ready/draft 모두 발행) ② deep cron 주1편→**매일 10:00 KST** ③ 비전·온디바이스 사전지식 deep 4편 작성·**즉시 수동 발행**(trend-agent-building-blocks, ax-01 제조비전, ax-04 온디바이스 재난탐지, ax-05 온디바이스 개발방법론) ④ 모두 push 완료(commit 30d8984). 남은 큐: deep에 5월 작성 5편(시리즈 2·6·7·8 + AX-03, 이제 자동발행 대상), light ready 4편, paper ready 4편 — 전부 cron이 매일 자동 발행(세션 불필요).

> **2026-06-19 2차 작업**: ① 이미지 표준 신설(PERSONA §10) — Mermaid 우선, 로컬 svg/png 보조, 논문 figure는 받아서 로컬, 외부 핫링크 금지. ② 발행된 4편에 mermaid 도식 보강. ③ `trend-agent-building-blocks`에 오케스트레이터 §5 추가(여섯 층 구성). ④ NPU를 ax-05에서 ax-06으로 분리·발행. ⑤ 시리즈 5편 작성(ready). **앞으로 모든 글에 도식 적극 사용(§10).**

> **2026-06-20 작업**: ① 발행글 5편 전부 깊이 보강(제품·수치·도식). ② 드래프트 11편 수동 발행(시리즈 2·5·6·7·8, ax-03, 논문 4, 멀티에이전트 트렌드) — cron이 안 돌아 수동으로. ③ **기초 3편(basics-ajax·rest-api·http-status)은 보류** — PERSONA §11 정책(개념글은 쉽게 시작→실제까지)대로 깊이 보강 후 발행 예정. ④ 깊이 정책 PERSONA §11 확정. **운영 모드: 세션 중에는 cron 기다리지 말고 수동 발행(빠르게).** ✅ **cron 점검 완료(2026-06-21): 정상 작동 중.** publish-deep/light/paper 모두 schedule 이벤트로 매일 자동 실행·전부 success(GitHub API로 확인). 앞서 "멈췄다"는 오진단이었음 — 실제로는 우리가 세션마다 큐를 수동으로 비워 cron 실행 시각에 ready 드래프트가 없어 패스했던 것. 단 GitHub cron은 설정 시각을 정확히 안 지키고 수십 분~수 시간 지연됨(정상). **결론: 큐에 status:ready로 쌓아두면 PC 안 켜도 자동 발행됨. 매번 수동 발행 불필요.**

> **2026-06-20~21 신규 글감 작성(병렬 서브에이전트 → 검수 → 발행)**: 온디바이스 클러스터(ax-07 OTA, ax-08 포팅, ax-09 프레임워크·코드), 지식추론 클러스터(kr-01 온톨로지/지식그래프, kr-02 GraphRAG, kr-03 뉴로심볼릭), 하드웨어 시리즈(ax-hw0 폼팩터, ax-10 서버 HW1, ax-11 워크스테이션 HW2, ax-12 엣지박스 HW3) 전부 발행 완료. 세 묶음 다 소진. **검수 시 주의: 서브에이전트가 가끔 "AI 기여도" 메타블록을 붙이는데, 스터디 노트엔 빼야 함(PERSONA §7은 자기 시스템 코드 분석글 전용).**

> **다음 세션 이어갈 것**: ⓐ "정보/코딩 교육 첫 글 단계" 결정 대기(IDEAS A3). ⓑ 시리즈 미작성분 3·4·5·9편(SERIES_OUTLINE). ⓒ 논문 리뷰 D5(매일 1건 페이스). ⓓ 사용자가 비전/온디바이스 실제 작업 자료를 올리면 references/ax-04-ondevice-disaster-vision/ 또는 새 슬러그로 트랙 A 후속 글. **새 초안 쓰기는 세션이 있어야 함(자동 생성 비활성). 발행 자체는 cron이 매일 자동.**

---

## 사이트·인프라 상태

- **사이트 URL**: https://millim1983.github.io/
- **저장소**: https://github.com/millim1983/millim1983.github.io
- **테마**: jekyll-theme-chirpy 7.x (한국어 lang, Asia/Seoul timezone)
- **빌드 방식**: GitHub Actions (`pages-deploy.yml`). Pages Source = "GitHub Actions" 설정 완료.
- **자동 발행 cron** (2026-05-30 옵션 B 확정):
  - ~~`publish-auto.yml`~~: **비활성** (cron 주석. API 키 부담 회피. 옵션 B로 운영)
  - `publish-light.yml`: 매일 09:00·13:00·17:00 KST — `_drafts/light/` ready 1편 발행
  - `publish-paper.yml`: 매일 12:00 KST — `_drafts/paper/` ready 1편 발행
  - `publish-deep.yml`: **매일 10:00 KST** — `_drafts/deep/` 1편 발행 (2026-06-19 주1편→매일 변경. 발행 cron은 파일 이동만 하고 API를 안 부르므로 토큰 비용 0. 주기를 올려도 요금 부담 없음. 비용은 세션에서 초안 쓸 때만 발생)
- **운영 모델 (옵션 B)**: 사용자가 Claude Code 세션을 켤 때마다 Claude가 발행 상태를 점검하고, ready 초안이 부족하면 IDEAS.md 큐에서 추출해 채워둔다. cron이 그 ready 초안을 자동으로 발행. 며칠 PC 안 켜면 발행이 끊기는 위험은 인지·수용.

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
| `_posts/2026-05-27-01-three-layers-of-data-source.md` | deep | building-with-ai | **published** | 2026-05-27 (시리즈 1편이 이미 _posts로 이동 확인됨) |
| `_drafts/deep/02-requests-session-cookie.md` | deep | building-with-ai | **draft** | 2026-05-28 작성. 사용자 검토 후 `status: ready`로 바꾸면 다음 월 09:00에 자동 발행 |
| `_drafts/deep/ax-03-physical-ai-petabyte.md` | deep | ax | **draft** | 2026-05-28 작성. 사용자 검토 후 `status: ready` 전환 |
| `_drafts/deep/08-double-click-ux.md` | deep | building-with-ai | **draft** | 2026-05-29 작성. 시리즈 8편(우선순위표 2위). 사용자 검토 후 `status: ready` 전환 |
| `_drafts/deep/07-ssot-decision.md` | deep | building-with-ai | **draft** | 2026-05-29 작성. 시리즈 7편(우선순위표 3위, 8편이 자연스럽게 예고). 사용자 검토 후 `status: ready` 전환 |
| `_posts/2026-06-19-trend-agent-building-blocks.md` | deep | building-with-ai | **published** | 2026-06-19 수동 발행. 에이전트 4부품(훅·스킬·MCP·워크플로) |
| `_posts/2026-06-19-ax-01-manufacturing-vision-agent.md` | deep | ax | **published** | 2026-06-19 수동 발행. 비전 기반 제조공정 에이전트 4단계 모델 |
| `_posts/2026-06-19-ax-04-ondevice-disaster-vision.md` | deep | ax | **published** | 2026-06-19 수동 발행. 온디바이스 비전 재난탐지 자료조사+엣지AI 트렌드 |
| `_posts/2026-06-19-ax-05-ondevice-vision-dev-methodology.md` | deep | ax | **published** | 2026-06-19 수동 발행. 양자화·증류·가지치기. NPU는 ax-06으로 분리(본문은 포인터) |
| `_posts/2026-06-19-ax-06-npu-edge-inference.md` | deep | ax | **published** | 2026-06-19 수동 발행. NPU 전용(B5에서 분리). mermaid 도식 |
| `_drafts/deep/05-incremental-watermark.md` | deep | building-with-ai | **ready** | 2026-06-19 작성. 시리즈 5편 증분수집 워터마크. mermaid 도식. cron 자동발행 대기 |

## 깊이 보강 백로그 (2026-06-20, 사용자 지시 "전부 깊이 조정")

사용자 피드백: 글이 얕고 개념적이라 정보가 없다. **기준선 = `ax-06-npu` 재작성본**(제품군+스펙 비교표, 실측 수치, 비유는 실제 설명 뒤 보조로만). 규칙은 PERSONA §10·§11. 메모리 `blog-depth-and-concreteness`.

| 글 | 상태 | 비고 |
|---|---|---|
| `ax-06-npu-edge-inference` | **완료** | 제품 4계층표+국산NPU(DeepX·Furiosa·Mobilint·Rebellions)+CPU/GPU/NPU 구조 비교 |
| `ax-01-manufacturing-vision-agent` | **완료** | MVTec AD·PatchCore/PaDiM/EfficientAD·Anomalib·카메라(Basler/Cognex)·엣지칩. 출처 산불→제조로 교정 |
| `ax-04-ondevice-disaster-vision` | **완료** | 2026-06-20. 실전배치(ALERTCalifornia 1,240대·Pano AI 725건·OroraTech·Dryad), 데이터셋표(FASDD·D-Fire·FLAME3·FIgLib·FloodNet·Sen1Floods11), YOLOv8n·증류·엣지칩 |
| `ax-05-ondevice-vision-dev-methodology` | **완료** | 2026-06-20. 경량 모델군표(MobileNetV3·EfficientDet-Lite·YOLO-NAS·MobileViT·LeYOLO), 양자화 PTQ 코드, 런타임표(TFLite·ONNX RT·ExecuTorch·OpenVINO·TensorRT), 지연수치. 제목 NPU→증류로 변경 |
| `trend-agent-building-blocks` | **완료** | 2026-06-20. MCP 수치(서버~9,650·월9,700만 다운로드·41% 프로덕션), 프레임워크 비교표(LangGraph·CrewAI 44.6k stars·MS Agent Framework·OpenAI Agents SDK·Google ADK·Claude SDK·Strands), 훅 17이벤트, dbt Skills |
| 드래프트(논문4·기초3·시리즈·ax-03) | **완료/발행** | 2026-06-20. 시리즈·ax-03·논문4·멀티에이전트 수동발행. 기초 3편(ajax·rest·http상태)은 "쉽게→실제(CORS·멱등성·캐싱)"로 보강 후 발행. **`_drafts/` 현재 비어 있음 → 큐 재충전 필요** |

> 진행 순서 제안: ax-04 → ax-05 → trend → 드래프트. 각 글마다 웹검색으로 제품·데이터셋·수치 확보 후 재작성. 한 번에 다 못 하므로 세션 이어가며 위 표 갱신.

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
├── ax-03-physical-ai-petabyte/                ★ 신설 (2026-05-28) — 페타바이트·피지컬 AI
├── series-08-double-click-ux/                 # 시리즈 8편 (자료 없어도 작성 가능)
├── ops-log/                                   # 운영 일지 자료 필요시
└── coding-education/                          # 정보/코딩 교육 단계별 자료
```

새 글감 생기면 `<카테고리>-<순번>-<주제>/` 형식으로 폴더 추가.

---

## 글감 큐 운영 (2026-05-29 신설)

글감 관리는 별도 파일 **`_meta/IDEAS.md`** 에서 한다. 두 트랙:

| 트랙 | 자료 출처 | 트리거 |
|---|---|---|
| A. 사용자 경험·작업 기반 | `references/<슬러그>/` 사용자 자료 | *"○○ 자료 올렸어"* 류 |
| B. 일반 주제·트렌드 | Claude WebSearch | *"○○에 대해 써줘"* 또는 큐에서 자동 추출 |

**규칙**:
- 사용자가 새 글감을 던지면 → 즉시 `IDEAS.md`에 한 줄 추가. 트랙 A면 `references/<슬러그>/notes.md`도 같이 생성.
- *"계속 써줘"* / *"다음 거 써줘"* 트리거: 시리즈 진행 중이면 시리즈 우선순위표 먼저. 시리즈 외면 `IDEAS.md`에서 우선순위 높음 → 트랙 A 자료 모인 것 → 트랙 B 순서.
- 글감이 글로 전환되면 `IDEAS.md` 행 상태만 갱신. 행 삭제 금지(어디서 왔는지 기록 보존).

## 검토 대기 초안 (사용자 결정 필요)

검토 OK인 것만 `status: draft → ready`로 바꾸면 다음 월 09:00 KST 자동 발행.

- `_drafts/deep/02-requests-session-cookie.md` (시리즈 2편)
- `_drafts/deep/07-ssot-decision.md` (시리즈 7편)
- `_drafts/deep/08-double-click-ux.md` (시리즈 8편)
- `_drafts/deep/ax-03-physical-ai-petabyte.md` (AX-03)

## 보류 중인 결정

- **정보/코딩 교육 첫 글 단계** — 블록 코딩(Scratch/엔트리) / 어린이 바이브 코딩 / AI 비전 / 아두이노 중 어디서 시작할지 사용자 결정 대기.
- **익명화** — GitHub username·저장소 이름 변경. 후보(`pair-notes`, `vibe-coder-kr`, `claude-runner` 등) 중 사용자 결정 후 진행.

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

> **2026-06-19 검토 게이트 제거**: 사용자 지시로 `scripts/publish_one.py`의 선정 규칙을 `status: ready`에서 `ready` 또는 `draft`로 확장. 이제 초안도 사용자 검토 없이 cron이 자동 발행한다(README 등 status 없는 문서·published 글은 제외). deep pool도 기존 draft 5편이 곧바로 발행 대상이 됨 → 다음 월 09:00 KST에 `ax-03`부터 발행. "검토 대기 초안" 개념은 사실상 폐지. 품질 문제가 검토 없이 노출될 수 있음을 인지·수용.

## 작성 규칙 변경 이력

- **2026-06-01**: `_meta/PERSONA.md` §9 "AI 글쓰기 흔적 제거" 추가. Wikipedia humanizer 가이드 중 한국어 유효 항목(의미 부풀리기·~며 연쇄·광고성 어휘·부정 평행구조·세 개 묶기 강박·동의어 순환·신호어·챗봇 잔재·em dash 남발 등 16개 항목)을 흡수. 새 글은 §9까지 적용해서 작성, 기존 ready 초안은 톤 일관성 차원에서 그대로 유지.

## 2026-06-26 빌드 실패 원인·해결 (중요)
- 증상: push는 되는데 사이트가 안 바뀜. "Build and Deploy" 워크플로의 **Build site(jekyll build) 단계가 2026-06-20부터 매번 실패**.
- 원인: `_posts/2026-06-20-paper-20260530-llm-agent-industry-survey.md`의 `{% post_url 2026-05-28-ax-03-physical-ai-petabyte %}` Liquid 태그가 실제 발행 파일명(2026-06-20-ax-03-...)과 안 맞아 Jekyll이 해석 실패 → 빌드 전체 중단. 그동안 쌓인 글이 라이브에 반영 안 됨.
- 해결: 일반 경로 링크 `/ax/ax-03-physical-ai-petabyte/`로 교체(commit a50b920) → 빌드 success, 밀린 글 전부 한 번에 반영.
- **교훈/규칙: 글 사이 링크에 `{% post_url %}` 쓰지 말 것. 발행 파일명(날짜)이 어긋나면 빌드가 통째로 깨진다. 항상 permalink 경로 `/<category>/<slug>/`로 직접 링크.** 코드/본문에 `{{`·`{%`가 들어가면 빌드 깨지므로 주의(서브에이전트 글 검수 시 grep 점검 추가).

## ⏰ 정기 체크인 (매 세션 시작 시 사용자에게 물어볼 것 — 2026-06-26 등록)
> 사용자 요청: 자료/준비 됐는지 주기적으로 물어봐 달라. 준비되면 해당 시리즈 착수.
1. **Figma MCP 개인 프로젝트** 자료 만들어졌는지? (회사 업무 버전은 못 씀 → 개인 프로젝트 필요)
2. **라즈베리파이 부품** 도착/피지컬 AI 준비 됐는지?
→ 둘 중 준비되면 그 시리즈 글감 착수. (Blender·Unity MCP는 자료 생기면)

## 시리즈 현황 (2026-06-26)
- ✅ 「AI와 개발하기」 9편(0~9) 완결 — 단, 제목이 정의서 톤이라 다음부터 개선.
- ✅ 「정의하는 사람」 0~7편 완결(2026-06-26). 훅 제목+척추+정의력 수렴 구조. 다음 시리즈는 MCP/라즈베리파이(자료 대기).
- ⏳ MCP 활용(Figma/Blender/Unity)·라즈베리파이 피지컬AI 시리즈 — 자료 대기(위 정기 체크인).
