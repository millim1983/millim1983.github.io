# evidence - ma-02-multiagent-research-directions

열람일: 2026-10-22 (전 출처 공통). 모든 논문은 arXiv PDF 전문을 내려받아 텍스트 추출 후 해당 절을 직접 읽었다.

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Why Do Multi-Agent LLM Systems Fail? | Mert Cemri, Melissa Z. Pan, Shuyi Yang 외 (UC Berkeley) | 2025 (NeurIPS 2025 D&B, arXiv v3) | https://arxiv.org/abs/2503.13657 | 초록, 1절, 그림1, 4절 FC1~FC3, 5절, 부록 H 표5 |
| S2 | Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems | Shaokun Zhang, Ming Yin 외 | 2025 (ICML 2025, arXiv v3) | https://arxiv.org/abs/2505.00212 | 초록, 4.1절(세 방법), 표1 캡션 |
| S3 | Towards a Science of Scaling Agent Systems | Yubin Kim, Ken Gu 외, Daniel McDuff, Xin Liu (Google Research, Google DeepMind, MIT) | 2025 (arXiv v3 2026-04-08) | https://arxiv.org/abs/2512.08296 | 초록, 1절 기여, 3절 토폴로지 정의, 5절 Limitations |
| S4 | Automated Design of Agentic Systems | Shengran Hu, Cong Lu, Jeff Clune | 2024 (ICLR 2025) | https://arxiv.org/abs/2408.08435 | 초록, 1절, 3절 Meta Agent Search, 4절 전이 결과, Safety Considerations |
| S5 | AFlow: Automating Agentic Workflow Generation | Jiayi Zhang, Jinyu Xiang 외, Yuyu Luo, Chenglin Wu | 2024 (ICLR 2025) | https://arxiv.org/abs/2410.10762 | 초록, 1절, 3절 Operators, 4절 초기화, 5절 Main Results |
| S6 | MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman Ozdaglar, Kaiqing Zhang, Joo-Kyung Kim | 2025 | https://arxiv.org/abs/2502.18439 | 초록, 1절, 5절 Remark 2 |
| S7 | Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs (v1 제목 "Stronger Together: On-Policy Reinforcement Learning for Collaborative LLMs") | Yujie Zhao, Lanxiang Hu, Yang Wang, Minmin Hou, Hao Zhang, Ke Ding, Jishen Zhao | 2025 (arXiv v5 2026-01-29) | https://arxiv.org/abs/2510.11062 | 초록, 1절, 그림1, 4절 grouping |
| S8 | Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune) | Guibin Zhang, Yanwei Yue, Zhixun Li 외 | 2024 | https://arxiv.org/abs/2410.02506 | 초록, 1절 기여 |
| S9 | Latent Collaboration in Multi-Agent Systems (LatentMAS) | Jiaru Zou, Ruizhong Qiu 외, Mengdi Wang, Ling Yang | 2025 (ICML 2026, arXiv v4) | https://arxiv.org/abs/2511.20639 | 초록, 그림1, 3절 KV cache, 부록 G |
| S10 | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | Guibin Zhang, Muxin Fu, Guancheng Wan, Miao Yu, Kun Wang, Shuicheng Yan | 2025 | https://arxiv.org/abs/2506.07398 | 초록, 1절, 3절 query graph |
| S11 | MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents | Kunlun Zhu, Hongyi Du, Zhaochen Hong 외, Heng Ji, Jiaxuan You | 2025 | https://arxiv.org/abs/2503.01935 | 초록, 3절 시나리오, 에이전트 수 ablation |

## 본문 문장 ↔ 원문 발췌

### S1 MAST
- [MAST-Data는 7개 프레임워크 1600개 이상(1642개) 트레이스] ↔ "We introduce MAST-Data, a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks." / "a comprehensive, high-quality collection of 1642 annotated execution traces."
- [150개 트레이스를 Grounded Theory로 분석, κ=0.88, 14개 실패 모드, 3범주] ↔ "We develop MAST through rigorous analysis of 150 traces, guided closely by expert human annotators and validated by high inter-annotator agreement (κ = 0.88). This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification."
- [트레이스 평균 1만 5천 줄 이상] ↔ "a close analysis of over 150 MAS execution traces (each averaging over 15,000 lines of text)."
- [o1 기반 LLM 판정기 κ=0.77] ↔ "using OpenAI's o1 model. We calibrate the LLM annotator to achieve high agreement with human expert annotations (κ = 0.77)"
- [7개 오픈소스 MAS 실패율 41~86.7%] ↔ "analysis reveals 41% to 86.7% failure rate on 7 state-of-the-art (SOTA) open-source MAS"
- [멀티에이전트 이득이 단일 에이전트나 best-of-N 대비 작다는 문제 제기] ↔ "their performance gains often remain minimal compared to single-agent frameworks [18] or simple baselines like best-of-N sampling [19]."
- [범주 비율 44.2 / 32.3 / 23.5] ↔ 그림1 범주 수치 "44.2% 32.3% 23.5%"; 세부: "failing to follow task requirements (FM-1.1, 11.8%) or agent roles (FM-1.2, 1.5%), step repetitions (FM-1.3, 15.7%), context loss (FM-1.4, 2.80%), or not recognizing task completion (FM-1.5, 12.4%)" (합 44.2), FC3 "premature termination (FM-3.1, 6.20%), no or incomplete verification (FM-3.2, 8.20%), or incorrect verification (FM-3.3, 9.10%)" (합 23.5)
- [추론-행동 불일치 13.2%, 명확화 요청 실패 6.8%] ↔ "proceeding with wrong assumptions instead of seeking clarification (FM-2.2, 6.80%) ... or mismatches between reasoning and action (FM-2.6, 13.2%)."
- [MCP·A2A 같은 형식 표준화로는 FC2가 안 풀린다, 다른 에이전트의 정보 요구를 모델링 못 함] ↔ "the errors we observe in FC2 occur even when agents within the same framework communicate using natural language. This signals a deeper agent interaction dynamic challenge: the collapse of 'theory of mind' [48], where agents fail to accurately model other agents' informational needs."
- [검증자가 컴파일 여부·TODO 같은 표면 검사만 한다, 체스 예시] ↔ "many existing verifiers perform only superficial checks, despite being prompted to perform thorough verification, such as checking if the code compiles or if there are leftover TODO comments." / "a ChatDev-generated chess program passes superficial checks (e.g., code compilation) but contains runtime bugs because it fails to validate against actual game rules"
- [역할 명세 개선 +9.4%, 상위 목표 검증 단계 +15.6%] ↔ "improving agent role specifications alone yields a +9.4% success rate increase for ChatDev with the same user prompt and LLM (GPT-4o)." / "adding a high-level task objective verification step to ChatDev yields a +15.6% improvement in task success on ProgramDev"
- [ChatDev ProgramDev-v0 25.0 → 34.4 → 40.6, DAG를 순환 그래프로] ↔ 표5 "Baseline ... 25.0 / Improved prompt ... 34.4 / New topology ... 40.6"; "We modified the framework's topology from a directed acyclic graph (DAG) to a cyclic graph. The process now terminates only when the CTO agent confirms that all reviews are properly satisfied, with a maximum iteration cutoff"
- [개입 후에도 성공률 낮음, 한계] ↔ "Although first step interventions lead to performance gains, not all failure modes are resolved, and task completion rates still remain low"
- [MAST가 모든 실패를 덮는다고 주장하지 않음] ↔ "we do not claim it covers every potential failure pattern."

### S2 Who&When
- [127개 MAS의 실패 로그, 에이전트·결정적 오류 단계 주석] ↔ "we introduce the Who&When dataset, comprising extensive failure logs from 127 LLM multi-agent systems with fine-grained annotations linking failures to specific agents and decisive error steps."
- [최고 방법이 에이전트 53.5%, 단계 14.2%, o1·R1도 실용 수준 미달] ↔ "The best method achieves 53.5% accuracy in identifying failure-responsible agents but only 14.2% in pinpointing failure steps, with some methods performing below random. Even SOTA reasoning models, such as OpenAI o1 and DeepSeek R1, fail to achieve practical usability."
- [세 방법: all-at-once, step-by-step, binary search] ↔ "(1) All-at-once: An LLM is provided with a query and the complete failure log ... (2) Step-by-step: ... the failure log is presented step-by-step ... (3) Binary search: ... determining whether the mistake occurred in the upper half or lower half of the failure logs."
- [에이전트 수준은 all-at-once, 단계 수준은 step-by-step이 낫다] ↔ "For agent-level accuracy, all-at-once outperforms binary search, which in turn surpasses step-by-step. Conversely, for step-level accuracy, step-by-step achieves the best performance"

### S3 Scaling Agent Systems
- [260개 구성, 6개 벤치마크, 5개 아키텍처, 3개 모델 계열, 도구·프롬프트·연산 통제] ↔ "Across 260 configurations spanning six agentic benchmarks, five canonical architectures (Single-Agent and four Multi-Agent: Independent, Centralized, Decentralized, Hybrid), and three LLM families, we perform controlled evaluations standardizing tools, prompts, and compute to isolate architectural effects."
- [벤치마크 6종 이름] ↔ "(1) web browsing (BrowseComp-Plus [32]), (2) financial analysis (Finance-Agent [33]), (3) game planning (PlanCraft [21]), (4) realistic workplace tasks (Workbench [34]), (5) software engineering (SWE-bench Verified [20]), and (6) terminal tasks (Terminal-Bench [25])."
- [교차검증 R²=0.373, 보류 구성의 87%에서 최적 아키텍처 예측] ↔ "The resulting model achieves a cross-validated R2=0.373 across all six benchmarks" / "it predicts the best-performing architecture for 87% of held-out task configurations"
- [+80.8% ~ -70.0%] ↔ "Relative performance change compared to single-agent baseline ranges from +80.8% on decomposable financial reasoning to -70.0% on sequential planning"
- [단일 에이전트가 45% 넘으면 에이전트 추가가 음의 수익] ↔ "a capability ceiling (β=-0.236, p=0.004): tasks where single-agent performance already exceeds 45% accuracy experience negative returns from additional agents"
- [도구 많은 작업의 조정 비용, 16개 도구] ↔ "a tool-coordination trade-off (β=-0.096, p=0.002): tool-heavy tasks (e.g., 16-tool business workflows) suffer from multi-agent coordination overhead"
- [Independent 17.2배, Centralized 4.4배 오류 증폭] ↔ "Independent systems amplify trace-level errors 17.2× through unchecked error propagation ... Centralized coordination, however, contains this to 4.4× by enforcing validation bottlenecks"
- [Decentralized 웹 탐색 +9.2%, 계획 작업 -39~-70%] ↔ "decentralized coordination benefits tasks requiring parallel exploration of high-entropy search spaces (dynamic web navigation: +9.2%), while all multi-agent variants universally degrade performance on tasks requiring sequential constraint satisfaction (planning: -39% to -70%)"
- [토폴로지 정의: Independent 집계자만, Centralized 오케스트레이터, Decentralized 전체 연결, Hybrid] ↔ "Independent: C = {(ai, aagg)} (agent-to-aggregator only, no peer communication) / Centralized: (orchestrator-to-agents only) / Decentralized: (all-to-all topology) / Hybrid: (orchestrator plus limited peer-to-peer)"
- [정적 벤치마크 HumanEval 5에이전트 89%] ↔ "Multi-agent systems that show monotonic improvement with team size on static benchmarks (reaching 89% on HumanEval with five agents) exhibit fundamentally different scaling behavior"
- [한계: 9개까지만, 통신 오버헤드 초선형, 이질 모델 혼합 -12.6pp] ↔ "preliminary exploration of scaling number of agents up to nine ... the communication overhead we measured grows superlinearly with agent count" / "centralized heterogeneous configurations underperform their strong-model homogeneous counterparts by a mean of 12.6 percentage points"

### S4 ADAS
- [에이전트를 코드로 정의, 메타 에이전트가 아카이브를 보며 새 에이전트 프로그래밍] ↔ "agents can be defined in code and new agents can be automatically discovered by a meta agent programming ever better ones in code." / "a meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries."
- [DROP F1 +13.6, MGSM +14.4%] ↔ "our agents improve F1 scores on reading comprehension tasks in DROP (Dua et al., 2019) by 13.6/100 and accuracy rates on math tasks in MGSM (Shi et al., 2023) by 14.4%."
- [GSM8K +25.9%, GSM-Hard +13.2% 전이] ↔ "our agents improve accuracy by 25.9% on GSM8K and 13.2% on GSM-Hard compared to the baselines when transferring within math domains."
- [생성 코드를 컨테이너에서 실행, 수동 점검] ↔ "we have implemented safety measures including containerized execution of all generated code in secure, isolated environments, thorough manual inspections"
- [성능 외 비용·지연·안전 목표도 가능] ↔ "different objectives to optimize, such as performance, cost, latency, or safety of agents."

### S5 AFlow
- [워크플로를 코드 그래프로 보고 MCTS 탐색] ↔ "we reformulate workflow optimization as a search problem over code-represented workflows, where LLM-invoking nodes are connected by edges. We introduce AFLOW, an automated framework that efficiently explores this space using Monte Carlo Tree Search"
- [평균 5.7% 향상, 기존 자동화 대비 19.5%, GPT-4o 비용의 4.55%] ↔ "yielding a 5.7% average improvement over state-of-the-art baselines. Furthermore, AFLOW enables smaller models to outperform GPT-4o on specific tasks at 4.55% of its inference cost in dollars." / "surpass contemporary automatic workflow optimization work by 19.5%"
- [Operator: Ensemble, Review & Revise] ↔ "operators - predefined, reusable combinations of nodes representing common agentic operations (e.g., Ensemble, Review & Revise)."
- [검증셋 20%, 테스트 80%, 시드 42, 분산 큰 문제만 남김] ↔ "we randomly partition the dataset into a validation set (20%) and a test set (80%), with the random seed fixed at 42 ... we select a subset of problems that exhibit high variance in scores, which becomes the final validation set."

### S6 MAPoRL
- [각자 답 → 다회 토론 → 검증자가 답과 토론을 채점 → 다중 에이전트 RL 보상] ↔ "multiple LLMs first generate their own responses independently and engage in a multi-turn discussion to collaboratively improve the final answer. In the end, a MAPoRL verifier evaluates both the answer and the discussion, by assigning a score that verifies the correctness of the answer, while adding incentives to encourage corrective and persuasive discussions. The score serves as the co-training reward, and is then maximized through multi-agent RL."
- [개별 LLM 단독 훈련으로는 협업이 안 생김] ↔ "our experiments demonstrate that training individual LLMs alone is insufficient to induce effective collaboration."
- [토론 없이 혼자 풀면 0.609 vs 0.604/0.611, 지식이 아니라 협업 능력] ↔ 표 "GSM8k 0.609 0.604 0.611 / ANLI 0.451 0.458 0.453" / "MAPoRL training did not enhance task-specific knowledge but rather improved the models' ability to collaborate effectively."
- [Phi-3-mini 주력, GSM8K·ANLI] ↔ "We primarily use the Microsoft Phi-3-mini-128k-" / "(GSM8k (Cobbe et al., 2021)) and natural language inference (ANLI (Nie et al., 2020))"

### S7 Stronger-MAS (AT-GRPO)
- [역할·턴마다 프롬프트가 달라 표준 GRPO 그룹 가정이 깨짐] ↔ "Standard GRPO grouping assumptions fail in MAS because prompts differ by role and turn."
- [group key = hash(환경, 에이전트, 턴)] ↔ "Define group key g ←hash(e, i, t)" / "unique group key g for each agent i at each turn t in each environment e using a lightweight hash"
- [장기 계획 14.0~47.0% → 96.0~99.5%, 코딩 3.87~7.62%, 수학 9.0~17.93%] ↔ "on long-horizon planning tasks, AT-GRPO boosts accuracy from a 14.0-47.0% single-agent RL baseline to 96.0-99.5%. Furthermore, it improves reasoning performance, with an average gain of 3.87-7.62% on coding and 9.0-17.93% on math."
- [Qwen3 1.7B·8B] ↔ "We train and evaluate Qwen3 models at 1.7B and 8B in the no-thinking"
- [역할 공유 정책 vs 역할 특화 정책은 작업 특성으로 결정] ↔ "whether to choose a role-sharing policy or role-specialized policies needs to be determined by the task characteristics."
- [체커가 붙은 환경] ↔ "We use instances with an automatic checker" / "All math tasks use verifier-checked numeric scoring."

### S8 AgentPrune
- [시공간 메시지 그래프 one-shot 가지치기] ↔ "efficiently performs one-shot pruning on the spatial-temporal message-passing graph, yielding a token-economic and high-performing communication topology."
- [$5.6 vs $43.7, 토큰 28.1~72.8% 감소] ↔ "achieves comparable results as state-of-the-art topologies at merely $5.6 cost compared to their $43.7, (II) integrates seamlessly into existing multi-agent frameworks with 28.1% ∼72.8% ↓token reduction"

### S9 LatentMAS
- [학습 없이 텍스트 대신 잠재 공간 협업, 마지막 층 은닉 임베딩, 공유 잠재 작업 메모리] ↔ "We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations"
- [KV cache를 작업 메모리로] ↔ 3절 소제목 "KV Cache as Working Memory." / "we extract the KV-caches from all L transformer layers"
- [9개 벤치마크, 정확도 최대 14.6%, 출력 토큰 70.8~83.7% 감소, 4~4.3배] ↔ "empirical evaluations across 9 comprehensive benchmarks ... achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4×-4.3× faster end-to-end inference."
- [모든 에이전트가 같은 층 구조라는 가정, 이질 모델은 어댑터 필요] ↔ "we assume that all agents in LatentMAS share the same shape of transformer layers. To relax this assumption and support heterogeneous agents in practice, one can ... introducing a trainable adapter"
- [Qwen3 계열] ↔ "from both the Qwen3 family (Yang et al., 2025) (4B, 8B,"

### S10 G-Memory
- [통찰·질의·상호작용 3층 그래프, 양방향 탐색] ↔ "manages the lengthy MAS interaction via a three-tier graph hierarchy: insight, query, and interaction graphs. Upon receiving a new user query, G-Memory performs bi-directional memory traversal to retrieve both high-level, generalizable insights ... and fine-grained, condensed interaction trajectories"
- [기존 MAS 메모리는 상호작용 궤적 무시, 시도 간·에이전트별 맞춤 없음] ↔ "prevailing MAS memory mechanisms (1) are overly simplistic, completely disregarding the nuanced inter-agent collaboration trajectories, and (2) lack cross-trial and agent-specific customization"
- [최대 20.89%, 10.12%, 프레임워크 무수정] ↔ "G-Memory improves success rates in embodied action and accuracy in knowledge QA by up to 20.89% and 10.12%, respectively, without any modifications to the original frameworks."
- [질의 그래프에 Failed/Resolved 상태] ↔ "status Ψi ∈{Failed, Resolved}, and its associated interaction graph"

### S11 MultiAgentBench
- [마일스톤 기반 KPI, star·chain·tree·graph] ↔ "Our framework measures not only task completion but also the quality of collaboration and competition using novel, milestone-based key performance indicators. Moreover, we evaluate various coordination protocols (including star, chain, tree, and graph topologies)"
- [gpt-4o-mini 최고, 연구 시나리오에서 graph 최고, cognitive planning +3%] ↔ "gpt-4o-mini reaches the average highest task score, graph structure performs the best among coordination protocols in the research scenario,and cognitive planning improves milestone achievement rates by 3%."
- [협업 시나리오: 연구, Minecraft, DB 오류 분석, 코딩 / 경쟁: Werewolf, Bargaining] ↔ "(1) research tasks ... (2) Minecraft-based building tasks ... (3) database error analysis involves exactly five agents ... (4) coding challenges" / "(e.g., Werewolf and Bargaining)"
- [1·3·5·7 에이전트, 늘수록 종합 KPI 하락, 1→3에서 조정 점수 상승] ↔ "We assess configurations with 1, 3, 5, and 7 agents in the research scenario ... increasing the number of agents leads to a decrease in the overall KPI ... the average coordination score improves significantly when moving from 1 to 3 agents"

### 보강 (S1, S3)
- [MAST: 기본 LLM은 에이전트 간 상호작용에 맞춰 사전학습되지 않음, 표적 학습이 해법 후보] ↔ "such as through targeted training, as base LLMs are generally not pre-trained for such nuanced inter-agent dynamics."
- [두 논문 모두 이득이 기대보다 작다는 관찰에서 출발] ↔ S1 "Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal." / S3 "concurrent works question whether multi-agent coordination outperforms single-agent systems (SAS)"
- [Centralized 재무 분석 +80.8%, Independent 순차 계획 -70.0%] ↔ "+80.8% relative improvement (structured financial reasoning under centralized coordination) to -70.0% degradation (sequential planning under independent coordination)"
- [도구 토큰 예산 분할이 원인] ↔ "the tool-coordination trade-off arises because multi-agent systems fragment the per-agent token budget, leaving insufficient capacity for complex tool orchestration"
- [혼합효과 회귀, 설명 변수] ↔ "We establish a predictive framework using a mixed-effects regression model with empirical coordination metrics: efficiency (success/overhead ratio), error amplification factors, message density and redundancy as predictors"
