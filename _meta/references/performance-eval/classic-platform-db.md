# 고전 플랫폼·데이터베이스의 "성능평가" — 리서치 노트

> 블로그 글감용 구조화 자료조사. 모든 수치는 WebSearch 검증, 출처 URL 명기.
> 미확인 항목은 "[미확인]"으로 표기. 작성일: 2026-06-26.

---

## 1. DB 성능 핵심 지표 (정의)

| 지표 | 의미 | 단위 | 비고 |
|---|---|---|---|
| 처리량 Throughput | 단위시간당 처리한 작업 수 | TPS(transactions/s), QPS(queries/s), RPS/req/s, ops/s | DB·결제는 TPS, 일반 쿼리는 QPS, 웹은 RPS |
| 지연 Latency | 한 요청의 응답 시간 | ms | 평균보다 **백분위(percentile)**가 중요 |
| p50 (중앙값) | 50%가 이보다 빠름 | ms | "전형적" 사용자 경험 |
| p95 | 95%가 이보다 빠름 | ms | 느린 요청(long tail) 진단 |
| p99 (tail latency) | 99%가 이보다 빠름, 상위 1% 최악 | ms | 대규모 분산시스템에서 사용자 체감 좌우 |
| 동시성 Concurrency | 동시에 처리하는 연결/세션 수 | connections | HammerDB가 부하 스케일링 시 핵심 변수 |
| 읽기/쓰기 비율 | 워크로드 read:write 구성 | % | 벤치 결과 해석에 필수(예: YCSB 워크로드 A~F) |

핵심 관계(검증): **처리량이 용량(capacity)에 근접하면 지연은 선형이 아니라 지수적으로 증가**한다. 한 출처는 "50% 용량 대비 80% 용량에서 지연 약 4배"로 설명. 따라서 처리량과 지연은 분리해 볼 수 없고, "처리량을 올려가며 지연 곡선이 꺾이는 포화점"을 보는 것이 평가의 정석(YCSB의 설계 철학).
- 출처: https://www.systemoverflow.com/learn/design-fundamentals/latency-throughput/what-are-latency-and-throughput-core-definitions-and-measurement
- 출처: https://oneuptime.com/blog/post/2025-09-15-p50-vs-p95-vs-p99-latency-percentiles/view
- 출처: https://sreschool.com/blog/p99-latency/
- 출처(tail latency): https://last9.io/blog/tail-latency/

### tail latency가 중요한 이유 (검증)
대부분 시스템은 long-tail 분포를 가져, "hockey stick(하키 스틱)" 곡선이 나타난다 — p50~p90까지는 평평하다가 p99 이후 급상승. 평균만 보면 이 꼬리를 놓친다.
- 출처: https://last9.io/blog/tail-latency/

---

## 2. 대표 DB 벤치마크 (무엇을·어떻게 재나)

### TPC 계열 (Transaction Processing Performance Council, 공식·감사받는 결과)

| 벤치 | 워크로드 유형 | 주 지표 | 측정 대상 |
|---|---|---|---|
| **TPC-C** | OLTP (주문처리) | **tpmC** (new-order transactions/min) + price/tpmC | 트랜잭션 처리 성능 |
| **TPC-H** | OLAP / 의사결정지원(ad-hoc 쿼리) | **QphH@Size** (Composite Query-per-Hour) + $/kQphH | 분석 쿼리 처리량 |
| **TPC-DS** | OLAP / 의사결정지원(복잡 쿼리) | **QphDS@Size** + Price/kQphDS@Size | 더 복잡한 분석 워크로드 |

**TPC-C 모델 구조 (검증)**: 도매 공급사 시나리오. 창고(warehouse) 1개당 10개 district, district당 3,000 customer, 전 창고가 100,000 품목 재고 유지. 측정 단위 tpmC = **new-order 트랜잭션/분**. New-Order는 단일 트랜잭션으로 10개 품목 주문을 입력·재고 갱신하는 중간 무게의 read-write 트랜잭션(고빈도, 엄격한 응답시간 요건).
- 출처: https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-c_v5.11.0.pdf
- 출처: https://en.wikipedia.org/wiki/TPC-C

**TPC-H vs TPC-DS 차이 (검증)**:
- TPC-H: 22개 쿼리, 비교적 단순, 3NF 정규화 8개 테이블, 균등 데이터 분포, shard-friendly.
- TPC-DS: 99개 쿼리, 고급 SQL·다양한 JOIN, Star schema 26개 테이블, 편향(skewed) 데이터 분포.
- 출처: https://atwong.medium.com/what-is-the-difference-between-tpc-h-and-tpc-ds-benchmarks-cb92fc104c32
- 출처: https://medium.com/hyrise/a-summary-of-tpc-ds-9fb5e7339a35

### 오픈소스/도구 벤치마크

| 도구 | 무엇을 재나 | 측정 방식 |
|---|---|---|
| **YCSB** (Yahoo Cloud Serving Benchmark) | key-value/NoSQL store, ops/sec | 워크로드 A~F(서로 다른 read/write 비율). **처리량을 올려가며 지연을 측정, 포화점까지 추적**해 throughput-latency 트레이드오프 도출 |
| **sysbench** | CPU·메모리·디스크 I/O·DB(주로 MySQL OLTP) | 합성 OLTP 부하 → 처리량·응답시간·자원사용률 |
| **HammerDB** | DB 엔진(여러 DB, TPROC-C=TPC-C형, TPROC-H=TPC-H형) | 연결·락·CPU 코어 스케일링 stress test → 처리량·응답시간·자원사용률. 자체 지표 **NOPM**(New Orders Per Minute) 사용 |

- 출처(종합): https://benchant.com/blog/benchmarking-suites
- 출처(YCSB 철학): https://benchmarking-suite.readthedocs.io/en/latest/benchmarks.html
- 출처(HammerDB tpmC/NOPM 해설): https://www.hammerdb.com/blog/uncategorized/how-to-understand-tpc-c-tpmc-and-tproc-c-nopm-and-what-is-good-performance/
- 출처(sysbench/HammerDB): https://www.hammerdb.com/blog/guest/how-to-assess-mysql-performance/

> 주의: HammerDB의 TPROC-C는 "TPC-C에서 파생됐으나 공식 TPC-C 결과가 아님"을 명시한다. tpmC라는 용어를 비공식 결과에 붙이지 말 것(HammerDB 권고).

---

## 3. 웹/애플리케이션 플랫폼 지표

### 가용성 "나인(nines)" — SLA별 연간 허용 다운타임 (검증)

| 가용성 | 별칭 | 연간 다운타임 | 월간 다운타임 | 전형적 용도 |
|---|---|---|---|---|
| 99% | two nines | 약 3.65일 | — | 비핵심 |
| 99.9% | three nines | 약 8시간 46분 | 약 43.8분 | 비즈니스 크리티컬 앱(가장 흔한 목표) |
| 99.99% | four nines | 약 52.6분 | 약 4.4분 | 결제·인증·핵심 인프라 |
| 99.999% | five nines | 약 5.26분 | — | 통신·미션 크리티컬 |

- **각 나인 추가 = 허용 다운타임 10배 축소**, 인프라·운영비용은 통상 3~10배 증가(다중 데이터센터·자동 페일오버·24/7 온콜 필요).
- 출처: https://web-alert.io/blog/uptime-sla-explained-99-9-vs-99-99-availability
- 출처: https://uptimerobot.com/blog/what-does-999-uptime-mean/
- 출처: https://en.wikipedia.org/wiki/High_availability

### 기타 웹 지표
- **처리량**: req/s (RPS).
- **지연**: p50/p95/**p99**(웹 tail latency가 SLA·사용자 체감 핵심).
- **에러율**: 실패 요청 비율(5xx 등). Apdex에서 server-side error는 자동 "frustrated"로 집계.

### Apdex (Application Performance Index) — 정의·공식 (검증)
사용자 만족도를 0~1로 환산하는 개방 표준. 목표 응답시간 T 기준:
- **Satisfied**: 응답시간 ≤ T (가중치 1)
- **Tolerating**: T < 응답시간 ≤ 4T (가중치 0.5)
- **Frustrated**: 응답시간 > 4T 또는 서버 에러 (가중치 0)

**공식: Apdex_T = (Satisfied + Tolerating×0.5) / 전체 샘플 수.** 0(최악)~1(최상).
- 출처: https://en.wikipedia.org/wiki/Apdex
- 출처: https://docs.newrelic.com/docs/apm/new-relic-apm/apdex/apdex-measure-user-satisfaction/

---

## 4. 세계 최고/참조 수준 (대표 수치 + 출처)

### TPC-C (tpmC)
| 시스템 | tpmC | price/tpmC | 시점 | 비고 |
|---|---|---|---|---|
| Alibaba Cloud **PolarDB** | **20.55억(2.055 billion) tpmC** | CNY 0.8 ≈ USD 0.11 | 2025-03 | 현재 세계기록. "직전 기록의 2.5배"(역산 시 직전 ≈ 8.2억 tpmC이나 직전 보유자·정확수치 기사 미명시 [미확인]) |
| Oracle DB 11gR2, SPARC SuperCluster (T3-4 × 27대, 클러스터) | 30,249,688 tpmC (약 3,025만) | $1.01/tpmC | 2010년대 초 | 단일 시스템 아님(클러스터). 당시 세계기록 |

- 출처(PolarDB): https://mid-east.info/alibaba-clouds-polardb-breaks-tpc-c-benchmark-world-record-with-innovative-three-layer-decoupling-architecture/
- 출처(Oracle SPARC SuperCluster): https://www.dbta.com/Editorial/News-Flashes/Oracle-Announces-World-Record-TPC-C-Benchmark-with-Oracle-DB-on-a-SPARC-Supercluster-with-SPARC-T3-T4-Servers-72719.aspx
- 공식 전체 결과 목록: https://www.tpc.org/tpcc/results/tpcc_results5.asp

> [미확인] PolarDB 기사는 mid-east.info(보도자료 재게재) 기준. TPC 공식 결과 페이지에서 동일 수치 교차검증 권장. 또한 분산/클라우드 결과와 단일시스템 결과는 직접 비교 부적절.

### TPC-H (QphH)
| 시스템 | 결과 | 시점 | 비고 |
|---|---|---|---|
| Lenovo ThinkSystem SR665 | **624,778.0 QphH@3000GB**, $239.94/kQphH@3000GB | 2021-04 | 3000GB 스케일 non-clustered price/performance 기록 |

- 출처: https://lenovopress.lenovo.com/lp1462-sr665-tpc-h-benchmark-result-2021-04-06

> TPC-H/DS 수치는 **반드시 @Size(스케일팩터: 1000GB/3000GB/10000GB 등)와 함께** 인용해야 의미가 있다(규모 다르면 비교 불가).

---

## 5. 평가 환경 명시의 중요성 (검증)

벤치마크 수치는 **환경 의존적**이므로 단독 수치는 무의미. 함께 반드시 명시할 것:
- **하드웨어**: CPU 코어 수·모델, 메모리, 스토리지(특히 flash/NVMe), 네트워크.
- **데이터 규모**: TPC-C 창고 수, TPC-H/DS 스케일팩터(@Size).
- **워크로드**: read/write 비율, 동시성(연결 수), 트랜잭션 믹스.
- **소프트웨어**: OS, DB 버전, 설정.
- 분산 DB는 벤치마킹이 특히 어렵다(노드 수·복제·네트워크가 결과를 크게 흔듦).
- 출처: https://www.pingcap.com/blog/why-benchmarking-distributed-databases-is-so-hard/
- 출처: https://benchant.com/blog/benchmarking-suites

> 실무 원칙: "tpmC 1만"은 창고 수·하드웨어 없이는 해석 불가. 공식 TPC 결과가 강력한 이유는 Full Disclosure Report(FDR)로 전 환경을 공개·감사하기 때문.

---

## 6. 개발기간별(1/2/3년) 성능 목표 설정 관점 — 일반 원칙

> 아래는 검증된 일반 원칙을 토대로 한 **관점 제안**(특정 제품 보장 수치 아님). 구체 목표는 워크로드·예산 의존.

**전제 원칙(검증 기반)**:
- 가용성은 나인 1개 추가마다 비용 3~10배 → 무리한 초기 목표는 비효율.
- 처리량은 포화점 근처에서 지연이 지수 증가 → "처리량 목표"와 "그 처리량에서의 p99 목표"를 **쌍으로** 잡아야 함.
- tail latency(p99)가 사용자 체감·SLA를 좌우 → 평균이 아니라 p99로 목표 설정.

| 연차 | 처리량 목표 관점 | 지연(p99) 관점 | 가용성 관점 | 근거 |
|---|---|---|---|---|
| **1년차 (MVP/안정화)** | 실제 피크의 2~3배 헤드룸 확보가 목표(절대 최고치 추구 X). 단일 노드/소규모로 베이스라인 확보 | p99를 측정 가능하게 만들고 SLO 후보값 설정(예: 주요 API p99 < 수백 ms) | 99.9%(연 8.8h) — 가장 흔한 출발점 | 초기엔 "측정·관측가능성 구축"이 최고치보다 우선. 나인 추가 비용 급증 |
| **2년차 (성장/수평확장)** | 수평확장으로 처리량 N배 선형성 검증, 포화점 이동 확인 | 부하 증가에도 p99 유지(용량의 ~70% 이하 운영으로 지수구간 회피) | 99.95~99.99%(연 52분~) — 중복화·자동 페일오버 도입 시 | 80% 용량≈4배 지연 → 헤드룸 유지가 p99 방어 |
| **3년차 (성숙/미션크리티컬)** | 분산·샤딩으로 대규모 처리량, 멀티리전 | 멀티리전에서도 p99 SLO 보장, tail 관리(헤징·타임아웃) | 99.99%(결제·인증급) 또는 그 이상, 멀티리전 페일오버 | five nines는 3~10배 비용 → 비즈니스 가치와 ROI로 판단 |

- 근거 출처: 나인 비용/다운타임 — https://web-alert.io/blog/uptime-sla-explained-99-9-vs-99-99-availability ; 용량-지연 관계 — https://www.systemoverflow.com/learn/design-fundamentals/latency-throughput/what-are-latency-and-throughput-core-definitions-and-measurement ; tail latency — https://last9.io/blog/tail-latency/

> [관점/미확인] 위 표의 연차별 구체 임계값(예: "p99 < 수백 ms", "용량 70%")은 일반 권고 범위이며 산업·워크로드별로 달라짐. 특정 수치를 단정 인용하지 말 것.

---

## 7. 미확인/주의 항목 정리
1. **PolarDB 2.055B tpmC 직전 기록 보유자·정확 수치**: 기사 미명시. TPC 공식 결과로 교차검증 필요. [미확인]
2. **PolarDB 수치의 TPC 공식 등재 여부**: 보도자료 재게재 출처 기준이라 tpc.org 공식 페이지 확인 권장. [미확인]
3. **연차별 목표의 구체 임계값**: 일반 원칙·관점이며 보장 수치 아님. [관점]
4. **단일시스템 vs 클러스터/클라우드 결과 비교**: 직접 비교 부적절(Oracle 3,025만은 27대 클러스터). 주의.
5. tpmC/QphH/QphDS는 **항상 @Size·환경과 함께** 인용해야 유효.
