# 참고자료 (사용자 업로드용)

이 폴더는 사용자가 **글감별 참고자료**(PDF·이미지·발췌·링크 모음·원문 등)를 올려두는 자리이다.

Jekyll은 `_` 로 시작하는 폴더를 빌드에서 자동 제외하므로, 여기 올라간 자료는 **사이트에 노출되지 않는다**. 안심하고 원문 그대로 두어도 된다.

---

## 폴더 명명 규칙

```
_meta/references/<카테고리-슬러그>-<순번>-<주제-슬러그>/
```

예시:
- `ax-01-manufacturing-multi-agent/` — AX 첫 글, 제조 멀티 에이전트
- `ax-02-physical-training-agent/` — AX 두 번째 글, 체력단련 AI 에이전트
- `series-08-double-click-ux/` — AI와 개발하기 시리즈 8편 추가 자료
- `coding-education/scratch-maze/` — 정보/코딩 교육의 Scratch 미로 게임 편

순번 없이도 OK. 한 글에 자료 폴더 하나가 원칙.

---

## 한 폴더 안에 넣을 수 있는 것

- 원문 PDF·DOCX·이미지·스크린샷
- 인터넷 발췌(`*.md`·`*.txt`)·기사 캡처
- 사용자가 직접 적은 메모(`notes.md` 권장)
- 관련 URL 목록(`links.md` 권장)
- 분석 대상 코드 스니펫(`code/` 하위)

자유 형식. 정리 안 돼 있어도 OK — Claude가 읽고 필요한 부분만 본문에 인용한다.

---

## 사용 흐름

```
사용자가 자료 업로드
   ↓
"이 자료로 <글 주제> 본문 한 편 써줘" 라고 Claude에게 요청
   ↓
Claude가 _meta/references/<폴더> 읽음 → 본문 작성 → _drafts/<풀>/<슬러그>.md
   ↓
사용자가 검토 → status: ready → push → 자동 발행
```

---

## 현재 준비된 폴더

| 폴더 | 어느 글용 | 상태 |
|---|---|---|
| `ax-01-manufacturing-multi-agent/` | AX 카테고리 첫 글 — 제조 분야 멀티 에이전트 구축 | **사용자 자료 업로드 대기 중** |
| `ax-02-physical-training-agent/` | AX 카테고리 두 번째 글 — 체력단련 AI 에이전트 | 제안서 완성 후 진행 |
| `series-08-double-click-ux/` | AI와 개발하기 시리즈 8편 — 더블클릭 UX | 자료 임의 추가 가능 (없어도 작성 가능) |
| `ops-log/` | 운영 일지 — 일상 운영 기록 | 자료 필요시 |
| `coding-education/` | 정보/코딩 교육 — 단계별 자료 모음 | 필요시 하위 폴더 추가 |

---

## 자료 업로드 후 Claude에게 요청 예

> "`_meta/references/ax-01-manufacturing-multi-agent/`에 자료 올렸어. 이걸로 AX 카테고리 첫 글 본문 한 편 써줘."

또는 단순히

> "AX 첫 글 자료 올렸어. 글 써줘."
