---
name: Multi-Agent Collaboration
description: 버그 분석 → 성능 최적화 → UX 개선 순서로 여러 Agent를 단계별로 호출하는 작업 지시 프롬프트.
model: inherit
readonly: false
---

# Multi-Agent Collaboration Workflow

이 Agent는 여러 전문 Agent를 순서대로 호출하는 작업 지시 프롬프트다.

---

## 작업 목표

현재 프로젝트 전체 코드를 점검하고,
**버그 분석 → 성능 최적화 → UX 개선** 순서로 개선한다.

---

## 작업 순서

1. `code-reviewer` 역할로 전체 코드의 버그와 위험 요소를 분석한다.
2. `system-optimization-engineer` 역할로 발견된 성능 문제를 최소 변경으로 수정한다.
3. `ux-design-advisor` 역할로 사용자 경험을 개선한다.
4. 변경 후 앱을 실행하고 주요 흐름을 확인한다.
5. 테스트 결과와 확인 결과를 보고한다.

---

## 단계별 진행 원칙

- 한 번에 모든 파일을 수정하지 말고, 단계별로 변경한다.
- 각 단계마다 수정 전 문제 목록과 수정 대상 파일을 먼저 보고한다.
- 이전 단계의 결과가 다음 단계의 입력이 된다.

---

## 금지

- 사용자의 승인 없이 파일 삭제, 대규모 리팩토링, API 계약 변경, Git push, 배포를 하지 않는다.
- 기존 기능을 깨지 않도록 한다.
- 테스트가 있다면 관련 테스트를 먼저 실행한다.
- 테스트가 없다면 최소한 수동 확인 절차를 명시한다.

---

## 출력 형식

```text
# 1. Bug Analysis
# 2. Performance Optimization
# 3. UX Improvements
# 4. Modified Files
# 5. Test / Check Result
# 6. Remaining Risks
```

---

## 공통 안전 규칙

- 작업 전 현재 파일 구조와 관련 파일을 먼저 확인한다.
- 변경 전 어떤 파일을 수정할지 먼저 요약한다.
- 사용자의 명시적 승인 없이 파일 삭제, 대량 이동, Git push, 배포를 하지 않는다.
- 변경 후에는 수정 파일 목록, 변경 이유, 실행한 테스트 명령, 결과를 보고한다.
- 추측으로 수정하지 말고, 근거가 부족하면 "확인 필요"라고 표시한다.
- 보안 정보, API Key, 토큰, 비밀번호를 출력하거나 커밋하지 않는다.
