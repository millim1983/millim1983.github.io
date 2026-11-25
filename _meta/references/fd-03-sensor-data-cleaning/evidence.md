# evidence - fd-03-sensor-data-cleaning

열람일: 2026-10-22 (전 출처 공통)

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress | Renjie Wu, Eamonn J. Keogh | 2021 (TKDE 수락, arXiv v1 2020) | https://arxiv.org/pdf/2009.13807 , https://arxiv.org/abs/2009.13807 | PDF 본문 Abstract, 1 Introduction, 2.2 Definition 1·식(6)·Table 1 직전 문단, 2.3, 2.5, 3 서두. abs 페이지 Comments·related DOI |
| S2 | Isolation Forest | Fei Tony Liu, Kai Ming Ting, Zhi-Hua Zhou | 2008 | https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf , 서지: https://api.crossref.org/works/10.1109/ICDM.2008.17 | PDF 2절(Isolation), 식(1)(2), 4.1 Training Stage(ψ, t). Crossref 서지 |
| S3 | Generalized Hampel Filters | Ronald K. Pearson, Yrjö Neuvo, Jaakko Astola, Moncef Gabbouj | 2016 | https://asp-eurasipjournals.springeropen.com/track/pdf/10.1186/s13634-016-0383-6 | PDF Abstract, 2절 식(3)(4)(5)(6), 3절 Implosion sequences 서두 |
| S4 | A New Approach to Linear Filtering and Prediction Problems | R. E. Kalman | 1960 | https://www.cs.yale.edu/homes/yry/readings/general/Kalman1960.pdf | 1쪽 초록 박스·Introduction (5)(6), 2쪽 (7) |
| S5 | Inference and Missing Data (초록) | Donald B. Rubin | 1976 | https://dash.harvard.edu/entities/publication/73120378-8764-6bd4-e053-0100007fdf3b | 리포지터리 메타데이터 페이지 초록 (본문 PDF 없음, Metadata Only) |
| S6 | Flexible Imputation of Missing Data, 2nd ed., 1.2 Concepts of MCAR, MAR and MNAR | Stef van Buuren | - | https://stefvanbuuren.name/fimd/sec-MCAR.html | 1.2절 |
| S7 | Smoothing and Differentiation of Data by Simplified Least Squares Procedures (서지만) | Abraham Savitzky, M. J. E. Golay | 1964 | https://api.crossref.org/works/10.1021/ac60214a047 | Crossref 메타데이터. ACS 본문은 403으로 열지 못함 |
| S8 | NIST/SEMATECH e-Handbook 1.3.5.17 Detection of Outliers | NIST | - | https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm | 해당 절 |
| S9 | NIST/SEMATECH e-Handbook 7.1.6 What are outliers in the data? | NIST | - | https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm | 해당 절 |
| S10 | pandas.DataFrame.resample | pandas | - | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html | Parameters closed/label/origin |
| S11 | pandas.DataFrame.interpolate | pandas | - | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html | Parameters method/limit/limit_area |
| S12 | pandas.Series.ffill | pandas | - | https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html | Parameters limit/limit_area |
| S13 | pandas.Series.rolling | pandas | - | https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html | Parameters window/center |
| S14 | pandas.merge_asof | pandas | - | https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html | 설명, direction/tolerance |
| S15 | scipy.signal.savgol_filter | SciPy | - | https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html | Parameters |
| S16 | scipy.signal.medfilt | SciPy | - | https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html | 설명, kernel_size |
| S17 | scipy.signal.decimate | SciPy | - | https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html | 설명, n/ftype/zero_phase |
| S18 | scipy.stats.median_abs_deviation | SciPy | - | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html | scale |
| S19 | sklearn.ensemble.IsolationForest | scikit-learn | - | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html | n_estimators, max_samples, References |
| S20 | sklearn.impute.IterativeImputer | scikit-learn | - | https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html | 설명, estimator, max_iter |
| S21 | sklearn.model_selection.TimeSeriesSplit | scikit-learn | - | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html | 설명, gap |
| S22 | Common pitfalls and recommended practices | scikit-learn | - | https://scikit-learn.org/stable/common_pitfalls.html | 12.2, 12.2.1 |
| S23 | scipy.signal.savgol_coeffs | SciPy | - | https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_coeffs.html | References (Savitzky & Golay 인용 확인) |

## 본문 사실 ↔ 원문 발췌

### 시간축 맞추기

- [resample closed/label 기본값은 대부분 left, 'ME','YE','QE','BME','BA','BQE','W'는 right] (S10)
  > "Which side of bin interval is closed. The default is 'left' for all frequency offsets except for 'ME', 'YE', 'QE', 'BME', 'BA', 'BQE', and 'W' which all have a default of 'right'."
- [decimate는 앤티앨리어싱 필터 후 다운샘플, 기본 8차 Chebyshev I형, zero_phase=True 기본] (S17)
  > "Downsample the signal after applying an anti-aliasing filter."
  > "By default, an order 8 Chebyshev type I filter is used."
  > "The default value of True is recommended, since a phase shift is generally not desired." (signature: zero_phase=True)
- [merge_asof: 같은 키가 아닌 가장 가까운 키로 매칭하는 왼쪽 조인, 양쪽 정렬 필요] (S14)
  > "This is similar to a left-join except that we match on nearest key rather than equal keys. Both DataFrames must be first sorted by the merge key in ascending order before calling this function."
- [direction backward(기본)/forward/nearest 의미] (S14)
  > "A "backward" search selects the last row in the right DataFrame whose 'on' key is less than or equal to the left's key."
  > "A "forward" search selects the first row in the right DataFrame whose 'on' key is greater than or equal to the left's key."
  > "A "nearest" search selects the row in the right DataFrame whose 'on' key is closest in absolute distance to the left's key."
- [tolerance로 허용 거리] (S14)
  > "Select asof tolerance within this range; must be compatible with the merge index."

### 결측

- [Rubin(1976)이 결측 문제를 세 범주로 분류] (S6)
  > "Rubin (1976) classified missing data problems into three categories."
- [MCAR/MAR/MNAR 정의] (S6)
  > "If the probability of being missing is the same for all cases, then the data are said to be missing completely at random (MCAR)."
  > "If the probability of being missing is the same only within groups defined by the observed data, then the data are missing at random (MAR)."
  > "If neither MCAR nor MAR holds, then we speak of missing not at random (MNAR)."
- [Rubin 초록: 결측 과정을 무시해도 되는 조건으로 missing at random 제시] (S5)
  > "When making direct-likelihood or Bayesian inferences about {theta}, it is appropriate to ignore the process that causes missing data if the missing data are missing at random and the parameter of the missing data process is 'distinct' from {theta}."
- [interpolate 'linear'은 인덱스 무시·등간격 가정, 'time'은 시간 간격 반영] (S11)
  > "'linear': Ignore the index and treat the values as equally spaced."
  > "'time': Works on daily and higher resolution data to interpolate given length of interval. This interpolates values based on time interval between observations."
- [spline/polynomial은 order 필요, SciPy 함수로 전달] (S11)
  > "Passed to scipy.interpolate.interp1d, whereas 'spline' is passed to scipy.interpolate.UnivariateSpline. ... Both 'polynomial' and 'spline' require that you also specify an order (int)"
- [limit_area="inside"는 양쪽에 값이 있는 NaN만 채움] (S11)
  > "'inside': Only fill NaNs surrounded by valid values (interpolate)."
- [limit보다 긴 연속 결측은 일부만 채워진다] (S12)
  > "if there is a gap with more than this number of consecutive NaNs, it will only be partially filled."
  - 보강: 로컬 합성 데이터로 interpolate(method="time", limit=5, limit_area="inside") 실행 결과 긴 공백에서 5칸이 채워지는 것을 확인 (scripts/test_code.py, "partially filled before revert: 5")
- [IterativeImputer: 각 특징을 다른 특징의 함수로 round-robin 모델링, 기본 BayesianRidge, max_iter 10, 실험적] (S20)
  > "A strategy for imputing missing values by modeling each feature with missing values as a function of other features in a round-robin fashion."
  > "estimator object, default=BayesianRidge()" / "max_iter int, default=10"
  > "This estimator is still experimental for now ... you need to explicitly import enable_iterative_imputer"

### 이상치 탐지

- [IQR 울타리 1.5 / 3, 경미·극단 이상치] (S9)
  > "Lower inner fence: Q1 - 1.5*IQ" "Upper inner fence: Q3 + 1.5*IQ" "Lower outer fence: Q1 - 3*IQ" "Upper outer fence: Q3 + 3*IQ"
  > "A point beyond an inner fence on either side is considered a mild outlier." "A point beyond an outer fence is considered an extreme outlier."
- [수정 Z-score = 0.6745(x - 중앙값)/MAD, Iglewicz와 Hoaglin 3.5 권고] (S8)
  > "M_i = 0.6745(x_i - x̃)/MAD ... with MAD denoting the median absolute deviation and x̃ denoting the median."
  > "These authors recommend that modified Z-scores with an absolute value of greater than 3.5 be labeled as potential outliers."
- [일반 Z-score 최댓값이 (n-1)/√n 이하라 작은 표본에서 오해 소지] (S8)
  > "Although it is common practice to use Z-scores to identify possible outliers, this can be misleading (particularly for small sample sizes) due to the fact that the maximum Z-score is at most (n-1)/sqrt(n)."
  - n=10이면 9/√10 ≈ 2.85 (본문 계산)
- [MAD는 표준편차와 비슷하지만 이상치에 더 강건] (S18, 일반 설명 보강)
  > "It is a measure of dispersion similar to the standard deviation but more robust to outliers"
- [Hampel 필터 정의: 창 중앙값·MAD 척도, |x-m|>tS이면 중앙값으로 대체] (S3 식 3, 4)
  > "y_k = x_k if |x_k - m_k| ≤ t S_k, m_k if |x_k - m_k| > t S_k ... where m_k is the median value from the moving data window and S_k is the MAD scale estimate, defined as: S_k = 1.4826 × median_{j∈[-K,K]}{|x_{k-j} - m_k|}."
- [1.4826은 가우시안에서 MAD를 표준편차 불편추정량으로] (S3)
  > "The factor 1.4826 makes the MAD scale estimate an unbiased estimate of the standard deviation for Gaussian data."
- [t=0이면 메디안 필터, t 커질수록 덜 공격적] (S3)
  > "This filter depends on both the window width and an additional tuning parameter t, reducing to the median filter when t = 0"
  > "the Hampel filter may be viewed as a "less aggressive extension" of the median filter, generally becoming less aggressive with increasing threshold value t."
- [implosion: 절반 이상 같은 값이면 MAD=0, 창 안 K+1개 이상 같으면 S_k=0, 출력은 중앙값] (S3 3절)
  > "if more than 50 % of the data values are the same, the MAD scale estimate is zero, independent of the other values in the data sequence. The practical consequences for the Hampel filter are that if K + 1 or more of the values in the data window W_k have the same value, then S_k = 0, implying that y_k = m_k, independent of the threshold parameter t."
- [Isolation Forest: 정상 프로파일 대신 이상치를 직접 고립] (S2 Abstract)
  > "This paper proposes a fundamentally different model-based method that explicitly isolates anomalies instead of profiles normal points."
- [이상치는 적고 달라서 고립되기 쉽고 경로가 짧다] (S2 2절)
  > "Since anomalies are 'few and different' and therefore they are more susceptible to isolation. ... This random partitioning produces noticeable shorter paths for anomalies"
- [점수식과 c(n), 0.5/1 극한] (S2 식 1, 2)
  > "c(n) = 2H(n - 1) - (2(n - 1)/n), where H(i) is the harmonic number"
  > "s(x, n) = 2^(-E(h(x))/c(n))" "when E(h(x)) → c(n), s → 0.5; when E(h(x)) → 0, s → 1"
  > "Given a data set of n instances, Section 10.3.3 of [9] gives the average path length of unsuccessful search in BST as" (c(n)이 BST 실패 탐색 평균 경로)
- [논문 기본값 ψ=256, t=100] (S2 4.1)
  > "Unless otherwise specified, we use ψ = 256 as the default value for our experiment."
  > "Unless otherwise specified, we shall use t = 100 as the default value in our experiment."
- [sklearn 기본 n_estimators=100, max_samples auto = min(256, n_samples)] (S19)
  > "n_estimators int, default=100" / "If "auto", then max_samples=min(256, n_samples)."
- [IsolationForest 서지: ICDM 2008, 413-422] (S2 Crossref, S19 References)
  > "F. T. Liu, K. M. Ting and Z. -H. Zhou. "Isolation forest." 2008 Eighth IEEE International Conference on Data Mining (ICDM), 2008, pp. 413-422."

### Wu & Keogh

- [대부분의 벤치마크가 네 결함 중 하나 이상: triviality, unrealistic anomaly density, mislabeled ground truth, run-to-failure bias; Yahoo·Numenta·NASA 등] (S1 1절)
  > "Most of these papers test on one or more of a handful of popular benchmark datasets, created by Yahoo [5], Numenta [6], NASA [2] or Pei's Lab (OMNI) [3], etc. In this work we make a surprising claim. The majority of the individual exemplars in these datasets suffer from one or more of four flaws. These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias."
- [자명함 = MATLAB 표준 함수 한 줄로 풀림] (S1 Definition 1)
  > "Definition 1. A time series anomaly detection problem is trivial if it can be solved with a single line of standard library MATLAB code."
- [Yahoo 367개 중 316개(86.1%) 한 줄 식, 식은 diff·movmean·movstd] (S1 2.2, 식 6)
  > "diff(TS) > movmean(diff(TS), k) + c * movstd(diff(TS), k) + b"
  > "we are surprised by the triviality of the Yahoo Benchmark: 316 out of 367 (86.1%) can be easily solved with a one-liner."
- [시험 데이터 절반 이상이 연속 이상 구간인 예] (S1 2.3)
  > "For some examples, more than half the test data exemplars consist of a contiguous region marked as anomalies."
- [run-to-failure: 마지막 점을 이상으로 찍는 단순 알고리즘이 맞을 확률 높음] (S1 2.5)
  > "A naïve algorithm that simply labels the last point as an anomaly has an excellent chance of being correct."
- [시험 시계열당 이상 1개, UCR Time Series Anomaly Archive 제시] (S1 2.3, 3)
  > "We believe that the ideal number of anomalies in a single testing time series is exactly one."
  > "we have used the lessons learned to create a new benchmark dataset, The UCR Time Series Anomaly Archive"
- [IEEE TKDE 수락, 연도 2021] (S1 abs 페이지)
  > Comments: "Full paper accepted by IEEE TKDE, extended abstract accepted by IEEE ICDE 2022" / Related DOI: "https://doi.org/10.1109/TKDE.2021.3112126"

### 노이즈 필터

- [medfilt: 커널 홀수, 기본 3, 0 패딩] (S16)
  > "Elements of kernel_size should be odd." "Default size is 3 for each dimension." "The array will automatically be zero-padded."
- [Savitzky-Golay 서지: Analytical Chemistry 36(8) 1627-1639, 1964] (S7)
  > Crossref: title "Smoothing and Differentiation of Data by Simplified Least Squares Procedures.", authors "Abraham Savitzky, M. J. E. Golay", "Analytical Chemistry", volume 36, issue 8, pages 1627-1639, 1964
  > SciPy savgol_coeffs References: "A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures." (S23)
  - 원문 본문은 열지 못함. 본문에는 서지 사실만 쓰고 원리 설명은 SciPy 문서 기준으로 씀
- [savgol_filter: polyorder는 맞출 다항식 차수, window_length보다 작아야, deriv로 미분] (S15)
  > "The order of the polynomial used to fit the samples." "polyorder must be less than window_length."
  > "The order of the derivative to compute. This must be a nonnegative integer."
- [mode 'interp' 기본: 패딩 없이 끝 window_length 값에 다항식 맞춰 끝 window_length//2 출력 계산] (S15)
  > "When the 'interp' mode is selected (the default), no extension is used. Instead, a degree polyorder polynomial is fit to the last window_length values of the edges, and this polynomial is used to evaluate the last window_length // 2 output values."
- [Kalman(1960): 필터링·예측 문제를 상태 전이 방법으로 재검토] (S4 초록)
  > "The classical filtering and prediction problem is re-examined using the Bode-Shannon representation of random processes and the "state transition" method of analysis of dynamic systems."
- [최적 추정 오차 공분산의 차분/미분 방정식, 그 해로 최적 선형 필터 계수를 바로 얻음] (S4 초록 (2))
  > "A nonlinear difference (or differential) equation is derived for the covariance matrix of the optimal estimation error. From the solution of this equation the coefficients of the difference (or differential) equation of the optimal linear filter are obtained without further calculations."
- [서지: Transactions of the ASME, Journal of Basic Engineering 82 (Series D) 35-45, 1960] (S4 각 쪽 하단)
  > "Transactions of the ASME-Journal of Basic Engineering, 82 (Series D): 35-45. Copyright © 1960 by ASME"
- [rolling center=True는 라벨을 창 중앙에] (S13)
  > "If False, set the window labels as the right edge of the window index. If True, set the window labels as the center of the window index."

### 스케일링·분할

- [시험 데이터에 fit 금지, 정규화 평균은 학습 구간 평균] (S22 12.2)
  > "Test data should never be used to make choices about the model. The general rule is to never call fit on the test data."
  > "if you have a normalization step where you divide by the average value, the average should be the average of the train subset, not the average of all the data."
- [TimeSeriesSplit: 다른 CV는 미래로 학습·과거로 평가, 학습 집합이 점점 커짐] (S21)
  > "Provides train/test indices to split time-ordered data, where other cross-validation methods are inappropriate, as they would lead to training on future data and evaluating on past data."
  > "successive training sets are supersets of those that come before them."
- [gap: 학습 끝에서 시험 전 제외할 표본 수] (S21)
  > "Number of samples to exclude from the end of each train set before the test set."

## 출처 없이 쓴 일반 지식 (발췌 불요)

- 이동평균·메디안 필터·업/다운샘플링·앨리어싱 정의, 집계 함수별 성질 표
- 영점·감도 드리프트, 2점 교정(a·출력 + b)
- 윈도 길이·stride·겹침과 분할 간격 W 논리, 라벨 위치 구분
- 스파이크·고착값의 형태와 런 길이·이동 표준편차 탐지
- 칼만 필터의 순차 갱신 성질(교과서 수준)

## 읽지 못해 뺀 내용

- Savitzky & Golay (1964) 본문: ACS 403. 원리·수치 인용 없이 서지 정보만 사용
- Rubin (1976) 본문: 저장소 Metadata Only. 초록만 사용, MCAR/MNAR 용어 정의는 van Buuren 1.2절로 대체
- Iglewicz & Hoaglin 원저: 미열람. NIST 핸드북의 소개 문장으로만 인용
