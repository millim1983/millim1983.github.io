# evidence - ma-01-multiagent-architecture-map

열람일: 2026-10-22 (전 출처 공통)

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | How we built our multi-agent research system | Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford (Anthropic) | 2025 (Published Jun 13, 2025) | https://www.anthropic.com/engineering/multi-agent-research-system | Architecture overview(그림 캡션), Prompt engineering 절 "Teach the orchestrator how to delegate", Production reliability 절, Appendix "Subagent output to a filesystem" |
| S2 | Why Do Multi-Agent LLM Systems Fail? | Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica | 2025 (v1 17 Mar 2025, 읽은 판 v3 26 Oct 2025) | https://arxiv.org/html/2503.13657v3 | Abstract, 1 Introduction, 3.1~3.2, 4절(FC1~FC3 비율과 Insight 1~3), 5절 앞부분, Figure 4 캡션 |
| S3 | Levels of Autonomy for AI Agents | K. J. Kevin Feng, David W. McDonald, Amy X. Zhang | 2025 (v2) | https://arxiv.org/html/2506.12469 | 다섯 단계 정의 절, autonomy certificates 절 |
| S4 | Checkpointers (LangGraph docs) | LangChain | n.d. | https://docs.langchain.com/oss/python/langgraph/checkpointers (.md 원문) | 도입부, Threads, Checkpoints/Super-steps, StateSnapshot fields, Replay, Update state, Durability modes |
| S5 | Interrupts (LangGraph docs) | LangChain | n.d. | https://docs.langchain.com/oss/python/langgraph/interrupts (.md 원문) | 도입부, Requirements, Resuming, Common patterns, Rules of interrupts |
| S6 | Handoffs (OpenAI Agents SDK) | OpenAI | n.d. | https://openai.github.io/openai-agents-python/handoffs/ | Creating a handoff, Customizing handoffs, input_type, Input filters, Recommended prompts |
| S7 | Agent orchestration (OpenAI Agents SDK) | OpenAI | n.d. | https://openai.github.io/openai-agents-python/multi_agent/ | Agents as tools / Handoffs 비교 |
| S8 | Human-in-the-loop (OpenAI Agents SDK) | OpenAI | n.d. | https://openai.github.io/openai-agents-python/human_in_the_loop/ | 도입부, Approval flow, Long-running approvals, Serialization 보안 주의 |
| S9 | 01 설계원리 (개인 정리 문서, 식별정보 제외 개념만 사용) | 본인 | - | 비공개 | 철칙 1~4, 자율성 L0~L4 표 |

## 본문 문장 ↔ 원문 발췌

### 2-1. 상태와 체크포인트

- [Anthropic: 에이전트는 상태를 가지며 오류는 누적된다] ↔ S1: "Agents are stateful and errors compound."
- [처음부터 재시작 대신 오류 지점에서 재개] ↔ S1: "When errors occur, we can't just restart from the beginning: restarts are expensive and frustrating for users. Instead, we built systems that can resume from where the agent was when the errors occurred."
- [재시도 로직과 정기 체크포인트 같은 결정적 안전장치를 모델 적응력과 함께] ↔ S1: "We combine the adaptability of AI agents built on Claude with deterministic safeguards like retry logic and regular checkpoints."
- [super-step 단위로 체크포인트, tick, 병렬 실행] ↔ S4: "LangGraph creates a checkpoint at each super-step boundary. A super-step is a single "tick" of the graph where all nodes scheduled for that step execute (potentially in parallel)."
- [thread로 묶이고 thread_id가 기본 키, 없으면 저장·재개 불가] ↔ S4: "The checkpointer uses `thread_id` as the primary key for storing and retrieving checkpoints. Without it, the checkpointer cannot save state or resume execution after an interrupt"
- [pending writes: 실패 시 같은 단계 성공 노드 재실행 안 함] ↔ S4: "When a graph node fails mid-execution at a given super-step, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that super-step. When you resume graph execution from that super-step you don't re-run the successful nodes."
- [update_state는 원 체크포인트를 바꾸지 않고 새 체크포인트, fork] ↔ S4: "This creates a new checkpoint with the updated values - it does not modify the original checkpoint." / "checkpointers make it possible to fork the graph state at arbitrary checkpoints to explore alternative trajectories."
- [durability 모드 exit] ↔ S4: "`"exit"`: LangGraph persists changes only when graph execution exits - successfully, with an error, or due to a human-in-the-loop interrupt. This provides the best performance for long-running graphs but means intermediate state is not saved, so you cannot recover from system failures (like process crashes) mid-execution."
- [durability 모드 async] ↔ S4: "`"async"`: LangGraph persists changes asynchronously while the next step executes. This provides good performance and durability, but there is a small risk that LangGraph does not write checkpoints if the process crashes during execution."
- [durability 모드 sync] ↔ S4: "`"sync"`: LangGraph persists changes synchronously before the next step starts. This ensures that LangGraph writes every checkpoint before continuing execution, providing high durability at the cost of some performance overhead."
- [replay 시 이후 노드의 LLM 호출·API 요청 재실행] ↔ S4: "Nodes after the checkpoint re-execute, including any LLM calls, API requests, or interrupts - which are always re-triggered during replay."
- [rainbow 배포: 구·신버전 동시 운용, 트래픽 점진 이동] ↔ S1: "we use rainbow deployments to avoid disrupting running agents, by gradually shifting traffic from old to new versions while keeping both running simultaneously."
- (멱등의 정의는 일반 정의, S5 문서의 정의와도 일치) ↔ S5: "idempotency means that the same operation can be applied multiple times without changing the result beyond the initial execution."

### 2-2. 핸드오프

- [handoff는 모델에게 도구로 보이고 transfer_to_refund_agent 이름] ↔ S6: "Handoffs are represented as tools to the LLM. So if there's a handoff to an agent named Refund Agent, the tool would be named transfer_to_refund_agent."
- [기본은 이전 대화 전체를 보며 이어받음, 바꾸려면 input_filter] ↔ S6: "When a handoff occurs, it's as though the new agent takes over the conversation, and gets to see the entire previous conversation history. If you want to change this, you can set an input_filter."
- [nest_handoff_history는 베타] ↔ S6: "Nested handoff history is available as an opt-in beta and is disabled by default while we stabilize it."
- [input_type으로 이유·우선순위 같은 작은 메타데이터] ↔ S6: "Use input_type when the handoff needs a small piece of model-generated metadata such as reason, language, priority, or summary."
- [agents-as-tools: 매니저가 주도권 유지] ↔ S7: "A manager agent keeps control of the conversation and calls specialist agents through Agent.as_tool()."
- [handoff: 선택된 전문 에이전트가 턴의 나머지를 소유 / 최종 답 책임·가드레일 한곳] ↔ S7: "Use agents as tools when a specialist should help with a bounded subtask but should not take over the user-facing conversation. Use handoffs when routing itself is part of the workflow and you want the chosen specialist to own the remainder of the current turn." / "You want one agent to own the final answer, combine outputs from multiple specialists, or enforce shared SDK guardrails in one place."
- [서브에이전트가 외부 시스템에 저장하고 가벼운 참조 반환, 정보 손실·토큰 절감] ↔ S1: "Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator. This prevents information loss during multi-stage processing and reduces token overhead from copying large outputs through conversation history."
- [위임 4요소, 없으면 중복·빈틈] ↔ S1: "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."

### 2-3. 실패 분류 (MAST)

- [150개 기록, 5개 프레임워크, 전문가 6명] ↔ S2 3.1: "we first collect 150 traces from five MAS frameworks, which are closely examined by six human experts."
- [14개 모드 3개 범주, κ=0.88] ↔ S2 Abstract: "We develop MAST through rigorous analysis of 150 traces, guided closely by expert human annotators and validated by high inter-annotator agreement (κ=0.88). This process identifies 14 unique modes, clustered into 3 categories"
- [o1 기반 LLM 주석기, κ=0.77] ↔ S2: "we then develop an LLM-as-a-judge pipeline (which we term the LLM annotator) [21] using OpenAI's o1 model. We calibrate the LLM annotator to achieve high agreement with human expert annotations (κ = 0.77)"
- [7개 프레임워크 1600여 개 기록 데이터셋] ↔ S2 Abstract: "We introduce MAST-Data, a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks."
- [FC1 비율] ↔ S2 4절: "These include failing to follow task requirements (FM-1.1, 11.8%) or agent roles (FM-1.2, 1.5%), step repetitions (FM-1.3, 15.7%), context loss (FM-1.4, 2.80%), or not recognizing task completion (FM-1.5, 12.4%)."
- [FC2 비율] ↔ S2 4절: "These include unexpected conversation resets (FM-2.1, 2.20%), proceeding with wrong assumptions instead of seeking clarification (FM-2.2, 6.80%), task derailment (FM-2.3, 7.40%), withholding crucial information (FM-2.4, 0.85%), ignoring other agents' input (FM-2.5, 1.90%), or mismatches between reasoning and action (FM-2.6, 13.2%)."
- [FC3 비율] ↔ S2 4절: "including premature termination (FM-3.1, 6.20%), no or incomplete verification (FM-3.2, 8.20%), or incorrect verification (FM-3.3, 9.10%)."
- [범주 합계 약 44/32/24%] ↔ 위 세 발췌의 수치를 내가 더한 값 (FC1 44.2, FC2 32.35, FC3 23.5). 논문에 범주 합계 문장은 없음. 본문에 "내가 더해 보면"으로 표기
- [모델 한계만으로 설명되지 않음] ↔ S2 Insight 1: "MAS failure is not merely a function of challenges in the underlying model"
- [기반 모델 개선만으로 부족할 것이라 추정] ↔ S2: "we conjecture that improvements in the base model capabilities will be insufficient to address the full MAST."
- [CEO 최종 결정권 흐름 수정 +9.4%] ↔ S2 Introduction: "We demonstrate that a straightforward system workflow adjustment ensuring the CEO had the final say contributed to a +9.4% increase in overall task success rate." (주의: 4절은 같은 +9.4%를 "improving agent role specifications alone"으로 기술. 본문은 Introduction 기술을 따름)
- [목표 검증 단계 +15.6%] ↔ S2 4절: "adding a high-level task objective verification step to ChatDev yields a +15.6% improvement in task success on ProgramDev"
- [같은 모델로 얻은 개선] ↔ S2 5절: "With the same underlying model, we achieve max improvements of 15.6%."
- [모든 실패가 해소되진 않고 완료율 여전히 낮음] ↔ S2: "not all failure modes are resolved, and task completion rates still remain low"
- [과업 영역: 코딩, 수학, 일반] ↔ S2: "covering domains of coding, math, and generic tasks."

### 2-4. 승인 지점과 자율성 단계

- [interrupt는 멈추고 외부 입력 대기] ↔ S5: "Interrupts allow you to pause graph execution at specific points and wait for external input before continuing."
- [체크포인터·thread_id 필수] ↔ S5: "A **checkpointer** to persist the graph state (use a durable checkpointer in production)" / "A **thread ID** in your config so the runtime knows which state to resume from"
- [Command(resume=...) 값이 interrupt 반환값] ↔ S5: "The value passed to `Command(resume=...)` becomes the return value of the interrupt call"
- [재개 시 노드를 처음부터 재실행] ↔ S5: "The node restarts from the beginning of the node where the interrupt was called when resumed, so any code before the interrupt runs again"
- [interrupt 앞 부작용은 멱등, 뒤로 옮기거나 별도 노드] ↔ S5: "side effects called before interrupt should (ideally) be idempotent." / "Place side effects after interrupt calls" / "Separate side effects into separate nodes when possible"
- [needs_approval, interruptions, RunState 직렬화 후 approve/reject] ↔ S8: "Tools declare when they need approval, run results surface pending approvals as interruptions, and RunState lets you serialize paused runs and resume them after decisions are made." / "Use state.to_json() or state.to_string() to store pending work in a database or queue and recreate it later with RunState.from_json(...)"
- [복원 함수가 스냅샷·제출자를 인증하지 않음, 신뢰 저장소만] ↔ S8: "RunState.from_json() and RunState.from_string() do not authenticate the snapshot or the person submitting it. Only deserialize snapshots from trusted storage"
- [Feng 등 다섯 단계 operator~observer] ↔ S3: Level 1 "User as an operator", Level 2 "User as a collaborator", Level 3 "User as a Consultant", Level 4 "User as an approver", Level 5 "User as an observer"
- [승인자 단계: 스스로 못 푸는 장애물에서만 개입] ↔ S3: "the user is only required to interact with the agent when the agent encounters a blocker it cannot resolve on its own."
- [자율성은 능력과 별개로 설계 가능] ↔ S3: "our framework views autonomy as a property that can also be designed independently of capability."
- [autonomy certificate: 최대 단계를 정함] ↔ S3: "a digital document that prescribes the maximum level of autonomy at which an agent can operate."
- [L0~L4 표, 업무 단위·측정 오류율로만 승격] ↔ S9 철칙 2 (개인 정리 문서, "내가 정리한 설계 원칙"으로 표기). 구체 수치(채택률 80%)는 본문에서 "기준 이상"으로 일반화

### 2-5. 대체 경로

- [도구 실패를 알려 에이전트가 적응하게 하는 방법이 잘 동작] ↔ S1: "letting the agent know when a tool is failing and letting it adapt works surprisingly well."
- 강등 3칸·트리거·코드 예시는 S9 철칙 1(AI 판단, 실행은 룰)과 철칙 4(금기는 코드로)를 바탕으로 내가 구성한 설계. 외부 사실 아님

### 3. 참조 아키텍처

- 설계 원칙 4개 ↔ S9 철칙 1~4 (개념만, 식별정보 없음)
- 관측에 트레이스 사용 근거는 기존 글 agent-05 링크. 신규 외부 사실 없음

## 읽지 못해 뺀 것

- 없음. LangGraph persistence 페이지는 개요만 있어 세부(super-step, StateSnapshot, durability)를 checkpointers 페이지 원문(.md)에서 확인해 그쪽을 출처로 씀
