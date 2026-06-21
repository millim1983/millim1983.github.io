# TTT-E2E (arXiv 2512.23675) — 논문 리뷰 자료 (2026-06-21 조사)

제목: End-to-End Test-Time Training for Long Context
저자: Arnuv Tandon, Karan Dalal, Xinhao Li, Daniel Koceja, Marcel Rød, Sam Buchanan, Xiaolong Wang, Jure Leskovec, Sanmi Koyejo, Tatsunori Hashimoto, Carlos Guestrin, Jed McCaleb, Yejin Choi, Yu Sun
소속: Astera Institute, NVIDIA, Stanford, UC Berkeley, UC San Diego
라이선스: CC BY 4.0 / 코드: https://github.com/test-time-training/e2e (JAX)

## 핵심
- 긴 컨텍스트를 아키텍처가 아니라 "지속 학습(continual learning)" 문제로 봄.
- 표준 트랜스포머 + 슬라이딩 윈도우 어텐션(SWA, 8k 윈도우). 추론 시(test time) 주어진 컨텍스트로 next-token prediction을 돌려 그 컨텍스트를 가중치에 압축.
- train time에는 메타러닝으로 "test time에 잘 학습되도록" 초기값을 최적화. = 이중 루프(dual loop), end-to-end.

## 메커니즘(inner/outer)
- inner: 학습 시퀀스를 1,000토큰 청크로 분할. 각 청크에 SWA(8k 윈도우)로 next-token 예측 → loss → 네트워크 마지막 1/4의 FC층 가중치 갱신.
- outer: 시뮬레이션된 가중치 갱신 후의 평균 next-token loss를 계산, 가중치 갱신 시퀀스를 통해 역전파하여 전체 가중치 조정(메타러닝).

## 규모·데이터
- 3B 파라미터, 총 164B 토큰. 사전학습: 필터링된 웹텍스트, 8,000토큰 시퀀스.
- 파인튜닝: The Pile의 Books 서브셋, 최대 128,000토큰 시퀀스.

## 결과(수치)
- 평균 loss(8k~128k): TTT-E2E 기준. vanilla transformer +0.015, Mamba2·Gated DeltaNet +0.03 높음(=TTT-E2E가 가장 낮음).
- Needle-in-a-Haystack(128k): **TTT-E2E 6%, Mamba2·Gated DeltaNet 각 7%, vanilla transformer 99%** ← 검색형 과제에서 TTT-E2E가 약함(중요 한계).
- 추론 속도(H100): TTT-E2E 첫 토큰 생성시간 1,000토큰당 +25ms 선형 증가(8k~128k). vanilla는 1,000토큰당 12→70ms로 증가. 128k에서 약 2.7배 빠름.
- 학습 지연: TTT-E2E 0.25s(8k)→0.33s(128k). Mamba2/GatedDeltaNet 약 0.06s 일정.

## 한계
- 8k 넘는 long-context retrieval(NIAH)에서 성능 급락. 학습 복잡도가 효율적 대안보다 큼 = 학습/추론 효율의 트레이드오프.

## 출처
- arXiv abs: https://arxiv.org/abs/2512.23675 / PDF: https://arxiv.org/pdf/2512.23675 / 프로젝트: https://test-time-training.github.io/e2e.pdf
- the Batch(deeplearning.ai): https://www.deeplearning.ai/the-batch/test-time-training-end-to-end-ttt-e2e-retrains-model-weights-to-handle-long-inputs
- VentureBeat: https://venturebeat.com/infrastructure/new-test-time-training-method-lets-ai-keep-learning-without-exploding
- 코드: https://github.com/test-time-training/e2e
