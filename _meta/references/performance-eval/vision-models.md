# 비전 인식 모델 성능평가 자료조사

> 자료조사 노트 (블로그 글 아님). 작성 2026-06-26. 대상: 이미지 분류·객체 검출·세그멘테이션·이상탐지(제조 결함 포함).
> 모든 수치는 WebSearch로 검증한 값이며, 출처 미확인은 "미확인"으로 표기. 추측 금지.
> 주의: 벤치마크 리더보드 수치는 빠르게 갱신되며, 본 노트는 2026-06 시점 검색 결과 기준이다.

---

## 1. 성능지표명·정의

| 지표 | 적용 태스크 | 정의 (요약) | 비고 |
|---|---|---|---|
| Top-1 accuracy | 이미지 분류 | 모델이 최고 확률로 예측한 1개 클래스가 정답과 일치하는 비율 | ImageNet-1k의 대표 지표 |
| Top-5 accuracy | 이미지 분류 | 상위 5개 예측 안에 정답이 포함된 비율 | 2018년경 사실상 포화(~99%), 현재 변별력 낮음 |
| Precision | 검출/분류/이상탐지 | TP / (TP+FP). 양성이라 예측한 것 중 실제 양성 비율 | |
| Recall (Sensitivity) | 검출/분류/이상탐지 | TP / (TP+FN). 실제 양성 중 잡아낸 비율 | 결함검출에서 미검(FN) 최소화 핵심 |
| F1-score | 분류/검출 | Precision·Recall의 조화평균 | 불균형 데이터에서 accuracy 보완 |
| IoU (Jaccard) | 검출/세그멘테이션 | 예측 영역 ∩ 정답 / 예측 영역 ∪ 정답 | 박스/마스크 겹침 정도 |
| mIoU | 세만틱 세그멘테이션 | 클래스별 IoU의 평균 | ADE20K·Cityscapes 대표 지표 |
| AP (Average Precision) | 객체 검출 | Precision-Recall 곡선 아래 면적 (클래스별) | |
| mAP | 객체 검출 | 전 클래스 AP 평균 | |
| mAP@0.5 | 객체 검출 | IoU 임계값 0.5 기준 mAP (PASCAL VOC 방식) | 느슨한 기준 |
| mAP@0.5:0.95 | 객체 검출 | IoU 0.5~0.95를 0.05 간격으로 평균 (COCO 기본 지표) | "box AP"로 흔히 표기, 더 엄격 |
| AUROC | 이상탐지/이진분류 | ROC 곡선(TPR vs FPR) 아래 면적. 1.0이 완벽 | 이미지단위(I-AUROC)·픽셀단위(P-AUROC) 구분 |
| AUPRO (PRO) | 이상탐지 (픽셀단위) | Per-Region-Overlap. 결함 영역별 정확한 위치 탐지 평가, FPR 0.3까지 적분 | 작은 결함에 민감, 픽셀 AUROC의 한계 보완 |
| AUPIMO | 이상탐지 | 이미지별 PIMO 곡선 기반의 최신 지표(2024). 빠르고 낮은 허용오차 | 신규 제안 지표 |
| FPS / Latency | 실시간 검출 | 초당 처리 프레임 수 / 1프레임 추론 지연(ms) | 하드웨어·정밀도(FP16/INT8)·해상도 의존 |

---

## 2. 측정 방식·대표 데이터셋·평가 프로토콜

| 데이터셋 | 태스크 | 규모·구성 | 주 지표 | 프로토콜 메모 |
|---|---|---|---|---|
| ImageNet-1k | 이미지 분류 | 1,000 클래스, 학습 ~128만 장, val 5만 장 | Top-1 / Top-5 | val set 정확도로 보고. 대형 모델은 ImageNet-21k 등 사전학습 후 fine-tune |
| COCO | 객체 검출·인스턴스 세그 | 80 클래스, ~12만 학습 이미지 | mAP@0.5:0.95 (box AP) | test-dev로 SOTA 보고. 객체 크기별(S/M/L) AP도 함께 |
| ADE20K | 세만틱 세그멘테이션 | 150 클래스, 학습 20k·val 2k·test 3k | mIoU | val 기준 single-scale/multi-scale(ms) 구분 보고 |
| Cityscapes | 세만틱 세그멘테이션(도로) | 19 클래스, fine-annotated 5,000장 | mIoU | 자율주행 장면 한정, val/test 구분 |
| MVTec AD | 산업 이상탐지(제조 결함) | 15개 객체/텍스처 카테고리, 정상만 학습(비지도) | I-AUROC, P-AUROC, AUPRO | 정상 이미지로만 학습 후 결함 분리 능력 평가. 산업 결함검출 표준 벤치마크 |

---

## 3. 세계 최고 수준 (SOTA, 2026-06 검색 기준)

| 태스크 / 벤치마크 | 지표 | SOTA 수치 | 모델 | 출처 |
|---|---|---|---|---|
| 이미지 분류 / ImageNet-1k | Top-1 | **91.0%** | CoCa (2.1B, fine-tuned encoder) | CodeSOTA, HiringNet |
| 이미지 분류 / ImageNet-1k | Top-1 | 90.45% | ViT-G/14 (이전 SOTA) | ResearchGate / 검색결과 |
| 객체 검출 / COCO test-dev | box AP (mAP@0.5:0.95) | **66.1** (리더보드 SOTA 표기 66.12) | ScyllaNet (2025-09) | CodeSOTA, paperswithcode |
| 객체 검출 / COCO test-dev | box AP | 66.0 | CW_Detection, SenseTime Basemodel, Thinker | CodeSOTA |
| 객체 검출 / COCO test-dev | box AP | 65.5 | InternImage-H (OneFormer) | CodeSOTA |
| 세만틱 세그 / ADE20K (val) | mIoU (ms) | **63.0** | ONE-PEACE (1.52B) | OFA-Sys/ONE-PEACE, OpenReview |
| 세만틱 세그 / ADE20K (val) | mIoU | 62.9 | InternImage-H + Mask2Former | InternImage paper |
| 세만틱 세그 / ADE20K (val) | mIoU | 62.8 | BEiT-3 | BEiT-3 / 검색결과 |
| 세만틱 세그 / Cityscapes | mIoU | **83.1** | SegFormer (+Mapillary 사전학습) | arXiv SegFormer |
| 이상탐지 / MVTec AD | I-AUROC | **99.8%** | EfficientAD | EfficientAD (WACV 2024) |
| 이상탐지 / MVTec AD | I-AUROC | 99.6% | SimpleNet | CodeSOTA, SimpleNet paper |
| 이상탐지 / MVTec AD | I-AUROC | ~99.1% | PatchCore | PatchCore/검색결과 |
| 이상탐지 / MVTec AD | AUPRO (픽셀) | 95.2% | ReContrast | ReContrast paper |
| 이상탐지 / MVTec AD | P-AUROC / AUPRO | 98.1% / 93.5% | PatchCore | 검색결과 |

비고: MVTec AD의 I-AUROC는 사실상 포화(상위권 97~99.8% 군집). 연구 프런티어가 **픽셀단위 위치탐지(P-AUROC·AUPRO·AUPIMO)** 및 추론속도로 이동.

### 실시간 객체 검출 (정확도-속도 트레이드오프)

| 모델 | mAP (COCO, box AP) | 지연/속도 | 하드웨어·조건 | 출처 |
|---|---|---|---|---|
| YOLOv12-N | 40.6 | 1.64 ms | T4 GPU, TensorRT FP16 | github sunsmarterjie/yolov12 |
| YOLOv11-S | 47.0 | 경량 모델 중 최고 mAP | — | arXiv YOLOv11 리뷰 |
| YOLOv12-X | 55.2 | ~12 ms (mAP50-95 ~56% 보고도 있음) | T4 GPU, TensorRT FP16 | github yolov12, DigitalOcean |
| (참고) 비실시간 SOTA | 60+ AP | < 5 FPS | — | CodeSOTA 메모 |
| (참고) 실시간 군 | 45~55 AP | 100+ FPS | 최신 GPU | CodeSOTA, HiringNet 메모 |

핵심 트레이드오프: 비실시간 대형 SOTA는 66 AP / <5 FPS, 실시간 YOLO·RT-DETR 계열은 45~55 AP / 100+ FPS.

---

## 4. 국내 최고 수준

| 주체 | 성과 | 수치 | 출처 / 비고 |
|---|---|---|---|
| ETRI 시각지능연구실 | VoVNet 백본 + CenterMask (실시간 anchor-free 인스턴스 세그) | "세계 최고 성능 달성" 자체표기 (CVPR 2020 발표) | ETRI Visual Intelligence Lab. 구체 mAP 수치 **공개자료 미확인** |
| ETRI | LPIRC 2018 (저전력 이미지인식 챌린지) track 3 우승 | 전년 1위 동일 HW 대비 최종 스코어 약 4배 | ETRI ettrends. 절대 정확도 수치는 미확인 |
| 삼성전자 | AI 품질검사로 반도체 불량률 절감 | 불량률 0.08%까지 | SAIGE/NEXA 블로그 인용 (1차 출처·측정조건 미확인) |
| 현대자동차 | AI 비전검사로 도장 불량 감소 | 도장 불량 95% 감소 | NEXA 블로그 인용 (1차 출처 미확인) |
| LG AI연구원 + KAIST | 제조 공정 변경에도 적응하는 결함검출 AI | 2025-08 국제학회 발표 | KAIST 보도자료. 정량 지표 본문 미확인 |
| 네이버·카카오 | 비전 모델 벤치마크 정량 성과 | — | **공개자료 미확인** (검색결과에 ImageNet/COCO 수치 없음) |
| 포스코 | 비전검사 불량 검출률 | — | **공개자료 미확인** |

요약: 국내는 ETRI의 실시간 검출/세그(VoVNet·CenterMask) 계열과 제조사(삼성·현대·LG)의 현장 적용 사례가 두드러지나, **ImageNet/COCO/MVTec 리더보드 형식의 비교 가능한 정량 SOTA 수치는 대체로 공개자료 미확인**. 제조 결함검출 분야 국내 상용 솔루션(예: SAIGE)이 활발하나 표준 벤치마크 수치는 미확인.

---

## 5. 개발기간별 목표 제안 (1년/2년/3년)

> 전제: 신규 비전 인식 모델/솔루션을 처음 개발한다고 가정. 현 SOTA와 데이터 확보 난이도를 고려해 **보수적**으로 제시.
> 실제 목표는 데이터 품질·라벨링 예산·도메인 난이도·팀 역량에 따라 조정 필요.

### 5-1. 제조 결함 검출 (이상탐지, MVTec AD형 / 비지도 또는 소량 지도)

| 차수 | 목표 (I-AUROC 기준) | 픽셀단위(AUPRO) | 근거 |
|---|---|---|---|
| 1년차 | I-AUROC ~95% | AUPRO ~85% | PatchCore/PaDiM 등 검증된 오픈소스 베이스라인으로 도달 가능. 자사 데이터 정상셋 구축 단계 |
| 2년차 | I-AUROC ~98% | AUPRO ~90% | 도메인 fine-tune + 데이터 증강·합성결함. 실 라인 데이터 축적 |
| 3년차 | I-AUROC ~99%+ (SOTA 근접) | AUPRO ~93~95% | EfficientAD/ReContrast급 근접. 단, 자사 도메인은 공개벤치보다 어려울 수 있어 여유 둘 것 |

비고: MVTec AD가 포화 상태라 공개벤치 수치는 빠르게 닿지만, **현장 데이터는 결함 다양성·조명 변동 때문에 공개벤치보다 어렵다.** 현장 목표는 위 수치에서 1~3%p 보수적으로.

### 5-2. 객체 검출 (COCO형 또는 도메인 특화 검출)

| 차수 | 목표 (도메인 검출, mAP@0.5:0.95) | 실시간성 | 근거 |
|---|---|---|---|
| 1년차 | mAP ~40~45 | 30+ FPS (YOLOv11/12 fine-tune) | 사전학습 YOLO 계열 전이학습으로 빠르게 베이스라인 |
| 2년차 | mAP ~50~55 | 30~60 FPS | 데이터 확대·하드네거티브 마이닝·해상도 조정 |
| 3년차 | mAP ~55~60 (도메인) | 목표 HW에서 실시간 유지 | RT-DETR/대형 백본 검토. 공개 COCO SOTA(66)는 비실시간·초대형이라 산업 적용 목표로는 비현실적 |

### 5-3. 이미지 분류 (도메인 특화 분류)

| 차수 | 목표 (도메인 Top-1) | 근거 |
|---|---|---|
| 1년차 | ~90% | ImageNet 사전학습 ViT/ConvNeXt fine-tune. 클래스 수 적으면 더 높을 수 있음 |
| 2년차 | ~95% | 데이터 정제·증강·앙상블 |
| 3년차 | ~97%+ | 도메인 난이도에 좌우. 혼동 클래스 해소가 관건 |

### 5-4. 세만틱 세그멘테이션 (도메인 특화)

| 차수 | 목표 (도메인 mIoU) | 근거 |
|---|---|---|
| 1년차 | ~70% | SegFormer/Mask2Former 전이학습 |
| 2년차 | ~78% | 라벨 품질 향상·해상도·멀티스케일 |
| 3년차 | ~82%+ | Cityscapes급(83) 근접. ADE20K급(63)은 클래스 다양성 때문에 도메인 단순하면 더 높게 가능 |

> 공통 주의: 위 차수별 목표는 "공개 벤치마크 SOTA를 따라가는 곡선"이 아니라 "자사 도메인 데이터에서 달성 가능한 현실 목표"로 해석할 것. SOTA 절대수치(예: ImageNet 91%, COCO 66 AP)는 초대형 모델·방대한 사전학습 자원의 산물이라 산업 신규개발의 직접 목표로 부적절.

---

## 6. 미확인 항목 보고

- 네이버·카카오의 ImageNet/COCO 등 표준 벤치마크 정량 성과: **공개자료 미확인**.
- 포스코 비전검사 불량 검출률 구체 수치: **미확인**.
- ETRI CenterMask/VoVNet의 구체적 COCO mAP·ADE20K mIoU 절대 수치: **미확인**("세계 최고 성능" 자체표기만 확인).
- 삼성 불량률 0.08%, 현대 도장불량 95% 감소: 마케팅/2차 블로그 인용이라 **1차 출처·측정조건 미확인** — 신뢰도 낮음, 인용 시 주의.
- COCO SOTA 66.1(ScyllaNet)은 상용 벤더 리더보드 제출값으로, 논문 동료심사 여부 **미확인**. 학술 SOTA로는 InternImage-H(65.5)가 더 안전한 인용.
- YOLOv12-X "~56% mAP" 일부 표기는 출처별 편차 있음(55.2 vs ~56) — 측정 조건 차이 가능.

---

## 7. 출처 URL 목록

- ImageNet-1k Leaderboard (CodeSOTA): https://www.codesota.com/benchmark/imagenet-1k
- Image Classification SOTA 2025 (HiringNet): https://hiringnet.com/image-classification-state-of-the-art-models-in-2025
- COCO Object Detection Leaderboard (CodeSOTA): https://www.codesota.com/browse/computer-vision/object-detection/coco
- Object Detection on COCO (Papers with Code): https://paperswithcode.com/sota/object-detection-on-coco
- ScyllaNet COCO 결과 (Scylla AI): https://www.scylla.ai/scyllanet-ranked-2nd-on-coco-leaderboard/
- ADE20K Semantic Segmentation SOTA (Wizwand): https://www.wizwand.com/sota/semantic-segmentation-on-ade20k
- ONE-PEACE (GitHub / OpenReview): https://github.com/OFA-Sys/ONE-PEACE , https://openreview.net/pdf/fe7c35568697b11f757f443787020a341b56d2eb.pdf
- InternImage (arXiv): https://arxiv.org/abs/2211.05778
- SegFormer (arXiv): https://arxiv.org/pdf/2105.15203
- MVTec AD Leaderboard (CodeSOTA): https://www.codesota.com/benchmark/mvtec-ad
- EfficientAD (WACV 2024): https://openaccess.thecvf.com/content/WACV2024/papers/Batzner_EfficientAD_Accurate_Visual_Anomaly_Detection_at_Millisecond-Level_Latencies_WACV_2024_paper.pdf
- SimpleNet (arXiv): https://arxiv.org/pdf/2303.15140
- ReContrast (arXiv): https://arxiv.org/pdf/2306.02602
- AUPIMO (arXiv): https://arxiv.org/pdf/2401.01984
- PatchCore (EmergentMind): https://www.emergentmind.com/topics/patchcore
- YOLOv12 (GitHub): https://github.com/sunsmarterjie/yolov12
- YOLOv12 분석 (DigitalOcean): https://www.digitalocean.com/community/tutorials/yolov12-next-big-leap-in-object-detection
- ETRI Visual Intelligence Lab: https://etri-visualintelligence.github.io/deepview/
- ETRI 모바일/임베디드 인식 동향 (ettrends): https://ettrends.etri.re.kr/ettrends/180/0905180012/
- KAIST 적응형 결함검출 연구 보도: https://www.kaist.ac.kr/researchnews/html/news/?mode=V&mng_no=50950
- 국내 제조 AI 비전검사 (SAIGE): https://saige.ai/blog/ai-vision-inspection/
- 머신러닝 품질관리 불량률 (NEXA): https://getnexa.io/blog/machine-learning-quality-control
