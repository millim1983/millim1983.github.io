# 멀티모달 LLM / AI 플랫폼 "성능평가" 리서치 노트

> 자료조사 노트 (블로그 글 아님). 작성: 2026-06-26. 모든 수치는 WebSearch/WebFetch로 검증. 미확인은 명시.
> **주의**: 일부 leaderboard 집계 사이트(BenchLM, pricepertoken 등)는 실존하지 않는 가공 모델명(예: "Claude Mythos 5", "GPT-5.4 Pro")을 노출함 → 본 노트는 1차 출처(모델 카드/기술보고서/Artificial Analysis/공식 블로그) 기반 수치만 채택.

---

## 1. 성능지표·벤치마크 — 무엇을 재나 / 측정 방식

| 벤치마크 | 측정 대상 | 규모·형식 | 측정 방식 |
|---|---|---|---|
| **MMMU** | 대학 수준 다학제 멀티모달 이해·추론(예술/경영/과학/의학/인문사회/공학 6개 분야, 30개 세부) | 약 11.5K 객관식(4지선다), 시험·교재·퀴즈 출처, ~30종 이미지(차트·도표·악보·화학구조 등) interleaved | 정확도(accuracy). zero-shot 기본 |
| **MMMU-Pro** | MMMU 강건화 버전(오염·텍스트만으로 풀림 방지) | 3단계: ①텍스트 전용 모델이 푸는 문항 제거 ②선택지 증강 ③질문을 이미지 안에 박은 vision-only 세팅 | 정확도. 진짜 시각이해 필요 |
| **MMBench** | 인지능력 세분 평가(지각→인지 20개 능력축) | 약 3,000 객관식, OpenCompass 제작 | 정확도. CircularEval(선택지 순환)로 추측 방지 |
| **MMStar** | "시각 필수(vision-indispensable)" 문항만 엄선 — 이미지 없이 풀리는 문항 제거 | 1,500 인간 선별 샘플, 6개 핵심능력·18축 | 정확도 |
| **MathVista** | 시각적 맥락에서의 수학적 추론 | 6,141 예제(28개 기존 데이터셋+신규 3개), mini=1,000 | 정확도 |
| **DocVQA** | 문서 이미지 기반 VQA(OCR+레이아웃+추론) | 5만 문항 / 1.2만+ 문서 이미지 | ANLS(정답 문자열 유사도) / accuracy |
| **ChartQA** | 차트·인포그래픽에 대한 시각+논리 추론 QA | 사람작성+기계생성 질의 혼합 | relaxed accuracy(수치 5% 오차 허용) |
| **AI2D** | 초등 과학 다이어그램 이해 | 5,000+ 다이어그램, 15,000+ 객관식 | 정확도 |
| **VQAv2** | 개방형 일반 VQA(시각인식·접지·공간추론+언어) | 100만+ Q-A쌍, COCO 이미지 기반 | VQA accuracy(다수결 정답 매칭). 이제 거의 포화/구식 |
| **Video-MME** | 영상 이해 종합(최초 풀스펙트럼) — 6개 도메인·30개 세부, 11초~1시간(단/중/장) | 비디오+자막+음성 멀티모달 입력 | 정확도. (v2는 3단계 난이도 위계) |
| **MME** | 멀티모달 LLM 종합(지각+인지 14개 하위태스크) | 예/아니오 형식 | 점수 합산(perception/cognition 별도) |
| **HLE (Humanity's Last Exam)** | "인류 지식 최전선" 폐쇄형 학술 최종시험, 멀티모달 포함 | 2,500 문항, 수십개 과목(수학·인문·자연과학) | 정확도(%). 프런티어 모델도 낮게 나오도록 설계 |

**핵심 트렌드**: MMMU·VQAv2·AI2D 등은 프런티어 모델 기준 사실상 **포화(saturation)**. 변별력 확보 위해 MMMU-Pro / HLE / Video-MME 등 난이도 높은 벤치로 이동. (출처: [benchmarkingagents.com/mmlu](https://benchmarkingagents.com/mmlu/), [MMMU-Pro OpenReview](https://openreview.net/forum?id=2jTdHYuguF))

---

## 2. 세계 최고 수준 (2026, 검증 수치)

### 사람 기준선(human baseline)
- **MMMU**: 전문가 최저 76.2% ~ 최고(medium expert) **88.6%**. (출처: [MMMU 논문 arXiv:2311.16502](https://arxiv.org/pdf/2311.16502), [llmindex.net](https://llmindex.net/benchmarks/mmmu))
- 참고: GPT-4V(2023) MMMU ~56% → 2026 프런티어는 사람 상위 전문가 수준에 근접/도달.

### 프런티어 모델 점수 (2026 상반기)

**MMMU-Pro** (가장 변별력 있는 대표 지표, 2026 기준 81~83%대 클러스터)
| 모델 | MMMU-Pro |
|---|---|
| GPT-5.5 | 82.8% |
| Gemini 3 Deep Think | 82.1% |
| Gemini 3 Pro | 81.0% |
| Claude Opus 4.7 | 81.4% |
| Qwen 3.5 Omni | 81.0% |
| GPT-5.1 | 76.0% |
출처: [digitalapplied.com 멀티모달 벤치 2026](https://www.digitalapplied.com/blog/multimodal-ai-benchmarks-2026-vision-audio-code), [vellum.ai Gemini 3 벤치](https://www.vellum.ai/blog/google-gemini-3-benchmarks)

**MMMU (원판, val)**: Claude Opus 4.7 ≈ **84.1%** (출처: [mindstudio.ai Opus 4.7 벤치](https://www.mindstudio.ai/blog/claude-opus-47-benchmark-breakdown))

**DocVQA**
| 모델 | DocVQA |
|---|---|
| Claude Opus 4.7 | 93.0% |
| GPT-5.5 | 91.5% |
| Gemini 3 | 90.8% |
| Qwen 3.5 Omni | 87.9% |

**ChartQA**: GPT-5.5 92.1% / Gemini 3 89.4% / Opus 4.7 88.0% / Qwen3.5 Omni 87.2%
**AI2D**: GPT-5.5 96.2% / Gemini 3 95.4% / Opus 4.7 94.8% / Qwen3.5 Omni 93.0%
**MathVista**: Claude Opus 4.7 ≈ 79.3% (전세대 대비 +9.5p). 그 외 프런티어 2026 수치는 출처별 일관성 부족 → **부분 미확인**
**Video-MME**: Gemini 3 Deep Think 78.4% / GPT-5.5 71.2% / Qwen3.5 Omni 69.5% / Opus 4.7 67.8%
**Video-MMMU**: Gemini 3 Pro 87.6% (출처: Google 공식)
출처: [digitalapplied.com](https://www.digitalapplied.com/blog/multimodal-ai-benchmarks-2026-vision-audio-code), [Gemini 3 Pro 공식 eval PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_model_evaluation.pdf)

**HLE (Humanity's Last Exam)** — Artificial Analysis 1차 leaderboard 기준
| 모델 | HLE |
|---|---|
| Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 fallback) | 53.3% |
| Claude Opus 4.8 (Adaptive Reasoning, Max Effort) | 45.7% |
| Gemini 3.1 Pro Preview | 44.7% |
| GPT-5.4 | 41.6% |
출처: [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam). ※ 멀티모달 포함 종합지표. 집계 사이트별 편차 큼(방법론 상이).

> **모델명 주의**: 2026 상반기 실존 프런티어 라인업은 대략 GPT-5.x(5.1/5.2/5.5), Gemini 3 / 3.1 Pro / Deep Think, Claude Opus 4.5~4.8 / Fable 5, Qwen 3.5 Omni 수준으로 확인됨. 그 이상 버전(예: GPT-5.4 Pro, "Mythos")은 집계 사이트 가공 가능성 있어 채택 시 주의.

---

## 3. 국내 최고 수준 (검증 수치)

### NAVER HyperCLOVA X 32B Think (Vision-Language, 2026.01 기술보고서)
한국어·한국문화 추론 특화 VLM. vision-to-text 벤치(Table 5):
| 벤치 | 점수 |
|---|---|
| DocVQA | 95.5 |
| TextVQA | 85.4 |
| SEED-IMG | 77.9 |
| LLaVA-W | 106.4 |
| **K-DTCBench**(한국어 문서·표·차트) | 93.3 |
| **K-MMBench**(한국어 MMBench) | 88.1 |
| **KoNET**(한국 시험) | 75.1 |
비교군: Qwen3-VL 32B-Thinking, InternVL3.5 38B-Thinking. ※ MMMU/MathVista/ChartQA는 보고서 미수록 → 해당 항목 **미확인**.
출처: [HyperCLOVA X 32B Think arXiv:2601.03286](https://arxiv.org/html/2601.03286)
- 참고: HyperCLOVA X 8B Omni는 DocVQA에서 동급 2위 수준. (출처: [arXiv:2601.01792](https://arxiv.org/html/2601.01792v1))

### LG EXAONE 4.5 (33B, Open-weight VLM, 2026.04 기술보고서)
"Physical AI/산업지능" 지향 오픈웨이트 VLM. (Reasoning 모드, Table 2):
| 벤치 | 점수 |
|---|---|
| MMMU | 78.7 |
| MMMU-Pro | 68.6 (GPT-5-mini 67.3 상회 주장) |
| MathVista (mini) | 85.0 |
| AI2D | 89.0 |
| ChartQAPro | 62.2 |
| OCRBench v2 | 63.2 |
| OmniDocBench v1.5 | 81.2 |
| **KMMMU**(한국어 MMMU) | 42.7 |
| **K-Viscuit** | 80.1 |
| **KRETA** | 91.9 |
- STEM 5개 벤치 평균 77.3 → GPT-5-mini(73.5), Claude Sonnet 4.5(74.6), Qwen3-235B(77.0) 상회 주장.
출처: [EXAONE 4.5 기술보고서 arXiv:2604.08644](https://arxiv.org/html/2604.08644), [LG 보도 PR Newswire](https://www.prnewswire.com/news-releases/lg-reveals-next-gen-multimodal-ai-exaone-4-5-302736993.html)

### Upstage Solar Pro 2
Frontier LM Intelligence leaderboard 유일 한국 모델로 언급. ※ 멀티모달(vision) 전용 벤치 공개 수치는 **미확인**. (출처: [marktechpost 한국 LLM 정리](https://www.marktechpost.com/2025/08/21/meet-south-koreas-llm-powerhouses-hyperclova-ax-solar-pro-and-more/))

### 카카오
공개된 멀티모달 벤치 점수 **미확인**.

> **국내 vs 세계 격차 메모**: 국내 모델은 한국어 멀티모달(K-* 벤치)에서 강하지만, 글로벌 공통 지표(MMMU-Pro)에선 EXAONE 4.5 68.6 vs 프런티어 81~83%로 약 13~15p 차이. 단 EXAONE은 33B 오픈웨이트 / 프런티어는 비공개 초대형이라 동급 비교는 아님. KMMMU(한국어판)는 42.7로 절대값 낮음 → 한국어 멀티모달 난이도가 높고 헤드룸 큼.

---

## 4. 평가 환경 (방법론·오염)

- **zero-shot / CoT**: MMMU·MMMU-Pro 기본은 zero-shot. CoT(Chain-of-Thought)는 일반적으로 점수 향상(특히 MathVista 류 추론). OCR 프롬프트는 영향 미미. (출처: [PathCoT](https://arxiv.org/html/2507.01029v1), [FewMMBench arXiv:2602.21854](https://arxiv.org/html/2602.21854))
- **with/without tools 구분**: 2026 보고에선 도구사용 유무를 분리 표기(예: GPT-5.2 MMMU-Pro 79.5% no-tools / 80.4% tools). 비교 시 동일 조건 확인 필수.
- **오염(contamination) / 포화(saturation)**:
  - 원판 MMMU·VQAv2·AI2D는 프런티어 기준 포화 → 변별력 상실. MMLU/MMMU 원판은 "프런티어 비교용으로 쓰지 말 것" 권고.
  - MMMU-Pro가 오염 대응: ①텍스트만으로 풀리는 문항 제거 ②선택지 증강(추측 방지) ③vision-only(질문을 이미지에 박음).
  - HLE는 애초에 "최전선·미공개 난이도"로 오염 회피 설계.
  출처: [benchmarkingagents.com](https://benchmarkingagents.com/mmlu/), [MMMU-Pro arXiv:2409.02813](https://arxiv.org/pdf/2409.02813)
- **집계 사이트 신뢰성**: 일부 leaderboard가 가공 모델명·수치 혼입 → 1차 출처(모델 카드/논문/Artificial Analysis) 교차검증 필수.

---

## 5. 개발기간별 목표 제안 (멀티모달 플랫폼 신규 개발 시)

전제: 신규 팀이 오픈웨이트 베이스(Qwen3-VL / InternVL 계열 등)에서 출발, 한국어 멀티모달 특화. 현 SOTA(MMMU-Pro 81~83%, DocVQA 93%, 국내 EXAONE 4.5 MMMU 78.7)를 기준으로 **보수적** 제안.

| 연차 | 목표(대표 지표) | 근거 |
|---|---|---|
| **1년차** | MMMU val 70%+ / DocVQA 88%+ / ChartQA 80%+ / 한국어 K-MMBench 80%+ | 오픈웨이트 SFT+한국어 데이터로 도달 가능 구간. 사람 baseline(MMMU 76~88%) 하단 근접. EXAONE/HyperCLOVA가 이미 입증한 현실선. |
| **2년차** | MMMU val 78%+ / MMMU-Pro 68%+ / DocVQA 92%+ / MathVista 80%+ / 한국어 K-DTCBench 90%+ | EXAONE 4.5(33B) 2026 수준 도달. 오염 대응형 MMMU-Pro에서 국내 SOTA권 진입. CoT·RLHF 고도화 필요. |
| **3년차** | MMMU-Pro 75%+ / DocVQA 93%+ / Video-MME 70%+ / KMMMU 55%+ | 글로벌 프런티어(81~83%) 대비 약 5~8p 추격. 비디오·장문서 등 신규 모달 확장. 한국어 헤드룸(KMMMU 42→55) 집중 공략이 차별화 포인트. |

**근거 요약**:
- 단일 지표 100% 목표 금지 — 사람 baseline(MMMU 88.6%)·포화 한계 고려.
- 원판 MMMU·VQAv2 같은 포화 벤치를 KPI로 잡지 말고, **MMMU-Pro·DocVQA·Video-MME + 한국어 K-*** 조합으로 변별력 확보.
- 국내 강점(한국어 문서·표·차트, K-DTCBench/KRETA 90%+)을 1·2년차 조기 달성 목표로, 글로벌 공통 추론(MMMU-Pro)은 3년차 추격 목표로 분리.
- 3년차에도 프런티어 동률은 비현실적(파라미터·데이터·컴퓨트 격차) → "동급 오픈웨이트 SOTA + 한국어 1위"가 현실적 승리조건.

---

## 6. 미확인 항목 (추가 조사 필요)

- **MathVista** 프런티어 2026 전체 비교표(Opus 4.7 79.3% 외 GPT/Gemini 동시점 수치 일관성 부족).
- **MMStar·MMBench·MME** 프런티어 2026 수치(검색 결과 미수록).
- **HyperCLOVA X**의 MMMU/MMMU-Pro/MathVista/ChartQA(보고서 vision 표에 미수록).
- **Upstage Solar Pro 2 / 카카오**의 멀티모달(vision) 공개 벤치 점수.
- **VQAv2** 2026 프런티어 수치(사실상 포화·구식이라 최신 보고 거의 없음).
- HLE 멀티모달 vs 텍스트전용 분리 점수의 모델별 정합성(집계처별 편차).
- 2026 후반 모델명(GPT-5.4/5.5, Claude Fable 5, Gemini 3.1) 일부는 1차 모델카드 미확인 → 집계 사이트 의존.
