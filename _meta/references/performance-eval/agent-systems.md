# 리서치 노트: 에이전트 시스템 + 제조현장 멀티에이전트(복합)의 성능평가

> 자료조사용 구조화 노트. 블로그 글 아님. 모든 수치는 WebSearch/WebFetch로 확인한 것이며, 미확인은 명시함.
> 조사일: 2026-06-26. 검색 결과는 US 기준, 일부 출처는 모델명·날짜가 매우 최신(2026)이라 **2차 출처(요약 사이트)임을 감안해 인용**할 것.

---

## 0. 핵심 요약 (한눈에)

- **일반 에이전트 평가의 표준 지표**: 최종 성공률(success rate, end-state 검증) + 궤적(trajectory) 평가 + 도구 호출 정확도 + 비용/지연 + **신뢰성(pass^k)**. "결과만 보면 거짓말한다(trajectory 봐야 한다)"가 2026년 컨센서스.
- **pass@k vs pass^k**: pass@k=k회 중 1회라도 성공할 확률(역량), pass^k=k회 **모두** 성공할 확률(일관성·배포 기준). 핵심 함정: per-trial 75%면 pass@3=98.4%인데 pass^3=42%. **배포 임계값은 pass^k로 잡아야 함.**
- **벤치마크 SOTA(2026)**: τ²-bench telecom ~99%, SWE-bench Verified ~88~95%, GAIA(시스템 기준) ~91~92%(휴먼 92%), WebArena ~74%(휴먼 ~78%). → 코딩·툴콜은 사실상 포화, **웹·범용 장기과업은 여전히 휴먼 미달**.
- **제조 비전 검사**: 현대 AI 검사 정확도 97~99%대 주장, escape rate를 2.3%→0.1% 줄인 사례. 단, **검출률↑은 항상 오검출(false call)↑와 트레이드오프** — 이게 제조 평가의 핵심.
- **제조 운영지표**: World-class OEE=85%(가용 90%×성능 95%×품질 99.9%), 글로벌 평균은 55~65%. 품질 99.9%가 "세계 최고" 기준선.

---

## 1. 일반 에이전트 시스템 평가 지표·벤치마크

### 1-1. 무엇을 재는가 (평가 계층)

세 계층으로 본다 (출처: Confident AI, morphllm, TianPan):

| 계층 | 측정 대상 | 대표 지표 |
|---|---|---|
| Final-answer | 마지막 메시지/최종 상태 | Success rate (end-state 검증), task completion |
| Trajectory | 도구 호출·단계의 **순서** | Trajectory match, tool-call accuracy, step/loop count |
| Per-turn | 운영 중 각 턴의 의미 | groundedness, per-turn 점수 |

- **도구 호출 정확도 세부**: Tool Selection Accuracy(올바른 도구 선택 또는 올바른 abstain 비율), Parsing Accuracy(추출 파라미터가 ground truth와 일치하는 비율).
- **비용/지연**: Latency=요청당 wall-clock(초), Cost=벤치 전체 API 비용(USD). "정확도와 비용을 함께 채점하지 않으면 에이전트가 무한 API 호출로 미세이득을 좇는다" → **cost–accuracy Pareto frontier**로 평가 권장.
- **궤적 평가의 효용**: 최종답이 틀렸을 때 추론 과정 어디서 실패했는지 정확히 짚어줌. "결과만 채점하면 거짓말한다(Grading outcomes alone will lie to you)".

### 1-2. pass@k vs pass^k (신뢰성·비결정성의 핵심)

(출처: agentpatterns.ai, philschmid.de, Confident AI)

- **pass@k** = k회 독립 시도 중 **최소 1회** 성공 확률 → **역량(capability)** 평가용. 개발 중 "풀 수 있나?" 판단.
- **pass^k** = k회 **모두** 성공 확률 → **일관성(consistency)·배포 기준**.
- 분기 예시(검증됨):
  - per-trial 75% → pass@3 = 98.4%, **pass^3 = 42%**
  - per-trial 70% → 두 지표 차이 **60%p 이상**. per-trial이 90%대 후반으로 올라가야 격차가 닫힘.
- **사용 원칙**:
  - pass@k 낮음 → 역량 부족(문제 자체를 못 품).
  - pass@k 높은데 pass^k 낮음 → 일관성 문제 → 명확한 지시·낮은 temperature·검증 단계 추가로 해결.
  - 자동 파이프라인이 5% 초과 실패를 못 견디면 → **승격 전 pass^k ≥ 0.95 요구**.

### 1-3. 평가 환경 — 비결정성 대응

(출처: agentpatterns.ai, arxiv 2601.15322 Replayable Financial Agents)

- 비결정성의 원천: 확률적 모델 출력, 도구 지연, 부분 실패, 적응적 의사결정. → **단일 실행은 표본크기 1**.
- 권고: **중요 과업은 최소 k=3 다회 측정**, pass@k와 pass^k **둘 다 보고**.
- 결정성 확보 기법: 낮은 temperature, 시드 고정, replay/determinism-faithfulness harness(금융 등 고위험 도메인).
- LiveMathBench의 **G-Pass@k**: 일관성을 정량화하는 일반화 지표(난이도별 안정성).

### 1-4. 주요 벤치마크 — 무엇을 재나 + 2026 SOTA

> ⚠️ SOTA 점수는 2차 요약 사이트(llm-stats, artificialanalysis, steel.dev, BenchLM 등) 기준. 모델명이 매우 최신(2026)이라 1차 검증이 어려운 항목은 △표시.

| 벤치마크 | 무엇을 재나 | 휴먼 기준 | 2026 SOTA (확인된 값) | 출처 |
|---|---|---|---|---|
| **τ-bench / τ²-bench** | 고객서비스 에이전트, **dual-control**(유저·에이전트 둘 다 툴콜) 대화. Dec-POMDP 프레임. 추론오류 vs 소통/조정오류 분리 | — | telecom: **JT-35B-Flash / GLM-5.2 99.1%**, Claude Opus 4.6 0.993△ / airline: LongCat-Flash-Thinking 0.765△ | artificialanalysis.ai, llm-stats.com |
| **SWE-bench Verified** | 실제 GitHub 이슈 해결(Python 500개, 사람 검수). **실제 테스트 실행**으로 채점 | — | Claude Mythos 5 **95.5%**△, Fable 5 95%△, **Opus 4.8 88.6%**△ (2026-06-18 기준) | steel.dev leaderboard, localaimaster |
| **GAIA** | 범용 AI 어시스턴트. 추론+멀티모달+웹브라우징+툴사용. Level1(<5스텝)/L2(5~10)/L3(최대50스텝) 466~466개 | **92%** | 시스템 기준 OPS-Agentic-Search **92.36%**△, Lemon Agent **91.36%**(L1 96.77/L2 89.31/L3 87.76)△ / 베어모델 스냅샷은 ~50%대 | arxiv 2311.12983, steel.dev, HAL(Princeton) |
| **WebArena** | 자가호스팅 실제 웹사이트 812개 과업(이커머스·포럼·CMS·맵 등). 장기과업, **프로그램적 채점(LLM judge 없음)** | **~78.24%** | WebTactix(DeepSeek v3.2) **74.3%**△, Claude Mythos Preview 68.7%△. (원조 GPT-4 베이스라인 14.41%) | steel.dev, awesomeagents.ai |
| **AgentBench** | 멀티환경(OS·DB·웹·게임 등) 종합 에이전트 역량 | — | (확정 SOTA 미확인 — 최신 단일 SOTA 수치 못 찾음) | benchmarkingagents.com |

**해석 메모**:
- SWE-bench·τ-bench는 사실상 **포화(90%대 후반)**. 단, SWE-bench는 "성숙·학습데이터 노출·일부 결함 테스트" 오염 caveat 있음 → 고점수는 보수적으로 해석.
- GAIA/WebArena는 **scaffold(스캐폴드) 의존성**이 커서, HAL(스캐폴드 통제) 숫자와 베어모델 숫자가 의미가 다름. 점수 비교 시 "모델+툴+정책" 셋업인지 확인 필수.
- WebArena·GAIA처럼 **장기·범용 과업은 아직 휴먼에 못 미치거나 막 따라잡는 수준** → 제조 같은 실세계 복합 시스템 목표 설정 시 현실적 근거.

---

## 2. 제조현장 멀티에이전트(복합) 시스템 평가 지표

### 2-1. 비전 검출 정확도 + 운영지표 결합

제조 복합 시스템은 **"검출 성능"과 "라인 운영지표"를 결합**해 평가한다.

#### (a) 검출 성능 지표 (분류기 관점)
- **결함 검출률 / Recall** = 실제 결함 중 잡아낸 비율
- **미검출률 / Escape rate / FNR** = 결함이 빠져나간 비율 (= 1 − Recall). 고객 유출 직결 → 가장 치명적
- **오검출률 / False call rate / FPR** = 양품을 불량으로 오판한 비율 → 양품 폐기·라인 정지·재검 비용
- **핵심 트레이드오프**: 임계값(threshold)을 낮추면 escape↓ 대신 false call↑. 둘을 동시에 0으로 못 만든다. (arxiv 2506.14521 "false call reduction" — PCB AOI 사례, 임계값 의존 트레이드오프를 PCA·threshold 분석으로 다룸. ※구체 수치는 PDF 텍스트 추출 실패로 **미확인**)

#### (b) 확인된 검출 성능 수치 (산업 주장값 — 벤더 블로그 다수, 보수적 해석 필요)

| 지표/사례 | 값 | 출처 | 비고 |
|---|---|---|---|
| 현대 AI 비전 검사 정확도 | **97~99%**, 일부 99.7% | ifactoryapp, agmis | 벤더 주장 |
| 처리량 | **10,000+ parts/hour**, sub-100ms 지연 | ifactoryapp | 벤더 주장 |
| Escape rate 개선 사례(전자) | **2.3% → 0.1%** (연 $1.8M 보증비용 절감) | ifactoryapp | 단일 사례 |
| 레거시 시스템 오탐 | **false positive 50%** | ifactoryapp | 비교 기준선 |
| 인간 육안검사 검출률 | 좋은 날 **80%**, 피로 시 **60%** | ifactoryapp | 비교 기준선 |
| AI 도입 후 검출률 | **95%** (엣지서버+라벨 500장) | ifactoryapp | 단일 사례 |
| 사례: BMW 결함 37%↓ / Foxconn 검출률 80%↑ | — | ifactoryapp | 단일 사례 |
| 반도체 yield detraction 감소 | **최대 30%** (AI 알고리즘) | netguru | 사례 |
| 첨단 노드 yield loss(현실) | **20~30%** | netguru | 도전 과제 |

> ⚠️ 위 검출 수치 대부분이 벤더/솔루션 블로그(ifactoryapp 등) 출처. **학술 표준 벤치 수치가 아니라 마케팅 주장**일 수 있으니 인용 시 "업계 주장" 명시 권장. 학술 벤치 리뷰는 arxiv 2305.13261 "A Review of Benchmarks for Visual Defect Detection in Manufacturing" 참조(개별 수치는 데이터셋별 상이).

#### (c) 라인 운영지표 (의사결정·시스템 관점)

(출처: Godlan, Evocon, Tractian, lean6sigmahub, tvsnext)

| 지표 | 정의 | World-class 기준 | 현실 평균 |
|---|---|---|---|
| **OEE** (Overall Equipment Effectiveness) | 가용성×성능×품질 | **85%** (Nakajima/TPM 1980s) | 글로벌 discrete 평균 **55~65%** |
| └ Availability | 가동 시간 비율 | ≥ 90% | — |
| └ Performance | 속도 효율 | ≥ 95% | — |
| └ **Quality** | 양품 비율 | **≥ 99.9%** | — |
| **UPH** (Units Per Hour) | 시간당 생산수량(처리량) | 라인별 상이 | — |
| OTIF | On-Time In-Full 납기 | P&L 가시 KPI | — |

- **주의(검증된 비판)**: "85% world-class"는 **이산·반복 제조** 기준. 연속공정·자본집약·규제산업은 설계상 더 낮음. 글로벌 평균은 55~65%로, 85% 지속 달성 공장은 극소수. → "OEE 85%를 무조건 목표로 잡지 말라"는 lean6sigmahub의 경고.

### 2-2. 멀티에이전트 시스템 자체의 평가 지표

(출처: usmsystems, tech-stack, arxiv 2603.29755 CausalPulse, arxiv 2602.16738)

- **MAS 성능 지표**: Iterations(평균 오류수정 횟수), Token Usage, Pass Rate(성공 완료 비율), Cost.
- **제조 적용 시 의사결정 정확도**: inspection agent가 결함을 조기 플래그 → upstream 설정과 상관분석 → 파라미터 조정 또는 hold-and-alert 제안. 이때 **"제안의 정확도(오경보로 라인 멈추지 않았나)"**가 의사결정 품질 지표.
- 2026 제조 평가 프레임: 단순 비용절감/usage가 아니라 **systemic performance uplift** — 4범주(financial / operational / data·model quality / strategic). KPI는 cycle time·throughput·quality·OEE·scrap rate·energy에 묶어라.
- 관련 학술(2026): CausalPulse(스마트제조 인과진단 뉴로심볼릭 MAS), Self-Evolving MAS for IIoT 예지보전 — 단, 표준화된 정확도 SOTA 수치는 도메인·데이터셋별로 달라 단일 SOTA 없음.

---

## 3. 세계 최고 / 국내 최고 수준

### 세계 최고 (벤치 SOTA, 위 표 재인용)
- τ²-bench telecom **~99%**, SWE-bench Verified **88~95%**, GAIA(시스템) **~92%**, WebArena **~74%**.
- 제조 검출: 업계 주장 **99%대 정확도 / escape 0.1%**, 운영지표 **OEE 85%·품질 99.9%**가 world-class 기준선.

### 국내 (확인된 범위)
- **삼성전자**: 2030년까지 국내외 공장 **'AI 자율 공장'** 전환 선언. 품질·생산·물류 영역별 **AI 에이전트**로 분석·예측 정확도 제고 (출처: 디일렉 thelec.kr). ※구체 검출률 수치는 **미확인**.
- **LG에너지솔루션**: 배터리 양극/음극 용접(패키지 웰딩) 공정 신규 불량을 **이상탐지 모델**로 최종 검출, 불량 유출 최소화 과제 진행 (출처: inside.lgensol.com, 2023). ※수치 **미확인**.
- **LG전자**: 스마트팩토리 고도화 + 오피스 자동화를 멀티에이전트로 연결 지향 (출처: 디일렉). ※수치 미확인.
- → **국내 사례는 "방향성·선언" 수준만 공개**, escape rate/검출률 같은 정량 수치는 공개 출처에서 확보 실패(미확인).

---

## 4. 개발기간별 목표 제안 (제조 멀티에이전트 신규 개발, 보수적)

> 근거: ①world-class 품질 99.9%·OEE 85%는 수년 누적의 결과(현실 평균 55~65%)이므로 신규 개발이 1년에 도달 불가. ②검출률↑↔오검출률↑ 트레이드오프 때문에 "검출률"만 올리는 1년차 목표는 위험 → escape와 false call을 **함께** 목표화. ③에이전트 신뢰성은 pass@k(역량) → pass^k(일관성) 순으로 성숙하므로 연차별로 신뢰성 지표를 강화. ④WebArena/GAIA 사례처럼 복합·장기 과업은 휴먼 추월에 시간이 걸림.

| 항목 | 1년차 (PoC/파일럿) | 2년차 (라인 실증) | 3년차 (양산 적용) |
|---|---|---|---|
| **결함 검출률(Recall)** | ≥ 90% (특정 결함군 한정) | ≥ 95% (주요 결함군 전반) | ≥ 98~99% |
| **미검출률(Escape/FNR)** | ≤ 5% (치명결함은 ≤1% 우선) | ≤ 2% | ≤ 0.5% (치명결함 ≈0 지향) |
| **오검출률(False call/FPR)** | ≤ 15% (재검 허용) | ≤ 5% | ≤ 1~2% |
| **에이전트 신뢰성** | 핵심과업 **pass@3 ≥ 0.9** (역량 확보) | 핵심과업 **pass^3 ≥ 0.9** (일관성) | 자동의사결정 **pass^k ≥ 0.95** |
| **자동화율(인간개입 없는 판정 비율)** | 30~50% (사람 검증 병행) | 60~80% (hold-and-alert 중심) | 85~95% (예외만 에스컬레이션) |
| **OEE 기여 / 처리량** | 측정체계 구축·베이스라인 확보 | 품질지표(scrap↓) 개선 입증 | OEE 품질항목 99%대 기여, UPH 손실 0에 수렴 |
| **평가방식** | 다회측정(k≥3)·시드고정 도입 | trajectory+비용 동시채점 | 운영 중 per-turn 모니터링·드리프트 감시 |

**전제·면책**:
- 위 수치는 **일반 트레이드오프 원리 + world-class 기준선에서 역산한 보수적 제안**이며, 특정 제품·결함난이도(미세결함·신규불량 등)에 따라 크게 달라짐.
- 치명결함(고객·안전 직결)은 연차 무관 **escape를 최우선 0에 수렴**시키고, 대신 false call을 양보하는 정책이 일반적.
- 자동화율·검출률 목표는 라인 데이터·라벨 확보량과 직결(사례: 라벨 500장으로 95% 도달했으나, 이는 결함이 비교적 명확한 경우).

---

## 5. 미확인 / 후속조사 필요 항목

1. **τ²-bench·SWE-bench·GAIA·WebArena의 2026 정확 SOTA 점수**: 2차 요약사이트 기준이라 모델명·수치가 1차(공식 리더보드)와 다를 수 있음. 인용 전 공식 리더보드(sierra-research/tau2-bench GitHub, swebench.com, HAL Princeton, webarena 공식) 재확인 권장.
2. **AgentBench 2026 단일 SOTA 수치**: 확정값 확보 실패.
3. **arxiv 2506.14521(false call reduction)의 구체 FPR/escape 수치**: PDF 텍스트 추출 실패로 미확인 → 필요 시 HTML/ar5iv 버전 재시도.
4. **국내(삼성·LG 등) 정량 검출률·escape rate**: 공개 출처에 수치 없음(선언·방향성만). 기업 발표자료·논문 추가 탐색 필요.
5. **제조 비전 검출 99%대 주장의 출처 신뢰도**: ifactoryapp 등 벤더 블로그 다수 → 학술 데이터셋(MVTec AD 등) 기준 수치로 교차검증 권장(arxiv 2305.13261 리뷰 활용).
6. **OEE의 AI/MAS 직접 기여분 분리 측정**: "AI로 OEE 몇 %p 상승"의 인과 입증 사례는 대부분 단일·벤더 사례 → 통제된 연구 필요.

---

## 출처 (URL)

**일반 에이전트 평가·벤치마크**
- pass@k/pass^k: https://agentpatterns.ai/verification/pass-at-k-metrics/ , https://www.philschmid.de/agents-pass-at-k-pass-power-k
- 궤적·툴콜·비용 평가: https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide , https://www.morphllm.com/ai-agent-evaluation , https://tianpan.co/blog/2026-02-07-evaluating-ai-agents-trajectories-not-just-outcomes
- 비결정성 harness: https://arxiv.org/pdf/2601.15322
- τ²-bench: https://artificialanalysis.ai/evaluations/tau2-bench , https://llm-stats.com/benchmarks/tau2-telecom , https://github.com/sierra-research/tau2-bench
- SWE-bench Verified: https://leaderboard.steel.dev/leaderboards/swe-bench-verified/ , https://localaimaster.com/models/swe-bench-explained-ai-benchmarks , https://www.codeant.ai/blogs/swe-bench-scores
- GAIA: https://arxiv.org/pdf/2311.12983 , https://leaderboard.steel.dev/leaderboards/gaia/ , https://hal.cs.princeton.edu/gaia
- WebArena: https://leaderboard.steel.dev/leaderboards/webarena/ , https://awesomeagents.ai/leaderboards/web-agent-benchmarks-leaderboard/
- AgentBench(개관): https://benchmarkingagents.com/agent-benchmarks/

**제조 검출·운영지표·MAS**
- 비전검사 정확도/escape 사례: https://ifactoryapp.com/article/ai-vision-inspection-manufacturing-defect-detection , https://agmis.com/ai-quality-control-in-manufacturing-the-path-to-99-defect-detection/
- false call 트레이드오프(학술): https://arxiv.org/pdf/2506.14521
- 결함검출 벤치 리뷰(학술): https://arxiv.org/pdf/2305.13261
- 반도체 yield AI: https://www.netguru.com/blog/yield-detraction-semiconductor-manufacturing-ai
- OEE 기준: https://evocon.com/articles/world-class-oee-industry-benchmarks-from-more-than-50-countries/ , https://godlan.com/oee-benchmark-industry/ , https://lean6sigmahub.com/the-oee-lie-why-world-class-85-is-just-a-number/
- 제조 MAS·KPI: https://usmsystems.com/agentic-ai-trends/ , https://tech-stack.com/blog/ai-adoption-in-manufacturing/ , https://arxiv.org/pdf/2603.29755 (CausalPulse), https://arxiv.org/pdf/2602.16738

**국내 사례**
- 삼성 AI 자율공장: https://www.thelec.kr/news/articleView.html?idxno=52887
- LG에너지솔루션 불량유출 최소화: https://inside.lgensol.com/2023/04/
