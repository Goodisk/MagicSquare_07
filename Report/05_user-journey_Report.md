# 사용자 여정 (User Journey) — 작업 보고서

> 날짜: 2026-05-28
> 관련 프롬프트 기록: Prompting/05_user-journey_Prompt.md

---

## 1. 작업 개요

Magic Square 4×4 TDD Practice 프로젝트의 전체 사용자 여정을 **Epic → User Journey → User Story → Technical Scenario → Verification** 5단계 계층 구조로 설계하였다. 이번 세션은 코드 구현 없이 설계 문서(텍스트 응답)만 작성하는 순수 설계 세션이었으며, 7개 불변 조건(INV-1~7)을 기반으로 Gherkin Scenario와 Acceptance Criteria를 도출하였다. 설계 결과는 다음 TDD 사이클 진입을 위한 명세 기반 역할을 한다.

---

## 2. 수정 / 생성한 파일

| 파일 경로 | 변경 유형 | 변경 내용 요약 |
|---|---|---|
| `Prompting/05_user-journey_Prompt.md` | 생성 | 세션 전체 대화 및 설계 결과 전문 Export |
| `Report/05_user-journey_Report.md` | 생성 | 세션 작업 보고서 |

> 이번 세션에서 `src/`, `tests/` 하위 코드 파일 변경 없음.

---

## 3. 주요 변경 내용

### Level 1: Epic — Business Goal

- **Epic Title**: "불변식 기반 사고 훈련 시스템 구축"
- Learning Goal 6개(LG-1~6), Success Criteria 8개(SC-1~8) 정의
- Key Invariants 7개(INV-1~7) 명문화
- Traceability Rule: `Concept → Invariant → Contract → Test → Implementation`
- Candidate User Stories 11개(US-1~11) 도출

### Level 2: User Journey

- Persona 정의: TDD + ECB 학습 중인 소프트웨어 개발 학습자
- Journey Goal 5개(JG-1~5) 정의
- Journey 5단계 설계:
  - Stage 1: Problem Recognition (INV-1~7 언어화)
  - Stage 2: Contract Definition (Gherkin Scenario 초안)
  - Stage 3: Domain Separation (BlankFinder / MissingNumberFinder / MagicSquareValidator / Solver 책임 분리)
  - Stage 4: Dual-Track TDD Progress (UI 트랙 / Logic 트랙 병행)
  - Stage 5: Regression Protection (전체 GREEN 검증)
- US-01~11 → Stage 매핑 완성

### Level 3: User Stories (5개)

| Story | Layer | 핵심 계약 | AC 수 |
|---|---|---|---|
| S-01: 입력 검증 | Boundary / InputValidator | 빈칸 수·중복·범위 오류 반환 | 7 |
| S-02: 빈칸 좌표 탐색 | Control / BlankFinder | 좌표 `list[tuple[int,int]]` 반환 | 5 |
| S-03: 누락 숫자 탐색 | Control / MissingNumberFinder | 오름차순 `list[int]` 반환 | 5 |
| S-04: 마방진 검증 | Control / MagicSquareValidator | 행·열·대각선 합 34 검증 | 7 |
| S-05: 두 가지 조합 시도 | Control + Boundary / Solver | small-first → large-first → None 반환 | 8 |

### Level 4: Technical Scenarios — Gherkin (4개)

| Scenario ID | 내용 | 검증 상태 |
|---|---|---|
| SC-DOM-SOL-001 | small-first 실패 → large-first로 마방진 완성 | ✅ 수치 검증 완료 (기대값 [3,3,6,4,4,1]) |
| SC-BND-VAL-001 | 빈칸 개수 오류 (Outline: 0·1·3·4개) | ✅ |
| SC-BND-VAL-002 | 중복 숫자 오류 | ✅ |
| SC-BND-VAL-003 | 값 범위 초과 오류 (Outline: 17, -1, 100) | ✅ |

### Level 5: Scenario Verification

- 적합성 점수: **7.5 / 10**
- 상태: **일부 수정 필요**

| 영역 | 결과 |
|---|---|
| Epic → Journey Consistency | ✅ |
| Journey → Story Consistency | ⚠️ Stage 5 전용 Story 없음 |
| Story → Scenario Consistency | ❌ S-02·S-03·S-04 대응 SC 없음 |
| Edge Case Coverage | ❌ small-first 성공·None 반환·4×4 크기 SC 누락 |
| Invariant Coverage | ⚠️ 14개 중 11개 (INV-1, INV-6, INV-7 미약) |

---

## 4. 실행한 명령

없음 (설계 전용 세션, 코드 실행 없음)

---

## 5. 테스트 결과

없음 (설계 전용 세션)

> 현재 저장소에 기존 테스트 파일 존재:
> - `tests/entity/test_types.py`
> - `tests/conftest.py`
>
> 다음 세션에서 RED 단계 진입 시 테스트 결과 기록 예정.

---

## 6. 남은 이슈

| 우선순위 | 항목 | 상태 |
|---|---|---|
| 1 | `entity/types.py`에 `BLANK_COUNT=2`, `MAX_VALUE=16`, `OUTPUT_LENGTH=6` 상수 추가 | 미완료 |
| 2 | SC-DOM-BLK-001 (BlankFinder Gherkin) 작성 | 미완료 |
| 3 | SC-DOM-MSN-001 (MissingNumberFinder Gherkin) 작성 | 미완료 |
| 4 | SC-DOM-VAL-001 (MagicSquareValidator Gherkin) 작성 | 미완료 |
| 5 | SC-BND-VAL-004 (4×4 크기 검증 Gherkin) 작성 | 미완료 |
| 6 | SC-DOM-SOL-002 (small-first 성공 케이스) 작성 | 미완료 |
| 7 | SC-DOM-SOL-003 (두 조합 모두 실패 → None 반환) 작성 | 미완료 |
| 8 | SC-BND-VAL-003 Examples에 `value=1` 경계값 추가 | 미완료 |
| 9 | Stage 5 (Regression Protection) 전용 User Story 보완 | 확인 필요 |

---

## 7. 다음 작업 제안

### 즉시 진행 가능 (다음 세션)

1. **`entity/types.py` 상수 보완**
   - `BLANK_COUNT: Final[int] = 2`
   - `MAX_VALUE: Final[int] = 16`
   - `OUTPUT_LENGTH: Final[int] = 6`
   - 브랜치: `red` 또는 `refactoring` (기존 코드 수정)

2. **누락 Gherkin Scenario 작성** (설계 문서 보완)
   - SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001
   - SC-BND-VAL-004, SC-DOM-SOL-002, SC-DOM-SOL-003

3. **Boundary RED 진입**
   - 브랜치: `red`
   - 대상: `tests/boundary/test_input_validator.py` 생성
   - 시나리오: SC-BND-VAL-001~004 기반 테스트 작성

### 이후 순서

4. **Boundary GREEN** — `src/magic_square/boundary/input_validator.py` 구현
5. **Domain RED 순차 진입** — BlankFinder → MissingNumberFinder → MagicSquareValidator → Solver
6. **전체 REFACTOR + Regression 검증** — Stage 5 완료

---

*이 보고서는 Report and Task Closer Agent에 의해 자동 생성되었습니다.*
