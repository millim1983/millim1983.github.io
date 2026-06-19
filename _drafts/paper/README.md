# `_drafts/paper/` — 논문 리뷰 큐

매일 12:00 KST에 `publish-paper.yml`이 이 폴더에서 `status: ready`인 글 1편을 선정해 `_posts/`로 옮긴다.

## 작성 규칙

- 슬러그: `paper-<YYYYMMDD>-<short-title>.md`
- frontmatter `categories: [paper-review]` (또는 잠정 카테고리 확정 전이면 `[building-with-ai]`)
- `status: draft` 로 시작, 사용자 검토 후 `status: ready` 로 전환
- 분량 1500~3500자
- 작성 6축: 모델 / 파인튜닝 / 학습 / 데이터 / 성능평가 / 실무 활용
- 도식 발췌(논문 Figure N) 직접 삽입, 출처 캡션 명기
- 원본 PDF·발췌 이미지는 `_meta/references/papers/<arXiv-id>/` 에 보관

운영 규칙 상세: `_meta/IDEAS.md` 트랙 D 섹션, 메모리 [[feedback-blog-idea-queue]].
