# AI 페어 개발 노트 (Jekyll 블로그)

코딩 에이전트(Claude Code)와 함께 실무 도구를 만든 기록.
GitHub Pages + GitHub Actions cron 기반 자동 발행.

## 폴더 구조

```
blog/
├── _config.yml            # Jekyll 설정
├── _posts/                # 발행된 글 (YYYY-MM-DD-슬러그.md)
├── _drafts/
│   ├── light/             # 가벼운 글 풀 (매일 2회 자동 발행)
│   └── deep/              # 깊이 있는 글 풀 (주 1회 월요일 자동 발행)
├── scripts/
│   └── publish_one.py     # ready 글 1편을 _posts/로 옮기는 스크립트
├── .github/workflows/
│   ├── publish-light.yml  # cron: 매일 09:00, 17:00 KST
│   └── publish-deep.yml   # cron: 매주 월요일 09:00 KST
├── assets/images/
├── index.md               # 사이트 홈
├── Gemfile                # 로컬 미리보기용 (선택)
├── PERSONA.md             # ★ 글쓰기 원칙 — 새 글 쓸 때마다 확인
├── REVIEW.md              # 검토 대기 큐
└── README.md
```

## 검토·발행 절차

```
1. Claude가 _drafts/light/ 또는 _drafts/deep/에 초안 작성 (status: draft)
2. 사용자가 검토 → 수정 요청 또는 OK
3. OK면 front matter의 status: draft → status: ready (한 글자만)
4. git commit & push
5. 다음 cron 시각에 GitHub Actions가:
   - status: ready 중 가장 오래된 1편 선택
   - 파일명 앞에 오늘 날짜(YYYY-MM-DD) 붙여 _posts/로 이동
   - 자기 자신을 commit & push
6. GitHub Pages가 자동 빌드 → 발행 완료
```

**즉시 발행하려면**: GitHub의 Actions 탭 → 해당 워크플로 → "Run workflow" 클릭.

## 발행 주기

| 풀 | 발행 빈도 | cron (UTC) | KST |
|---|---|---|---|
| light | 매일 2회 | `0 0,8 * * *` | 09:00, 17:00 |
| deep  | 주 1회   | `0 0 * * 1`   | 월요일 09:00 |

## 새 글 쓰기

1. `PERSONA.md`를 한 번 훑는다.
2. `_drafts/light/슬러그.md` 또는 `_drafts/deep/슬러그.md` 작성.
3. front matter:

   ```yaml
   ---
   layout: post
   title: "글 제목"
   subtitle: "부제 (선택)"
   categories: [분류]
   tags: [태그1, 태그2]
   toc: true
   status: draft     # 검토 후 ready로 변경
   ---
   ```

   (`date` 필드는 발행 스크립트가 자동 삽입한다.)

4. 본문은 평어체. "나"·"Claude"·"AI" 호칭을 일관 사용.

## 로컬 미리보기 (선택)

```bash
bundle install              # 최초 1회
bundle exec jekyll serve --drafts    # _drafts/도 보기
# http://localhost:4000
```

Ruby 미설치 환경이라면 미리보기 없이 push만으로도 무방.

## 최초 발행 설정 (1회만)

1. GitHub에서 public 저장소 생성 (예: `blog`).
2. 로컬에서:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<USERNAME>/<REPO>.git
   git push -u origin main
   ```

3. GitHub 저장소 Settings → Pages → Source = "Deploy from a branch / main / / (root)".
4. Settings → Actions → General → "Workflow permissions" = **Read and write permissions** 활성화. (자동 발행 cron이 push할 권한 필요)

이후 검토·발행은 자동.
