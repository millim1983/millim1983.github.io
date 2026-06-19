# `_drafts/auto/` — 자동 생성 큐

`publish-auto.yml`이 매일 06:00 KST에 Claude API를 호출해 IDEAS.md 큐에서 다음 글감을 골라 본문을 생성하고 이 폴더에 `status: ready`로 떨어뜨린다.

이후 흐름:
- 09:00 / 13:00 / 17:00 KST `publish-light.yml`이 `_drafts/light/` 풀을 먼저 보고, 비어 있으면 이 폴더에서 가져간다.

**경고**: 자동 생성된 글은 사용자 검토 없이 사이트에 올라간다. 품질·정확성 문제가 그대로 노출될 수 있다. 사용 전 인지하고, 결과가 마음에 안 들면 워크플로(`publish-auto.yml`)를 비활성화하거나 cron을 끈다.

## 사전 조건

- GitHub 저장소 Settings → Secrets → `ANTHROPIC_API_KEY` 등록 필요. 사용자가 직접 설정해야 함.

## 임시 비활성화 방법

`.github/workflows/publish-auto.yml` 의 `on:.schedule:` 블록을 주석 처리하거나, GitHub Actions 탭에서 워크플로를 disable.
