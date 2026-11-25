# evidence: fd-02-onprem-data-export-and-storage

열람일: 2026-10-22 (전 출처 공통)

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Guide to Operational Technology (OT) Security, NIST SP 800-82r3 | Stouffer, Pease, Tang, Zimmerman, Pillitteri, Lightman, Hahn, Saravia, Sherule, Thompson | 2023 | https://doi.org/10.6028/NIST.SP.800-82r3 (PDF 내려받아 전문 텍스트 추출) | 표지, 1장 요약 p.4, 5.2.3.1 (pp.71-73, Fig.16), 5.4.1 (p.86), 용어집 (data diode, data historian, demilitarized zone, unidirectional gateway), C.2.2 Improper data linking, 부록 E.1.2 (p.207), SCADA 구성 설명 p.13 |
| S2 | ANSI/ISA-62443-3-2-2020 preview | ISA | 2020 | https://www.isa.org/getmedia/661c718f-8e64-446d-acf9-2c6286db1b33/isa-62443-3-2-preview.pdf | Introduction, 1 Scope, 3.1.3 conduit |
| S3 | ISA/IEC 62443 Series of Standards (웹 페이지) | ISA | - | https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards | 표준 목록 (3-2, 3-3 명칭 확인용) |
| S4 | Toward Safe Integration of Legacy SCADA Systems in the Smart Grid | Aldar C-F. Chan, Jianying Zhou | 2022 (arXiv v2, 2022-05-03) | https://arxiv.org/abs/2107.05863 (PDF 본문) | 3 Data Diode Approach (pp.6-8), 4 첫 문단 |
| S5 | Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores | Armbrust 외 (Databricks 등) | 2020 | https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf | 2 Motivation (객체 저장소 특성·과제), 3.1.2 txn action, 4 Exactly-Once Streaming Writes |
| S6 | Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics | Michael Armbrust, Ali Ghodsi, Reynold Xin, Matei Zaharia | 2021 (CIDR '21) | https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf | Abstract, 3.1 Implementing a Lakehouse System |
| S7 | MQTT Version 5.0 (OASIS Standard) | OASIS | 2019 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html | 4.3.2 QoS 1 |
| S8 | How to create nested Azure IoT Edge device hierarchies | Microsoft Learn | 2026 (updated 2026-09-14) | https://learn.microsoft.com/en-us/azure/iot-edge/how-to-connect-downstream-iot-edge-device | 계층 소개, ISA-95 절, 네트워크 운영자 설정 |
| S9 | Operate Azure IoT Edge devices offline | Microsoft Learn | 2026 (updated 2026-03-03) | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities | How it works, Optional offline settings, Time to live |
| S10 | mosquitto.conf(5) man page 원본 (mosquitto.conf.5.xml) | Eclipse Mosquitto | - | https://raw.githubusercontent.com/eclipse-mosquitto/mosquitto/master/man/mosquitto.conf.5.xml (mosquitto.org 접속 거부되어 GitHub 원본 열람) | Configuring Bridges: address, cleansession, topic; max_queued_messages |
| S11 | Geo-Replication (Cross-Cluster Data Mirroring) | Apache Kafka | 4.3 문서 | https://kafka.apache.org/43/operations/geo-replication-cross-cluster-data-mirroring/ | 개요, 배치 권장, replication flow, 토픽 이름, exactly-once |
| S12 | Producer Configs | Apache Kafka | 4.3 문서 | https://kafka.apache.org/43/configuration/producer-configs/ | enable.idempotence, acks |
| S13 | Debezium FAQ | Debezium | - | https://debezium.io/documentation/faq/ | 전달 보장 관련 문항 |
| S14 | What is the medallion lakehouse architecture? | Databricks | - | https://docs.databricks.com/aws/en/lakehouse/medallion | bronze/silver/gold 절 |
| S15 | When to partition tables on Databricks | Databricks | - | https://docs.databricks.com/aws/en/tables/partitions | 파티션 기준 |
| S16 | InfluxDB schema design | InfluxData | v2 문서 | https://docs.influxdata.com/influxdb/v2/write-data/best-practices/schema-design/ | tags vs fields |
| S17 | Hypertables | Tiger Data (TimescaleDB) | - | https://www.tigerdata.com/docs/use-timescale/latest/hypertables | 정의 |
| S18 | Improve hypertable and query performance | Tiger Data | - | https://tigerdata.com/docs/build/performance-optimization/improve-hypertable-performance | 청크 간격 |
| S19 | Apache Parquet docs: Overview, Concepts, File Format, Configurations | Apache Parquet | - | https://parquet.apache.org/docs/ | 각 페이지 |
| S20 | Tabular Datasets | Apache Arrow (PyArrow) | - | https://arrow.apache.org/docs/python/dataset.html | Hive 파티션, write_to_dataset |

## 본문 사실 ↔ 원문 발췌

### Purdue·DMZ (S1)

1. [NIST SP 800-82r3가 Purdue, ISA-95, IIoT 3계층을 분할 기준으로 제시]
   > "Organizations may also consider using an industry-recognized model to organize their OT network segmentation, such as the Purdue model [Williams], ISA-95 levels [IEC62264], the three-tier IIoT system architecture [IIRA19], or a combination of these models." (5.2.3.1, p.71)
2. [그림 16에 Purdue+DMZ 예시, 계층 명칭 표]
   > "Additional, organizations may consider incorporating a DMZ as an enforcement boundary between network segments, as depicted in Fig. 16." (p.72)
   > Fig. 16 (페이지 이미지 판독): "Purdue with DMZ: DMZ / Level 5 - Enterprise / Level 4 - Business Planning / Logistics / DMZ / Level 3 - Operations / Control / Level 2 - Area Control (HMI) / Level 1 - Controller Network / Level 0 - Field I/O Devices"; 옆 패널 "ISA/IEC 62443: Enterprise, Conduit, DMZ, Conduit, Control Center, BCPS, Conduit, SIS" (원 그림의 구분 기호는 하이픈으로 옮김)
3. [인접 계층만 허용, Level 4가 2·1·0과 직접 통신 금지]
   > "Firewall rulesets should be established to only permit connections between adjacent levels, tiers, or zones. For example, organizations that utilize a Purdue model architecture should implement firewall rules and connection paths that prevent Level 4 devices from directly communicating with Level 2, 1, or 0 devices." (p.73)
4. [업무-운영 관리 계층 통신은 모두 DMZ 서비스를 거침]
   > "Implement a DMZ to separate the OT environment from the enterprise network. Any communications between the enterprise level and the operations management level are required to go through services within the DMZ." (5.4.1, p.86)
5. [outbound 규칙도 inbound만큼 엄격하게]
   > "Allowing outbound connections from lower levels, tiers, or zones could represent a significant risk if unmanaged. Organizations should consider making outbound rules as stringent as inbound rules to reduce these risks." (p.73)

### zone·conduit (S2, S1)

6. [conduit 정의]
   > "3.1.3 conduit: logical grouping of communication channels that share common security requirements connecting two or more zones" (S2)
7. [3-2 범위: zone/conduit 분할, 위험 평가, SL-T]
   > "partitioning the SUC into zones and conduits; assessing risk for each zone and conduit; establishing the target security level (SL-T) for each zone and conduit; and documenting the security requirements." (S2, 1 Scope)
8. [zone·conduit은 62443-1-1에서 도입]
   > "A key concept in this document is the application of IACS security zones and conduits. Zones and conduits are introduced in ISA-62443-1-1." (S2, Introduction)
9. [3-2 명칭: 시스템 설계를 위한 보안 위험 평가]
   > "Part 3-2: Security risk assessment for system design" (S3)

### outbound-only 예 (S8)

10. [ISA-95 같은 구조에서 최상위만 클라우드 연결, 하위는 부모·자식만]
   > "Some network architectures, like those that follow the ISA-95 standard, seek to minimize the number of internet connections. In those scenarios, you can configure downstream IoT Edge devices without direct internet connectivity."
   > "This network configuration requires that only the IoT Edge device in the top layer of a gateway hierarchy has direct connections to the cloud. IoT Edge devices in the lower layers can only communicate with their parent device or any children devices."
11. [방화벽 설정은 outbound, 443·5671]
   > "Authorize outbound communication from this IP address to your Azure IoT Hub hostname over ports 443 (HTTPS) and 5671 (AMQP)."
   > "Authorize outbound communications from this IP address to the parent gateway's IP address over ports 443 (HTTPS) and 5671 (AMQP)."

### Kafka MirrorMaker 2 (S11)

12. [대상 가까이 배치 권장, 이유는 프로듀서가 불안정 네트워크에 더 취약]
   > "it is recommended to locate MirrorMaker processes as close as possible to their target clusters, i.e., the clusters that it produces data to"
   > "Kafka producers typically struggle more with unreliable or high-latency network connections than Kafka consumers."
13. [복제 토픽 이름 {source}.{source_topic_name}]
   > "By default as per DefaultReplicationPolicy, the names of replicated topics in the target clusters have the format `{source}.{source_topic_name}`"
14. [전용 MirrorMaker 클러스터 exactly-once는 3.5.0부터]
   > "Exactly-once semantics are supported for dedicated MirrorMaker clusters as of version 3.5.0."

### 데이터 다이오드 (S1, S4)

15. [단방향 게이트웨이 정의: HW는 역방향 불가, SW는 DB 복제·프로토콜 서버 흉내]
   > "Unidirectional gateways are a combination of hardware and software. The hardware permits data to flow from one network to another but is physically unable to send any information at all back to the source network. The software replicates databases and emulates protocol servers and devices." (S1 용어집)
16. [방화벽과 달리 양방향 설정 불가]
   > "Unlike a firewall, data diodes cannot be programmed to allow data to flow in both directions because the hardware is incapable." (S1 E.1.2)
17. [Level 2-3 사이 배치 시 Level 0~2 보호]
   > "For example, a unidirectional gateway deployed between Layers 2 and 3 may protect Layer 0, 1, and 2 devices from a cybersecurity event that occurs at Layers 3, 4, or 5." (S1 p.73)
18. [광 결합기, 송신부/수신부 제거]
   > "Data diodes are often built using fibre optics coupler or transceivers, through the removal of the transmitter component from one side of the communication and the respective receiver component from the opposite side." (S4 §3)
19. [TCP 프로토콜 통과에 핸드셰이크·ACK 흉내, 프록시·프로토콜 브레이커, FEC]
   > "In order to support TCP/IP-based SCADA protocols, such as MODBUS/TCP and DNP3, data diodes usually have to make use of additional software components for each side of the unidirectional link to emulate the bidirectional message flow for the three-way handshake and acknowledgements needed in a typical TCP session." (S4 §3)
   > "The application proxy emulates the TCP server on the sender side to respond to the SCADA device (TCP client) with TCP connection-oriented messages and acknowledgements ... Similarly, the application proxy emulates the TCP client on the receiver side." (S4 §3)
   > "The protocol breaker acts as a middleware for packet encapsulation and possibly applying encryption and forward error correction (FEC) to data transferred over the unidirectional link." (S4 §3)
20. [피드백은 사람 소통으로, 역방향 채널 추가 시 이점 유지 불확실]
   > "Should the analysis lead to desired actions to be carried out in the SCADA system, the feedback will be through human communications." (S4 §3)
   > "Proposals such as [30] therefore emerged to add a reverse channel to data diodes. But whether the advantages of a data diode over a typical firewall can be preserved in such a modification is highly uncertain." (S4 §4)
   - 비고: 한계 표의 "재전송 요청 불가, 흐름 제어 없음, 송신 측 성공 모름"은 위 정의(역방향 정보 전송 물리적 불가, ACK는 송신 측 프록시가 생성)에서 도출한 설명이다. 설계 대응 열(순번·체크섬·용량 설계)은 저자 정리.

### 전송 방식 (S10, S13, S1)

21. [Mosquitto topic 방향 out/in/both, 기본 out]
   > "The second parameter defines the direction that the messages will be shared in, so it is possible to import messages from a remote broker using in, export messages to a remote broker using out or share messages in both directions. If this parameter is not defined, the default of out is used."
22. [브리지는 로컬이 원격 주소로 접속]
   > "Multiple bridges (connections to other brokers) can be configured using the following variables." / "Specify the address and optionally the port of the bridge to connect to."
23. [cleansession 기본 false, 끊겨도 원격 구독 유지]
   > "Setting to false (the default), means that all subscriptions on the remote broker are kept in case of the network connection dropping."
24. [max_queued_messages 기본 1000, QoS 1·2 per client]
   > "The maximum number of QoS 1 or 2 messages to hold in the queue (per client) above those messages that are currently in flight. Defaults to 1000."
25. [Debezium: 정상 시 정확히 한 번, 장애 시 최소 한 번, 중복이 하위에 보임]
   > "Therefore, under normal operating scenarios, the application sees every event exactly one time."
   > "However, when things go wrong it is always possible for consuming applications to see events at least once."
   > "these duplicates will always be visible to downstream consuming applications."
26. [DB 링크로 히스토리안 복제 시 위험]
   > "OT data storage systems may be linked to non-OT data sources. An example of this is database links, which allow data from one database (e.g., data historian) to be automatically replicated on others. Data linkage may create a vulnerability if it is not properly configured and may allow unauthorized data access or manipulation." (S1 C.2.2)
   - 비교표의 지연(분~시간, 초 등)·맞는 경우 열은 저자 정리이며 외부 수치 아님.

### 저장 후 전송·멱등성 (S9, S7, S5, S12)

27. [오프라인 시 저장 후 재연결, 저장 순서대로 전달]
   > "Stores any messages that go upstream and saves them until the device reconnects."
   > "Messages are delivered in the same order in which they were stored."
28. [TTL 기본 7,200초, TTL·디스크 늘리라는 권고]
   > "The time to live setting is how long (in seconds) a message waits to be delivered before it expires. The default value is 7,200 seconds (two hours)."
   > "Increase the time to live setting so the IoT Edge hub keeps messages until your device reconnects." / "Add more disk space for message storage."
29. [MQTT QoS 1 최소 한 번]
   > "4.3.2 QoS 1: At least once delivery. This Quality of Service level ensures that the message arrives at the receiver at least once."
30. [Delta Lake: 멱등 쓰기 필요, 고유 키 또는 last version 원자 갱신, (appId, version)]
   > "In general, stream processing systems that aim to update data in an external store need some mechanism to make their writes idempotent in order to avoid duplicate writes after a failure. This could be done by ensuring that each record has a unique key in the case of overwrites, or more generally, by atomically updating a "last version written" record together with each write, which can then be used to only write newer changes. Delta Lake facilitates this latter pattern by allowing applications to update an (appId, version) pair with each transaction." (S5 §4)
31. [Kafka enable.idempotence 기본 true, 재시도 중복 방지 범위]
   > "When set to 'true', the producer will ensure that exactly one copy of each message is written in the stream. If 'false', producer retries due to broker failures, etc., may write duplicates of the retried message in the stream." / "Idempotence is enabled by default if no conflicting configurations are set." (S12, Default: true)
   - 비고: "현장 큐의 재전송은 범위 밖"은 위 정의(프로듀서 재시도 중복)에서 도출한 해석.

### 저장 구조 (S1, S16, S17, S18, S5, S6)

32. [히스토리안 정의]
   > "data historian: A centralized database that supports data analysis using statistical process control techniques." (S1 용어집)
33. [제어 센터 LAN의 HMI·엔지니어링 워크스테이션·히스토리안]
   > "Other control center components include the HMI, engineering workstations, and the data historian, which are all connected by a local area network (LAN)." (S1 p.13)
34. [InfluxDB tag 인덱싱, field 미인덱싱, 메타데이터는 tag, 고유·변동 값은 field, 카디널리티]
   > "Tag values are indexed and field values aren't." / "Store unique or frequently changing values as field values." / "Store values as tag values if the values are shared across multiple data points, i.e. metadata about the field." / "Good schema design can prevent high series cardinality, resulting in better performing queries."
35. [hypertable 정의]
   > "PostgreSQL tables that automatically partition your time-series data by time and optionally by other dimensions." (S17)
36. [기본 청크 7일, 인덱스가 메모리 25% 안]
   > "The default chunk interval is 7 days." / "...the indexes for chunks currently being ingested into fit within 25% of main memory" (S18)
37. [객체 저장소 다중 객체 원자성 없음, LIST 비용 수치]
   > "No atomicity across multiple objects: Any transaction that needs to write or update multiple objects risks having partial writes visible to other clients." (S5 §2)
   > "S3's LIST only returns up to 1000 keys per call, and each call takes tens to hundreds of milliseconds, so it can take minutes to list a dataset with millions of objects using a sequential implementation." (S5 §2)
38. [바이트 범위 읽기]
   > "When reading an object, cloud object stores usually support byte-range requests, so it is efficient to read just a range within a large object" (S5 §2)
39. [Lakehouse: 객체 저장소 + Parquet + 트랜잭션 메타데이터 계층, Delta Lake·Iceberg]
   > "The first key idea we propose for implementing a Lakehouse is to have the system store data in a low-cost object store (e.g., Amazon S3) using a standard file format such as Apache Parquet, but implement a transactional metadata layer on top of the object store that defines which objects are part of a table version." (S6 §3.1)
   > "Several recent systems, including Delta Lake [10] and Apache Iceberg [7] have successfully added management features to data lakes in this fashion" (S6 §3.1)

### 메달리온 (S14)

40. [bronze/silver/gold 설명]
   > "The bronze layer contains raw, unvalidated data." / "Contains and maintains the raw state of the data source in its original formats." / "Is appended incrementally and grows over time." / "Enables reprocessing and auditing by retaining all historical data."
   > "The silver layer represents validated, cleaned, and enriched versions of the data." / "Is where you perform data cleansing, deduplication, and normalization."
   > "Consists of aggregated data tailored for analytics and reporting." / "Aligns with business logic and requirements."

### Parquet·파티셔닝 (S19, S20, S15)

41. [Parquet 열 지향]
   > "Apache Parquet is an open source, column-oriented data file format designed for efficient data storage and retrieval." (Overview)
42. [row group, column chunk, page]
   > "A logical horizontal partitioning of the data into rows." / "A row group consists of a column chunk for each column in the dataset." / "They live in a particular row group and are guaranteed to be contiguous in the file." / "A page is conceptually an indivisible unit (in terms of compression and encoding)." (Concepts)
43. [메타데이터 뒤에 기록, single pass]
   > "File metadata is written after the data to allow for single pass writing." (File Format)
44. [행 그룹 512MB~1GB, 페이지 8KB]
   > "We recommend large row groups (512MB - 1GB)." / "We recommend 8KB for page sizes." (Configurations)
45. [Hive 방식 /key=value/, write_to_dataset partition_cols]
   > "The above partitioning scheme is using "/key=value/" directory names, as found in Apache Hive." ; 예시 `pq.write_to_dataset(table, "parquet_dataset_partitioned", partition_cols=['part'])` (S20)
46. [1TB 미만 파티션 금지, 파티션당 1GB 이상, 카디널리티]
   > "With less than 1 TB of data, don't partition." / "For partitions, verify that each partition contains at least 1 GB of data." (S15)
   > 저카디널리티(날짜·위치)는 파티션에 적합, "high cardinality such as timestamps"는 부적합 (S15, WebFetch 요약 경유 확인한 문장 조각)
47. [100TB 미만 대부분 불필요, 파티션 없는 테이블은 적재 시각 클러스터링 자동]
   > "Most tables on Databricks with less than 100 TB of data don't need partitioning." / "By using Delta Lake, unpartitioned tables automatically use ingestion time clustering." (S15)

## 출처 없이 쓴 내용 (저자 정리·일반 지식)

- outbound-only를 "실무 원칙"으로 부른 것, 그림의 흐름 구성, 전송 방식 비교표의 지연·적합 용도 열, 결정적 이벤트 ID 코드와 seq·수신 시각 설명, 설비 ID를 파티션 대신 열로 두는 판단(S15 근거에서 도출), 마지막 절의 사람·도구 구분.

## 읽지 못해 뺀 내용

- IEC 62443-1-1/3-2 본문의 zone 정의 원문: 유료, 미리보기에 zone 정의 없음. zone은 정의 인용 없이 "ISA-62443-1-1에서 도입" 수준으로만 썼다.
- ISAGCA Quick Start Guide PDF: URL이 HTML로 응답해 열람 실패. 사용 안 함.
- Purdue 원전(Williams 1994): 열람 안 함. NIST 경유로만 계층 명칭 인용.
- mosquitto.org man 페이지: 접속 거부(ECONNREFUSED). 같은 내용의 GitHub 원본 XML로 대체.
- 데이터 다이오드 EAL7 등 논문의 추가 주장: 본문에 쓰지 않음.
