# evidence - fd-05-training-data-preparation

열람일: 2026-10-22 (전부). PDF는 `src/` 에 내려받아 PyMuPDF로 텍스트 추출(`src/*.txt`) 후 해당 부분을 직접 읽음. 웹 문서는 WebFetch로 원문 페이지를 열어 읽음.

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Leakage in Data Mining: Formulation, Detection, and Avoidance | Shachar Kaufman, Saharon Rosset, Claudia Perlich | 2011 (KDD '11) | https://www.cs.umb.edu/~ding/history/470_670_fall_2011/papers/cs670_Tran_PreferredPaper_LeakingInDataMining.pdf | Abstract, 2절(KDD-Cup 2008), 3.2절, 3.4절, 4.1절, 5절 |
| S2 | Leakage and the Reproducibility Crisis in ML-based Science | Sayash Kapoor, Arvind Narayanan | 2022 (arXiv:2207.07048v1) | https://arxiv.org/abs/2207.07048 | Abstract, 2.4절 taxonomy, Figure 1 캡션, 4절 civil war |
| S3 | SMOTE: Synthetic Minority Over-sampling Technique | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence O. Hall, W. Philip Kegelmeyer | 2002 (JAIR 16, 321-357) | https://arxiv.org/abs/1106.1813 | Abstract, 4.2절 |
| S4 | Data Validation for Machine Learning | Eric Breck, Neoklis Polyzotis, Sudip Roy, Steven Euijong Whang, Martin Zinkevich | 2019 (SysML) | https://proceedings.mlsys.org/paper_files/paper/2019/file/928f1160e52192e3e0017fb63ab65391-Paper.pdf | Abstract, 3절(Schema Life Cycle), 4절(Training-Serving Skew, Quantifying Distribution Distance) |
| S5 | Data-centric Artificial Intelligence: A Survey | Daochen Zha 외 6인 | 2023 (arXiv:2303.10158v3) | https://arxiv.org/abs/2303.10158 | Abstract, 1절, 2.1 Definitions, 2.3 goals |
| S6 | Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks | Curtis G. Northcutt, Anish Athalye, Jonas Mueller | 2021 (NeurIPS Datasets and Benchmarks) | https://arxiv.org/abs/2103.14749 | Abstract |
| S7 | Datasheets for Datasets | Timnit Gebru 외 6인 | 2021 (arXiv:1803.09010v8) | https://arxiv.org/abs/1803.09010 | 2절 Questions and Workflow, Composition·Preprocessing 질문 |
| S8 | Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI | Mahima Pushkarna, Andrew Zaldivar, Oddur Kjartansson | 2022 (arXiv:2204.01075v1) | https://arxiv.org/abs/2204.01075 | Abstract, telescopes/periscopes/microscopes 절, themes 절 |
| S9 | Cross-validation: evaluating estimator performance | scikit-learn | - | https://scikit-learn.org/stable/modules/cross_validation.html | 3.1.2.1 note, GroupKFold, StratifiedGroupKFold, TimeSeriesSplit |
| S10 | TimeSeriesSplit API | scikit-learn | - | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html | 클래스 설명, gap 인자 |
| S11 | LogisticRegression API (class_weight) | scikit-learn | - | https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html | class_weight |
| S12 | Tuning the decision threshold for class prediction | scikit-learn | - | https://scikit-learn.org/stable/modules/classification_threshold.html | 도입부, TunedThresholdClassifierCV |
| S13 | Common pitfalls and recommended practices | imbalanced-learn | - | https://imbalanced-learn.org/stable/common_pitfalls.html | Data leakage 절 출력값 |
| S14 | Get started with TensorFlow Data Validation | TensorFlow | - | https://www.tensorflow.org/tfx/data_validation/get_started | Schema, Checking data skew and drift |
| S15 | Expectation (용어 정의) | Great Expectations | - | https://docs.greatexpectations.io/docs/reference/learn/terms/expectation/ | 정의, 예시 |
| S16 | Get Started: Data Versioning | DVC | - | https://doc.dvc.org/start | dvc add, push/pull, checkout |
| S17 | dvc.yaml files | DVC | - | https://doc.dvc.org/user-guide/project-structure/dvcyaml-files | Stage entries, dvc.lock |
| S18 | Rules of Machine Learning | Google for Developers | - | https://developers.google.com/machine-learning/guides/rules-of-ml | Training-serving skew, Rule #29, #32 |

## 본문 사실 ↔ 원문 발췌

### 데이터 중심 AI (S5, S6)
- [데이터 중심 AI = 데이터를 개발·반복·유지하는 프레임워크] ↔ S5 2.1: "Data-centric AI refers to a framework to develop, iterate, and maintain data for AI systems [269]."
- [세 목표와 하위 목표] ↔ S5 2.3: "It consists of five sub-goals, including 1) data collection for gathering raw training data, 2) data labeling for adding informative labels, 3) data preparation for cleaning and transforming data, 4) data reduction ... and 5) data augmentation" / "There are three sub-goals in this effort: 1) in-distribution evaluation and 2) out-of-distribution evaluation ... while 3) prompt engineering" / "It involves three essential sub-goals: 1) data understanding ... 2) data quality assurance ... and 3) data storage & retrieval"
- [모델 중심은 데이터를 거의 고정하고 모델을 찾음] ↔ S5 1절: "researchers and developers primarily focus on identifying more effective models to improve AI performance while keeping the data largely unchanged."
- [10개 데이터셋 평균 최소 3.3%, ImageNet 최소 6%, ResNet-18 > ResNet-50] ↔ S6 Abstract: "we estimate an average of at least 3.3% errors across the 10 datasets, where for example label errors comprise at least 6% of the ImageNet validation set." / "on ImageNet with corrected labels: ResNet-18 outperforms ResNet-50 if the prevalence of originally mislabeled test examples increases by just 6%."

### 분할 (S9, S10)
- [i.i.d. 거의 성립 안 함, 시계열/그룹 CV 권장] ↔ S9: "While i.i.d. data is a common assumption in machine learning theory, it rarely holds in practice. ... it is safer to use a time-series aware cross-validation scheme. Similarly, if we know that the generative process has a group structure (samples collected from different subjects, experiments, measurement devices), it is safer to use group-wise cross-validation."
- [GroupKFold: 같은 그룹이 양쪽에 안 들어감, 피험자 예] ↔ S9: "GroupKFold is a variation of k-fold which ensures that the same group is not represented in both testing and training sets. For example if the data is obtained from different subjects with several samples per-subject ..."
- [StratifiedGroupKFold: 그룹 유지 + 클래스 비율] ↔ S9: "The idea is to try to preserve the distribution of classes in each split while keeping each group within a single split."
- [StratifiedKFold: 클래스 비율 유지] ↔ S9: "each set contains approximately the same percentage of samples of each target class as the complete set."
- [TimeSeriesSplit: k개 학습, k+1 시험] ↔ S10: "In the k-th split, it returns the first k folds as the train set and the (k+1)-th fold as the test set."
- [gap 인자, 0.24 추가] ↔ S10: "gap int, default=0. Number of samples to exclude from the end of each train set before the test set. Added in version 0.24."
- (라벨 지평만큼 gap을 둔다는 설명, 표의 "위험" 열 일부는 위 정의에서 내가 끌어낸 방법론적 해석. 외부 수치 없음)

### 누수: Kaufman 등 (S1)
- [누수 정의] ↔ S1 Abstract: "leakage is essentially the introduction of information about the data mining target, which should not be legitimately available to mine from."
- [두 갈래: leaking features / leakage in training examples] ↔ S1 3.1: "The discussion proceeds along these two possible sources of leakage for a model: features and training examples." (3.2 "Leaking Features", 3.3 "Leakage in Training Examples")
- [no-time-machine] ↔ S1 3.2: "The prevailing example for this type of leakage is what we call the no-time-machine requirement. ... a legitimate model only build on features with information from a time earlier (or sometimes, no later) than that of the target."
- [KDD Cup 2008 Patient ID] ↔ S1 2절: "KDD-Cup 2008 dealt with cancer detection from mammography data. ... the “Patient ID” feature (ignored by most competitors) has tremendous and unexpected predictive power. They hypothesize that multiple clinical study, institution or equipment sources were used ... some of these sources were assigned their population with prior knowledge of the patient's condition."
- [정당성 태그 + learn-predict 분리] ↔ S1 4.1: "Our suggested methodology for avoiding leakage is a two stage process of tagging every observation with legitimacy tags during collection and then observing what we call a learn-predict separation."
- [시간 문제에서 태그 = 타임스탬프, 분리 = 시점 절단] ↔ S1 4.1: "legitimacy tags are time-stamps with sufficient precision. ... Learn-predict separation is implemented by a cut at some point in time that segments training from evaluation examples."
- [레코드 갱신 시각 미보존이 근원] ↔ S1 4.1: "Updates to database records are usually not time-stamped and not stored separately, and at best whole records end up with one time-stamp. ... this loss of information is often the source of all evil that allows leakage to find its way into predictive models."
- [탐지: 의외의 예측변수(EDA), 의외의 성능, 현장 시험, 도메인 지식 필요] ↔ S1 5절: "this kind of examination can expose leakage as patterns in the data that are surprising." / "A substantial divergence from this expected performance is surprising" / "early in-the-field testing of initial models" / "they all require some degree of domain knowledge"
- [설계 결정 누수: 모델·메타파라미터 선택 (체크리스트 '시험 세트 봉인')] ↔ S1 3.4: "Examples could be: (i) selecting or designing features ..., (ii) algorithm or parametric model selection, and (iii) meta-parameter value choices. This form of leakage is perhaps the most dangerous"

### 누수: Kapoor & Narayanan (S2)
- [17개 분야, 329편, 8유형] ↔ S2 Abstract: "we find 17 fields where errors have been found, collectively affecting 329 papers ... we present a fine-grained taxonomy of 8 types of leakage"
- [L1.1~L3.3 정의] ↔ S2 2.4: "[L1.1] No test set." / "[L1.2] Pre-processing on training and test set. Using the entire dataset for any pre-processing steps such as imputation or over/under sampling." / "[L1.3] Feature selection on training and test set." / "[L1.4] Duplicates in datasets." / "[L2] Model uses features that are not legitimate. ... One instance when this can happen is if a feature is a proxy for the outcome variable" / "[L3.1] Temporal leakage." / "[L3.2] Nonindependence between train and test samples. ... train and test samples come from the same people or units." / "[L3.3] Sampling bias in test distribution."
- [L2 하위 유형 없음] ↔ S2 2.4: "The judgement of whether the use of a given feature is legitimate for a modeling task requires domain knowledge and can be highly problem specific. As a result, we do not provide sub-categories for this sort of leakage."
- [L3.2 대응: 블록 교차검증] ↔ S2 2.4: "Methods such as ‘block cross validation’ can partition the dataset strategically"
- [12편 중 4편, 그 4편이 복잡 모델 우위 주장, Wang 0.14 → 0.01] ↔ S2 4절: "We narrowed this list to the 12 papers ... We found errors in 4 of the 12 papers-exactly the 4 papers that claimed superior performance of complex ML models over baseline LR models" / "complex ML models perform no better than baseline LR models in each case except Wang (2019), where the difference between the AUC of the complex ML models and LR models drops from 0.14 to 0.01."
- [원인 3종] ↔ S2 Figure 1 캡션: "Muchlinski et al. (2016) impute the training and test data together, Colaresi & Mahmood (2017) and Wang (2019) incorrectly reuse an imputed dataset, and Kaufman et al. (2019) use proxies for the target variable"
- [논문 읽기로는 못 잡고 모델 정보 시트로는 탐지] ↔ S2 Abstract: "While none of these errors could have been caught by reading the papers, model info sheets would enable the detection of leakage in each case."
- (표의 "설비 데이터에 대입하면" 열은 본문에 명시한 대로 내 해석)

### 불균형 (S3, S11, S12, S13)
- [SMOTE: k 최근접 이웃 선분 위 합성, 특징 공간] ↔ S3 4.2: "The minority class is over-sampled by taking each minority class sample and introducing synthetic examples along the line segments joining any/all of the k minority class nearest neighbors." / "by operating in “feature space” rather than “data space”"
- [이웃 5개, 200%면 2개] ↔ S3 4.2: "Our implementation currently uses five nearest neighbors. For instance, if the amount of over-sampling needed is 200%, only two neighbors from the five nearest neighbors are chosen and one sample is generated in the direction of each."
- [식 x_i + λ(x_nn - x_i), λ∈(0,1)] ↔ S3 4.2: "Take the difference between the feature vector (sample) under consideration and its nearest neighbor. Multiply this difference by a random number between 0 and 1, and add it to the feature vector under consideration."
- [결정 영역이 넓어짐] ↔ S3 4.2: "The synthetic examples cause the classifier to create larger and less specific decision regions"
- [유방촬영 10,923 / 260] ↔ S3 4.2: "There were 10923 examples in the majority class and 260 examples in the minority class originally."
- [balanced 공식] ↔ S11: "The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y))." (0.505, 50은 이 공식으로 계산)
- [기본 임계값 0.5] ↔ S12: "a positive class is predicted when the conditional probability P(y|X) is greater than 0.5"
- [TunedThresholdClassifierCV, 기본 지표 balanced accuracy] ↔ S12: "The TunedThresholdClassifierCV tunes this threshold using an internal cross-validation. The optimum threshold is chosen to maximize a given metric." / "By default, the balanced accuracy is the metric used but be aware that one should choose a meaningful metric for their use case."
- [imbalanced-learn 수치 0.609/0.628, 0.724/0.698, 0.732/0.727] ↔ S13 출력: "Balanced accuracy mean +/- std. dev.: 0.609 +/- 0.024" / "0.628 +/- 0.009" / "0.724 +/- 0.042" / "The cross-validation performance looks good, but evaluating the classifiers on the left-out data shows a different picture: ... 0.698 +/- 0.014" / "using a Pipeline avoids to make any data leakage ... 0.732 +/- 0.019" / "0.727 +/- 0.008"
- (기법 비교표의 "피할 때" 열은 일반 방법론 정리이며 외부 수치 없음)

### 학습/추론 일관성 (S4, S18)
- [학습-서빙 스큐 정의와 세 원인] ↔ S18: "Training-serving skew is a difference between performance during training and performance during serving. This skew can be caused by: A discrepancy between how you handle data in the training and serving pipelines. A change in the data between when you train and when you serve. A feedback loop between your model and your algorithm."
- [Rule #29] ↔ S18: "Rule #29: The best way to make sure that you train like you serve is to save the set of features used at serving time, and then pipe those features to a log to use them at training time. Even if you can't do this for every example, do it for a small fraction, such that you can verify the consistency between serving and training."
- [Rule #32] ↔ S18: "Rule #32: Re-use code between your training pipeline and your serving pipeline whenever possible."
- [특징 스큐, time travel, 클릭 수 예] ↔ S4 4절: "Feature skew occurs when a particular feature for an example assumes different values in training versus at serving time. ... A more interesting mechanism through which feature skew occurs is termed time travel. ... the click count for each impression will appear higher compared to the serving data"
- [분포 스큐] ↔ S4 4절: "Distribution skew occurs when the distribution of feature values over a batch of training data is different from that seen at serving time. ... Any flaw in the sampling scheme can result in training data distributions that look significantly different"
- [점수/서빙 스큐] ↔ S4 4절: "Scoring/Serving Skew occurs when only a subset of the scored examples are actually served. ... the ninety videos that were never served may not have associated labels and therefore may never appear in the training data."

### 데이터 검증 (S4, S14, S15)
- [TFX 일부, 수백 팀, 하루 수 페타바이트] ↔ S4 Abstract: "This system is deployed in production as an integral part of TFX ... It is used by hundreds of product teams use it to continuously monitor and validate several petabytes of production data per day."
- [스키마 추론 후 사람이 검토, 버전 관리] ↔ S4 3절: "many machine learning pipelines use thousands of features, and so constructing a schema manually ..." / "component synthesizes a basic version of the schema" / "We expect owners of pipelines to treat the schema as a production asset ... in our pipelines the schema is stored in the version-control system for source code."
- [카이제곱 실험: 1억 N(0,1), 1만 N(0,2), 0.01%, 10번 중 7번] ↔ S4 4절: "We begin with a control sample of 100 million points from a N(0,1) distribution and then randomly replace 10 thousand points by sampling from a N(0,2) distribution. This replacement introduces a minute amount of noise (0.01%)" / "this method would needlessly fire an alert 7 out of 10 times"
- [d∞ 지표, 1% 예, culprit 값, '-1' 사례] ↔ S4 4절: "we use d∞(p, q) = max_{i∈S} |p_i - q_i|" / "(e.g., “allow changes of only up to 1% for each value”). Moreover, an alert comes with a “culprit” value" / "if the highest change in frequency is observed in value '-1' then this might be an issue with some backend failing and producing a default value. (This is an actual situation observed in one of our production pipelines.)"
- [TFDV infer_schema, validate_statistics, 스큐/드리프트] ↔ S14: "schema = tfdv.infer_schema(stats)" / "anomalies = tfdv.validate_statistics(statistics=other_stats, schema=schema)" / "TFDV also provides functionalities to detect: skew between training and serving data; drift between different days of training data."
- [L∞는 범주형만, JS는 수치형 포함] ↔ S14: "NOTE L-infinity norm will only detect skew for the categorical features. Instead of specifying an infinity_norm threshold, specifying a jensen_shannon_divergence threshold in the skew_comparator would detect skew for both numeric and categorical features."
- [skew_comparator infinity_norm threshold 0.01 코드] ↔ S14: "tfdv.get_feature(schema, 'payment_type').skew_comparator.infinity_norm.threshold = 0.01"
- [generate_statistics_from_dataframe 존재] ↔ S14: 페이지에 `tfdv.generate_statistics_from_dataframe` 언급 확인
- [GX Expectation 정의·예시·Suite·Checkpoint] ↔ S15: "An Expectation is a verifiable assertion about data." / 예시 `expect_column_values_to_not_be_null` / Expectation Suite "A collection of verifiable assertions about data." / Checkpoint "The primary means for validating data in a production deployment of Great Expectations."

### 버전 관리 (S16, S17)
- [dvc add → 캐시, .dvc 파일(md5, path)] ↔ S16: dvc add "moved the data to the project's cache" / "This small, human-readable metadata file acts as a placeholder for the original data for the purpose of Git tracking." / "outs: - md5: 22a1a2931c8370d3aeedd7183606fd7f path: data.xml"
- [Git에는 .dvc만, 원본은 .gitignore] ↔ S16: "$ git add data/data.xml.dvc data/.gitignore"
- [push/pull] ↔ S16: dvc push "copied the data cached locally to the remote storage we set up earlier." / dvc pull "Usually, we run it after git pull or git clone."
- [git checkout + dvc checkout] ↔ S16: "$ git checkout HEAD~1 data/data.xml.dvc / $ dvc checkout"
- [dvc.yaml cmd/deps/params/outs, dvc.lock 해시·파라미터, 변경 감지] ↔ S17: cmd "(Required) One or more shell commands to execute" / dvc.lock entries include "a content hash field (md5, etag, or checksum)" / dvc.lock lets DVC "detect when stage definitions, or their dependencies have changed", which "invalidates stages, requiring their reproduction."

### 문서화 (S7, S8)
- [Datasheets 7개 섹션] ↔ S7 2절: "The questions are grouped into sections that roughly match the key stages of the dataset lifecycle: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution, and maintenance."
- [권장 분할 질문] ↔ S7 Composition: "Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them."
- [원본 저장 질문] ↔ S7 Preprocessing: "Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?"
- [20개 넘는 Data Card] ↔ S8 Abstract: "Finally, we present lessons learned from deploying over 20 Data Cards."
- [31개 주제] ↔ S8: "we identified 31 broad, generalizable themes (Table 2)"
- [텔레스코프/페리스코프/마이크로스코프] ↔ S8: "Telescopes provide an overview of the dataset. ... for example "Does this dataset contain Sensitive Human Attributes?"" / "Periscopes ... often reproducible and can be automated" / "Microscopes offer fine-grained details. These are questions about the “unobservable” human processes, decisions, assumptions and policies that shape the dataset."
- [마이크로스코프가 가장 어려움] ↔ S8: "We observed that microscopic questions were most challenging to answer since they require articulating implicit knowledge."

## 읽지 못해 쓰지 않은 것
- Kaufman, Rosset, Perlich, Stitelman (2012), ACM TKDD 6(4) 확장판: ACM 페이월로 열지 못함. 본문은 KDD 2011 학회판(S1)만 근거로 쓰고 참고에 그 사실을 명시.
- Kapoor & Narayanan의 Patterns(2023) 게재판: cell.com 403, PMC reCAPTCHA로 열지 못함. 본문 수치(17개 분야, 329편)는 arXiv v1 기준이며 게재판 수치와 다를 수 있어 버전을 본문에 명시.
