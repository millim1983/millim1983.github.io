# 검토 대기 큐

이 문서는 검토를 기다리는 초안을 한눈에 보기 위한 목록이다.
각 초안은 `_drafts/light/` 또는 `_drafts/deep/`에 위치하며, front matter의 `status` 값으로 단계가 표시된다.

| status | 의미 |
|---|---|
| `draft`  | Claude 초안 작성 완료. 검토 대기 중. |
| `ready`  | 사용자 검토 완료. 다음 cron에 자동 발행됨. |
| `published` | 발행 완료 후 _posts/로 이동된 상태(자동 갱신). |

## 검토 절차

1. `_drafts/light/` 또는 `_drafts/deep/`에서 글을 연다.
2. 본문을 읽고, 필요하면 직접 수정한다(또는 Claude에게 수정 요청).
3. 발행해도 좋다 판단되면 front matter 최상단의 `status: draft`를 `status: ready`로 한 글자만 바꾼다.
4. git에 commit & push 한다.
5. 다음 cron 도래 시(`publish-light`: 매일 09:00, 17:00 / `publish-deep`: 매주 월 09:00) GitHub Actions가 자동으로 `_posts/`로 옮기고 사이트에 발행한다.

> 즉시 발행하고 싶으면 GitHub Actions 페이지에서 해당 워크플로 → "Run workflow" 수동 실행.

## 현재 대기 중인 초안

| 풀 | 파일 | 카테고리 | 제목 | status |
|---|---|---|---|---|
| light | `a-year-with-claude-code.md` | thoughts | 1년 동안 Claude Code를 쓴 사람으로서 | **ready** |
| deep | `01-three-layers-of-data-source.md` | building-with-ai | 데이터 출처의 세 층위 — HTML·AJAX·공식 OpenAPI의 진짜 차이 | draft |
