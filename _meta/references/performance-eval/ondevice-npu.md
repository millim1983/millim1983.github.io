# 온디바이스 AI(양자화 모델·NPU 디바이스) 성능평가 — 리서치 노트

> 조사일 2026-06-26. 대상: 양자화 모델이 탑재된 엣지 NPU 기반 온디바이스 AI(특히 비전 추론).
> 블로그 글감용 구조화 자료. 모든 수치는 WebSearch 검증, 미확인은 명시. 출처 URL 포함.
> 주의: 벤더 공개 수치(특히 TOPS, FPS)는 정밀도·배치·하드웨어·전력모드에 따라 달라지므로 "조건 명시"가 필수(아래 5절).

---

## 1. 성능지표 — 정의와 단위

| 지표 | 정의 | 단위 | 비고 |
|---|---|---|---|
| 추론 지연 (Latency) | 1건 입력→결과까지 시간. MLPerf의 single-stream이 대표 | ms | 낮을수록 좋음 |
| TTFT (Time To First Token) | LLM에서 프롬프트 입력 후 첫 토큰까지 대기시간 | s (또는 ms) | 생성형 응답성 지표. MLPerf Client v1.0 핵심 메트릭 |
| 처리량 (Throughput) | 단위시간당 처리 건수 | FPS, inferences/s, tokens/s | 높을수록 좋음. 비전은 FPS, LLM은 tokens/s |
| 연산성능 (TOPS) | 초당 정수연산 횟수 (Tera Operations Per Second) | TOPS | **이론 최대치(peak)**, 실측 성능 아님 — 마케팅 수치 주의 |
| 전력효율 | TOPS를 소비전력으로 나눈 값 | TOPS/W | 엣지 핵심. 같은 TOPS라도 W 다르면 의미 다름 |
| 에너지/추론 | 추론 1건당 소비 에너지 | mJ/inference (TinyML은 µJ) | MLPerf Tiny가 µJ/inference로 측정 |
| 메모리 풋프린트 | 모델·런타임이 점유하는 메모리 | MB | 양자화로 4×↓ 가능(FP32→INT8) |
| 양자화 후 정확도 손실 | FP32 대비 INT8/INT4 정확도 하락 | %p (퍼센트포인트) | 아래 4절. 비전 분류 기준 |

핵심 주의: **TOPS는 이론 peak이고 실제 추론 성능(FPS·latency)과 선형 비례하지 않는다.** 메모리 대역폭·컴파일러·양자화 효율이 실측을 좌우. 그래서 MLPerf 같은 표준 실측 벤치마크가 필요.

---

## 2. 대표 벤치마크 (MLPerf 계열, MLCommons)

| 벤치마크 | 대상 | 측정 항목 | 대표 태스크 |
|---|---|---|---|
| **MLPerf Inference: Edge** | 엣지 시스템(서버·임베디드) | 처리속도(latency·throughput), 옵션으로 MLPerf Power | 이미지분류(ResNet), 객체탐지, 최근 LLM 시나리오 추가(v5.1) |
| **MLPerf Tiny** | 초저전력 TinyML (활성전력 ~1mW대) | **latency(inf/s), energy(µJ/inference), accuracy** 3축 | keyword spotting, visual wake words, image classification, anomaly detection |
| **MLPerf Mobile** | 스마트폰·노트북 | latency·throughput (single-stream / offline) | 이미지분류, 객체탐지, 시맨틱 분할, QA. **v6.0(2026-06)에 온디바이스 LLM 추가** |
| **MLPerf Client** | AI PC / 클라이언트 | **TTFT(s), TPS(tokens/s)** | LLM(Llama 2 7B, Llama 3.1 8B, Phi 3.5 Mini). v1.0 = 2025-07 |

추가 동향:
- **객체탐지 벤치 현대화**: MLPerf Inference Edge의 객체탐지 기준모델을 RetinaNet→**Ultralytics YOLO11**로 업그레이드(2026-03, YOLO Task Force). 출처: MLCommons.
- **MLPerf Power**: 성능+전력 동시 측정 옵션. v5.1에서 데이터센터(Lenovo)·엣지(GATEOverflow) 제출 존재.
- **MLPerf Mobile v6.0(2026-06)**: Llama 3.2 1B/3B, Llama 3.1 8B 추가. TinyMMLU·IFEval로 성능+정확도 측정. Llama 3.1 8B는 Snapdragon 8 Elite Gen 5에서 NPU 가속 실행 지원. 신규 지원: MediaTek Dimensity 9500, Exynos 2600.
- **제출 방식**: MLCommons가 정의한 데이터셋·시나리오로 LoadGen이 추론요청 생성→latency/throughput 측정. closed(동일 모델·규칙)/open 디비전, 결과는 mlcommons.org 결과DB 공개.

출처:
- https://mlcommons.org/benchmarks/inference-edge/
- https://arxiv.org/abs/2106.07597 (MLPerf Tiny)
- https://mlcommons.org/benchmarks/inference-mobile/
- https://mlcommons.org/2026/06/mlperf-mobile-v6/
- https://mlcommons.org/benchmarks/client/
- https://mlcommons.org/2025/07/mlperf-client-v1-0/
- https://mlcommons.org/2026/03/yolo-inference/

---

## 3. 세계·국내 대표 엣지 NPU 공개 수치

> ⚠️ 대부분 **벤더 공개 peak TOPS / 자체 FPS**다. MLPerf 같은 중립 실측이 아니면 그렇게 표기.

### 3-1. 해외 대표

| 디바이스 | 정밀도/TOPS | 전력 | 전력효율(계산/공개) | 비고·출처 |
|---|---|---|---|---|
| **NVIDIA Jetson AGX Orin 64GB** | 275 TOPS(플랫폼 종합, 마케팅) / GPU 단독 **170 INT8 dense TOPS** | 15–60W 구성 | ≈4.6 TOPS/W (275÷60W, 종합기준) | 마케팅 275 vs 실 GPU 170 차이 큼. Ampere GPU |
| **NVIDIA Jetson AGX Thor** | **1035 TOPS(FP8)**, 2070 TFLOPS(FP4) | (개발키트) | Orin 대비 약 7.5× 연산, 3.5× 효율 | Blackwell GPU, 128GB. 물리AI용 |
| **Hailo-8** | **26 TOPS** | typ. 2.5W | **≈3 TOPS/W(공식), 26÷2.5=10.4 환산** | 온칩 메모리 통합, dataflow 아키텍처. M.2/PCIe |
| **Google Coral Edge TPU** | **4 TOPS** | TOPS당 0.5W | **2 TOPS/W** | USB/M.2. INT8 전용 |
| **Qualcomm QCS8550** | NPU **48 TOPS** | (SoC) | 미확인(SoC 전체전력 별도) | 엣지 비전 SoC |

> Hailo 공식은 "약 3 TOPS/W"로 표기. 26÷2.5W=10.4는 단순 환산치이며 동일 기준 아님 — 인용 시 "공식 vs 환산" 구분 필요.

### 3-2. 국내(한국) 대표

| 디바이스/기업 | 정밀도/TOPS | 전력 | 효율·실측 | 비고·출처 |
|---|---|---|---|---|
| **DeepX DX-M1** | **25 TOPS (INT8)** | typ. 3W (1–5W) | **공개 >10 TOPS/W(ResNet50)**; ResNet50 1186 FPS, 496 FPS/W; YOLOv8L 366 FPS | 엣지 비전용 NPU. M.2. (벤더 공개치) |
| **Mobilint ARIES / MLA100** | **80 TOPS** | 25W | **≈3.2 TOPS/W(80÷25)**; MobileNetV2 11,551 FPS, ResNet-50 3,082 FPS, YOLO-11s 784 FPS, YOLO-11l 259 FPS | MXM 모듈. (벤더 공개치) |
| **Rebellions ATOM (RBLN-CA22)** | **128 INT8 TOPS** | 150W TDP | MLPerf Inference **v3.0** ResNet50 single-stream **0.239ms**, BERT-Large 4.297ms | 16GB GDDR6. 데이터센터급(엣지 아님). MLPerf 실제 제출 |
| **FuriosaAI RNGD** | 미확인(TOPS 미공개) | 180W급(추정)·H100 대비 비교만 | LLM에서 H100 대비 와트당 약 3× 주장 | 10B급 모델 2,000–3,000 tokens/s. 데이터센터 추론칩(엣지 아님) |

핵심 구분: **DeepX·Mobilint = 엣지/온디바이스 비전 타깃. Rebellions·FuriosaAI = 데이터센터/서버 추론 타깃**(온디바이스 비전 디바이스 직접 비교 대상은 DeepX·Mobilint·Hailo·Jetson·Coral 쪽).

출처:
- https://developer.nvidia.com/embedded/jetson-benchmarks
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/
- https://hothardware.com/reviews/nvidia-jetson-agx-thor-developer-kit-hands-on
- https://hailo.ai/products/ai-accelerators/hailo-8-ai-accelerator/
- https://www.coral.ai/docs/edgetpu/faq/
- https://deepx.ai/products/dx-m1/
- https://linuxgizmos.com/radxa-launches-aicore-dx-m1-edge-ai-accelerator-with-deepx-dx-m1-npu/
- https://www.mobilint.com/aries/mla100
- https://aithority.com/machine-learning/mobilint-introduces-mla100-mxm-an-80-tops-npu-module-for-high-efficiency-embedded-ai-pcs/
- https://rebellions.ai/rebellions-product/rbln-ca22/
- https://www.kedglobal.com/korean-chipmakers/newsView/ked202304070010
- https://furiosa.ai/blog/rngd-hot-chips-press-release

---

## 4. 양자화 후 정확도 손실 (FP32 → INT8 / INT4)

### INT8 (비전 분류, ResNet50/ImageNet 기준)
- 성숙 기법(PTQ/QAT) 적용 시 **FP32 대비 <1%p 하락**이 일반적.
  - 예: ResNet50 INT8 PTQ 76.01% (-0.07%p), 다른 사례 -0.34%p(오히려 미세 개선).
  - CLE/BC 8-bit: ResNet-50 75.45% vs FP32 76.05% (약 0.6%p).
- 순수 INT8 end-to-end 학습은 ImageNet에서 **top-1 1~3%p 하락** 범위 보고도 있음.
- 효과: 메모리 4×↓, 에너지효율 10~30×↑(FPGA 사례).

### INT4 (비전 CNN)
- **나이브 INT4는 큰 정확도 붕괴 위험.** 4bit 미만은 일반화 어려움.
- 모델·데이터셋 의존성 큼:
  - CIFAR-10: 90.8%→52.7% (**약 38%p 붕괴**, 나이브)
  - GTSRB: 96.0%→95.6% (**<1%p**, 영향 미미)
- 고급 기법(양자화 인지 학습 QAT, 안정화 gradient quant): 전 모델 **최대 4.57%p** 이내로 억제 가능.
- 일부 연구: ImageNet에서 8·4bit 모두 FP32 대비 <1%p 주장(기법·모델 한정).

정리: **INT8은 "거의 무손실(<1%p)"이 현실적 기대치, INT4는 QAT 등 정교한 기법 없으면 위험.** 데이터셋·태스크 난이도에 따라 손실 폭이 크게 갈림.

출처:
- https://developer.nvidia.com/blog/achieving-fp32-accuracy-for-int8-inference-using-quantization-aware-training-with-tensorrt/
- https://arxiv.org/pdf/2407.15904
- https://www.edge-ai-vision.com/2024/04/quantization-of-convolutional-neural-networks-quantization-analysis/
- https://arxiv.org/pdf/2301.12017 (INT4 for LM)
- (배경) ax-04 노트: 양자화가 메모리·전력 제약에서 가장 확실한 압축, 16bit 학습→4bit 배치, GPTQ/AWQ

---

## 5. 평가 환경 명시의 중요성 (수치 비교 시 필수 체크)

같은 모델·같은 칩이라도 아래가 다르면 수치가 달라진다. 비교·인용 시 반드시 명시:
1. **정밀도**: FP32 / FP16 / INT8 / INT4 (TOPS와 정확도 둘 다 좌우). dense vs sparse도 구분(Jetson Orin 170 dense INT8 사례).
2. **배치 크기 / 시나리오**: single-stream(지연) vs offline·multi-stream(처리량). MLPerf는 시나리오를 분리.
3. **하드웨어·전력모드**: 같은 Jetson Orin도 15W vs 60W에서 성능 다름. 전력 envelope 명시.
4. **모델·데이터셋·기준모델 버전**: ResNet50 vs YOLO11, ImageNet vs 커스텀.
5. **peak TOPS vs 실측 FPS 구분**: peak는 이론치. 실측은 MLPerf 같은 중립 벤치 우선.

→ 블로그 메시지: "TOPS 숫자만으로 우열 가리지 말 것. 정밀도·배치·전력·벤치마크 조건을 함께 봐야 함."

---

## 6. 신규 온디바이스 비전 디바이스 개발 — 연차별 목표 제안 (보수적)

> 전제: 양자화(INT8 기본) 비전 추론 디바이스를 신규 개발하는 팀 기준. 객체탐지(YOLO계열)·분류 혼합 워크로드 가정.
> 수치는 위 공개 벤치(Hailo 3 TOPS/W, DeepX >10 TOPS/W ResNet50, Coral 2 TOPS/W, Jetson Orin ~4.6 TOPS/W)를 현실 기준선으로 삼아 **보수적으로** 설정. 절대 목표 아니라 출발 가이드.

| 항목 | 1년차 (PoC·기준확립) | 2년차 (최적화) | 3년차 (양산급) |
|---|---|---|---|
| 추론 지연(단일, 분류기준) | < 30 ms | < 15 ms | < 10 ms |
| 처리량(객체탐지, YOLO계열) | 15–30 FPS | 30–60 FPS | 60+ FPS(다중스트림) |
| 양자화 정확도 손실(INT8, 분류) | ≤ 2 %p | ≤ 1 %p | ≤ 0.5 %p |
| INT4 적용 | 미적용/실험만 | 일부 레이어 INT4 + QAT | 핵심경로 INT4, 손실 ≤ 2 %p |
| 전력효율 | 1–3 TOPS/W (Coral·범용 NPU 수준) | 3–5 TOPS/W (Hailo·Jetson 수준) | 5–10 TOPS/W (DeepX 상위권 지향) |
| 검증 | 자체 데이터셋 latency/accuracy | MLPerf Tiny/Edge 유사 셋업 자체측정 | MLPerf Edge 정식 제출 목표 |

근거·논리:
- **1년차**: 양산칩 신뢰수치보다 한참 보수적으로. INT8 PTQ로 <2%p는 일반적 달성선(4절). 전력효율 1–3 TOPS/W는 범용 엣지 NPU(Coral 2) 수준.
- **2년차**: QAT·컴파일러 최적화로 정확도 손실 <1%p(ResNet50급 현실치), 효율 3–5 TOPS/W는 Hailo(3)·Jetson Orin(4.6) 구간.
- **3년차**: DeepX 공개 >10 TOPS/W가 현 세계 상위. 양산 목표를 5–10 TOPS/W로 두되 보수적으로 5부터. MLPerf Edge 정식 제출로 외부 신뢰 확보.
- INT4는 정확도 위험이 커(4절 CIFAR 붕괴 사례) 단계적·QAT 동반 전제로만.

> 주의: 위 목표치는 일반 가이드라인이며 **세계기록(Thor 1035 TOPS 등)과 직접 경쟁 목표가 아님.** 워크로드·모델·전력 envelope 확정 후 재산정 필요.

---

## 7. 핵심 수치 요약 (인용용)

1. Hailo-8: **26 TOPS, 약 3 TOPS/W**(typ. 2.5W). (hailo.ai)
2. Google Coral Edge TPU: **4 TOPS, 2 TOPS/W**(TOPS당 0.5W). (coral.ai)
3. NVIDIA Jetson AGX Orin: 종합 **275 TOPS**(GPU 단독 170 INT8 dense), 15–60W → ≈4.6 TOPS/W. (NVIDIA)
4. NVIDIA Jetson AGX Thor: **1035 TOPS(FP8)**, Orin 대비 7.5× 연산·3.5× 효율. (NVIDIA/HotHardware)
5. DeepX DX-M1(국산): **25 TOPS INT8, typ. 3W, 공개 >10 TOPS/W(ResNet50)**, ResNet50 1186 FPS / 496 FPS/W. (deepx.ai, linuxgizmos)
6. Mobilint MLA100(국산): **80 TOPS, 25W (≈3.2 TOPS/W)**, ResNet-50 3,082 FPS, YOLO-11s 784 FPS. (mobilint.com)
7. Rebellions ATOM(국산, 서버급): **128 INT8 TOPS, 150W**, MLPerf v3.0 ResNet50 single-stream **0.239 ms**. (rebellions.ai, KED)
8. INT8 양자화 정확도 손실: ResNet50/ImageNet **<1%p**(성숙 기법). (NVIDIA TensorRT 블로그)
9. INT4 정확도: 나이브 시 붕괴 가능(CIFAR-10 90.8→52.7%), QAT 시 최대 4.57%p 이내. (arXiv)
10. MLPerf Tiny 측정 3축: **latency(inf/s), energy(µJ/inference), accuracy**. (arXiv 2106.07597)
11. MLPerf Client v1.0 메트릭: **TTFT(s) + TPS(tokens/s)**, 모델 Llama 2 7B·Llama 3.1 8B·Phi 3.5 Mini. (MLCommons)

---

## 8. 미확인 / 추가확인 필요 항목

- **Mobilint·DeepX의 MLPerf 정식 제출 결과(ResNet50 등 공식 스코어)**: 벤더 자체 FPS는 확보했으나, MLCommons 결과DB에서의 공식 제출 수치는 이번 검색으로 확정 못함. mlcommons.org 결과DB 직접 확인 필요. ("MLPerf에서 두각" 같은 정성적 언급만 확인됨.)
- **FuriosaAI RNGD의 TOPS 공식 수치**: 미공개(tokens/s·H100 대비 비교만 확인).
- **Qualcomm QCS8550 NPU의 TOPS/W**: NPU 48 TOPS는 확인, 전력효율은 SoC 전체전력과 분리 안 돼 미확인.
- **Jetson Thor의 정확한 TDP·실측 TOPS/W**: 개발키트 기준 연산성능만 확인, 효율 배수(3.5×)는 NVIDIA 주장.
- 6절 연차 목표치는 **공개 벤치 기반 보수적 추정**이며 특정 사업 목표 아님 — 실제 워크로드 확정 후 재산정.
- DeepX ">10 TOPS/W", Hailo "3 TOPS/W"는 벤더 공개 기준치라 측정조건(모델·정밀도) 동일성 보장 안 됨 — 동일조건 비교 아님 주의.
