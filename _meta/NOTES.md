# 블로그 작업 노트

> 세션 간 연속성용 노트. 새 세션 시작 시 가장 먼저 확인할 파일.
> "현재 상태 / 다음 할 일 / 막힌 부분"이 항상 최신이어야 한다.

---

## 한 줄 요약 (2026-06-19 갱신)

2026-06-19 작업: ① 검토 게이트 제거(`publish_one.py`가 ready/draft 모두 발행) ② deep cron 주1편→**매일 10:00 KST** ③ 비전·온디바이스 사전지식 deep 4편 작성·**즉시 수동 발행**(trend-agent-building-blocks, ax-01 제조비전, ax-04 온디바이스 재난탐지, ax-05 온디바이스 개발방법론) ④ 모두 push 완료(commit 30d8984). 남은 큐: deep에 5월 작성 5편(시리즈 2·6·7·8 + AX-03, 이제 자동발행 대상), light ready 4편, paper ready 4편 — 전부 cron이 매일 자동 발행(세션 불필요).

> **2026-06-19 2차 작업**: ① 이미지 표준 신설(PERSONA §10) — Mermaid 우선, 로컬 svg/png 보조, 논문 figure는 받아서 로컬, 외부 핫링크 금지. ② 발행된 4편에 mermaid 도식 보강. ③ `trend-agent-building-blocks`에 오케스트레이터 §5 추가(여섯 층 구성). ④ NPU를 ax-05에서 ax-06으로 분리·발행. ⑤ 시리즈 5편 작성(ready). **앞으로 모든 글에 도식 적극 사용(§10).**

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
| 드래프트(논문4·기초4·시리즈·ax-03) | **대기** | 사용자 "기존 드래프트까지 전부". 논문리뷰는 이미 figure/수치 있음, 기초·시리즈 보강 검토 |

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
