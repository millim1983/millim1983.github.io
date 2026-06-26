---
layout: post
title: "JSON이란 무엇인가 — 데이터를 주고받는 가장 흔한 포맷"
subtitle: "키-값 텍스트라는 쉬운 정의에서 시작해 숫자 정밀도·인코딩·스키마 검증까지"
categories: [questions]
tags: [json, serialization, api, json-schema, ndjson, data-format, basics]
toc: true
mermaid: true
status: published
date: 2026-06-26 10:15:20 +09:00
---

## 0. 한 줄 정의

JSON(JavaScript Object Notation) — 데이터를 사람이 읽을 수 있는 텍스트로 적는 포맷. 키-값 쌍과 목록을 중괄호·대괄호로 표현한다.

이렇게 생겼다.

```json
{
  "name": "김철수",
  "age": 30,
  "active": true,
  "tags": ["admin", "user"]
}
```

이 한 토막이 JSON의 전부에 가깝다. 중괄호 안에 `"키": 값`을 쉼표로 나열하고, 값이 여러 개면 대괄호로 묶는다. 이름은 JavaScript에서 왔지만 지금은 파이썬·자바·Go·러스트 등 거의 모든 언어가 읽고 쓴다. 언어에 묶이지 않은 텍스트 포맷이다.

여기까지가 쉬운 정의다. 이 글은 거기서 멈추지 않고, 실제로 JSON을 주고받을 때 누구나 부딪히는 복잡함(숫자 정밀도·인코딩·스키마 검증·보안)까지 내려간다.

## 1. 자료형은 딱 여섯 가지

JSON 값은 정확히 여섯 종류뿐이다. RFC 8259와 ECMA-404 두 표준이 같은 문법을 정의한다.

| 자료형 | 예시 | 비고 |
|---|---|---|
| object(객체) | `{"a": 1}` | 키-값 모음. 키는 반드시 큰따옴표 문자열 |
| array(배열) | `[1, 2, 3]` | 순서 있는 목록 |
| string(문자열) | `"hello"` | 큰따옴표만. 작은따옴표 안 됨 |
| number(숫자) | `42`, `3.14`, `-1e10` | 정수·소수 구분 없이 하나의 number |
| boolean | `true`, `false` | 소문자만 |
| null | `null` | 값 없음 |

문법은 이게 끝이다. 그런데 더 중요한 건 **JSON에 없는 것**이다. 익숙한 다른 포맷에는 있는데 JSON에는 없어서 자주 헷갈린다.

| JSON에 없는 것 | 무슨 뜻인가 |
|---|---|
| 주석 | `//`나 `/* */`를 쓸 수 없다. 설정 파일에 메모를 남길 데가 없다 |
| 정수/실수 타입 구분 | `42`와 `42.0`을 표준은 똑같은 number로 본다. int·float 구분이 없다 |
| 날짜 타입 | `2026-06-26` 같은 날짜는 그냥 문자열이다. 약속(ISO 8601 등)으로 표현할 뿐 |
| 후행 콤마(trailing comma) | `[1, 2, 3,]`처럼 마지막에 콤마를 붙이면 파싱 오류다 |
| `Infinity` / `NaN` | 무한대·비수(非數)는 표현할 수 없다. 표준이 금지한다 |

> JSON 문법은 한 페이지로 끝난다. 실무의 함정은 "JSON에 있는 것"이 아니라 "JSON에 없는데 있을 줄 알았던 것"에서 나온다.

## 2. 직렬화와 역직렬화

프로그램 안의 데이터(객체·딕셔너리·구조체)는 메모리에만 있는 형태라 그대로 네트워크로 보내거나 파일에 쓸 수 없다. 그래서 JSON 텍스트로 바꿔서 내보내고, 받은 쪽이 다시 자기 언어의 객체로 되돌린다.

- 직렬화(serialize): 메모리 속 객체 → JSON 텍스트
- 역직렬화(parse, 파싱): JSON 텍스트 → 메모리 속 객체

이 코드를 보이는 목적은 두 방향이 실제로 어떻게 한 줄씩 호출되는지 확인하기 위해서다.

`example.py`
```python
import json

data = {"name": "김철수", "age": 30, "tags": ["admin"]}

# 직렬화: 파이썬 딕셔너리 → JSON 문자열
# ensure_ascii=False 를 빼면 한글이 \uXXXX 로 깨져 나온다
text = json.dumps(data, ensure_ascii=False)
# 결과: {"name": "김철수", "age": 30, "tags": ["admin"]}

# 역직렬화: JSON 문자열 → 파이썬 딕셔너리
back = json.loads(text)
print(back["name"])   # 김철수
```

JavaScript에서는 `JSON.stringify()`(직렬화)와 `JSON.parse()`(역직렬화)가 같은 일을 한다. 이름만 다를 뿐 모든 언어에 짝이 있다.

```mermaid
flowchart LR
  A["메모리 속 객체<br/>(딕셔너리/구조체)"] -->|"직렬화<br/>dumps / stringify"| B["JSON 텍스트<br/>{ ... }"]
  B -->|"전송·저장"| C["네트워크 / 파일"]
  C -->|"수신·읽기"| D["JSON 텍스트<br/>{ ... }"]
  D -->|"역직렬화<br/>loads / parse"| E["메모리 속 객체"]
```

*그림. 객체는 직렬화로 JSON 텍스트가 되어 오가고, 받은 쪽이 역직렬화로 다시 객체로 되돌린다.*

## 3. 숫자가 깨진다 — 가장 비싼 함정

JSON에서 가장 자주, 그리고 가장 조용히 사람을 무는 함정이다.

JSON 표준 자체는 숫자 크기에 제한을 두지 않는다. 자릿수가 아무리 길어도 문법상 올바른 number다. 문제는 받는 쪽 언어다. JavaScript는 모든 숫자를 IEEE 754 배정밀도 부동소수(double, 64비트)로 다룬다. 이 형식이 정확히 표현할 수 있는 정수의 한계는 2의 53제곱에서 1을 뺀 값, 즉 9,007,199,254,740,991이다(`Number.MAX_SAFE_INTEGER`).

이보다 큰 정수를 JavaScript로 파싱하면 오류 없이 조용히 값이 바뀐다.

```javascript
JSON.parse("9007199254740993")
// 결과: 9007199254740992  ← 1 차이로 다른 값이 됐는데 에러도 안 난다
```

왜냐하면 double의 가수(mantissa)는 52비트뿐이라, 한계를 넘으면 연속한 두 정수가 같은 부동소수 값으로 뭉개지기 때문이다. 더 무서운 건 이게 언어 간 호환성 버그라는 점이다. 같은 JSON을 파이썬이나 자바로 파싱하면 큰 정수를 정확히 읽는다. 즉 서버(파이썬)는 멀쩡한데 브라우저(JavaScript)에서만 ID가 1 틀어진다.

현실에서 이 한계를 넘는 숫자는 흔하다. 트위터·디스코드가 쓰는 Snowflake ID, 64비트 데이터베이스 기본키, 일부 주문번호가 그렇다. 해법은 두 가지다.

- 큰 정수는 처음부터 **문자열로** 보낸다(`"id": "9007199254740993"`). 가장 안전하고 흔한 방법이다.
- JavaScript라면 파싱 시 BigInt(2020년 ECMAScript에 추가된 임의 정밀도 정수형)로 변환한다.

> 숫자가 큰 ID는 JSON에서 따옴표로 묶어 문자열로 보낸다. number로 보내는 순간, 어느 한 언어에서 소리 없이 틀어질 수 있다.

## 4. 인코딩 — 한글이 깨지는 이유

JSON 텍스트의 표준 인코딩은 UTF-8이다(RFC 8259). 대부분의 도구가 UTF-8을 기본으로 쓰므로 평소엔 신경 쓸 일이 없다. 문제는 출력 옵션이다.

파이썬 `json.dumps`는 기본값으로 한글 같은 비ASCII 문자를 `김` 같은 이스케이프로 바꿔 버린다. 이게 틀린 건 아니다. 받는 쪽이 다시 파싱하면 "김"으로 정상 복원된다. 다만 사람이 파일을 열어 보면 못 읽는다. 그래서 위 3절 코드에서 `ensure_ascii=False`를 줬다. 파일을 사람이 직접 들여다볼 일이 있으면 이 옵션이 필요하다.

## 5. JSON의 친척들 — JSON5, JSONC, NDJSON

표준 JSON이 주석도 후행 콤마도 안 받다 보니, 불편함을 푼 변종들이 생겼다. 다만 변종은 표준이 아니라서, 시스템 간 교환용으로 쓰면 상대가 못 읽을 수 있다.

| 포맷 | 표준 JSON과 다른 점 | 주 용도 |
|---|---|---|
| JSONC | `//`, `/* */` 주석 허용. 후행 콤마는 파서에 따라 선택적 | VS Code 설정 파일(`settings.json`) 등 |
| JSON5 | 주석 + 후행 콤마 + 따옴표 없는 키 + 작은따옴표 문자열 + 16진수 | 사람이 손으로 쓰고 읽는 설정 파일 |
| NDJSON(JSON Lines) | 한 줄에 JSON 객체 하나씩. 전체를 배열로 감싸지 않음 | 로그, 스트리밍, 대용량 데이터를 한 줄씩 처리 |

NDJSON은 쓰임이 또렷하다. 거대한 데이터를 통째로 하나의 JSON 배열로 만들면 전부 메모리에 올려야 파싱이 된다. NDJSON은 한 줄이 곧 한 레코드라, `grep`이나 한 줄씩 읽기 같은 유닉스식 도구로 스트리밍 처리하기 좋다.

원칙은 단순하다. API로 교환하거나 정체 모를 도구가 읽을 데이터는 **엄격한 표준 JSON**으로 쓴다. 주석과 후행 콤마는 내가 손으로 관리하는 설정 파일에만 허용한다.

## 6. 스키마 검증 — 구조를 강제하기

JSON 문법이 맞다고 해서 내가 기대한 모양인 건 아니다. `age`가 숫자여야 하는데 문자열로 왔거나, 필수 키가 빠졌어도 문법상으론 올바른 JSON이다. 이 구조 검증을 표준화한 게 JSON Schema다(현재 draft 2020-12).

JSON Schema 자체도 JSON으로 적는다. "이 객체는 `name`과 `age`를 반드시 가지며, `age`는 정수다" 같은 규칙을 선언한다.

`schema.json`
```json
{
  "type": "object",
  "required": ["name", "age"],
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer", "minimum": 0 }
  }
}
```

이 스키마를 검증기에 통과시키면, 들어온 JSON이 규칙에 맞는지 자동으로 확인한다. API가 받은 입력을 거르거나, 설정 파일이 올바른지 점검할 때 쓴다. 손으로 `if`문을 줄줄이 쓰는 대신 규칙을 데이터로 선언해 둔다.

## 7. 보안 — 작은 입력이 서버를 죽인다

JSON을 받는 서버는 신뢰할 수 없는 입력을 다룬다는 사실을 잊으면 안 된다. 대표적 공격이 깊은 중첩(deeply nested)이다.

파서는 `[` 또는 `{`를 만날 때마다 호출 스택에 한 단계를 쌓는다. 중첩 깊이에 제한이 없으면, 공격자가 `[[[[...]]]]`처럼 수천 단계 중첩된 작은 JSON 한 조각을 보내 스택을 고갈시킬 수 있다. 그러면 `StackOverflowError`로 프로세스가 죽는다. 보내는 쪽은 몇 KB짜리 작은 페이로드인데 받는 쪽은 비대칭적으로 큰 피해를 입는 증폭 공격이다. 인증도 필요 없다.

이건 추상적 위험이 아니라 실제 취약점으로 반복 보고됐다. 자바의 Jackson Core(CVE-2025-52999)는 2.15.0 이전 버전이 깊은 중첩 JSON에 스택 오버플로로 무너졌고, .NET의 Newtonsoft.Json(CVE-2024-21907)도 같은 패턴이었다. 대응은 파서에 중첩 깊이 한도와 페이로드 크기 한도를 거는 것이다. 최신 파서들은 기본 한도를 갖추는 방향으로 바뀌었다.

## 8. 언제 JSON, 언제 다른 포맷

JSON이 늘 정답은 아니다. 세 후보를 나란히 두면 선택 기준이 분명해진다.

| 항목 | JSON | YAML | Protobuf |
|---|---|---|---|
| 사람이 읽기 | 쉬움 | 가장 쉬움(주석 가능) | 불가(바이너리) |
| 크기 | 보통(텍스트) | 보통(텍스트) | 작음(JSON의 약 1/3~1/5) |
| 파싱 속도 | 보통 | 느림 | 빠름(JSON의 약 3~10배) |
| 스키마 강제 | 선택(JSON Schema) | 선택 | 필수(`.proto` 파일) |
| 주로 쓰는 곳 | 웹 API, 설정 | 설정 파일 | 고성능 내부 통신 |

Protobuf와 JSON의 크기·속도 차이는 측정 환경마다 다르지만, 대략 Protobuf가 페이로드는 3~5배 작고 파싱은 3~10배 빠르다고 보고된다. 대신 바이너리라 로그에 찍으면 사람이 못 읽는다.

정리하면 이렇게 고른다.

- **웹 API 응답, 사람이 가끔 들여다볼 데이터** → JSON. 가장 흔하고 도구가 풍부하다.
- **사람이 손으로 자주 편집하는 설정 파일** → YAML 또는 JSON5(주석이 필요할 때).
- **서비스 간 대량·고빈도 통신, 속도와 크기가 중요** → Protobuf 같은 바이너리.
- **행 단위 표 형태의 단순 데이터** → CSV가 더 작고 빠르다.

## 9. 한 줄 마무리

> JSON = 키-값을 텍스트로 적는, 언어에 묶이지 않은 데이터 포맷. 문법은 여섯 자료형으로 끝나지만, 실제로는 직렬화·숫자 정밀도·인코딩·스키마 검증·중첩 공격이 줄줄이 따라온다.

쉬운 입구로 들어와 이 다섯 가지 실제 복잡함까지 알면, "JSON으로 주고받는다"는 한 문장을 한 단계가 아니라 두세 단계 깊게 읽을 수 있다. 특히 숫자 ID는 문자열로 보낸다는 한 줄만 기억해도, 언젠가 한 번은 새벽에 디버깅할 일을 면한다.

## 출처

- RFC 8259, The JavaScript Object Notation (JSON) Data Interchange Format: <https://www.rfc-editor.org/rfc/rfc8259>
- ECMA-404, The JSON Data Interchange Syntax: <https://ecma-international.org/publications-and-standards/standards/ecma-404/>
- MDN, Number.MAX_SAFE_INTEGER: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER>
- MDN, BigInt: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt>
- JSON Schema Draft 2020-12: <https://json-schema.org/draft/2020-12>
- NDJSON Specification: <https://jsonltools.com/ndjson-format-specification>
- JSONC Specification: <https://jsonc.org/>
- JSON5: <https://json5.org/>
- CVE-2025-52999, Jackson Core DoS via deeply nested JSON: <https://www.herodevs.com/blog-posts/cve-2025-52999-denial-of-service-via-stack-overflow-in-jackson-core>
- CVE-2024-21907, Newtonsoft.Json DoS: <https://www.sentinelone.com/vulnerability-database/cve-2024-21907/>
- Protobuf vs JSON 성능 비교: <https://www.gravitee.io/blog/protobuf-vs-json>
