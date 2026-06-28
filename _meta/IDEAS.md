# 글감 큐 (Ideas Queue)

> 사용자가 던지는 글감 아이디어를 모아 두는 자리.
> "계속 써줘" 같은 트리거가 오면 Claude가 이 큐에서 다음 글감을 꺼내 작성한다.
> 새 글감이 들어오면 반드시 여기에 추가하고, 필요시 `references/<슬러그>/` 폴더를 같이 만든다.

---

## 발행 빈도 목표 (2026-05-29 결정)

**하루 3건 이상 발행.** 카테고리 분포는 다음 4축에서 골고루:

| 축 | 트랙 | 일 1건 목표 | 누가 작성 |
|---|---|---|---|
| 논문 리뷰 | D | 1건 | Claude (AI 분야 최신 히트 논문 자동 추적) |
| 최신 트렌드 | B | 1건 | Claude (WebSearch) |
| 경험 (사용자 작업·시리즈) | A + 시리즈 | 1건 | Claude (시리즈 회차 또는 사용자 자료 기반) |
| 기초 개념 | C | 주 1~2건 (천천히) | Claude |

> 자동 발행 cron이 이 빈도를 따라가도록 워크플로(`publish-light.yml`·`publish-deep.yml` 등) 조정 필요. 별도 항목 참조.

---

## 네 트랙

| 트랙 | 자료 출처 | 발행 속도 | 폴더 |
|---|---|---|---|
| **A. 사용자 경험·작업 기반** | 사용자 자료·메모 업로드 (`references/<슬러그>/`) | 자료 모이는 대로 (일 1건 목표) | 자료 폴더 있어야 함 |
| **B. 최신 주제·트렌드** | Claude가 WebSearch로 직접 수집 | **빠르게** — 일 1건 목표 (트렌드는 신선도가 자산) | 폴더 선택 |
| **C. 기초 개념 학습** | Claude가 WebSearch + 일반 지식으로 작성 | **천천히** — 주 1~2건 (소진 위험 회피·짬내서 한 편씩) | 폴더 선택 |
| **D. 논문 리뷰** | Claude가 arXiv·OpenReview·주요 랩 발표 추적 | **하루 1건** (히트 논문 위주) | `references/papers/<arXiv-id>/` 선택 |

> **분기 규칙**:
> - 사용자가 직접 작업한 시스템·자기 경험·특정 사업·RFP → **트랙 A**
> - 산업 동향·세계 트렌드·정책·신기술 발표 → **트랙 B** (신선도 중요, 우선 발행)
> - "AJAX가 뭔지", "REST API의 의미", "HTTP 상태코드 정리" 같은 변하지 않는 기초 개념 → **트랙 C** (천천히, 짬내서)
> - 최근 화제가 된 AI 논문 한 편을 정리·해설 → **트랙 D** (매일 1건)
> - 애매하면 트랙 A.

> **발행 속도 원칙**: 트랙 B·D는 신선도가 사라지기 전에 빠르게 비운다. 트랙 C는 한꺼번에 쏟지 않고 한 편씩 끼워 넣는다. 트랙 A는 자료가 모이는 속도에 맞춘다.

---

## 트랙 A — 사용자 경험·작업 기반 (자료 대기)

| # | 슬러그 | 카테고리 | 한 줄 | 자료 상태 | 우선 |
|---|---|---|---|---|---|
| A1 | `ax-01-manufacturing-multi-agent` | ax | 제조 분야 멀티 에이전트 구축 | **대기** — 사용자가 `references/ax-01-manufacturing-multi-agent/`에 자료 업로드 후 *"AX 첫 글 자료 올렸어"* | 중 |
| A2 | `ax-02-physical-training-agent` | ax | 피지컬 트레이닝 에이전트 (학습 방법론) | **대기** — 제안서 완성 후 자료 업로드 | 낮 |
| A3 | `coding-education-01-trash-sorter` | coding-education | **아이와 만드는 분리수거 도우미** (설명서형 튜토리얼). Teachable Machine으로 캔/페트/종이 사진을 아이가 직접 모아 노코드 이미지 분류 모델 학습 → Claude로 바이브코딩한 웹페이지에 연결해 웹캠 인식 → (선택) 라즈베리파이+서보/LED로 피지컬 AI 확장. "의도 정의+결과 검증"을 아이가 체험하는 게 목표(PERSONA §1·§9). 단계별 캡처·코드. | **글감 확정 (2026-06-20)** — **교육 세션(`/edu-post`) 담당**. 기술글 세션은 작성하지 않음 | 높 |
| A4 | (운영 일지 첫 편) | ops-log | 짧고 가벼운 첫 운영 기록 (300~1000자) | 자료 불필요 — 사용자가 그날 운영 사건 한 줄만 던지면 즉시 작성 | 낮 |

## 트랙 B — 최신 주제·트렌드 (Claude 웹 검색, 빠르게 발행)

| # | 슬러그 | 카테고리 | 한 줄 | 자료 상태 | 우선 |
|---|---|---|---|---|---|
| B1 | `ax-03-physical-ai-petabyte` | ax | 피지컬 AI 시대의 데이터 단위는 페타바이트다 | **초안 작성됨** (`_drafts/deep/ax-03-physical-ai-petabyte.md`, status: draft) | — |
| B2 | `trend-multi-agent-becomes-default` | thoughts | 멀티 에이전트가 기본값이 됐다 — 2026년 5월의 코딩 도구 풍경 | **초안 작성됨 (ready, 2026-05-30)** `_drafts/light/` | — |
| B3 | `trend-agent-building-blocks` | building-with-ai | 에이전트를 이루는 네 부품 — 훅·스킬·MCP·워크플로 | **초안 작성됨 (ready, 2026-06-19)** `_drafts/deep/` | 높 |

## 트랙 A·B 추가 — 비전·온디바이스 (2026-06-19 사용자 지시)

> 사용자가 비전 기반 제조공정 / 온디바이스 비전 재난탐지 도메인의 사전지식 글을 요청. 페르소나 §2 규칙대로 특정 사업·소속을 드러내지 않고 일반화된 스터디 노트로 작성.

| # | 슬러그 | 카테고리 | 한 줄 | 자료 상태 | 우선 |
|---|---|---|---|---|---|
| A5 | `ax-01-manufacturing-vision-agent` | ax | 비전 기반 제조공정 에이전트 — 검사에서 판단까지 (A1 글감의 구체화) | **초안 작성됨 (ready, 2026-06-19)** `_drafts/deep/` | 높 |
| B4 | `ax-04-ondevice-disaster-vision` | ax | 온디바이스 비전으로 재난을 탐지한다 — 자료조사 + 엣지 AI 트렌드 | **초안 작성됨 (ready, 2026-06-19)** `_drafts/deep/` | 높 |
| B5 | `ax-05-ondevice-vision-dev-methodology` | ax | 온디바이스 비전 모델 개발 방법론 — 양자화·증류·NPU | **발행됨 (2026-06-19)**. NPU 부분은 B6으로 분리, 본문은 포인터만 남김 | 높 |
| B6 | `ax-06-npu-edge-inference` | ax | NPU란 무엇인가 — 온디바이스 비전을 떠받치는 칩 (B5에서 분리, 사용자 지시 2026-06-19) | **발행됨 (2026-06-19 수동)** `_posts/`. mermaid 도식 포함 | 높 |

> 2026-06-19 추가 지시: ① `trend-agent-building-blocks`에 **오케스트레이터** 섹션 추가(§5 신설, 네 부품→지휘층까지). ② NPU를 B5에서 B6으로 분리. ③ 발행된 4편에 mermaid 도식 보강. ④ PERSONA §10 이미지 표준 신설.

## 2026-06-21 에이전트 클러스터 (사용자 지시)

> 기본 아키텍처→구축방법론→설계패턴→메모리→평가·관측 + 논문/학술 이슈. 도식은 출처표기 mermaid 재구성 또는 예시코드 포함. 카테고리 building-with-ai(트렌드 글과 동일 계열), 논문은 paper-review.

| # | 슬러그 | 한 줄 | 상태 |
|---|---|---|---|
| AG1 | `agent-01-architecture` | 에이전트 기본 아키텍처(LLM코어·도구·메모리·루프, ReAct/plan-execute) | pending |
| AG2 | `agent-02-build-methodology` | 구축 방법론(프롬프트→도구→오케스트레이션, eval 주도, 반복) | pending |
| AG3 | `agent-03-design-patterns` | 설계 패턴(ReAct·Reflexion·Plan-Execute·Router·Orchestrator-Worker·Evaluator-Optimizer) | pending |
| AG4 | `agent-04-memory` | 에이전트 메모리(단기/장기·벡터·지식그래프, MemGPT 등) | pending |
| AG5 | `agent-05-eval-observability` | 평가·관측(τ-bench·SWE-bench·GAIA, LangSmith·Langfuse·OTel) | pending |
| AG6 | `paper-20260621-why-reasoning-fails-to-plan` | 논문 D6: Why Reasoning Fails to Plan (arXiv 2601.22311) | pending |

## 2026-06-20 사용자 글감 6종 (그루핑 확정)

> 사용자 제안 6개를 두 클러스터 + 단독으로 묶음. 모두 ax 또는 building-with-ai, 깊이 기준 = ax-06(제품·수치·코드). #3 그루핑은 Claude가 정함(아래).

**클러스터 1 — 온디바이스 (프로젝트 핵심, ax-05·ax-06과 한 줄기)**

| # | 슬러그 | 카테고리 | 한 줄 | 상태 |
|---|---|---|---|---|
| OD1 | `ax-07-ota-edge` | ax | OTA — 엣지/온디바이스 모델·펌웨어 무선 갱신 (델타·A/B파티션·롤백, Mender/balena/AWS IoT Greengrass) | pending |
| OD2 | `ax-08-ondevice-porting` | ax | 온디바이스 포팅 — 모델을 장치로 옮기기 (ONNX 변환, 연산자 지원/폴백, 그래프 최적화) | pending |
| OD3 | `ax-09-ondevice-frameworks-code` | ax | 온디바이스 프레임워크·경량화 (실제 코드) — TFLite·ONNX Runtime·ExecuTorch·NCNN·llama.cpp + 양자화 코드 예시 | pending |
| OD0 | `ax-hw0-formfactor-glossary` | ax | **하드웨어 기초편(시리즈 0)**: 폼팩터(칩·SoC·SoM·모듈·SBC·캐리어보드)와 NPU/GPU 적용 유형, 스펙 용어 사전(TOPS·TFLOPS·TDP·메모리대역폭·공정노드nm·INT8/FP16·LPDDR·PCIe lane 등) + 실제 제품 전격 비교 예시 | pending |
| OD4~ | `ax-10-hw-*` | ax | **하드웨어 시리즈**: HW1 서버(H200·B200/GB200·AMD MI300), HW2 워크스테이션(RTX PRO Blackwell 등), HW3 엣지(Jetson Thor/Orin·Hailo), HW4 온디바이스(NPU=ax-06 연계). ※ OD0(폼팩터·용어)가 이 시리즈의 진입편 | pending |

**클러스터 2 — 지식·추론 (#2 뉴로심볼릭 + #3 온톨로지/지식그래프/그래프DB 묶음)**

| # | 슬러그 | 카테고리 | 한 줄 | 상태 |
|---|---|---|---|---|
| KR1 | `kr-01-ontology-knowledge-graph` | ax | 온톨로지·지식그래프·그래프DB 기초 (개념 + RDF/OWL/SPARQL vs property graph, Neo4j) | pending |
| KR2 | `kr-02-graphrag` | ax | 그래프DB 실전 + GraphRAG (지식그래프로 LLM 환각 줄이기) | pending |
| KR3 | `kr-03-neurosymbolic-ai` | ax | 뉴로심볼릭 AI (신경망+기호추론, AlphaGeometry 등) — KR 묶음의 우산/다리 | pending |

> **#3 그루핑 결정**: 온톨로지·지식그래프·그래프DB를 KR1(기초)로 한데 묶고, KR2(GraphRAG 실전)로 LLM과 연결, KR3(뉴로심볼릭)을 그 위 우산 개념으로. 신경망+기호추론과 지식그래프가 같은 "기호적 표현" 줄기라 한 클러스터로 둠.

> 진행: 깊이 보강 백로그(NOTES) 먼저 끝낸 뒤, 위 신규 글감을 OD1→OD4, KR1→KR3 순으로. 각 글 웹검색으로 제품·수치·코드 확보 후 작성.

> **2026-06-20 발행 완료(병렬 서브에이전트 작성→검수→발행)**:
> - 1차: OD0 `ax-hw0-formfactor-glossary`, OD1 `ax-07-ota-edge`, KR1 `kr-01-ontology-knowledge-graph`, KR3 `kr-03-neurosymbolic-ai`
> - 2차: OD2 `ax-08-ondevice-porting`, OD3 `ax-09-ondevice-frameworks-code`, OD4-HW1 `ax-10-hw1-server`(서버 H200·B200/GB200·MI300·TPU), KR2 `kr-02-graphrag`
> - **지식·추론 클러스터(KR1~KR3) 완료.** 온디바이스 핵심(OD0~OD3) 완료.
> - 3차(2026-06-21): HW2 워크스테이션 `ax-11-hw2-workstation`, HW3 엣지박스 `ax-12-hw3-edge-box` 발행. **하드웨어 시리즈(HW0~HW3 + 온디바이스 ax-06) 완료.**
> - **온디바이스 클러스터·지식추론 클러스터·하드웨어 시리즈 3개 다 소진.** 다음은 IDEAS 평시 큐: 시리즈 미작성분(0편 서문·3편 AJAX분석·4편 CP949·9편 종결), 트랙 B 트렌드, 트랙 D 논문(D5~), 트랙 C 기초(basics-nodejs 등). 아이 교육글은 `/edu-post` 세션.

## 트랙 C — 기초 개념 학습 (천천히, 짬내서)

변하지 않는 웹·네트워크·도구 기초 개념. 한꺼번에 쏟지 말고 시리즈·트렌드 사이에 한 편씩 끼워 넣는다. 카테고리는 짧으면 `questions`(질문 노트), 길면 별도 학습 글로 분류. 카테고리 신설(예: `web-basics`) 여부는 글감이 5편 이상 쌓이면 사용자와 재논의.

| # | 슬러그 | 잠정 카테고리 | 한 줄 | 자료 상태 | 분량 잠정 |
|---|---|---|---|---|---|
| C1 | `basics-ajax` | questions | AJAX란 무엇인가 — 화면 새로고침 없이 서버와 대화하는 방식 | **초안 작성됨 (ready, 2026-05-30)** `_drafts/light/basics-ajax.md` | 800~1500자 |
| C2 | `basics-rest-api` | questions | REST API란 무엇인가 — 자원에 HTTP 메서드를 매핑하는 약속 | **초안 작성됨 (ready, 2026-06-01)** `_drafts/light/basics-rest-api.md` | 1500~1800자 |
| C3 | `basics-nodejs` | questions | Node.js — 이벤트루프·논블로킹·CJS/ESM·공급망까지 | **발행 (2026-06-26)** | 1000~1800자 |
| C4 | `basics-http-status-codes` | questions | HTTP 상태 코드 정리 — 200·301·401·403·404·429·500의 의미와 만났을 때의 대응 | **초안 작성됨 (ready, 2026-05-30)** `_drafts/light/basics-http-status-codes.md` | 1000~2000자 |
| C5 | (사용자 추가 자리) | — | (예: "JSON이 뭔지", "쿠키와 세션", "DNS와 도메인", "환경변수", "포트와 호스트") | — | — |

> **트랙 C 운영 규칙**: 한 세션에 2편 이상 연속 작성 금지. 시리즈 회차 또는 트랙 B 트렌드 글을 작성한 다음 그 사이에 한 편 끼워 넣는 식.

## 트랙 D — 논문 리뷰 (하루 1건, AI 분야 최신 히트 논문)

매일 1편씩 AI 분야에서 최근 화제가 된 논문을 정리·해설.

### 논문 선정

출처: arXiv·OpenReview·주요 랩 블로그(Anthropic·OpenAI·Google DeepMind·Meta FAIR·Mistral·DeepSeek 등)·Hacker News·Papers with Code 트렌드.

**히트 판단 기준**:
- arXiv submission이 최근 1~14일 이내
- Twitter/X·Hacker News에서 활발히 인용
- 주요 랩 공식 발표
- Papers with Code 트렌드 상위
- 직전 7일 내 같은 주제 미발행 (중복 회피)

### 논문 다운로드 (사용자 지시)

- **Claude가 직접 다운로드**: WebFetch로 arXiv PDF·HTML·Abstract를 직접 받아 분석.
- **권한 막힐 때만** 사용자에게 요청 — "이 논문(arXiv:XXXX.YYYY) PDF가 다운로드 안 됩니다, `_meta/references/papers/<arXiv-id>/` 에 넣어주세요" 식으로 명확히. 사용자가 넣어주면 그 파일로 작업 재개.
- 다운받은 자료는 `_meta/references/papers/<arXiv-id>/` 에 보관(원본 PDF + 발췌 도식 이미지).

### 도식 발췌 직접 사용 (사용자 지시)

리뷰글에는 논문의 **Figure·Table·Diagram을 직접 발췌해서 사용**. 단순 텍스트 요약이 아니라 시각 자료를 그대로 가져온다. 각 도식 캡션 옆에 출처(논문 Figure N) 명기.

### 작성 6축 — 리뷰 목적 (사용자 지시)

리뷰글이 다뤄야 할 6가지를 모두 채운다. 이게 리뷰의 정체성. ※ "1축/2축" 같은 내부 라벨은 본문 헤더에 노출 금지(독자에겐 군더더기). 축은 점검용일 뿐, 헤더는 자연어 소제목으로.

1. **이런 모델이 있구나** — 아키텍처·파라미터 규모·구조적 특징
2. **이렇게 파인튜닝했구나** — SFT·RLHF·DPO·LoRA 등 방법
3. **이렇게 학습시켰구나** — pretraining 절차·objective·loss·하이퍼파라미터
4. **이런 데이터를 준비했구나** — 출처·전처리·규모·라벨링·필터링
5. **성능평가 방법이 이런 거구나** — 벤치마크·지표·비교 대상·ablation
6. **우리는 이걸 어떻게 활용하면 좋겠구나** — 실무 함의·재현 가능성·국내 적용·라이선스

### 작성 패턴 (고정 템플릿)

1. **TL;DR** — 1~2문장
2. **모델 한눈에** (1축) — 표 또는 발췌 도식
3. **데이터 준비** (4축)
4. **학습 절차** (3축) — 사전학습 도식 발췌
5. **파인튜닝** (2축) — 있을 때
6. **성능 평가** (5축) — 결과 표 발췌
7. **실무 활용 함의** (6축) — 분량 절반 이상
8. **arXiv 링크·코드 링크·라이선스**

**잠정 카테고리**: 신설 카테고리 `paper-review` 후보. 일단 잠정 슬러그는 `paper-<YYYYMMDD>-<short-title>` 형식. 카테고리 신설 여부는 첫 1편 작성 후 사용자와 확정.

**분량**: 1500~3500자. light pool. 6축이 모두 들어가야 해서 단순 TL;DR보다 길다.

| # | 슬러그 | 상태 | 발행일 |
|---|---|---|---|
| D1 | `paper-20260530-llm-agent-industry-survey` | **초안 작성됨 (ready, 2026-05-30)** | 다음 12:00 KST |
| D2 | `paper-20260530-cattle-trade-multi-agent-benchmark` | **초안 작성됨 (ready, 2026-05-30)** | D1 다음 12:00 |
| D3 | `paper-20260530-llm-agent-evaluation-survey` | **초안 작성됨 (ready, 2026-05-30)** | D2 다음 12:00 |
| D4 | `paper-20260603-ai-scientific-taste` | **초안 작성됨 (ready, 2026-06-03)** `_drafts/paper/` | D3 다음 12:00 |
| D5 | `paper-20260621-ttt-e2e-long-context` (TTT-E2E, arXiv 2512.23675) | **발행 (2026-06-21)** | 6축 리뷰, mermaid 도식(inner/outer loop). 자료 `_meta/references/papers/2512.23675/` |
| D6 | `paper-20260621-why-reasoning-fails-to-plan` | **발행 (2026-06-25)** | FLARE, 6축, 도식 |
| D7 | `paper-20260626-reasoning-agentic-rag` (arXiv 2506.10408) | **발행 (2026-06-26)** | System1/2 분류 서베이, taxonomy 도식 |

> **트랙 D 운영 규칙**: 매일 새 세션 시작 시 Claude가 먼저 arXiv·OpenReview·랩 블로그 트렌드를 1회 WebSearch로 훑고, 가장 적합한 1편을 선정해 사용자에게 후보 1~3개 보고 → 사용자가 1개 고르면 본문 작성 진입. 사용자가 *"오늘 논문 뭐 골랐어?"* 또는 *"논문 리뷰 써줘"* 라고 하면 트리거.

---

## 진행 중인 시리즈 — "AI와 개발하기" (별도 트랙)

별도 골격이 `SERIES_OUTLINE.md`에 잡혀 있어서 글감 큐와는 분리해서 본다.

| 회차 | 슬러그 | 상태 |
|---|---|---|
| 0편 (서문) | `series-intro-ai-pair-development` | **발행 (2026-06-21)** |
| 1편 | `01-three-layers-of-data-source` | **published** (2026-05-27) |
| 2편 | `02-requests-session-cookie` | **draft** (검토 대기) |
| 3편 | `03-ajax-endpoint-analysis` | **발행 (2026-06-21)** |
| 4편 | `04-cp949-zip-encoding` | **발행 (2026-06-21)** |
| 5편 | `05-incremental-watermark` | **초안 작성됨 (ready, 2026-06-19)** `_drafts/deep/`. 워터마크·미래날짜 함정·보정모드. mermaid 도식 포함 |
| 6편 | `06-data-lifetime-separation` | **draft** (2026-05-30 작성) |
| 7편 | `07-ssot-decision` | **draft** (2026-05-29 작성) |
| 8편 | `08-double-click-ux` | **draft** (2026-05-29 작성) |
| 9편 (종결) | `09-what-remains-for-humans` | **발행 (2026-06-21)** |

다음 시리즈 회차 우선순위는 `SERIES_OUTLINE.md` 하단 표 참고.

---

## 운영 규칙

1. **새 글감이 들어오면**: 즉시 해당 트랙 표에 한 줄 추가. 트랙 A면 `references/<슬러그>/notes.md`도 같이 생성(자료 자리 잡기). 트랙 B·C·D는 자료 폴더 선택.
2. **"계속 써줘" / "다음 거 써줘" 트리거 시 우선순위**:
   1. 시리즈가 진행 중이면 시리즈 우선순위표(SERIES_OUTLINE.md 하단)
   2. **트랙 B(트렌드)** — 신선도 보존 우선
   3. **트랙 D(논문 리뷰)** — 매일 1건 페이스 유지
   4. **트랙 A(자료 모인 것)**
   5. **트랙 C(기초)** — 시리즈·트렌드 사이 빈자리에 한 편씩
   - 모호하면 사용자에게 묻는다.
3. **글감이 글로 전환되면**: 해당 행 상태만 갱신("초안 작성됨" / "발행됨"). 행을 지우지 않는다 — 어떤 글감이 어디서 왔는지 기록 보존.
4. **참고자료 폴더 자동 생성**: 트랙 A 글감이 들어오면 `references/<슬러그>/notes.md` 템플릿을 자동 생성. 사용자가 그 안에 자유 형식으로 자료를 채운다.
5. **하루 3건 목표 점검**: 매일 작업 시작 시 발행 빈도(논문리뷰·트렌드·경험·기초 4축) 확인. 빈 슬롯이 있으면 그 축에서 우선 추출.

---

## 자동 발행 워크플로 (2026-05-30 옵션 B 확정)

**사용자 결정 (2026-05-30)**: 옵션 3(자동 생성) 비활성화. *"PC 켜면 Claude가 직접 ready 초안을 채워두는"* 운영(옵션 B)으로 간다. API 키 등록·비용 부담 회피. 옵션 1·2(cron 확장 + 논문 전용)는 그대로 활성.

일일 cron 흐름:

| 시각 (KST) | 워크플로 | 동작 |
|---|---|---|
| ~~06:00~~ | ~~`publish-auto.yml`~~ | **비활성** (cron 주석 처리, 수동 실행만 가능) |
| 09:00 | `publish-light.yml` | `_drafts/light/` ready 1편 → `_posts/` |
| 12:00 | `publish-paper.yml` | `_drafts/paper/` ready 1편 → `_posts/` |
| 13:00 | `publish-light.yml` | `_drafts/light/` ready 1편 → `_posts/` |
| 17:00 | `publish-light.yml` | `_drafts/light/` ready 1편 → `_posts/` |
| 월 09:00 | `publish-deep.yml` | `_drafts/deep/` ready 1편 → `_posts/`. 시리즈·AX 등 긴 글 |

**결과적 일일 발행량**: 최대 4건/일 + 주 1건(월 deep). 단, **각 슬롯은 `_drafts/<풀>/`에 `status: ready`인 글이 있을 때만 발행됨.** 비어 있으면 그 슬롯은 그냥 패스.

### 옵션 B 운영 규칙 — 사용자 세션 트리거

사용자가 Claude Code 세션을 켤 때마다 Claude는 다음 순서를 자동으로 점검·실행한다:

1. **발행 상태 점검**: `_drafts/light/`·`_drafts/paper/`·`_drafts/deep/` 각각 `status: ready`인 글이 몇 편 있는지 확인. 다음 24~48시간 cron 슬롯을 커버할 만큼 있는지.
2. **부족하면 채우기**: IDEAS.md 큐에서 우선순위(시리즈 > B 트렌드 > D 논문 > A 자료 모인 것 > C 기초) 따라 다음 글감 추출 → 본문 작성 → 해당 풀에 `status: ready`로 적재.
3. **사용자 검토 자리 명시**: 작성한 초안 목록을 보고. 사용자가 OK면 그대로 cron이 가져감. 수정 요청이 있으면 반영.
4. **자료 대기 행은 건너뜀**: 트랙 A 글감은 `references/<슬러그>/`에 사용자 자료가 모인 것만 작성 대상.

**위험 인지**: 사용자가 며칠 PC를 안 켜면 ready 초안이 소진돼 그 기간엔 발행이 끊긴다. 옵션 3을 끈 대가. 사용자가 인지하고 받아들임.

### 풀(pool) 구조

```
_drafts/
├── light/      # 짧은 글 (운영일지·도구사용기·질문노트·짧은 thoughts·기초 개념)
├── deep/       # 긴 글 (시리즈·AX·아키텍처·교육)
├── paper/      # 논문 리뷰 전용 (트랙 D)
└── auto/       # (예비) 옵션 3 부활 시 자동 생성 글이 떨어질 자리. 지금은 비활성.
```
> 2026-06-21~25 에이전트 클러스터 발행 완료: AG1 agent-01-architecture, AG2 agent-02-build-methodology, AG3 agent-03-design-patterns, AG4 agent-04-memory, AG5 agent-05-eval-observability, AG6 paper-20260621-why-reasoning-fails-to-plan(논문 D6, arXiv 2601.22311). 도식+예시코드 포함, 검수(AI기여도 메타·핫링크 제거) 후 발행.

## 2026-06-25 MCP 완전정복 3부작 (사용자 지시)
- mcp-01-protocol-architecture (프로토콜·아키텍처·프리미티브·전송)
- mcp-02-build-and-secure (서버 만들기·OAuth·tool poisoning·생태계)
- mcp-03-deploy-infra-cases (연결 방식·개발vs인프라·클라우드/로컬/G-Cloud 사례) ← 사용자 실무 질문 답
전부 발행. 도식+코드+출처. 향후 확장 후보: 멀티에이전트 A2A, MCP Apps.

## 2026-06-25 에이전트·프로토콜 확장 3편
- agent-06-a2a-protocol (A2A=에이전트↔에이전트, Agent Card·Task, v1.0, MCP와 보완)
- agent-07-multiagent-collaboration (토폴로지·토큰15배·90.2%, Anthropic vs Cognition)
- agent-08-security (lethal trifecta·OWASP·EchoLeak CVE-2025-32711·Rule of Two)
전부 발행. 에이전트 클러스터 AG1~AG8 + MCP 3부작 완성.

## 2026-06-26 성능평가 카테고리 (사용자 지시) — 1차 자료조사 단계
> 새 카테고리 `performance-eval`(CATEGORIES §11). **한 번에 글 쓰지 않음.** 도메인별 1차 자료조사(서브에이전트) → 조사 결과 보고 → 글 구성 방향(1글=1주제 다지표 vs 1지표=여러 모델 비교) 결정 → 작성.
> 조사 도메인 5종 → `_meta/references/performance-eval/`: vision-models, multimodal-llm, ondevice-npu, agent-systems(+제조 멀티에이전트), classic-platform-db.
> 각 도메인: 지표명·정의·측정방식·평가환경·대표벤치마크·세계최고/국내최고 수준(수치+출처)·개발기간별(1/2/3년) 목표 제안.

## 설계·디자인 패턴 글감 (design-architecture, 카테고리 #3 — 아직 0편. 2026-06-26 메모)
> 사용자: "디자인패턴 설계패턴 같은거 쓰기로 했었다". CATEGORIES §3 design-architecture. 에이전트 설계패턴(agent-03)과 별개의 "소프트웨어 설계·아키텍처 패턴".
| # | 슬러그(잠정) | 한 줄 |
|---|---|---|
| DA1 | `design-solid` | SOLID 원칙 — AI가 짠 코드를 리뷰어 눈으로 읽기 |
| DA2 | `design-gof-patterns` | GoF 디자인 패턴 카탈로그(Strategy·Factory·Adapter·Observer 등) + 실코드 매핑 |
| DA3 | `design-plugin-adapter-arch` | 플러그인/어댑터 아키텍처(sites/<name>/ 격리 구조) |
| DA4 | `design-dependency-inversion` | 의존성 역전(DIP)·헥사고날·레이어드 |
| DA5 | `design-event-driven` | 이벤트 주도·트랜잭션 경계 |

## 트랙 C 추가 글감 (기초)
| # | 슬러그 | 한 줄 | 상태 |
|---|---|---|---|
| C6 | `basics-json` | JSON이란 무엇인가 — 데이터 교환 포맷, 쉬운 정의→스키마·직렬화·함정까지 | 작성 중(2026-06-26) |

## 2026-06-26 시리즈 확정 + 신규 시리즈 글감 (사용자 지시)
- **「정의하는 사람」 시리즈 확정**(경험 중심). 구성표: `_meta/SERIES_defining-person.md`. 카테고리 thoughts/building-with-ai 확정 대기. → 구성표 확정 후 0편부터.
- **MCP 활용 시리즈**(비전문가 시점: 과거 방식 vs MCP 연동 후, 뭘 할 때/어떻게 쓰나):
  | 슬러그(잠정) | 한 줄 | 자료 상태 |
  |---|---|---|
  | `mcp-use-figma-series` | Figma MCP 연결·활용(비전문가) | ★자료 대기 — 회사 업무로 만든 거라 **개인 프로젝트 별도 제작 필요**. 정기 체크인 대상 |
  | `mcp-use-blender-series` | Blender MCP 연결·활용 | 자료 준비 시 착수 |
  | `mcp-use-unity-series` | Unity MCP 연결·활용 | 자료 준비 시 착수 |
- **라즈베리파이 피지컬 AI 시리즈** `rpi-physical-ai-series`: 재료 구매부터 → 피지컬 AI 개발. ★재료 구매·준비 중. 정기 체크인 대상.

## 2026-06-28~29 발행
- 논문 D9 `paper-20260628-verification-horizon` (The Verification Horizon, arXiv 2606.26300 Qwen팀) — 검증>생성, 보상해킹 수치. 블로그 명제와 정합.
- `skills-review-2026` (building-with-ai) — Agent Skills 리뷰: 공식(docx/pdf/pptx/xlsx·skill-creator·mcp-builder)+커뮤니티(superpowers 등)+보안 비판(출처불명 스킬 위험).
