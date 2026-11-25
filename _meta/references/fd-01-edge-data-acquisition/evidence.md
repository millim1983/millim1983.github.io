# evidence: fd-01-edge-data-acquisition

열람일: 2026-10-22 (전 출처 공통). PDF는 내려받아 PyMuPDF로 텍스트 추출 후 해당 구간을 직접 읽음. 웹 사양은 해당 절 페이지를 직접 열람.

## 출처 목록

| # | 제목 | 저자 | 연도 | URL | 읽은 위치 |
|---|---|---|---|---|---|
| S1 | Communication in the Presence of Noise | C. E. Shannon | 1949 (Proc. IEEE 1998 재수록) | https://web.cs.miami.edu/home/burt/learning/Csc524.092/docs/shannonpaper.pdf | 1쪽 각주(원 게재 정보), Section II Theorem 1과 이어지는 단락 |
| S2 | Assessing Open Interfaces and Protocols of PLCs for Computation Offloading at Field Level | M. Gundall, H. D. Schotten | 2021 (WFCS) | https://arxiv.org/abs/2106.04517 (PDF v1) | Table I, Sec. II-C-1 Server Client, II-C-2 PubSub, II-D Summary, III Conclusion |
| S3 | Real-Time Performance of OPC UA | E. Kirdan, F. Rezabek, N. Mühlbauer, G. Carle, M.-O. Pahl | 2023 | https://arxiv.org/abs/2310.17052 (PDF v2) | Sec. II-A OPC UA PubSub, II-B Time Synchronization |
| S4 | Sparkplug Specification Version 3.0.0 | Eclipse Sparkplug Contributors | 2022-11-16 | https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf | 1.x Primary Host Application, 2.2, 2.3, 2.4, 4.1, 4.1.1, 4.1.3, 4.2.1 NBIRTH/NDEATH, 5.x Edge Node Session Establishment, Reorder Timeout, 6.4.x Quality Codes |
| S5 | OPC 10000-1 Part 1: Overview and Concepts v1.05.06 | OPC Foundation | 2025 | https://reference.opcfoundation.org/Core/Part1/v105/docs/4.4.2 , /5.5 | 4.4.2, 5.5 |
| S6 | OPC 10000-3 Part 3: Address Space Model v1.05 | OPC Foundation | - | https://reference.opcfoundation.org/Core/Part3/v105/docs/4.6.1 , /4.1 | 4.1(목차 포함), 4.6.1 |
| S7 | OPC 10000-4 Part 4: Services v1.05 | OPC Foundation | - | https://reference.opcfoundation.org/Core/Part4/v105/docs/5.13.1.2 , /7.22.2 , /7.38.1 , /7.38.2 , /7.39 | 5.13.1.2, 7.22.2, 7.38.1 Table 176-177, 7.38.2 Table 179, 7.39 |
| S8 | OPC 10000-8 Part 8: Data Access v1.05 | OPC Foundation | - | https://reference.opcfoundation.org/Core/Part8/v105/docs/7.3.2 | 7.3.2 Table 61, Table 62 |
| S9 | OPC 10000-14 Part 14: PubSub v1.05.06 | OPC Foundation | 2025 | https://reference.opcfoundation.org/Core/Part14/v105/docs/5.1 , /5.4.6 | 5.1, 5.4.6.2, 5.4.6.3 |
| S10 | OPC 40001-1 OPC UA for Machinery Part 1: Basic Building Blocks | OPC Foundation | - | https://reference.opcfoundation.org/specs/OPC-40001-1/full | 1 Scope, 8.2, 8.6 Table 22 |
| S11 | MODBUS Application Protocol Specification V1.1b3 | Modbus Organization | 2012-04-26 | https://www.modbus.org/file/secure/modbusprotocolspecification.pdf | 1 Introduction, 4.1 PDU 크기, 4.3 Data model |
| S12 | MODBUS over Serial Line Specification and Implementation Guide V1.02 | Modbus Organization | - | https://www.modbus.org/file/secure/modbusoverserial.pdf | 2.5.1, 2.5.1.1 RTU Framing |
| S13 | MODBUS Messaging on TCP/IP Implementation Guide V1.0b | Modbus Organization | - | https://www.modbus.org/file/secure/messagingimplementationguide.pdf | MBAP Header, port 502 단락 |
| S14 | EtherNet/IP: CIP on Ethernet Technology (PUB00138R8) | ODVA | 2024-02 | https://www.odva.org/wp-content/uploads/2024/04/PUB00138R8_Ethernet.pdf | 2쪽 서두, TCP/IP 단락, Messaging connections 단락 |
| S15 | PROFINET RT: Real-Time Performance | PI North America (us.profinet.com) | 날짜 미표기 | https://us.profinet.com/profinet-rt-real-time-performance/ | 본문 전체 |
| S16 | PROFINET IRT- Isochronous Real Time | PI North America (us.profinet.com) | 날짜 미표기 | https://us.profinet.com/?p=19941 | 본문, FAQ |
| S17 | MQTT Version 5.0 OASIS Standard | OASIS | 2019-03-07 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html | Abstract(QoS 3단계), 3.1.2.5 Will Flag, 3.1.2.10 Keep Alive, 4.2 Network Connections 비규범 주석 |
| S18 | RFC 5905 Network Time Protocol Version 4 | D. Mills, J. Martin, J. Burbank, W. Kasch | 2010-06 | https://www.rfc-editor.org/rfc/rfc5905 | 1 Introduction, 8 On-Wire Protocol |
| S19 | IEEE 1588-2019 (표준 페이지 초록) | IEEE | 2019-11-07 승인 | https://standards.ieee.org/ieee/1588/6825/ | Abstract |
| S20 | Introduction to IEEE 1588 | NIST | 2010 작성, 2021 갱신 | https://www.nist.gov/el/intelligent-systems-division-73500/introduction-ieee-1588 | 본문 |
| S21 | RFC 5424 The Syslog Protocol | R. Gerhards | 2009-03 | https://www.rfc-editor.org/rfc/rfc5424 | 6.2.1 Severity 표, 6.2.3 TIMESTAMP, 6 ABNF |
| S22 | US7805281B2 Vibration analysis | N. Leigh | 2010-09-28 | https://patents.google.com/patent/US7805281B2/en | Description, Equation 1 주변 |
| S23 | AFE782H1, AFE882H1 Data Sheet (SLASF43A) | Texas Instruments | - | https://ti.com/document-viewer/AFE882H1/datasheet/GUID-0EB0D283-B3DA-4517-859D-DA20A442BBED | 1 Features |

## 본문 사실 ↔ 원문 발췌

### 데이터 원천

- [Modbus 데이터 모델은 네 기본 표(Discretes Input, Coils, Input Registers, Holding Registers), 비트·16비트 워드] ↔ S11 4.3: "MODBUS bases its data model on a series of tables that have distinguishing characteristics. The four primary tables are: ... Discretes Input Single bit Read-Only ... Coils Single bit Read-Write ... Input Registers 16-bit word Read-Only ... Holding Registers 16-bit word Read-Write"
- [NAMUR NE 43: 3.6 mA 미만, 21 mA 초과를 센서 고장 신호 수준으로 씀] ↔ S23 Features: "Out-of-range current output capability less than 3.6mA and greater than 21mA for NAMUR NE43 sensor-fault signal levels"
- [syslog 심각도 0(Emergency)~7(Debug)] ↔ S21 6.2.1: "0 Emergency: system is unusable ... 7 Debug: debug-level messages"
- [TIMESTAMP는 RFC 3339 기반, 대문자 T 필수] ↔ S21 6.2.3: "The TIMESTAMP field is a formalized timestamp derived from [RFC3339]." / "The "T" and "Z" characters in this syntax MUST be upper case." / "Usage of the "T" character is REQUIRED."

### 프로토콜 비교

- [Modbus 1979년부터, OSI 7계층 요청·응답, 포트 502] ↔ S11 1: "MODBUS is an application layer messaging protocol, positioned at level 7 of the OSI model" / "The industry's serial de facto standard since 1979" / "a reserved system port 502 on the TCP/IP stack." / "MODBUS is a request/reply protocol"
- [PDU 253바이트, 직렬 ADU 256, TCP ADU 260 (MBAP 7)] ↔ S11 4.1: "MODBUS PDU for serial line communication = 256 - Server address (1 byte) - CRC (2 bytes) = 253 bytes." / "TCP MODBUS ADU = 253 bytes + MBAP (7 bytes) = 260 bytes."
- [RTU 프레임 최대 256바이트, 3.5문자 무신호, 1.5문자 초과 시 불완전 프레임 폐기] ↔ S12 2.5.1: "The maximum size of a MODBUS RTU frame is 256 bytes." / 2.5.1.1: "In RTU mode, message frames are separated by a silent interval of at least 3.5 character times." / "If a silent interval of more than 1.5 character times occurs between two characters, the message frame is declared incomplete and should be discarded by the receiver."
- [Modbus TCP 포트 502] ↔ S13: "All MODBUS/TCP ADU are sent via TCP to registered port 502."
- [EtherNet/IP 2001년 도입, 상위 계층 CIP] ↔ S14 2쪽: "EtherNet/IP™ was introduced in 2001" / "EtherNet/IP is a member of a family of networks that implements the Common Industrial Protocol (CIP™) at its upper layers."
- [명시적 메시지는 TCP/IP, 설정·진단용] ↔ S14: "EtherNet/IP uses TCP/IP to encapsulate CIP explicit messages, which are generally used to transmit configuration and diagnostic data"
- [명시적 연결은 요청·응답, 암시적은 정해진 간격 I/O, UDP 멀티캐스트] ↔ S14: "Explicit messaging connections are point-to-point relationships that are established to facilitate request-response transactions between two nodes." / "Implicit (I/O data) connections are established to move application-specific I/O data at regular intervals." / "Implicit messaging uses UDP/IP resources to make multicast data transfers over Ethernet a reality."
- [PROFINET RT는 TCP/IP를 거치지 않음, EtherType 0x8892, 주기 250 µs ~ 512 ms] ↔ S15: "The frame goes directly from Ethernet (Layer 2) to PROFINET (Layer 7)." / "skips the TCP/IP layers and avoids the variable time it takes to be processed." / "An arriving PROFINET RT Ethernet frame has the PROFINET EtherType: 0×8892." / "vary within the range of 250 µs to 512 ms for PROFINET RT."
- [IRT 최저 31.25 µs, 지터 1 µs 미만, 공통 시계, Conformance Class C 인증, 사이 노드도 IRT 필요] ↔ S16: "it can be reduced to as low as 31.25 µs with the appropriate hardware." / "PROFINET IRT enables applications having a jitter of less than 1 microsecond." / "all devices involved in the synchronous communication must have a common clock." / "Only Conformance Class C devices support PROFINET IRT." / "all nodes in between those controllers and devices require IRT capabilities."
- [MQTT QoS 0·1·2 정의] ↔ S17 Abstract: ""At most once", where messages are delivered according to the best efforts of the operating environment. Message loss can occur." / ""At least once", where messages are assured to arrive but duplicates can occur." / ""Exactly once", where messages are assured to arrive exactly once."
- [Keep Alive 1.5배 초과 시 서버가 연결 종료] ↔ S17 3.1.2.10: "If the Keep Alive value is non-zero and the Server does not receive an MQTT Control Packet from the Client within one and a half times the Keep Alive time period, it MUST close the Network Connection to the Client as if the network had failed"
- [포트 1883 평문, 8883 TLS] ↔ S17 4.2 비규범 주석: "TCP ports 8883 and 1883 are registered with IANA for MQTT TLS and non-TLS communication respectively."
- [Will 메시지는 연결 종료 후 발행] ↔ S17 3.1.2.5: "The Will Message MUST be published after the Network Connection is subsequently closed"
- [OPC UA PubSub이 MQTT를 전송 수단으로 쓸 수 있음] ↔ S9 5.4.6.3.2: "It requires use of messaging protocols that a Broker understands, like MQTT defined in ISO/IEC 20922:2016."

### OPC UA 정보모델·구독·PubSub

- [주소 공간 = 참조로 연결된 노드 집합] ↔ S5 4.4.2: "The OPC UA AddressSpace represents its contents as a set of Nodes connected by References."
- [노드 클래스: 객체·변수·메서드] ↔ S6 목차: "5.5 Objects (5.5.1 Object NodeClass; 5.5.2 ObjectType NodeClass)", "5.6 Variables", "5.7 Methods (5.7.1 Method NodeClass)"
- [서버는 객체·변수 타입 정의 제공, 잘 알려진 타입은 서버 간 공통, 클라이언트는 다시 읽지 않고 해석] ↔ S6 4.6.1: "OPC UA Servers shall provide type definitions for Objects and Variables." / "Well-known NodeIds of TypeDefinitionNodes provide for commonality across OPC UA Servers" / "allow Clients to interpret the TypeDefinitionNode without having to read it from the Server."
- [Machinery 빌딩 블록, MachineIdentificationType, Manufacturer, SerialNumber, ProductInstanceUri] ↔ S10 1: "The OPC UA for Machinery specification contains various building blocks for Machinery" / 8.6 Table 22: "Contains information about the identification and nameplate of a machine." / 8.2: "provides a human-readable, localized name of the manufacturer." / "is a string containing a unique production number of the manufacturer." / "is intended to uniquely identify the MachineryItem and shall not change during the life-cycle."
- [샘플링 간격 0 = 가장 빠른 주기, 서버가 수정 가능, 0으로 수정 시 예외 기반] ↔ S7 5.13.1.2: "The Client may also specify 0 for the sampling interval, which indicates that the Server should use the fastest practical rate." / "the Server assigns to the MonitoredItem the most appropriate interval as determined by the Server." / "indicates that the data item is exception-based rather than being sampled at some period."
- [PubSub은 요청·응답 없음, 연결 수립 없음, 발행자 부하가 구독자 수와 무관] ↔ S5 5.5: "OPC UA Applications do not directly exchange requests and responses." / "There is no connection establishment between Publisher and Subscriber." / "Effort and resource requirements for the Publisher are predictable and do not depend on the number of Subscribers."
- [브로커 없는 방식은 네트워크 인프라가 전달, UDP는 적시성·전달·순서·중복 보장 없음] ↔ S9 5.4.6.2.1: "With this option, OPC UA PubSub relies on the network infrastructure to deliver NetworkMessages to one or more receivers." / 5.4.6.2.2: "With OPC UA UDP there is no guarantee of timeliness, delivery, ordering, or duplicate protection."
- [브로커 방식은 MQTT·AMQP 브로커가 중계] ↔ S5 5.5: "use standard messaging protocols like AMQP or MQTT to communicate with the Broker" / S9 5.4.6.3.2: "In this model the Message Oriented Middleware will be a Broker that relays NetworkMessages from Publishers to Subscribers."
- [인코딩 UADP와 JSON] ↔ S3 II-A: "OPC UA PubSub messages can be mapped to JSON or binary Unified Architecture Datagram Protocol (UADP)."
- [Gundall: 상용 PLC 두 기종 비교] ↔ S2 Abstract: "we investigate open communication interfaces of two typical PLCs of Siemens S7 series."
- [Read 서비스 1/10/100개: 9.11/30.35/246.1 ms, PubSub 1/10개: 1.02/1.26 ms] ↔ S2 Table I (S7-1512 열): "Read Service UATCP + + 0.8 n/a 9.11 3.7 n/a 30.35 5.4 n/a 246.1" / "OPC UA PubSub UADP - ◦ 5.5 n/a 1.02 33.9 n/a 1.26 70.41 n/a 2.301" / 본문: "OPC UA PubSub performs best in terms of update times for 1 and 10 data values of ≈1ms and 1.26 ms, respectively."
- [WriteRequest 234바이트, 효율 1% 미만, 원인은 메타데이터] ↔ S2 II-C-1: "the WriteRequests have the sizes of 234 bytes, 396 bytes, and 2154 bytes for 1, 10, and 100 data values" / "This results in a low protocol efficiency that is, for example, < 1% for 1 data value."
- [PubSub은 좋은 절충, Read는 PLC 재설정 없이 직접 접근 장점, PubSub은 WriterGroup·DataSetWriter 설정 필요] ↔ S2 II-D: "UDP-based OPC UA PubSub provides a very good trade-off in terms of update time, protocol efficiency, and the presence of at least some meta information" / II-C-1: "what is an advantage for this interface is the direct access to the data without reconfiguration of the PLC." / II-C-2: "interface requires reconfiguration of the PLC, it is not plug & play capable. First a WriterGroup must be defined. Under the WriterGroup are logically grouped the so-called DataSetWriters"

### Sparkplug B

- [3.0.0, 2022-11-16] ↔ S4 표지: "Sparkplug 3.0.0 ... Version 3.0.0, 2022-11-16"
- [토픽 구조, spBv1.0] ↔ S4 4.1: "namespace/group_id/message_type/edge_node_id/[device_id]" / 4.1.1: "the UTF-8 string constant for the namespace element MUST be: spBv1.0"
- [메시지 유형 9종] ↔ S4 4.1.3: "NBIRTH - Birth certificate for Sparkplug Edge Nodes • NDEATH - Death certificate for Sparkplug Edge Nodes • DBIRTH ... • DDEATH ... • NDATA - Edge Node data message • DDATA ... • NCMD ... • DCMD ... • STATE - Sparkplug Host Application state message"
- [출생 인증서가 전체 메트릭 현재값을 담음] ↔ S4 2.2: "In the initial BIRTH messages, all of the current metric values are published in the payload." / 4.2.1: "The Sparkplug Edge Node Birth Certificate payload contains everything required to build out a data structure for all metrics for this Edge Node."
- [CONNECT에 NDEATH를 Will로 등록, bdSeq INT64] ↔ S4 5.x: "When a Sparkplug Edge Node sends its MQTT CONNECT packet, it MUST include a Will Message." / "The Edge Node's MQTT Will Message's topic MUST be of the form spBv1.0/group_id/NDEATH/edge_node_id" / "MUST include a metric with the name of bdSeq, the datatype of INT64"
- [비정상 단절 시에도 사망 인증서 전달] ↔ S4 2.4: "By using the MQTT Will message, the Death Certificates will be delivered to subscribers even if the MQTT client connection is lost ungracefully."
- [bdSeq 일치 시 전체 메트릭 STALE, 수신 시각 기록] ↔ S4 4.2.1 NDEATH: "Immediately upon reception of an Edge Node Death Certificate (NDEATH message) with a bdSeq number that matches the preceding bdSeq number in the NBIRTH, any Host Application subscribed to this Edge Node should set the data quality of all metrics to STALE and should note the timestamp when the NDEATH message was received."
- [중복 bdSeq의 Will 사망 메시지는 무시] ↔ S4: "Because it has a duplicate bdSeq, the Will Message Death message MUST be ignored by the subscribing Sparkplug Host Application clients."
- [seq 0~255 순환] ↔ S4: "The Edge Node's NBIRTH payload MUST include a seq number that is between 0 and 255 (inclusive)." / "one more than the previous up to 255 where it wraps back to zero."
- [1,2,4 수신 시 Reorder 타이머, 3 미도착 시 Rebirth Request, 일반 환경 몇 초] ↔ S4: "if a Sparkplug Host Application receives messages from an Edge Node with sequence numbers 1, 2, and 4 then at the time the message with a sequence number 4 arrives, a timer SHOULD be started" / "If a message with sequence number 3 does not arrive before the timeout, a Rebirth Request should be sent to the Edge Node." / "In typical environments this timeout can be as little as a couple of seconds."
- [RBE 원칙, 주기 발행 지양(SHOULD)] ↔ S4 2.2: "[tck-id-principles-rbe-recommended] Because of the stateful nature of Sparkplug sessions, data SHOULD NOT be published from Edge Nodes on a periodic basis and instead SHOULD be published using a RBE based approach."
- [RBE는 세션 상태를 알아야 성립] ↔ S4 2.3: "But for RBE to work properly in real-time SCADA, the "state" of the end device needs to be always known."
- [STATE 토픽 spBv1.0/STATE/sparkplug_host_id] ↔ S4 2.4: "For Host Applications, the spBv1.0/STATE/sparkplug_host_id topic is used."
- [1차 호스트 오프라인 동안 엣지 저장, 복귀 시 이력 데이터 전송] ↔ S4 1.x: "an Edge Node may store data at the edge until a Primary Host Application comes back online. When the Primary Host Application publishes a new STATE message denoting it is online, the Edge Node can resume publishing data and also flush any historical data that it may have stored while offline."
- [Quality 속성 키, 0 BAD / 192 GOOD / 500 STALE, 선택 사항, GOOD 아닐 때만] ↔ S4 6.4.x Quality Codes: "There is one specific property key in Sparkplug called Quality." / "This property is optional and is only required if the quality of the metric is not GOOD." / "• 0 ◦BAD • 192 ◦GOOD • 500 ◦STALE"

### 폴링·데드밴드

- [데드밴드 유형 없음·절대·퍼센트, 절대 판정식, 기준은 마지막으로 큐에 넣은 값] ↔ S7 7.22.2: "0 None No Deadband calculation should be applied." / "Generate a Notification if (absolute value of (last cached value - current value) > AbsoluteDeadband)" / last cached value는 "the last value pushed to the queue"로 정의

### 샘플링

- [Shannon 1949, Proc. IRE 37(1) 10-21] ↔ S1: "This paper is reprinted from the PROCEEDINGS OF THE IRE, vol. 37, no. 1, pp. 10-21, Jan. 1949."
- [Theorem 1] ↔ S1 II: "Theorem 1: If a function f(t) contains no frequencies higher than W cps, it is completely determined by giving its ordinates at a series of points spaced 1/2W seconds apart."
- [통신 분야에서 알려진 사실, Nyquist 언급] ↔ S1 II: "This is a fact which is common knowledge in the communication art." / "Nyquist, however, and more recently Gabor, have pointed out that approximately 2TW numbers are sufficient"
- [Fmax x 2.56, 업계 흔한 값, 나이퀴스트·필터 요구 충족] ↔ S22: "The value of 2.56 is typical in the industry and is chosen to satisfy normal Nyquist and filtering requirements." (Equation 1: 표본화율 = Fmax(high) x 2.56)
- 앨리어싱 접힘식 |f - k·fs|, 950 Hz → 50 Hz 예시, 안티앨리어싱 필터 원리는 일반 신호처리 상식으로 출처 없이 서술하고 코드로 직접 확인함

### 시간 동기

- [NTP 오프셋·지연 식] ↔ S18 8: "theta = T(B) - T(A) = 1/2 * [(T2-T1) + (T3-T4)]" / "delta = T(ABA) = (T4-T1) - (T3-T2)."
- [NTP 정밀도: 1차 수십 µs, LAN 2차 수백 µs, 36시간 폴링 시 수십 ms] ↔ S18 1: "Typical primary servers using modern machines are precise within a few tens of microseconds. Typical secondary servers and clients on fast LANs are within a few hundred microseconds with poll intervals up to 1024 seconds" / "With NTPv4, servers and clients are precise within a few tens of milliseconds with poll intervals up to 36 hours."
- [IEEE 1588-2019: 마이크로초 미만, 잘 설계된 망에서 나노초 미만] ↔ S19: "The protocol supports synchronization accuracy and precision in the sub-microsecond range" / "Sub-nanosecond time transfer accuracy can be achieved in a properly designed network."
- [IEEE 1588-2019 승인일, 정식 명칭] ↔ S19: "IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems", Board approval 2019-11-07
- [NIST: 측정·제어 시스템 동기 요구, 2019판 IEC 61588:2021 채택(참고용)] ↔ S20: "IEEE 1588 addresses the clock synchronization requirements of measurement and control systems." / "IEEE 1588-2019 was approved to be published as a full-use standard"
- [ptp4l·phc2sys, I210 하드웨어 타임스탬프로 나노초 수준] ↔ S3 II-B: "The ptp4l tool, a command-line utility, implements the PTP standard IEEE 1588" / "Hardware timestamping can be leveraged to achieve nanosecond-level precision when utilizing a Network interface card (NIC) that supports IEEE 802.1AS, such as the commercially available Intel® I210 NIC."
- [TimestampsToReturn: SOURCE, SERVER, BOTH, NEITHER] ↔ S7 7.39: TimestampsToReturn "specifies the Timestamp Attributes to be transmitted" / SOURCE_0, SERVER_1, BOTH_2, NEITHER_3, INVALID_4

### 품질 플래그

- [StatusCode 32비트, 심각도 30:31 Good/Uncertain/Bad 의미, 하위 코드 16:27] ↔ S7 7.38.1: "The StatusCode is a 32-bit unsigned integer." / Good "Indicates that the operation was successful and the associated results may be used." / Uncertain "Indicates that the operation was partially successful and that associated results might not be suitable for some purposes." / Bad "Indicates that the operation failed and any associated results cannot be used." / SubCode(16:27) "The code is a numeric value assigned to represent different conditions."
- [Bad_NoCommunication 정의] ↔ S7 7.38.2 Table 179: "Communication with the data source is defined, but not established, and there is no last known value available."
- [Part 8 코드들] ↔ S8 Table 61: Bad_SensorFailure "There has been a failure in the sensor from which the value is derived by the device/data source." / Bad_DeviceFailure "There has been a failure in the device/data source that generates the value that has affected the value." / Bad_OutOfService "The source of the data is not operational." ; Table 62: Uncertain_LastUsableValue "Whatever was updating this value has stopped doing so." / Uncertain_SensorNotAccurate "The value is at one of the sensor limits." / Uncertain_EngineeringUnitsExceeded "The value is outside of the range of values defined for this parameter."

## 열람 실패·제외

- Profanter et al. (2019) "OPC UA versus ROS, DDS, and MQTT" (ICIT 2019): TUM 저장소 PDF가 봇 차단(Anubis)으로 열리지 않아 인용하지 않음
- EtherNet/IP 포트 번호(44818/2222): ODVA 문서에서 확인하지 못해 본문에서 뺌
- PROFINET 장치 기술 파일(GSD): 공식 문서 미열람으로 뺌
