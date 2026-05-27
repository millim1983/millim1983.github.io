# 블로그 운영 매뉴얼 — 사용자(검토자)용

이 블로그는 Claude가 초안을 쓰고, 사용자가 검토하고, GitHub Actions가 정해진 시각에 자동 발행하도록 설계되어 있다. 이 문서는 **사용자 입장에서 무엇을 언제 하는가**만 정리한다.

**인프라 요약**: Jekyll + Chirpy 테마 + GitHub Pages(Source: GitHub Actions). 새 글 push → Chirpy `Build and Deploy` 워크플로 자동 빌드 → 사이트 반영. 자동 발행 cron은 `_drafts/<풀>/`의 `status: ready` 글을 정해진 시각에 `_posts/`로 옮긴다.

---

## 1. 평소 흐름 (한 글의 생애)

```
① Claude가 초안을 _drafts/light/ 또는 _drafts/deep/에 작성
        ↓
② 사용자가 글을 열어 읽는다
        ↓
③ OK면 status: draft → status: ready 로 한 글자 변경
   수정 필요하면 직접 고치거나 Claude에게 요청
        ↓
④ git commit & push
        ↓
⑤ 다음 cron 시각에 GitHub Actions가 자동으로:
   - 파일을 _posts/YYYY-MM-DD-슬러그.md 로 이동
   - 자기 자신을 commit & push
        ↓
⑥ GitHub Pages가 자동 빌드 → 사이트에 발행 완료
```

사용자가 직접 하는 일은 **②③④** 세 단계뿐.

---

## 2. 검토 단계별 가이드

### 2-1. 글 위치 확인

```
_drafts/
├── light/        ← 가벼운 글 (매일 2회 발행 풀)
└── deep/         ← 깊이 있는 글 (주 1회 월요일 발행 풀)
```

검토 대기 목록은 `REVIEW.md`에서도 한눈에 본다.

### 2-2. 글 읽기

에디터(VS Code, 메모장 등)로 해당 `.md` 파일을 연다.
front matter (맨 위 `---` 블록) 안의 다음 항목을 확인:

```yaml
title: "..."          # 제목 (괜찮은가)
subtitle: "..."       # 부제
categories: [...]     # 분류
tags: [...]           # 태그
toc: true             # 목차 표시 여부
status: draft         # ← 검토 후 ready로 바꿀 자리
```

본문 검토 시 다음 7가지를 본다 (`PERSONA.md` § 8과 동일).

- [ ] 평어체(-다 종결)로 일관되어 있는가
- [ ] "나" / "Claude" / "AI" 호칭이 일관되는가 ("필자" 잔재 없는가)
- [ ] 직업·소속·도메인 식별 단서가 노출되지 않는가
- [ ] AI 수행 부분과 사람 판단 부분이 명시 구분되었는가
- [ ] 비개발자가 따라갈 수 있는 어휘·예시인가
- [ ] "사람에게 남는 일"이 결론에 분명히 들어갔는가
- [ ] 은어·구어·추측형 표현이 남아있지 않은가

### 2-3. 수정이 필요한 경우

**가벼운 수정**: 직접 파일을 고친다. 저장만 하면 끝.

**구조적 수정 / 톤 재조정**: Claude에게 메시지로 요청.

```
예시 요청:
"_drafts/deep/series-intro-...md 의 3절을 더 구체적인 사례 중심으로 다시 써줘.
지금은 추상적이라 와닿지 않는다."
```

### 2-4. 승인 (발행 예약)

front matter의 한 줄만 수정한다.

```yaml
# 변경 전
status: draft

# 변경 후
status: ready
```

이게 끝. 다음 cron 시각에 자동 발행된다.

### 2-5. git에 반영

```powershell
cd C:\Users\kbj\projects\blog
git add .
git commit -m "review: <글 슬러그>"
git push
```

또는 사용 중인 git GUI 도구(GitHub Desktop, SourceTree 등)로 commit & push.

---

## 3. 발행 시각

| 풀 | 발행 시각 (KST) | 대상 |
|---|---|---|
| `light` | 매일 09:00, 17:00 | `_drafts/light/`에서 `status: ready` 1편 |
| `deep`  | 매주 월요일 09:00 | `_drafts/deep/`에서 `status: ready` 1편 |

발행할 글이 없으면 cron은 조용히 종료된다(에러 아님).

여러 글이 `ready` 상태이면 **mtime 가장 오래된 것부터** 1편씩 발행된다.

---

## 4. 즉시 발행하고 싶을 때

cron 시각을 기다리지 않고 지금 바로 발행하려면 두 가지 방법:

### 방법 A — GitHub Actions 수동 실행

1. GitHub 저장소 페이지 → **Actions** 탭
2. 좌측에서 `publish-light` 또는 `publish-deep` 선택
3. 우측 상단 **"Run workflow"** 버튼 → **Run workflow** 클릭

수 초 안에 발행된다.

### 방법 B — 로컬에서 수동 발행

```powershell
cd C:\Users\kbj\projects\blog
python scripts/publish_one.py deep      # 또는 light
git add .
git commit -m "manual publish"
git push
```

특정 글을 강제로(status 무관) 발행하려면:

```powershell
python scripts/publish_one.py --slug 슬러그명
```

---

## 5. 사이트 미리보기 (선택)

Ruby와 Bundler가 설치돼 있다면:

```powershell
cd C:\Users\kbj\projects\blog
bundle install                          # 최초 1회
bundle exec jekyll serve --drafts       # _drafts/도 보임
```

브라우저에서 http://localhost:4000 접속.

Ruby가 없으면 미리보기 단계는 건너뛰고 push만 해도 GitHub Pages가 처리한다.

---

## 6. 발행 후 확인

1. GitHub 저장소의 **Actions** 탭에서 가장 최근 워크플로 실행이 ✅인지 확인.
2. 저장소의 `_posts/` 폴더에 새 글이 생겼는지 확인.
3. GitHub Pages URL(`https://<USERNAME>.github.io/<REPO>/`)에 접속해 글이 보이는지 확인.

GitHub Pages 빌드는 push 후 약 1~2분 소요된다.

---

## 7. 자주 묻는 운영 질문

| 상황 | 처리 |
|---|---|
| 검토 중에 발행해서는 안 되는 사실관계 오류를 발견 | front matter status를 `draft`로 되돌리고 commit. cron이 가져가지 않는다. |
| 이미 발행된 글을 수정하고 싶다 | `_posts/<파일명>.md` 직접 편집 → commit & push. 즉시 재빌드된다. |
| 이미 발행된 글을 비공개로 돌리고 싶다 | 해당 파일을 `_drafts/`로 다시 옮기거나, front matter에 `published: false` 추가 후 commit. |
| 글의 발행 날짜를 미루고 싶다 | front matter `date:`를 미래 날짜로 수정. GitHub Pages는 미래 날짜 글을 빌드 결과에서 숨긴다(추가 cron 트리거 시 노출). |
| cron이 동작하지 않는다 | Settings → Actions → General → Workflow permissions가 **Read and write permissions**인지 확인. 또는 저장소가 60일 이상 비활성이면 cron이 자동 중단됨(commit 한 번이면 재개). |
| 같은 글을 두 번 발행하고 싶다 | `_drafts/`에 같은 슬러그로 다시 만들거나, `_posts/`의 파일을 복제 후 날짜·슬러그 변경. |

---

## 8. 매일·매주 점검 권장 사항

| 주기 | 확인 |
|---|---|
| 매일 | `REVIEW.md`로 검토 대기 큐 확인. light 풀이 비어 있으면 새 초안 요청. |
| 매주 월요일 후 | 발행 결과 확인. Actions 탭에서 ✅. |
| 월 1회 | `PERSONA.md` 원칙이 여전히 유효한지 점검. 새 톤/방향이 정해지면 갱신. |

---

## 9. 한 줄 요약

> **검토 → `status: ready`로 한 글자 수정 → git push** — 이게 전부.
> 나머지는 GitHub Actions가 알아서 처리한다.
