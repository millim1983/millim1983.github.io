---
layout: post
title: "멀티 에이전트가 기본값이 됐다 — 2026년 5월의 코딩 도구 풍경"
subtitle: "도구가 도구를 다루기 시작한 시점"
categories: [thoughts]
tags: [claude-code, cursor, antigravity, copilot, multi-agent, trends]
toc: false
status: published
date: 2026-06-20 05:48:38 +09:00
---

## 0. 1년 전과 지금의 차이

1년 전(2025년 5월)에 "AI 코딩 에이전트"라고 부르던 건 대부분 단일 에이전트였다. 한 대화창 안에서 한 가지 일을 시키는 모양. 그 모양을 둘러싼 도구 7개 — Claude Code·Cursor·GitHub Copilot·Codex·Windsurf·Kiro·Google Antigravity — 가 1년 만에 같은 한 가지 방향으로 움직였다.

> **멀티 에이전트가 default가 됐다.**

2026년 5월에 정리하는 흐름이다. 한 글로 짧게 적어 둔다.

## 1. 같은 한 달에 일어난 일

- **Antigravity 2.0** (5월 19일, Google) — dynamic subagents·scheduled background tasks·SDK·Gemini 3.5 Flash 통합. 본격적인 멀티 에이전트 thesis 강화.
- **Cursor 3 + Composer 2.5** — "Build in Parallel" 기능으로 여러 에이전트가 동시에 다중 파일을 편집.
- **Kiro Pro** — parallel Spec 실행. 한 사람이 동시에 여러 사양을 진행.
- **OpenAI Codex 데스크톱** — 멀티 에이전트가 여러 프로젝트를 가로질러 돈다.
- **Anthropic Project Glasswing** — Claude Mythos Preview 미공개 모델을 통한 대규모 코드베이스 취약점 자동 수정. 사실상 보안 전용 에이전트의 멀티 작업.

도구마다 표현은 다르지만 공통의 모양이 있다 — **한 사람이 직접 마주하는 에이전트 1개 뒤에, 그 에이전트가 부리는 subagent N개가 병렬로 일한다.** 사용자가 손을 떼고 있어도 백그라운드에서 일이 진행된다.

## 2. 왜 같은 시기에 같은 방향이 됐나

세 가지가 동시에 익은 시기다.

**컨텍스트 윈도우의 평준화**: 100만 토큰급이 표준이 됐다. 한 에이전트가 큰 작업 단위(여러 파일·여러 단계)를 다 들고 있을 수 있다는 전제가 깔렸다.

**도구 호출(tool use)의 표준화**: MCP(Model Context Protocol) 같은 인터페이스가 정착했다. 에이전트가 외부 시스템·다른 에이전트를 일관된 방식으로 호출할 수 있다.

**비용 곡선의 분기**: 프런티어 모델은 비싸지만, 작은 모델(Haiku 4.5·Gemini 3.5 Flash 등)이 충분히 똑똑해졌다. **메인 에이전트는 큰 모델, subagent는 작은 모델**의 분업이 경제적으로 성립한다.

이 셋이 동시에 익자, 각 도구가 같은 방향으로 움직였다.

## 3. 사용자에게 의미하는 것

사용자 입장에서 1년 전과 가장 크게 달라진 건 두 가지다.

**작업 단위가 커졌다**: 1년 전 "한 함수 짜줘"였던 게 지금은 "이 사양 전체 구현해줘"가 된다. 메인 에이전트가 받아서 subagent들에게 나눠 분배한다. 사람이 한 번에 다루는 단위가 함수→파일→사양으로 한 단계씩 올라갔다.

**병렬 실행이 일상이 됐다**: 1년 전엔 에이전트가 일하는 동안 사용자가 기다리는 모양이었다. 지금은 여러 작업을 동시에 던지고, 결과를 모아 검토하는 모양이다. 사람의 일은 **분배·검토·통합**으로 옮겨 갔다.

> **도구가 한 일과 사용자가 한 일의 구분이, 한 에이전트 안이 아니라 여러 에이전트 사이의 통합 시점으로 옮겨 갔다.**

이 한 줄이 1년 전 글과 지금 글의 가장 큰 차이다. 본 블로그가 시리즈로 다루는 "사람에게 남는 일"의 자리도 이 흐름을 따라 움직인다.

## 4. 짧은 가이드 — 어떤 도구를 골라 쓰나

| 사용 패턴 | 적합한 도구 |
|---|---|
| 깊은 단일 작업·정확한 추론·문서 작업 | Claude Code (Opus 4.7) |
| IDE 내장 + 병렬 다중 파일 편집 | Cursor 3 + Composer 2.5 |
| GitHub 워크플로 통합·진입 비용 최저 | GitHub Copilot |
| Google 생태계·subagent 본격 | Antigravity 2.0 |

조합도 자연스러워졌다. Pragmatic Engineer의 2026년 H1 데이터에 따르면 직장 도입률은 Copilot 29 %·Cursor 18 %·Claude Code 18 %로 분산돼 있다(2026년 2월 전문 개발자 사용률은 Claude Code 41 %로 별도 1위). **한 도구만 쓰는 사용자보다 두세 개를 작업 성격별로 갈아 쓰는 사용자가 늘었다.**

## 5. 마무리

1년 전엔 "어떤 코딩 에이전트가 가장 좋은가"라는 질문이 흔했다. 지금은 "여러 에이전트를 어떻게 부려 통합할 것인가"라는 질문이 흔하다. 도구가 도구를 다루기 시작한 시점이다. 사람의 자리는 한 번 더 위로 옮겨졌다.

---

### 출처

- Pragmatic Engineer, "AI Tooling for Software Engineers in 2026", https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- DigitalApplied, "AI Coding H1 2026: Cursor, Claude Code, Codex Data Recap", https://www.digitalapplied.com/blog/ai-coding-h1-2026-retrospective-cursor-claude-code-codex-data
- Lushbinary, "AI Coding Agents 2026: Claude Code vs Antigravity 2.0 vs Codex vs Cursor vs Kiro vs Copilot vs Windsurf", https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/
- CNBC, "Google debuts new AI models, personal AI agents" (2026-05-19), https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html
- llm-stats.com, "AI Updates Today (May 2026)", https://llm-stats.com/llm-updates
