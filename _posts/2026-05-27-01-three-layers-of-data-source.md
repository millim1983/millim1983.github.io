---
layout: post
title: "데이터 출처의 세 층위 — HTML·AJAX·공식 OpenAPI의 진짜 차이"
subtitle: "AI와 개발하기 시리즈 1편"
categories: [building-with-ai]
tags: [claude-code, crawling, openapi, ajax, html-scraping, python]
toc: true
status: published
date: 2026-05-27 16:37:44 +09:00
---

## 0. 정부 사업 공고 서비스는 많지만 ... 

정부사업공고 모니터링 도구는 내 회사생활의 거의 숙원사업과 같은 존재였다. 
업무상 수많은 정부사이트, 공고사이트들을 돌아다니며 원하는 키워드, 관심사업공고 들을 찾고,
확인한 공고를 내가 보고 지나가는게 아니라 활요할수있게 만들려면 시간을 너무 많이 쏟아야 했다. 

빅데이터 분석을 배웠지만 딱히 사용하기가 어려웠다. 왜냐면 ? 빅데이터가 없어서..  


> **데이터는 어떻게 가져오지?**

이를 해결하기 위해 내가 만들고 있던 도구는 두 종류였다. 
하나는 정부 R&D 사업공고를 매일 자동으로 수집하는 모니터
다른 하나는 나라장터 입찰·낙찰 데이터를 누적해 분석하는 시스템. 



둘 다 "공공기관 사이트에서 데이터를 가져온다"는 점은 같지만,
데이터를 내주는 방식은 사이트마다 다 달랐다.

이 차이를 처음에는 단순한 기술 디테일로 봤다. 그런데 실제로 도구를 만들어 보면 이 차이가 **시스템의 안정성·유지보수 비용·윤리적 한도**까지 결정한다는 것을 알게 됐다. 도구가 코드를 다 짜 주는 시대에도, **이 데이터가 어느 층위에 있는가**를 판단하는 일은 사용자가 한다.

이 글은 그 세 층위를 정리한다.

---

## 1. 세 층위의 정의

데이터 출처는 사이트가 "사용자에게 데이터를 어떻게 내주느냐"에 따라 세 층으로 나뉜다.

### 1-1. HTML 층 — 화면 그 자체를 파싱

가장 흔한 방식. 브라우저로 사이트에 접속해 보이는 HTML을 그대로 받아 파싱한다. Python에서는 `requests` + `BeautifulSoup` 조합이 표준.

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://example.gov.kr/list?page=1")
soup = BeautifulSoup(r.text, "lxml")
for row in soup.select("table.list-table tr"):
    title = row.select_one("td.title").get_text(strip=True)
    print(title)
```

배우기 쉽고 어떤 사이트에서도 시작할 수 있다. 그런데 **사이트가 HTML 구조를 한 번만 바꿔도 코드 전체가 깨진다.** 클래스 이름 한 글자 추가, 테이블 안에 또 테이블이 들어가는 리뉴얼, 클라이언트 사이드 렌더링으로의 전환 — 모두 코드 손질을 요구한다.

### 1-2. AJAX 층 — 화면 뒤편의 데이터 응답을 직접 호출

요즘 정부·공공기관 사이트 대부분은 첫 HTML을 받은 뒤 자바스크립트가 추가로 데이터를 비동기로 받아 화면을 채운다. 그 데이터는 보통 JSON(또는 XML)으로 오고, 화면에 표시되는 양보다 훨씬 풍부하다. 브라우저 개발자 도구의 **Network → XHR** 탭에서 캡처할 수 있다.

캡처한 요청을 그대로 Python으로 재현하면 HTML 파싱을 우회하고 데이터 자체에 직접 닿는다.

다음은 IRIS(범부처 통합연구지원시스템)의 사업공고 목록을 가져오는 실제 코드다.

```python
# sites/iris/crawler.py:92-107
def _fetch_list_page(session, ancm_prg, page, per_page=100):
    r = session.post(
        LIST_API_URL,                                    # /contents/retrieveBsnsAncmBtinSituList.do
        data={
            "ancmPrg": ancm_prg,                         # ancmIng(접수중) / ancmPre(접수예정)
            "pageIndex": str(page),
            "recordCountPerPage": str(per_page),
        },
        headers={
            "X-Requested-With": "XMLHttpRequest",
            "Referer": LIST_VIEW_URL,
        },
        timeout=20,
    )
    r.raise_for_status()
    return r.json()
```

응답은 한 페이지에 100건씩 JSON 배열로 돌아온다. HTML을 파싱했다면 페이지의 표 구조를 따라가야 했을 정보를, JSON 키 한 줄로 바로 가져온다.

```python
# sites/iris/crawler.py:110-133 — JSON 응답 한 행을 한국어 키로 정규화
def _row_from_api(item, ancm_prg):
    return {
        "site": "iris",
        "item_id": item.get("ancmId", ""),
        "공고번호": item.get("ancmNo", ""),
        "제목": item.get("ancmTl", ""),
        "전문기관": item.get("sorgnNm", ""),
        "소관부처": item.get("blngGovdSeNm", ""),
        "접수시작": _norm_date(item.get("rcveStrDe", "")),
        "마감일":   _norm_date(item.get("rcveEndDe", "")),
        "D-day":   f"D-{item.get('dDay')}" if item.get("dDay") is not None else "",
        "등록일":   _norm_date(item.get("ancmDe", "")),
        ...
    }
```

HTML 파싱 대비 두 가지 이득이 분명하다.

1. **안정성**: 사이트 디자인 개편이 일어나도 AJAX 엔드포인트는 그대로인 경우가 많다.
2. **정보 밀도**: HTML이 화면에 보여주는 칸 수보다 많은 필드가 응답에 포함되어 있다. (예: `dDay`, `blngGovdSeNm`, 카테고리 코드 등.)

다만 한 가지 결정적 단점이 있다. **이 엔드포인트는 공식 API가 아니다.** 사이트 운영자가 자기 화면에 데이터를 채우려고 만든 내부 통로일 뿐, 외부에서 호출하라고 만든 게 아니다. 사용해도 되는지, 어느 빈도까지 호출해도 되는지는 사이트 약관·`robots.txt`·일반적 인터넷 윤리로 사용자가 직접 판단해야 한다.

### 1-3. 공식 OpenAPI 층 — 데이터 제공자가 보장하는 인터페이스

데이터 제공 측이 공식 문서·인증키 발급 절차·SLA(서비스 약속)와 함께 제공하는 API. 한국 공공 데이터의 경우 [공공데이터포털(data.go.kr)](https://www.data.go.kr/)이 허브.

조달청은 나라장터 데이터를 **5개 OpenAPI**로 공식 공개한다.

| 도메인 | 엔드포인트 (base) |
|---|---|
| 입찰공고 | `https://apis.data.go.kr/1230000/ad/BidPublicInfoService` |
| 낙찰/개찰 | `https://apis.data.go.kr/1230000/as/ScsbidInfoService` |
| 발주계획 | `https://apis.data.go.kr/1230000/ao/OrderPlanSttusService` |
| 사전규격 | `https://apis.data.go.kr/1230000/ao/HrcspSsstndrdInfoService` |
| 계약정보 | `https://apis.data.go.kr/1230000/ao/CntrctInfoService` |

호출은 인증키 + 페이징 파라미터 + 기간 파라미터로 단순하다.

```python
# 나라장터 OpenAPI 호출 예 (개찰 결과)
params = {
    "serviceKey":  API_KEY_DECODING,
    "pageNo":      str(page),
    "numOfRows":   "100",
    "inqryDiv":    "1",                    # 1=조회기간 기준
    "inqryBgnDt":  "202504250000",
    "inqryEndDt":  "202505250000",
    "type":        "json",
}
r = requests.get(BASE + "/getOpengResultListInfoServc", params=params, timeout=20)
items = r.json()["response"]["body"]["items"]
```

HTML·AJAX 대비 OpenAPI의 강점은 명확하다.

- **공식 보장**: 응답 스키마가 문서화되어 있고, 사이트 개편과 무관하게 유지된다.
- **윤리적 명료성**: 인증키 발급 절차 자체가 "쓰셔도 좋습니다"의 명시적 동의다.
- **장기 데이터**: 화면에서 보여주는 최근 N개월 너머의 과거 데이터도 페이지네이션으로 접근 가능.

대신 두 가지 제약이 있다.

- **인증키와 한도**: 일 단위 트래픽 한도(나라장터는 운영용 키 기준 약 1만 콜/일)가 있고, 초과 시 HTTP 429를 받는다. 청크 단위 SKIP과 다음 날 재개를 미리 설계해 둬야 한다.
- **가용 데이터 범위**: 화면에는 있는데 OpenAPI에는 없는 필드가 존재할 수 있다. 데이터 일부를 위해 다시 HTML/AJAX 층으로 돌아가야 하는 경우가 생긴다.

---

## 2. 세 층위의 트레이드오프

세 층위를 한 표로 정리하면 다음과 같다.

| | HTML 스크래핑 | AJAX 직접 호출 | 공식 OpenAPI |
|---|---|---|---|
| **진입 난이도** | 가장 쉬움 | 중간 (Network 탭 캡처 필요) | 인증키 발급 절차 |
| **안정성** | 사이트 개편에 가장 약함 | AJAX 엔드포인트가 바뀌면 깨짐 | 가장 안정 (공식 스키마) |
| **정보 밀도** | 화면에 보이는 만큼 | 화면보다 풍부 | 문서가 보장하는 범위 |
| **장기 데이터** | 화면 페이지네이션 한도 | 보통 화면과 동일 | 보장 (과거치 조회) |
| **윤리·합법성** | 사이트 약관·`robots.txt` 판단 | 비공식. 사용자 판단 필요 | 명시적 동의(인증키) |
| **호출 한도** | 자율 (서버 부하 자율 관리) | 자율 (서버 부하 자율 관리) | 일 단위 명시 한도 |
| **유지보수 비용** | 사이트 개편마다 손질 | 가끔 | 가장 낮음 |

이 표를 외울 필요는 없다. **새 사이트를 보면 가장 먼저 어느 층에 데이터가 있는지부터 확인한다**는 한 가지 습관만 있으면 된다. 확인 순서는 거꾸로다.

1. 공공데이터포털에서 공식 OpenAPI가 있는지 검색.
2. 없다면 브라우저 Network 탭에서 AJAX 응답을 확인.
3. 그것도 없다면 HTML 파싱.

---

## 3. 사용자가 자기 자리에서 한 일

이 시리즈의 다른 회차와 마찬가지로, 이 결정에서도 도구(Claude Code)가 한 일과 사용자가 한 일의 구분이 분명하다.

### 3-1. Claude Code가 자동으로 해낸 일

- 캡처한 cURL 요청 한 줄을 받아 `requests.post(...)` 호출 코드로 변환.
- JSON 응답의 키를 한국어로 매핑하는 정규화 함수 작성(`_row_from_api`).
- 페이지네이션 루프와 early-stop 로직 구현.
- OpenAPI 클라이언트의 인증키 보호(`.env`), 일일 한도 도달 시 청크 단위 SKIP, 다음 날 재개 로직.
- 한국어 인코딩 변환(CP949 ↔ UTF-8), 콘솔 출력 reconfigure.

키보드 노동 측면에서 한 사람이 단독으로 처음부터 다 짜기에는 부담스러운 분량이다. 도구 이후 이 부분의 비용은 거의 0에 수렴했다.

### 3-2. 사용자가 결정한 일

- **어느 층위가 적합한지 판단**: IRIS는 AJAX 비공식 호출이 합리적이라고 판단(공식 API 없음, 화면 뒤편의 JSON이 풍부). 나라장터는 공식 OpenAPI를 우선 사용한다고 결정(공식 인증키 제공, 5년치 누적 조회 보장).
- **JSON이 곧 "공식"을 의미하지 않는다는 점을 분리**: 응답이 JSON으로 온다고 해서 사이트가 외부 사용을 허락한 게 아니라는 사실을 코드 주석·문서에 명시.
- **비공식 호출의 한도 결정**: 일 1회 실행, 페이지당 0.2~0.25초 sleep, 첨부 다운로드는 신규분만, 같은 항목 재호출 금지(state 기반 스킵). "일반 사용자가 화면을 보는 정도의 부하"를 상한선으로.
- **공식 API의 일일 한도 대응 설계**: 30일 청크로 백필을 분할하고, HTTP 429를 받으면 그 청크를 in_progress로 남겨 두고 종료. 다음 날 같은 명령을 다시 돌리면 done 청크는 SKIP되고 미완료부터 재개.
- **장애 시 격리**: 어댑터를 사이트별 폴더(`sites/<name>/`)로 분리. 한 사이트의 AJAX가 사이트 개편으로 깨져도 나머지 사이트는 계속 돈다.

코드 작성량으로는 1 %도 안 되는 결정들이다. 그런데 시스템이 1년을 깨지지 않고 굴러가는 이유의 거의 전부가 여기에 있다.

---

## 4. 이번 단계에서 사용자에게 새로 요구되는 능력

세 층위의 차이를 알아두는 것 자체는 그리 어려운 학습이 아니다. 그러나 **새 사이트를 마주쳤을 때 어느 층위로 갈지 판단하는 능력**, 그리고 **선택한 층위에 따라오는 책임(윤리·한도·장애 격리)을 같이 설계하는 능력**은 도구가 대신 해 주지 않는다.

엑셀이 함수 계산을 자동화한 뒤로 "어떤 함수를 어디에 쓸지" 정하는 것이 사용자의 일이 됐다. Claude Code가 호출 코드를 자동화한 지금, **어떤 데이터를 어느 층위에서 가져올지** 정하는 것이 사용자의 일이 됐다. 정확히 같은 종류의 자리 이동이다.

다음 회차에서는 이렇게 결정된 호출이 실제로 한 번에 성공하기까지 필요한 **세션·헤더·인증키·재시도** 같은 작은 조건들을 다룬다.

---

> **AI 기여도**: 본 글이 분석하는 시스템 코드는 Claude Code가 약 90 %를 작성했다. 나는 어느 사이트가 어느 층위에 적합한지 판단하고, 비공식 호출의 한도와 공식 API의 청크 설계를 결정했으며, 표본 검증과 어댑터 격리 구조를 명시했다.
>
> **글 자체의 작성**: 초안 1회 / 직접 교정 0회.
