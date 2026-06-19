---
layout: post
title: "피지컬 AI 시대의 데이터 단위는 페타바이트다"
subtitle: "자율주행·휴머노이드 로봇이 만들어내는 데이터 양적 단절"
categories: [ax]
tags: [physical-ai, autonomous-driving, humanoid, data, nvidia, waymo, tesla]
toc: true
status: published
date: 2026-06-20 05:48:37 +09:00
---

## 0. 단위가 한 칸 옮겨갔다

피지컬 AI(Physical AI)는 IBM의 정의 그대로 "센서로 물리 세계를 인지하고 액추에이터로 작용하는 AI"다. 자율주행차·휴머노이드 로봇·산업용 매니퓰레이터·드론이 같은 범주에 들어간다. 텍스트 기반 LLM 시대의 학습 데이터는 인터넷 텍스트 전체를 끌어모아도 테라바이트 단위에서 끝났다. 피지컬 AI는 그렇지 않다. **차량 1대·로봇 1대가 하루에 만들어내는 raw 센서 로그만으로 페타바이트로 진입한다.**

> **피지컬 AI는 모델의 문제이기 이전에 데이터 양의 문제다.**

이 글은 그 양적 단절이 산업·정책·인프라에 어떤 모양으로 떨어지고 있는지의 관찰 노트다.

## 1. 차량 1대가 하루에 만드는 데이터

스토리지 업체 Tuxera가 정리한 수치에 따르면, 자율주행·ADAS 테스트 차량 1대는 **하루에 11 TB ~ 152 TB**의 데이터를 만들어낸다. 시간당으로는 1.4 TB ~ 19 TB. 카메라(다중)·LiDAR·레이더·IMU·GPS·V2X 로그가 동시에 돈다.

플릿 단위로 보면 단위가 한 번 더 올라간다. 같은 자료는 Waymo가 2018년경 약 200대 규모의 테스트 플릿을 운영했을 때 **하루 2.2 PB ~ 30.4 PB**의 센서 데이터를 저장했을 것으로 추정했다. 2026년 현재 플릿 규모는 그때보다 훨씬 크다. Waymo는 2026년 주당 100만 건의 자율 운행을 목표로 도시 확장 중이다.

이 숫자는 단순히 저장 비용만의 문제가 아니다. 차량 내 엣지 저장·차고지 다운로드 노드·중앙 클라우드 적재까지 **세 단계의 데이터 파이프라인**이 모두 페타바이트를 견디도록 다시 설계돼야 한다. AWS와 NVIDIA가 2026년에 공동 발표한 "Autonomous Vehicle 3.0" 파이프라인이 정확히 그 자리를 메우는 참조 아키텍처다.

## 2. 휴머노이드 로봇 — 또 한 칸의 단위 상승

자율주행이 페타바이트의 1막이라면, 휴머노이드 로봇은 2막이다. Elon Musk는 Tesla Optimus의 학습에 필요한 AI 컴퓨트가 **차량의 약 10배**가 될 것이라고 명시했다. 데이터 측면에서도 비슷한 비율이 따라온다.

Tesla는 Fremont 공장에서 1년 넘게 사람 작업자의 작업 영상을 녹화해 학습 데이터로 쓰고 있다. 2026년 1월 기준 Tesla는 Gigafactory Texas와 Fremont에 1,000대 이상의 Optimus Gen 3를 배치했고, Q2 2026에는 Fremont를 휴머노이드 전용 공장으로 전환해 연 100만 대 생산을 목표로 한다고 발표했다. **로봇 1대가 사람 작업자의 카메라 시점 영상을 모으는 수집기로도 동시에 동작한다는 뜻이다.**

같은 시기 한국에서는 NC AI를 중심으로 15개 기관이 참여한 'K-피지컬 AI 얼라이언스'가 출범했고, 정부는 2030년 피지컬 AI 세계 1위를 명시적 목표로 내건 'AI 행동계획(2026~2028)'을 확정했다. 이 정책 문서에서 데이터 관련 과제 비중이 크다는 사실은, 한국이 모델보다 데이터에서 먼저 격차를 인식했다는 신호로 읽힌다.

## 3. 그래서 무엇이 바뀌는가

데이터가 양적으로 한 칸 옮겨가면, 그 위에서 굴러가던 작업들이 모두 다시 설계된다.

**저장과 전송**: S3 같은 객체 스토리지가 페타바이트급 raw 센서 로그의 1차 적재지가 됐다. NVIDIA는 2026년 GTC에서 'Physical AI Data Factory Blueprint'를 공개했다. 컴퓨트를 학습 데이터로 변환하는 단일 파이프라인으로, Cosmos 월드 파운데이션 모델과 OSMO 오퍼레이터가 큐레이션·증강·평가를 묶는다. FieldAI·Hexagon Robotics·Skild AI·Teradyne Robotics 같은 회사들이 이미 이 블루프린트로 작업한다.

**라벨링과 큐레이션**: 페타바이트를 사람이 라벨링하는 건 산술적으로 불가능하다. 자동 라벨링·액티브 러닝·약지도 학습이 표준이 됐다.

**시뮬레이션의 비중 급증**: Waymo는 2026년 2월에 'Waymo World Model'을 발표했다. Google DeepMind의 Genie 3 위에 자율주행 도메인을 입힌 생성형 시뮬레이터다. 카메라 영상과 LiDAR를 동시에 합성하며, "도로에 코끼리가 있는" 상황 같은 엣지 시나리오까지 텍스트 프롬프트로 만들어낸다. Waymo는 **수십억 마일의 가상 주행으로 모델을 학습·평가**한다고 밝혔다. 합성 데이터 비중이 점점 올라가는 이유는 단순하다 — 실제 도로에서 보기 힘든 상황을 실제 도로에서 기다리는 비용보다, 모델로 만드는 비용이 훨씬 싸다.

**평가의 재현성**: 같은 모델을 6개월 뒤 다시 평가하려면 페타바이트 단위 데이터셋의 버전을 어떻게 고정할 것인가가 새로운 문제가 된다. NVIDIA Cosmos 3·Cosmos Predict 2.5·Cosmos Reason 2가 묶음으로 발표된 이유 중 하나는 **시뮬레이션 자체를 버전 관리 가능한 자산으로 만드는 것**이다.

## 4. AX 공모·정책의 자리

정부 AX 사업에서 피지컬 AI 관련 RFP는 더 이상 "데이터를 어떻게 수집할 것인가"만 묻지 않는다. **데이터 거버넌스·합성 데이터 비중·시뮬레이션 환경·평가 재현성**까지가 평가표 안에 들어온다. 한국이 자율주행에서 강점이 있다는 진단은 옳지만, 그 강점은 차량 OEM의 강점이지 페타바이트급 데이터 파이프라인 운영의 강점은 아니다. 산업계에서 "자유로운 데이터 수집과 임시 운행허가가 필요하다"는 요구가 2026년 4월 국회 토론회에서 공식 의제로 올라온 배경이다.

> **모델은 사올 수 있다. 데이터 파이프라인은 사올 수 없다.**

AX 사업 제안서를 쓰는 입장에서 이 한 줄이 가장 중요하다. 모델 성능을 약속하는 제안은 점점 흔해지지만, "페타바이트급 멀티 모달 센서 데이터를 어떻게 적재·큐레이션·합성·평가할 것인가"의 답을 가진 제안은 흔하지 않다. 격차는 여기서 벌어진다.

## 5. 사람에게 남는 일

페타바이트 단위의 데이터에서 사람은 더 이상 라벨을 붙이지 않는다. 그러나 **어떤 데이터를 모을지·어떤 시나리오를 합성할지·무엇을 평가의 기준으로 둘지는 여전히 사람이 결정한다.** 자동화의 양이 커질수록 그 결정의 잔존 무게도 커진다. 이 시리즈가 반복해 던지는 질문이 여기서도 그대로다 — 이 단계에서 코딩·AI 에이전트가 보편화된 환경의 사람에게 새로 요구되는 능력은 무엇인가.

피지컬 AI에 대해서는 한 줄로 답할 수 있다. **데이터의 단위가 페타바이트로 옮겨갔다는 사실을 산업의 언어로 통역하는 능력**, 그리고 **그 단위 위에서 의사결정이 가능한 운영 정책을 명문화하는 능력**이다.

---

## 출처

- NVIDIA, "Open Physical AI Data Factory Blueprint" (2026), https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development
- NVIDIA Newsroom, "Major Release of Cosmos World Foundation Models" (2026), https://nvidianews.nvidia.com/news/nvidia-announces-major-release-of-cosmos-world-foundation-models-and-physical-ai-data-tools
- AWS Industries Blog, "End-to-End Physical AI Data Pipeline for Autonomous Vehicle 3.0" (2026), https://aws.amazon.com/blogs/industries/building-an-end-to-end-physical-ai-data-pipeline-for-autonomous-vehicle-3-0-on-aws-with-nvidia/
- Tuxera, "Autonomous and ADAS test cars produce over 11 TB of data per day", https://www.tuxera.com/blog/autonomous-and-adas-test-cars-produce-over-11-tb-of-data-per-day/
- Waymo, "The Waymo World Model: A New Frontier For Autonomous Driving Simulation" (2026-02), https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/
- Technology Magazine, "Waymo Targets One Million Weekly Autonomous Trips by 2026", https://technologymagazine.com/news/waymo-brings-robotaxis-to-three-more-us-cities
- eWeek, "Why Tesla's Robot Optimus Has a New Training Strategy", https://www.eweek.com/news/tesla-optimus-robot-training/
- Programming Helper Tech, "Tesla Optimus Gen 3 Goes Into Production" (2026), https://www.programming-helper.com/tech/tesla-optimus-gen3-production-deployment-2026-factory-robots-revolution
- IBM, "What is Physical AI?", https://www.ibm.com/think/topics/physical-ai
- Deloitte Insights, "AI goes physical: Navigating the convergence of AI and robotics" (Tech Trends 2026), https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/physical-ai-humanoid-robots.html
- MS Today, "2030년 피지컬 AI 세계 1위 목표, 정부 AI 행동계획 공개", https://www.mstoday.co.kr/news/articleView.html?idxno=99992
- ZDNet Korea, "정부 '2030 피지컬 AI 1위' 정조준", https://zdnet.co.kr/view/?no=20260211094955
- 서울경제, "한국, 자율주행에 강점…'피지컬 AI 주도권' 목표로 매진해야", https://www.sedaily.com/article/20003851

*※ 일부 수치(차량 1대당 데이터량, Waymo 플릿 추정치)는 인용 출처가 제시한 추정값이며, 차량 세대·센서 구성에 따라 폭이 크다. 본문에서도 "추정"을 유지함.*
