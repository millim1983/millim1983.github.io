---
layout: post
title: "온디바이스 비전을 떠받치는 칩 — NPU란 무엇인가"
subtitle: "모델을 아무리 줄여도, 그 모델을 빠르게 굴릴 칩이 없으면 소용없다"
categories: [ax]
tags: [npu, edge-ai, on-device, inference, hardware, quantization, accelerator]
toc: true
mermaid: true
status: published
date: 2026-06-19 21:31:02 +09:00
---

## 0. 모델을 줄이는 이야기의 나머지 절반

온디바이스 비전이 가능해진 배경을 둘로 나누면, 절반은 모델을 작게 만드는 기술(양자화·증류)이고 나머지 절반은 그 작은 모델을 빠르게 굴리는 하드웨어다. 그 하드웨어의 중심에 NPU(Neural Processing Unit), AI 추론에 특화된 칩이 있다.

문제는 "NPU"가 한 물건이 아니라는 점이다. 2W를 먹고 4 TOPS를 내는 Google Coral Edge TPU도 NPU고, 60W까지 먹고 275 TOPS를 내는 NVIDIA Jetson AGX Orin도 NPU다. 둘은 성능이 70배 차이 나는데도 같은 "엣지 AI 칩"으로 묶인다. 그래서 "NPU에 올리면 빨라진다"는 말은 거의 정보가 없다. 어느 NPU에, 어떤 정밀도로, 어떤 런타임으로 올리느냐가 전부다.

> **"NPU에 올린다"는 결정의 90%는 칩을 고르는 순간 정해진다. 그 칩이 무엇을 INT 몇 비트로 처리하는지가 모델 설계를 거꾸로 규정한다.**

이 글은 실제 제품군으로 NPU를 네 계층으로 나누고, 각 칩이 지원하는 정밀도·런타임·전력을 수치로 비교한다.

## 1. NPU는 CPU·GPU와 무엇이 다른가

신경망 추론 연산의 대부분은 행렬곱과 누적(MAC)이다. NPU는 이 MAC을 수백~수천 개의 전용 연산기로 한꺼번에 처리하는 칩이다. ARM Ethos-U85가 128~2,048개의 MAC을 갖는 식으로, 같은 곱셈-덧셈을 병렬로 쏟아낸다.

| 칩 | 잘하는 일 | 한계 |
|---|---|---|
| CPU | 복잡한 분기·순차 로직 | 행렬곱이 느리고 전력당 성능이 낮다 |
| GPU | 대규모 병렬(학습·고처리량) | 전력·발열이 커 배터리 장비에 부담 |
| NPU | 저정밀 행렬곱 추론 | 지원 연산자가 한정적, 학습엔 부적합 |

GPU도 병렬 연산에 강하지만 학습용 고처리량에 맞춰져 전력을 많이 쓴다. NPU는 추론 한 가지, 그것도 INT8 같은 저정밀 연산에 집중해 전력당 성능(TOPS/W)을 끌어올린 칩이다. Hailo-8이 26 TOPS를 2.5~3W에 내는 것이 이 특화의 결과다.

## 2. 제품군으로 보는 NPU 네 계층

온디바이스 비전에서 마주치는 NPU는 성능·전력대로 네 계층으로 나뉜다. 각 계층의 대표 제품과 스펙은 다음과 같다.

| 계층 | 대표 제품 | NPU 성능 | 지원 정밀도 | 전력 | 런타임/SDK | 전형적 용도 |
|---|---|---|---|---|---|---|
| MCU / TinyML | Arm Ethos-U85 (Cortex-M85 결합) | 0.25~4 TOPS | INT8 가중치, INT8/INT16 활성 | mW급 | Vela 컴파일러 + TFLite Micro | 상시 켜진 초저전력 센서, 단순 분류 |
| 임베디드 SoC | Rockchip RK3588 | 6 TOPS | INT4/INT8/INT16/FP16 혼합 | 수 W | RKNN-Toolkit | 저가 비전 보드, 산업용 IPC |
| 전용 비전 가속기 | Hailo-8 / Google Coral Edge TPU | 26 TOPS / 4 TOPS | INT8(Hailo 일부 INT4) / INT8 전용 | 2.5~3W / 2W | Hailo Dataflow Compiler / TFLite int8 | 상시 다중 카메라 / 배터리 카메라 |
| 고성능 엣지 | NVIDIA Jetson Orin (Nano~AGX) | 40~275 TOPS | INT8/FP16(+희소성) | 7~60W | TensorRT / CUDA | 멀티카메라, 로봇, 자율주행, 산업 검사 |

여기에 노트북·스마트폰의 내장 NPU가 한 축 더 있다. AI PC용으로는 Qualcomm Snapdragon X2 Elite의 Hexagon NPU 6가 80 TOPS로 현재 노트북 최고치이고, 1세대 Snapdragon X Elite는 약 45 TOPS, Intel Core Ultra(Lunar Lake)는 48 TOPS, AMD Ryzen AI(XDNA)는 50~75 TOPS, Apple M4/M5의 Neural Engine은 38~45 TOPS다. Microsoft의 Copilot+ PC 인증 기준선이 40 TOPS인 것도 이 수치들과 맞물린다.

같은 "NPU"라도 Ethos-U85(0.25 TOPS, mW)와 Jetson AGX Orin(275 TOPS, 60W)은 1,000배의 성능 격차가 있다. 재난 탐지 센서 노드에 Jetson을 넣을 수 없고, 자율주행 멀티카메라를 Coral 하나로 돌릴 수 없다. 계층 선택이 곧 설계 제약이다.

## 3. 칩마다 잘 받는 모델이 다르다 — 정밀도와 연산자

계층을 골랐다고 끝이 아니다. 같은 계층 안에서도 칩마다 지원하는 정밀도와 연산자가 다르다. 이게 모델 설계를 직접 규정한다.

- **Google Coral Edge TPU**: INT8 전용이다. 모델 전체를 INT8로 양자화한 TensorFlow Lite로만 돌아간다. FP16이나 INT4는 아예 못 받는다. 게다가 Edge TPU가 지원하지 않는 연산자가 모델에 하나라도 있으면, 그 연산자부터 끝까지가 통째로 CPU로 떨어진다.
- **Rockchip RK3588**: INT4/INT8/INT16/FP16을 혼합 지원한다. RKNN-Toolkit으로 변환하며, INT8에 가장 최적화돼 있다. Coral보다 유연하지만 변환 단계에서 미지원 연산자를 직접 걷어내야 한다.
- **Arm Ethos-U85**: INT8 가중치에 INT8/INT16 활성만 받는다. Vela 컴파일러가 모델을 훑어 NPU가 처리할 수 있는 연산자만 NPU에 올리고, 나머지는 짝을 이루는 Cortex-M85 코어로 넘긴다.
- **NVIDIA Jetson Orin**: TensorRT가 FP16·INT8 엔진을 빌드하며, 위 칩들 중 지원 연산자 범위가 가장 넓다. PyTorch 모델을 비교적 그대로 가져갈 수 있어 개발 부담이 가장 작다. 대신 전력과 단가가 가장 높다.

```mermaid
flowchart LR
  M["학습된 모델 (FP32/FP16)"] --> Q["양자화<br/>칩이 받는 정밀도로<br/>(예: Coral=INT8 전용)"]
  Q --> CMP["목표 칩 컴파일러<br/>TFLite / RKNN / Vela / TensorRT"]
  CMP --> RUN["NPU에서 추론<br/>저전력·실시간"]
  CMP -. 미지원 연산자 .-> FALL["CPU 폴백<br/>그 지점부터 느려짐"]
```

*그림. 같은 모델이라도 목표 칩의 정밀도·연산자에 맞춰 컴파일해야 한다. Coral은 INT8 전용이라 그 외 정밀도는 못 받고, 미지원 연산자는 CPU로 폴백돼 실시간이 깨진다.*

## 4. TOPS 숫자의 함정

칩을 고를 때 TOPS만 보면 틀린다. TOPS는 정점 정수 연산량일 뿐, 실제 추론 속도는 메모리 대역폭과 컴파일러 성숙도가 좌우한다.

대표적 사례가 Apple이다. M5의 Neural Engine은 raw TOPS가 80 TOPS짜리 Snapdragon보다 낮은데도, 로컬 LLM 추론에서 더 높은 TOPS의 Windows 칩을 앞서는 경우가 잦다. M5 Pro가 273 GB/s, M5 Max가 546 GB/s에 이르는 통합 메모리 대역폭으로 NPU·CPU·GPU가 같은 메모리 풀에 빠르게 접근하기 때문이다. 연산기가 아무리 빨라도 데이터가 못 따라오면 놀고 있는 것이다.

반대 방향의 함정도 있다. Coral Edge TPU의 4 TOPS와 Jetson AGX Orin의 275 TOPS는 70배 차이지만, 늘 켜져 있어야 하는 2W 배터리 카메라에는 4 TOPS Coral이 정답이고 275 TOPS Jetson은 전력 예산을 넘겨 오답이다. TOPS가 높다고 그 용도에 맞는 게 아니다. 비전 워크로드의 실시간 요구·전력 예산·카메라 수가 먼저고, TOPS는 그 다음이다.

> **TOPS는 칩의 정점 속도지 내 모델의 속도가 아니다. 전력 예산과 메모리 대역폭을 같이 보지 않으면 숫자에 속는다.**

## 5. 그래서 목표 칩을 먼저 정한다

이 제약들은 개발 순서를 뒤집는다. 모델을 먼저 만들고 나중에 칩을 고르면, 다 만든 모델이 목표 칩의 정밀도·연산자에 안 맞아 다시 설계해야 한다. 그래서 온디바이스 비전은 목표 칩을 먼저 못 박고 거꾸로 내려온다.

대략의 선택 기준은 이렇게 정리된다.

- **상시 배터리 센서, 단순 분류**: Ethos-U85급 MCU NPU 또는 Coral Edge TPU. INT8로 끝까지 양자화 가능한 모델만 설계한다.
- **저가 고정형 비전(IPC·키오스크)**: RK3588급 임베디드 SoC. 정밀도 선택지가 넓어 모델 제약이 덜하다.
- **상시 다중 카메라, 전력 민감**: Hailo-8. TOPS/W가 동급 최고라 항상 켜두는 감시에 맞는다.
- **멀티카메라·로봇·자율주행**: Jetson Orin. 전력·단가를 감수하는 대신 PyTorch 모델을 거의 그대로 올린다.

이 선택이 양자화 비트수, 쓸 수 있는 연산자, 모델 크기 상한을 한꺼번에 결정한다.

## 6. 사람에게 남는 일

양자화도, 컴파일도, 연산자 매핑도 도구가 자동으로 한다. 코딩 에이전트에게 "이 모델을 Jetson Orin용 TensorRT INT8 엔진으로 빌드하라"고 지시하면 절차는 도구가 처리한다. 그럴수록 사람의 일은 절차 실행에서 칩을 고르는 결정으로 옮겨간다.

배터리 예산이 2W인가 60W인가, 카메라가 한 대인가 여덟 대인가, 모델을 INT8로 끝까지 양자화할 수 있는가, 그 칩의 컴파일러가 내 모델의 연산자를 받는가. 이 질문들의 답이 Coral과 Jetson 사이 어디에 설지를 정한다. 도구는 주어진 칩에 맞춰 컴파일하지만, 어느 칩에 맞출지는 묻지 않으면 정해 주지 않는다.

도구가 모델을 자동으로 칩에 맞춰 주는 시대에 사람에게 남는 일은, 전력·카메라 수·정밀도 제약을 읽어 목표 칩을 고르는 능력과 그 칩에서 모델이 폴백 없이 실제로 빨라지는지 현장에서 검증하는 능력이다.

---

## 출처

- Notebookcheck, "Hexagon NPU 6 in the Snapdragon X2 Elite Extreme: 80 TOPS", https://www.notebookcheck.net/Hexagon-NPU-6-in-the-Snapdragon-X2-Elite-Extreme-80-TOPS-performance-that-is-up-to-95-faster-than-Apple-M4-and-122-faster-than-Intel-Lunar-Lake.1166576.0.html
- Local AI Master, "NPU Comparison 2026: Intel vs Qualcomm vs AMD vs Apple", https://localaimaster.com/blog/npu-comparison-2026
- SolidAITech, "NPU Guide 2026: TOPS, Copilot+ PCs & Memory Bandwidth Explained", https://www.solidaitech.com/2026/05/npu-neural-processing-unit-complete-guide.html
- ThinkRobotics, "Edge-AI Accelerators (Jetson vs Coral TPU): A Detailed Comparison for Developers", https://thinkrobotics.com/blogs/learn/edge-ai-accelerators-jetson-vs-coral-tpu-a-detailed-comparison-for-developers
- SumGuy's Ramblings, "Hailo-8 vs Coral: AI Accelerators for the Edge", https://sumguy.com/hailo-8-vs-coral-ai-accelerators/
- CNX Software, "Arm Ethos-U85 NPU delivers up to 4 TOPS for Edge AI applications", https://www.cnx-software.com/2024/04/09/arm-ethos-u85-npu-delivers-up-to-4-tops-for-edge-ai-applications-in-cortex-m7-to-cortex-a520-socs/
- Chipmall, "Rockchip RK3588 SoC, Mali-G610 GPU, and 6 TOPS NPU", https://www.chipmall.com/news/rockchip-rk3588-soc-mali-g610-gpu-and-6-tops-npu-for-8k-for-edge-ai-applications_435
- AIMultiple Research, "Top Edge AI Chip Makers with Use Cases in 2026", https://research.aimultiple.com/edge-ai-chips/

*※ 수치는 위 출처가 제시한 제품 사양값이다. Jetson Orin의 40~275 TOPS는 Orin Nano급부터 AGX Orin까지의 제품군 범위이며, 모듈·전력 모드에 따라 달라진다. Ethos-U85의 0.25~4 TOPS는 MAC 구성(128~2,048)과 클럭에 따른 범위다.*
