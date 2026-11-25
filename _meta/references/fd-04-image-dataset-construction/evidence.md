# evidence - fd-04-image-dataset-construction

열람일: 2026-10-22 (전 출처 공통). PDF는 원문을 내려받아 텍스트 추출 후 해당 쪽을 직접 읽었다.

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks | Curtis G. Northcutt, Anish Athalye, Jonas Mueller | 2021 (NeurIPS 2021 Datasets and Benchmarks Track) | https://arxiv.org/abs/2103.14749 (PDF v4) | Abstract, 1 Introduction, 4 Validating label errors with Mechanical Turk |
| S2 | Confident Learning: Estimating Uncertainty in Dataset Labels | Curtis G. Northcutt, Lu Jiang, Isaac L. Chuang | 2021 (JAIR; arXiv v6 2022) | https://arxiv.org/abs/1911.00068 (PDF v6) | Abstract, 2 (inputs), 3.1 confident joint 식 (1)(2), 3.2 pruning, 실험 설정 (4-fold CV) |
| S3 | MVTec AD - A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection | Paul Bergmann, Michael Fauser, David Sattlegger, Carsten Steger | 2019 (CVPR 2019) | https://openaccess.thecvf.com/content_CVPR_2019/papers/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.pdf | Abstract, 3 Dataset Description, Table 1, 4.2 Data Augmentation, 4.3 Evaluation Metric |
| S4 | A Survey of Deep Active Learning | Pengzhen Ren, Yun Xiao, Xiaojun Chang, Po-Yao Huang, Zhihui Li, Brij B. Gupta, Xiaojiang Chen, Xin Wang | 2021 | https://arxiv.org/abs/2009.00236 (PDF v2) | Abstract, 1 (pool-based cycle), 3.1 BMDAL, Uncertainty-based and Hybrid Query Strategies |
| S5 | Do we train on test data? Purging CIFAR of near-duplicates | Björn Barz, Joachim Denzler | 2019 (arXiv) | https://arxiv.org/abs/1902.00423 | Abstract, 3.1 Mining Duplicate Candidates, 3.2 Manual Annotation |
| S6 | Datasheets for Datasets | Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford | 2021 (arXiv v8) | https://arxiv.org/abs/1803.09010 | 1 Introduction, 2 Questions and workflow, Collection Process |
| S7 | A survey on Image Data Augmentation for Deep Learning | Connor Shorten, Taghi M. Khoshgoftaar | 2019 | https://journalofbigdata.springeropen.com/articles/10.1186/s40537-019-0197-0 (J Big Data (2019) 6:60, PDF) | Geometric augmentations 절 (safety, Flipping, Cropping, Rotation) |
| S8 | Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, Pieter Abbeel | 2017 | https://arxiv.org/abs/1703.06907 | Abstract, A. Domain randomization |
| S9 | CVAT 공식 문서 (Automatic annotation / Dataset formats / Auto QA / Quality control / Shapes 메뉴) | CVAT.ai | 2026 열람 | https://docs.cvat.ai/docs/annotation/auto-annotation/automatic-annotation/ , https://docs.cvat.ai/docs/dataset_management/formats/ , https://docs.cvat.ai/docs/qa-analytics/auto-qa/ , https://docs.cvat.ai/docs/qa-analytics/quality-control/ , https://docs.cvat.ai/docs/annotation/manual-annotation/shapes/shape-mode-basics/ | 각 페이지 본문 및 내비게이션 |
| S10 | Label Studio 공식 문서 (Labeling config / Tags / ML backend) | HumanSignal | 2026 열람 | https://labelstud.io/guide/setup , https://labelstud.io/tags/ , https://labelstud.io/guide/ml | 각 페이지 본문 |

## 본문 문장 ↔ 원문 발췌

### S1 Pervasive Label Errors
- [10개 벤치마크 테스트셋에 평균 3.3% 이상, ImageNet 검증셋 6% 이상 라벨 오류] ↔ "we estimate an average of at least 3.3% errors across the 10 datasets, where for example label errors comprise at least 6% of the ImageNet validation set."
- [ImageNet 검증셋 오류 2,916건] ↔ "We identify, for example, 2916 (6%) errors in the ImageNet validation set (which is commonly used as a test set), and estimate over 5 million (10%) errors in QuickDraw."
- [CL로 후보를 뽑고 크라우드소싱으로 사람이 검증, 후보의 평균 51%가 실제 오류] ↔ "Putative label errors are identified using confident learning algorithms and then human-validated via crowdsourcing (51% of the algorithmically-flagged candidates are indeed erroneously labeled, on average across the datasets)."
- [후보 1건을 5명에게 독립 제시, 3명 미만이 기존 라벨에 동의하면 오류로 확정] ↔ "Each CL-flagged label error was independently presented to five workers. We consider the example validated (an “error”) if fewer than three of the workers agree that the data point has the given label (agreement threshold = 3 of 5)"
- [교정 라벨 기준 ImageNet에서 오라벨 비율이 6%p만 늘어도 ResNet-18이 ResNet-50을 앞선다, CIFAR-10에서 VGG-11이 VGG-19를 5%p에서] ↔ "on ImageNet with corrected labels: ResNet-18 outperforms ResNet-50 if the prevalence of originally mislabeled test examples increases by just 6%. On CIFAR-10 with corrected labels: VGG-11 outperforms VGG-19 if the prevalence of originally mislabeled test examples increases by just 5%."
- [교정 라벨에서는 NASNet보다 ResNet-18이 낫다] ↔ "NASNet is superior to ResNet-18 based on the test accuracy over originally given labels, but NASNet is in fact worse than ResNet-18 based on the test accuracy over corrected labels."

### S2 Confident Learning
- [CL은 노이즈 라벨과 참 라벨의 결합 분포를 직접 추정, 클래스 조건부 노이즈 가정] ↔ "building on the assumption of a class-conditional noise process to directly estimate the joint distribution between noisy (given) labels and uncorrupted (unknown) labels."
- [입력은 표본 외(out-of-sample) 예측 확률과 주어진 라벨, 교차검증으로 얻는다] ↔ "CL requires two inputs: (1) the out-of-sample predicted probabilities ... (e.g. cross-validation)" / "In practice, cross-validation might introduce a hyper-parameter: k-fold. However, in our paper k = 4 is fixed in the experiments using cross-validation."
- [클래스별 임계값 t_j = 해당 클래스로 라벨된 표본의 그 클래스 예측 확률 평균(self-confidence)] ↔ "and the threshold tj is the expected (average) self-confidence for each class" (식 (2): tj = 1/|X_{ỹ=j}| Σ p̂(ỹ = j; x, θ))
- [confident joint 정의: 라벨 i인 표본 중 클래스 j 확률이 t_j 이상이고 그중 최대인 표본 수] ↔ "the set of examples x labeled ỹ=i with large enough p̂(ỹ = j; x, θ) to likely belong to class y∗=j, determined by a per-class threshold, tj." (식 (1))
- [임계값은 클래스 불균형과 클래스별 확률 분포 차이에 강건하게 하려는 장치] ↔ "using thresholding and collision handling to enable robustness to class imbalance and heterogeneity in predicted probability distributions across classes."
- [모델·데이터 형식에 묶이지 않음, cleanlab 오픈소스] ↔ "the CL framework is not coupled to a specific data modality or model" / "These results are replicable using the open-source cleanlab framework."
- [오류 후보 제거 방식: 클래스별 개수만큼(prune by class), 비대각 칸별(prune by noise rate)] ↔ "number of errors in each class (prune by class), or prune for every off-diagonal partition (prune by noise rate). The choice of which examples to remove is made by ranking the"

### S3 MVTec AD
- [5354장, 15개 카테고리] ↔ "We introduce the MVTec Anomaly Detection (MVTec AD) dataset containing 5354 high-resolution color images" / "comprises 15 categories with 3629 images for training and validation and 1725 images for testing."
- [학습셋은 정상만, 테스트셋은 결함과 정상 모두] ↔ "The training set contains only images without defects. The test set contains both: images containing various types of defects and defect-free images."
- [텍스처 5종, 객체 10종] ↔ "Five categories cover different types of regular (carpet, grid) or random (leather, tile, wood) textures, while the remaining ten categories represent various types of objects."
- [결함 73종, 카테고리당 평균 5종, 결함은 사람이 일부러 만든 것] ↔ "In total, 73 different defect types are present, on average five per category. The defects were manually generated with the aim to produce realistic anomalies"
- [테스트 정상 467, 테스트 결함 1258, 결함 영역 1888] ↔ Table 1 Total 행: "Total 3629 467 1258 73 1888" (열: # Train, # Test (good), # Test (defective), # Defect groups, # Defect regions)
- [2048x2048 산업용 RGB 센서와 텔레센트릭 렌즈, 해상도 700~1024 정사각, 3종은 흑백] ↔ "All images were acquired using a 2048 × 2048 pixel high-resolution industrial RGB sensor in combination with two bilateral telecentric lenses" / "All image resolutions are in the range between 700 × 700 and 1024 × 1024 pixels." / "three object categories (grid, screw, and zipper) are made available solely as single-channel images."
- [조명을 강하게 통제, 일부 클래스는 일부러 바꿈] ↔ "The images were acquired under highly controlled illumination conditions. For some object classes, however, the illumination was altered intentionally to increase variability."
- [픽셀 단위 정답 영역 약 1900개] ↔ "We provide pixel-precise ground truth labels for each defective image region. In total, the dataset contains almost 1900 manually annotated regions."
- [증강: 회전·이동, 미러링은 객체가 허용할 때만, 카테고리당 10000 패치] ↔ "For each object category, we apply a random translation and rotation. Additional mirroring is applied where the object permits it. We augment each category to create 10000 training patches."
- [임계값은 학습에서 뺀 정상 검증 이미지로 추정] ↔ "we propose a well-defined way to estimate the threshold from a set of randomly selected validation images that we exclude from the training set."

### S4 A Survey of Deep Active Learning
- [AL 목표: 가장 적은 표본에 라벨을 붙여 성능 이득 최대화] ↔ "Active learning (AL) attempts to maximize a model’s performance gain while annotating the fewest samples possible."
- [pool-based 순환: 무작위 초기 표본 라벨 → 학습 → 다음 질의 선택 → 반복, 예산 소진이나 종료 조건까지] ↔ "In the initial state, we can randomly select one or more samples from the unlabeled pool U, give this sample to the oracle query label to get the labeled dataset L, and then train the model on L ... This process is repeated until the label budget is exhausted or the pre-defined termination conditions are reached"
- [주요 질의 전략: 불확실성, 다양성, 기대 모델 변화, 혼합] ↔ "the main query strategies include the uncertainty-based approach ..., diversity-based approach ... and expected model change .... In addition, many works have also studied hybrid query strategies"
- [불확실성만 쓰면 샘플링 편향, 다양성만 쓰면 정보량 낮은 표본까지 골라 비용 증가] ↔ "Because separate sampling based on uncertainty often results in sampling bias [26, 44], the currently selected sample is not representative of the distribution of unlabeled datasets. On the other hand, considering only strategies that promote diversity in sampling may lead to increased labeling costs"
- [margin = P(y1|x) - P(y2|x), 작을수록 불확실] ↔ "margin M is defined as the difference between the predicted highest probability and the predicted second highest probability ... M = P(y1 | x) - P(y2 | x)" / "The smaller the margin M, the greater the uncertainty of the sample x."
- [엔트로피 E(x) = -Σ P log P, 클수록 불확실] ↔ "E(x) = - Σ P(yi | x) · log (P(yi | x))" / "The greater the entropy of the sample, the greater its uncertainty."
- [딥러닝 AL은 배치 단위 질의, 한 장씩 고르면 재학습이 잦고 과적합 위험] ↔ "DeepAL uses batch-based sample querying. In traditional AL, most algorithms use a one-by-one query method, which leads to frequent training of the learning model but little change in the training data."
- [클래스가 많고 배치가 클수록 다양성 기반이, 배치가 작고 내용이 단순할수록 불확실성 기반이 유리] ↔ "the richer the category content of the dataset, the larger the batch size, and the better the effect of diversity-based methods; by contrast, an uncertainty-based query strategy will perform better with smaller batch sizes and less rich content."
- [BADGE는 불확실성과 다양성 자동 균형] ↔ "BADGE can achieve an automatic balance between forecast uncertainty and sample diversity"

### S5 Barz & Denzler
- [CIFAR-10 테스트 3.3%, CIFAR-100 10%가 학습셋에 중복] ↔ "we find that 3.3% and 10% of the images from the test sets of these datasets have duplicates in the training set."
- [중복 교체 후 정확도가 상대적으로 9~14% 떨어짐] ↔ "We find a significant drop in classification accuracy of between 9% and 14% relative to the original performance on the duplicate-free test set."
- [픽셀 단위 비교만으로는 부족, CNN 특징 L2 정규화 후 최근접 이웃 검색] ↔ "simply searching for exact pixel-level duplicates is not sufficient, since there may also be slightly modified variants of the same scene that vary by contrast, hue, translation, stretching etc." / "extract L2-normalized features from the global average pooling layer of the trained network" / "we find the nearest neighbor from the training set in terms of the Euclidean distance in that feature space."
- [거리 임계값만 쓰면 오탐 많아 거리순 정렬 후 사람이 확인, 4분류] ↔ "simply thresholding the distance between these pairs. However, such an approach would result in a high number of false positives as well. Therefore, we inspect the detected pairs manually, sorted by increasing distance." / 분류: "Exact Duplicate", "Near-Duplicate ... both originated from the same camera shot", "Very Similar", "Different"

### S6 Datasheets for Datasets
- [전자부품 데이터시트 유비] ↔ "In the electronics industry, every component, no matter how simple or complex, is accompanied with a datasheet describing its operating characteristics, test results, recommended usage, and other information."
- [7개 묶음: 동기·구성·수집 과정·전처리/정제/라벨링·용도·배포·유지보수] ↔ "The questions are grouped into sections that roughly match the key stages of the dataset lifecycle: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution, and maintenance."
- [수집 전에 질문을 읽어 두라] ↔ "dataset creators should read through these questions prior to any data collection to flag potential issues and then provide answers once collection is complete."

### S7 Shorten & Khoshgoftaar
- [증강의 safety = 변환 후 라벨이 유지될 가능성, 6 대 9 예시] ↔ "The safety of a Data Augmentation method refers to its likelihood of preserving the label post-transformation. For example, rotations and flips are generally safe on ImageNet challenges such as cat versus dog, but not safe for digit recognition tasks such as 6 versus 9."
- [어떤 변환이든 강도가 커지면 라벨을 바꿀 수 있다, 도메인 의존] ↔ "This is somewhat domain dependent" / "There is no image processing function that cannot result in a label changing transformation at some distortion magnitude."
- [크롭 비율에 따라 라벨 비보존] ↔ "Depending on the reduction threshold chosen for cropping, this might not be a label-preserving transformation."
- [회전 안전성은 각도에 좌우] ↔ "The safety of rotation augmentations is heavily determined by the rotation degree parameter."

### S8 Tobin et al. Domain Randomization
- [시뮬레이터 렌더링을 무작위화해 현실을 변형 중 하나로 보이게] ↔ "domain randomization, a simple technique for training models on simulated images that transfer to real images by randomizing rendering in the simulator. With enough variability in the simulator, the real world may appear to the model as just another variation."
- [무작위화 항목: 물체 위치·텍스처, 카메라 위치·방향·화각, 조명 수·위치, 노이즈] ↔ "Position and texture of all objects on the table" / "Position, orientation, and field of view of the camera" / "Number of lights in the scene" / "Type and amount of random noise added to images"
- [비현실적 무작위 텍스처의 시뮬레이터 데이터만으로 1.5cm 정확도 검출기] ↔ "it is possible to train a real-world object detector that is accurate to 1.5 cm and robust to distractors and partial occlusions using only data from a simulator with non-realistic random textures."

### S9 CVAT 문서
- [자동 주석 = 사전학습 모델로 사전 라벨] ↔ "Automatic annotation in CVAT is a tool that you can use to automatically pre-annotate your data with pre-trained models."
- [detector 또는 reidentifier 모델 필요, Nuclio 함수] ↔ "To use automatic annotation, you must be able to access at least one AI model of type “detector” or “reidentifier”" / "Region of interest is supported for detector models, including Nuclio functions"
- [도형 종류: 사각형·폴리곤·폴리라인·점·타원·큐보이드·스켈레톤·브러시(마스크)·태그] ↔ 문서 내비게이션 제목: "Annotation with polygons", "Annotation with polylines", "Annotation with points", "Annotation with ellipses", "Annotation with cuboids", "Annotation with skeletons", "Annotation with brush tool", "Annotation with tags", "Creating masks"; 본문 "You need to select `Rectangle` on the controls sidebar"
- [내보내기 형식: COCO, PASCAL VOC, YOLO, Ultralytics YOLO, Segmentation Mask, Datumaro 등] ↔ "The table below outlines the available formats for data export in CVAT." 목록에 "COCO 1.0", "PASCAL VOC 1.1", "YOLO 1.1", "Ultralytics YOLO Detection 1.0", "Ultralytics YOLO Segmentation 1.0", "Segmentation Mask 1.1", "Datumaro 1.0", "ImageNet 1.0"
- [Ground Truth 작업과 비교해 품질 측정] ↔ "CVAT compares all other jobs in the task against the established Ground truth job"
- [Honeypot: 검증 프레임을 일반 작업에 무작위로 섞음] ↔ "In this mode some random frames of the task are selected into the validation set." / "Then, validation frames are randomly mixed into regular annotation jobs."
- [IoU 임계값으로 매칭 판정] ↔ "IoU = intersection area / union area." / "The minimum overlap used to distinguish matching and unmatched spatial annotations."
- [검증용으로 데이터 5~15%면 대개 충분] ↔ "5-15% of the data is typically good enough"

### S10 Label Studio 문서
- [라벨링 설정은 XML, Object·Control·Visual 3종 태그] ↔ "The labeling configuration for a project is an XML file that contains three types of tags specific to Label Studio."
- [Choices 예시] ↔ `<Choices name="image_classes" toName="image_object">`
- [이미지용 컨트롤 태그 RectangleLabels, PolygonLabels, BrushLabels, KeyPointLabels 등] ↔ Tags 페이지 목록: "BrushLabels", "PolygonLabels", "RectangleLabels", "KeyPointLabels", "Choices"
- [ML 백엔드: 사전 라벨 후 사람이 검토] ↔ "Let ML/AI models predict labels autonomously, which can then be reviewed by human annotators."
- [자동 액티브 러닝 루프는 Enterprise] ↔ "You can use Label Studio Enterprise to build an automated active learning loop with a machine learning model backend."

## 출처 없이 쓴 일반 서술 (외부 수치 아님)
- mm/픽셀 환산 계산 예시(화각 폭 ÷ 가로 픽셀 수)는 산술 예시이며 특정 출처의 수치가 아니다.
- 시리즈 다른 편과 기존 글 링크는 내부 링크다.

## 추가 발췌 (본문 반영분)
- S2 [표범은 욕조보다 재규어로 잘못 붙기 쉽다] ↔ "For example, in ImageNet, a leopard is more likely to be mislabeled jaguar than bathtub."
- S4 [다양성 기반 예: 코어셋은 전체를 덮도록 멀리 떨어진 점을 고름] ↔ "core-set-based methods [75, 192] often simply try to query data points as far as possible to cover all"
- S4 [BADGE = 기울기 임베딩 기반] ↔ "BADGE (Batch Active learning by Diverse Gradient Embeddings) [14] samples point groups that are disparate and high magnitude when represented"
- S1 [6%, 5%는 논문 표현 그대로 "increases by just 6%/5%"로 옮김. %p로 해석하지 않음]

## 내 추론·일반 서술로 쓴 부분 (외부 출처 귀속 안 함)
- 산업 이미지에서 증강이 라벨을 깨는 예시 표(뒤집기·회전·크롭·색·블러): S7의 safety 원칙을 산업 사례에 적용한 내 정리
- 사전 라벨 편향과 비교 절차, 판정 불가 이미지가 불확실성 질의에 걸리는 문제, 라벨 형식 간 변환 방향, 스키마 항목, 해시+임베딩 2단계 중복 제거 순서, 촬영 설계 4항목 표: 일반 방법론 정리
- "학습에 쓴 이미지는 점수가 낮게 나오므로 임계값 추정에 쓰지 않는다": S3의 절차(학습 제외 검증 이미지로 임계값)에 대한 일반적 이유 설명
