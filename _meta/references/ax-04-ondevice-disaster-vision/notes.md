# 온디바이스 비전 재난탐지 — 자료 노트 (2026-06-19 조사)

> ax-04(자료조사+트렌드), ax-05(개발 방법론) 두 글의 근거. 다음 세션 재사용용.

## 사례 (2026)
- **Edge Alert Sentinel (EAS)**: SDG&E + Qualcomm + UC San Diego Scripps, 2026-06 발표. 산불·극한기상, 위험지점 실시간 엣지 추론. (Sempra newsroom)
- **위성 온보드 홍수 변화탐지**: arXiv 2601.13751 "Towards Onboard Continuous Change Detection for Floods".
- **UAV 화재 탐지 + 증류**: arXiv 2502.20979 "Real-Time Aerial Fire Detection on Resource-Constrained Devices Using Knowledge Distillation".
- **UAV 산불관리 서베이**: Springer AI Review 10.1007/s10462-025-11415-3.
- **엣지AI 산불탐지**: Springer Discover Computing 10.1007/s10791-026-09989-9.
- **위성 온보드 엣지(재난관리)**: UN-SPIDER Knowledge Portal.

## 기술 통설 (온디바이스 모델 압축, 2026)
- **양자화가 가장 확실**: 메모리·전력 제약 빡빡할수록 양자화 > 가지치기·증류. (Nature s41598-025-94205-9)
- 16비트 학습 → 4비트 배치. PTQ: GPTQ·AWQ로 품질 유지하며 메모리 4배↓.
- 증류: 큰 교사 + 고품질 합성데이터가 파라미터 증설보다 효과적일 때 있음.
- **NPU 표준화**: 2026 스마트폰·노트북·산업장비 기본 부품. (Edge AI Vision Alliance)
- 개발 순서: 장비 확정 → 상한 계산 → 기준 모델 → 압축 → 현장 검증(발열·전력 포함).

## 페르소나 주의
- 특정 사업·발주처·소속 노출 금지. 일반화 스터디 노트 톤.
