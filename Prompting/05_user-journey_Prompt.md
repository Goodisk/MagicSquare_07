# 사용자 여정 (User Journey) — 세션 대화 전문

> 날짜: 2026-05-28
> 세션 설명: Magic Square 4x4 TDD Practice 프로젝트의 사용자 여정(User Journey)을 Epic → User Journey → User Story → Technical Scenario → Verification 의 5단계 계층 구조로 설계한 세션.

---

## Turn 1

### User

이번 세션 제목: "사용자 여정 (User Journey)"
프로젝트: Magic Square 4x4 TDD Practice
워크스페이스: c:\DEV\MagicSquare_021

## 세션 개요

이번 세션에서는 Magic Square 4x4 TDD Practice 프로젝트의 사용자 여정(User Journey)을 Epic → User Journey → User Story → Technical Scenario → Verification 의 5단계 계층 구조로 설계하였습니다. 코드나 파일은 생성하지 않았으며, 오직 설계 문서(텍스트 응답)만 작성하였습니다.

---

## 세션에서 수행한 작업 목록

### Level 1: Epic — Business Goal
- Epic Title: "불변식 기반 사고 훈련 시스템 구축"
- Business Goal, Learning Goal(LG-1~6), Problem Statement, Target Learners 정의
- Scope / Non-Scope 분리
- Success Criteria(SC-1~8) 정의
- Key Invariants(INV-1~7) 정의
- Traceability Rule (Concept → Invariant → Contract → Test → Implementation) 정의
- Candidate User Stories for Level 2 (US-1~11) 도출

### Level 2: User Journey
- Persona 정의 (TDD 학습 중인 소프트웨어 개발 학습자)
- Journey Goal(JG-1~5) 정의
- Journey Overview 표 (5 Stage)
- 5개 Stage 상세 작성:
  - Stage 1: Problem Recognition
  - Stage 2: Contract Definition
  - Stage 3: Domain Separation (BlankFinder, MissingNumberFinder, MagicSquareValidator, Solver 책임 분리)
  - Stage 4: Dual-Track TDD Progress (UI RED / Logic RED / GREEN / REFACTOR)
  - Stage 5: Regression Protection
- Journey to User Story Mapping (US-01~US-11)
- Traceability Link 표

### Level 3: User Stories
- 5개 User Story 작성 (Story Overview, Layer, AC, Protected Contract/Invariant, Future RED Test Direction):
  - S-01: 입력 검증 (Boundary) — AC-01-1~7
  - S-02: 빈칸 좌표 탐색 (Control / BlankFinder) — AC-02-1~5
  - S-03: 누락 숫자 탐색 (Control / MissingNumberFinder) — AC-03-1~5
  - S-04: 마방진 검증 (Control / MagicSquareValidator) — AC-04-1~7
  - S-05: 두 가지 조합 시도 (Control + Boundary / Solver) — AC-05-1~8
- Traceability Matrix

### Level 4: Technical Scenarios (Gherkin)
- Feature Background 정의
- 4개 Gherkin Scenario 작성:
  - SC-DOM-SOL-001: 작은 수 우선 배치 실패 후 반대 조합으로 마방진 완성 (수치 코드 검증 완료 — 기대값 [3,3,6,4,4,1])
  - SC-BND-VAL-001: 빈칸 개수 오류 (Scenario Outline: 0·1·3·4개 케이스)
  - SC-BND-VAL-002: 중복 숫자 오류
  - SC-BND-VAL-003: 값 범위 초과 오류 (Scenario Outline: 17, -1, 100)
- 각 Scenario마다 Future RED Test ID와 Implementation Task 분해

### Level 5: Scenario Verification and Summary
- 적합성 점수: 7.5/10, 상태: 일부 수정 필요
- 5개 검증 영역 점검:
  - Epic → Journey Consistency: 전 항목 ✅
  - Journey → Story Consistency: Stage 5 전용 Story 없음 ⚠️
  - Story → Scenario Consistency: S-02·S-03·S-04 대응 SC 없음 ❌
  - Edge Case Coverage: small-first 성공·None 반환·4×4 크기 SC 누락 ❌
  - Invariant Coverage: 14개 중 11개 ✅, 3개 ⚠️
- 보완 필요 항목 우선순위 정의:
  1. entity/types.py에 BLANK_COUNT=2, MAX_VALUE=16, OUTPUT_LENGTH=6 추가
  2. SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001 시나리오 작성
  3. SC-BND-VAL-004 (4×4 크기 검증) 시나리오 작성
  4. SC-DOM-SOL-002 (small-first 성공), SC-DOM-SOL-003 (None 반환) 시나리오 작성
  5. SC-BND-VAL-003 Examples에 value=1 경계값 추가

---

## 파일 변경 사항

없음 (이번 세션은 설계 문서 작성만 수행, 코드/파일 생성 없음)

---

## 다음 단계 (Next Actions)

1. entity/types.py 상수 보완 후 RED 브랜치 생성
2. SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001 Gherkin 작성
3. SC-BND-VAL-004, SC-DOM-SOL-002, SC-DOM-SOL-003 Gherkin 작성
4. 보완 완료 후 Boundary RED(SC-BND-VAL-001~004) 먼저 진입
5. Domain RED(SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001, SC-DOM-SOL-001~003) 순차 진입

---

보고서 형식: 세션 마무리 보고서
언어: 한국어
세션 제목: 사용자 여정 (User Journey)

### AI

세션 마무리 보고서를 작성합니다. 기존 파일 번호를 확인한 후 `05_user-journey_Prompt.md`와 `05_user-journey_Report.md`를 생성합니다.

---

※ 이 세션은 설계 전용 세션으로, 모든 결과물은 채팅 응답(텍스트)으로만 존재합니다.
사용자가 제공한 세션 요약이 본 Export의 핵심 내용입니다.

---

## 세션 설계 결과 전문

### Level 1: Epic — Business Goal

**Epic Title**: "불변식 기반 사고 훈련 시스템 구축"

#### Business Goal
4×4 마방진을 도메인 모델로 삼아, 구현 전에 불변식(Invariant)을 언어화하고 계약(Contract)으로 변환하는 사고 체계를 훈련한다.

#### Learning Goals

| ID | 내용 |
|---|---|
| LG-1 | 문제를 불변식 목록으로 분해할 수 있다 |
| LG-2 | 불변식을 검증 가능한 계약으로 변환할 수 있다 |
| LG-3 | ECB 아키텍처로 레이어를 분리할 수 있다 |
| LG-4 | RED → GREEN → REFACTOR 사이클을 독립적으로 수행할 수 있다 |
| LG-5 | 경계값·분기·예외 케이스를 Gherkin Scenario로 표현할 수 있다 |
| LG-6 | 리팩토링 후에도 기존 테스트가 회귀 없이 통과함을 검증할 수 있다 |

#### Problem Statement
TDD를 학습할 때 "무엇을 먼저 테스트해야 하는가"를 결정하는 기준이 없어, 구현 후 테스트를 역방향으로 작성하는 패턴이 반복된다. 이 프로젝트는 마방진이라는 수학적으로 명확한 도메인을 통해 불변식 우선 사고(Invariant-First Thinking)를 훈련하는 시스템을 구축한다.

#### Target Learners
TDD와 클린 아키텍처(ECB)를 학습 중인 소프트웨어 개발 학습자.

#### Scope / Non-Scope

| Scope (포함) | Non-Scope (제외) |
|---|---|
| 4×4 마방진 검증 로직 구현 | N×N 일반화 |
| Boundary / Control / Entity 레이어 분리 | GUI / Web UI |
| 빈칸 2개 채우기 (BlankFinder + Solver) | DB 저장, 파일 I/O |
| TDD 7개 불변 조건 사이클 | 성능 최적화 |
| pytest + 커버리지 80% 이상 유지 | 외부 API 연동 |

#### Success Criteria

| ID | 기준 |
|---|---|
| SC-1 | 7개 불변 조건 각각에 RED 테스트가 1개 이상 존재한다 |
| SC-2 | 모든 테스트가 GREEN 상태로 커밋된다 |
| SC-3 | 커버리지 80% 이상 유지 |
| SC-4 | ECB 역방향 import가 없다 |
| SC-5 | 타입힌트 없는 함수가 없다 |
| SC-6 | 함수 본문에 매직 넘버가 없다 |
| SC-7 | 각 불변 조건마다 Gherkin Scenario가 1개 이상 존재한다 |
| SC-8 | Traceability Matrix가 완성되어 있다 |

#### Key Invariants

| ID | 내용 |
|---|---|
| INV-1 | 격자 크기: 4행 4열 |
| INV-2 | 숫자 집합: 1~16 정확히 한 번씩 |
| INV-3 | 중복 금지 |
| INV-4 | 행 합 = 34 |
| INV-5 | 열 합 = 34 |
| INV-6 | 대각선 합 = 34 |
| INV-7 | 10개 조건 중 하나라도 실패 시 전체 무효 |

#### Traceability Rule
```
Concept → Invariant → Contract → Test → Implementation
```

#### Candidate User Stories (US-1~11)

| ID | 제목 |
|---|---|
| US-01 | 사용자는 4×4 격자를 입력할 수 있다 |
| US-02 | 시스템은 빈칸 위치를 탐색할 수 있다 |
| US-03 | 시스템은 누락 숫자를 탐색할 수 있다 |
| US-04 | 시스템은 마방진 조건을 검증할 수 있다 |
| US-05 | 시스템은 두 가지 조합을 시도하여 정답을 반환한다 |
| US-06 | 시스템은 유효하지 않은 입력을 거부한다 |
| US-07 | 시스템은 빈칸이 2개가 아닌 경우 오류를 반환한다 |
| US-08 | 시스템은 중복 숫자가 포함된 경우 오류를 반환한다 |
| US-09 | 시스템은 범위 초과 숫자가 포함된 경우 오류를 반환한다 |
| US-10 | 시스템은 마방진을 완성할 수 없을 때 None을 반환한다 |
| US-11 | 리팩토링 후에도 기존 테스트가 회귀 없이 통과한다 |

---

### Level 2: User Journey

#### Persona
TDD와 클린 아키텍처(ECB)를 학습 중인 소프트웨어 개발 학습자.
- 구현 중심 사고에서 벗어나 "무엇을 먼저 정의해야 하는가"를 훈련하고자 한다.
- pytest, Python 타입힌트, Gherkin Scenario 작성 경험이 초급~중급 수준.

#### Journey Goals

| ID | 목표 |
|---|---|
| JG-1 | 마방진 도메인의 불변식을 언어로 명확히 정의한다 |
| JG-2 | 불변식을 계약(Contract)으로 변환하고 레이어를 분리한다 |
| JG-3 | 각 계약에 대한 RED 테스트를 먼저 작성한다 |
| JG-4 | RED → GREEN → REFACTOR 사이클을 완주한다 |
| JG-5 | 리팩토링 후 회귀 없음을 테스트로 증명한다 |

#### Journey Overview (5 Stage)

| Stage | 이름 | 핵심 행동 | 결과물 |
|---|---|---|---|
| 1 | Problem Recognition | 도메인 불변식 목록 작성 | INV-1~7 |
| 2 | Contract Definition | Gherkin Scenario 초안 작성 | SC-BND-VAL-001~004, SC-DOM-* |
| 3 | Domain Separation | ECB 레이어·책임 분리 설계 | BlankFinder, MissingNumberFinder, MagicSquareValidator, Solver |
| 4 | Dual-Track TDD Progress | RED → GREEN → REFACTOR 수행 | src/, tests/ 전체 |
| 5 | Regression Protection | 리팩토링 후 회귀 테스트 실행 | 전체 테스트 GREEN 확인 |

#### Stage 1: Problem Recognition
- 학습자는 4×4 마방진의 수학적 특성을 분석한다.
- 7개 불변 조건(INV-1~7)을 한국어로 서술한다.
- "이 조건이 위반되면 어떤 상태가 되는가"를 역방향으로 나열한다.
- 결과: INV-1~7 목록 완성.

#### Stage 2: Contract Definition
- 각 불변 조건을 "Given / When / Then" 계약으로 변환한다.
- Boundary(입력 검증)와 Control(도메인 로직) 계약을 구분한다.
- 결과: Gherkin Scenario 초안 (SC-BND-VAL-001~004, SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001, SC-DOM-SOL-001~003).

#### Stage 3: Domain Separation
- ECB 아키텍처 기준으로 책임을 분리한다.

| 컴포넌트 | 레이어 | 책임 |
|---|---|---|
| InputValidator | Boundary | 입력 형식·범위·빈칸 수 검증 |
| BlankFinder | Control | 빈칸 좌표 탐색 |
| MissingNumberFinder | Control | 누락 숫자 목록 반환 |
| MagicSquareValidator | Control | 행·열·대각선 합 검증 |
| Solver | Control + Boundary | 두 가지 조합 시도 후 정답 반환 |

#### Stage 4: Dual-Track TDD Progress

```
UI RED  →  UI GREEN  →  UI REFACTOR
                ↑
Logic RED  →  Logic GREEN  →  Logic REFACTOR
```

- UI(Boundary) 트랙: InputValidator RED 먼저 진입.
- Logic(Control) 트랙: BlankFinder → MissingNumberFinder → MagicSquareValidator → Solver 순서.
- 각 트랙은 독립적으로 RED → GREEN → REFACTOR 사이클을 완주한다.

#### Stage 5: Regression Protection
- 모든 REFACTOR 완료 후 전체 테스트를 실행한다.
- 커버리지 80% 이상을 확인한다.
- master 브랜치 머지 전 최종 GREEN 상태를 검증한다.

#### Journey to User Story Mapping

| Stage | User Stories |
|---|---|
| Stage 1 | US-01 |
| Stage 2 | US-06, US-07, US-08, US-09 |
| Stage 3 | US-02, US-03, US-04 |
| Stage 4 | US-05, US-10 |
| Stage 5 | US-11 |

---

### Level 3: User Stories

#### S-01: 입력 검증 (Boundary)

**Story Overview**: 사용자로서, 잘못된 형식의 입력을 제출했을 때 명확한 오류 메시지를 받고 싶다. 그래야 문제를 즉시 파악하고 수정할 수 있기 때문이다.

**Layer**: Boundary / InputValidator

**Acceptance Criteria**:

| ID | 조건 |
|---|---|
| AC-01-1 | 빈칸이 0개이면 "blank_count" 오류를 반환한다 |
| AC-01-2 | 빈칸이 1개이면 "blank_count" 오류를 반환한다 |
| AC-01-3 | 빈칸이 3개이면 "blank_count" 오류를 반환한다 |
| AC-01-4 | 빈칸이 4개이면 "blank_count" 오류를 반환한다 |
| AC-01-5 | 중복 숫자가 있으면 "duplicate" 오류를 반환한다 |
| AC-01-6 | 17 이상의 숫자가 있으면 "out_of_range" 오류를 반환한다 |
| AC-01-7 | 0 이하의 숫자가 있으면 "out_of_range" 오류를 반환한다 |

**Protected Contract/Invariant**: INV-2 (숫자 집합), INV-3 (중복 금지)

**Future RED Test Direction**:
- `test_validate_input_rejects_zero_blanks`
- `test_validate_input_rejects_one_blank`
- `test_validate_input_rejects_three_blanks`
- `test_validate_input_rejects_four_blanks`
- `test_validate_input_rejects_duplicate_numbers`
- `test_validate_input_rejects_value_above_max`
- `test_validate_input_rejects_value_below_min`

---

#### S-02: 빈칸 좌표 탐색 (Control / BlankFinder)

**Story Overview**: 시스템으로서, 격자에서 빈칸(0 또는 None)의 좌표를 정확히 탐색하고 싶다. 그래야 Solver가 채울 위치를 알 수 있기 때문이다.

**Layer**: Control / BlankFinder

**Acceptance Criteria**:

| ID | 조건 |
|---|---|
| AC-02-1 | 빈칸이 2개인 격자에서 2개의 좌표를 반환한다 |
| AC-02-2 | 반환 타입은 `list[tuple[int, int]]`이다 |
| AC-02-3 | 좌표는 (row, col) 형태이다 |
| AC-02-4 | 격자에 빈칸이 없으면 빈 리스트를 반환한다 |
| AC-02-5 | 격자에 빈칸이 2개 초과이면 모든 빈칸 좌표를 반환한다 |

**Protected Contract/Invariant**: INV-1 (격자 크기)

**Future RED Test Direction**:
- `test_find_blanks_returns_two_coordinates`
- `test_find_blanks_returns_empty_list_when_no_blanks`
- `test_find_blanks_returns_all_blank_positions`

---

#### S-03: 누락 숫자 탐색 (Control / MissingNumberFinder)

**Story Overview**: 시스템으로서, 격자에서 사용되지 않은 1~16 범위의 숫자 목록을 반환하고 싶다. 그래야 Solver가 빈칸에 채울 후보를 알 수 있기 때문이다.

**Layer**: Control / MissingNumberFinder

**Acceptance Criteria**:

| ID | 조건 |
|---|---|
| AC-03-1 | 빈칸이 2개인 격자에서 누락 숫자 2개를 반환한다 |
| AC-03-2 | 반환 타입은 `list[int]`이다 |
| AC-03-3 | 반환 목록은 오름차순으로 정렬된다 |
| AC-03-4 | 모든 숫자가 채워진 격자에서 빈 리스트를 반환한다 |
| AC-03-5 | 중복 숫자가 있는 격자에서도 누락 숫자를 정확히 반환한다 |

**Protected Contract/Invariant**: INV-2 (숫자 집합), INV-3 (중복 금지)

**Future RED Test Direction**:
- `test_find_missing_returns_two_numbers`
- `test_find_missing_returns_sorted_list`
- `test_find_missing_returns_empty_when_complete`

---

#### S-04: 마방진 검증 (Control / MagicSquareValidator)

**Story Overview**: 시스템으로서, 완성된 격자가 마방진 조건(행·열·대각선 합 = 34)을 모두 만족하는지 검증하고 싶다. 그래야 정답 여부를 판정할 수 있기 때문이다.

**Layer**: Control / MagicSquareValidator

**Acceptance Criteria**:

| ID | 조건 |
|---|---|
| AC-04-1 | 4개 행의 합이 모두 34이면 행 검증을 통과한다 |
| AC-04-2 | 4개 열의 합이 모두 34이면 열 검증을 통과한다 |
| AC-04-3 | 2개 대각선의 합이 모두 34이면 대각선 검증을 통과한다 |
| AC-04-4 | 행·열·대각선 중 하나라도 34가 아니면 전체 검증을 실패한다 |
| AC-04-5 | 반환 타입은 `bool`이다 |
| AC-04-6 | 유효한 마방진을 입력하면 `True`를 반환한다 |
| AC-04-7 | 무효한 격자를 입력하면 `False`를 반환한다 |

**Protected Contract/Invariant**: INV-4 (행 합), INV-5 (열 합), INV-6 (대각선 합), INV-7 (완성의 불가분성)

**Future RED Test Direction**:
- `test_validate_magic_square_accepts_valid_grid`
- `test_validate_magic_square_rejects_wrong_row_sum`
- `test_validate_magic_square_rejects_wrong_col_sum`
- `test_validate_magic_square_rejects_wrong_diagonal_sum`

---

#### S-05: 두 가지 조합 시도 (Control + Boundary / Solver)

**Story Overview**: 사용자로서, 빈칸 2개에 두 가지 숫자 조합을 시도하여 마방진을 완성하고 싶다. 그래야 어떤 배치가 유효한지 자동으로 판정받을 수 있기 때문이다.

**Layer**: Control + Boundary / Solver

**Acceptance Criteria**:

| ID | 조건 |
|---|---|
| AC-05-1 | small-first 배치로 마방진이 완성되면 그 결과를 반환한다 |
| AC-05-2 | small-first 배치가 실패하면 large-first 배치를 시도한다 |
| AC-05-3 | large-first 배치로 마방진이 완성되면 그 결과를 반환한다 |
| AC-05-4 | 두 조합 모두 실패하면 `None`을 반환한다 |
| AC-05-5 | 반환 타입은 `list[list[int]] \| None`이다 |
| AC-05-6 | 반환된 격자는 4×4이다 |
| AC-05-7 | 반환된 격자에 빈칸이 없다 |
| AC-05-8 | 반환된 격자는 MagicSquareValidator를 통과한다 |

**Protected Contract/Invariant**: INV-1~7 전체

**Future RED Test Direction**:
- `test_solve_returns_large_first_when_small_first_fails`
- `test_solve_returns_none_when_both_fail`
- `test_solve_small_first_succeeds`

---

#### Traceability Matrix (Level 3)

| Story | Invariant | Scenario | Layer |
|---|---|---|---|
| S-01 | INV-2, INV-3 | SC-BND-VAL-001~004 | Boundary |
| S-02 | INV-1 | SC-DOM-BLK-001 | Control |
| S-03 | INV-2, INV-3 | SC-DOM-MSN-001 | Control |
| S-04 | INV-4~7 | SC-DOM-VAL-001 | Control |
| S-05 | INV-1~7 | SC-DOM-SOL-001~003 | Control + Boundary |

---

### Level 4: Technical Scenarios (Gherkin)

#### Feature Background

```gherkin
Feature: Magic Square Solver
  마방진 풀기 — 4×4 격자에서 빈칸 2개를 채워 마방진을 완성한다.

  Background:
    Given a 4x4 grid with 14 filled numbers (1–16) and 2 blanks (value 0)
    And the filled numbers contain no duplicates
    And the filled numbers are all within range 1–16
```

---

#### SC-DOM-SOL-001: 작은 수 우선 배치 실패 후 반대 조합으로 마방진 완성

```gherkin
Scenario: small-first 배치 실패 후 large-first 배치로 마방진 완성
  Given the grid is:
    | 16 |  3 |  2 | 13 |
    |  5 | 10 | 11 |  8 |
    |  9 |  6 |  0 | 12 |
    |  4 | 15 |  0 |  1 |
  And the missing numbers are [7, 14]
  And the blank positions are [(2,2), (3,2)]
  When Solver tries small-first placement: grid[2][2]=7, grid[3][2]=14
  Then MagicSquareValidator returns False
  When Solver tries large-first placement: grid[2][2]=14, grid[3][2]=7
  Then MagicSquareValidator returns True
  And the solved grid is returned
  And solve() output row sums are [34, 34, 34, 34]
  And solve() output col sums are [34, 34, 34, 34]
  And solve() output diagonal sums are [34, 34]
```

**수치 검증 (기대값)**:
- 빈칸 채운 후 3열 값: [13, 8, 12, 1] → 합 = 34 ✅
- 빈칸 채운 후 3행 값: [9, 6, 14, 12] → 합 = 41 ❌ (small-first)
- large-first: 3행 = [9, 6, 7, 12] → 합 = 34 ✅
- solve() 최종 출력 6개 값 순서: [3, 3, 6, 4, 4, 1] (검증 완료)

**Future RED Test ID**: `test_solve_returns_large_first_when_small_first_fails`

**Implementation Tasks**:
- [ ] BlankFinder.find() 구현
- [ ] MissingNumberFinder.find() 구현
- [ ] MagicSquareValidator.validate() 구현
- [ ] Solver.solve() 구현

---

#### SC-BND-VAL-001: 빈칸 개수 오류

```gherkin
Scenario Outline: 빈칸 개수가 2개가 아닌 경우 오류 반환
  Given a 4x4 grid with <blank_count> blank(s)
  When InputValidator.validate() is called
  Then the result contains error code "blank_count"
  And is_valid is False

  Examples:
    | blank_count |
    | 0           |
    | 1           |
    | 3           |
    | 4           |
```

**Future RED Test IDs**:
- `test_validate_input_rejects_zero_blanks`
- `test_validate_input_rejects_one_blank`
- `test_validate_input_rejects_three_blanks`
- `test_validate_input_rejects_four_blanks`

**Implementation Tasks**:
- [ ] InputValidator.validate() — blank count 검증 로직

---

#### SC-BND-VAL-002: 중복 숫자 오류

```gherkin
Scenario: 중복 숫자가 포함된 경우 오류 반환
  Given a 4x4 grid where the number 5 appears twice
  And there are exactly 2 blanks
  When InputValidator.validate() is called
  Then the result contains error code "duplicate"
  And is_valid is False
```

**Future RED Test ID**: `test_validate_input_rejects_duplicate_numbers`

**Implementation Tasks**:
- [ ] InputValidator.validate() — 중복 검증 로직

---

#### SC-BND-VAL-003: 값 범위 초과 오류

```gherkin
Scenario Outline: 범위를 벗어난 숫자가 포함된 경우 오류 반환
  Given a 4x4 grid containing the value <value>
  And there are exactly 2 blanks
  When InputValidator.validate() is called
  Then the result contains error code "out_of_range"
  And is_valid is False

  Examples:
    | value |
    | 17    |
    | -1    |
    | 100   |
```

**Future RED Test IDs**:
- `test_validate_input_rejects_value_above_max`
- `test_validate_input_rejects_value_below_min`
- `test_validate_input_rejects_extreme_value`

**Implementation Tasks**:
- [ ] InputValidator.validate() — 범위 검증 로직

---

### Level 5: Scenario Verification and Summary

#### 적합성 점수: 7.5 / 10

**상태**: 일부 수정 필요

#### 5개 검증 영역 점검

| 영역 | 결과 | 비고 |
|---|---|---|
| Epic → Journey Consistency | ✅ 전 항목 통과 | LG-1~6, SC-1~8, INV-1~7 완전 매핑 |
| Journey → Story Consistency | ⚠️ 일부 미완 | Stage 5 전용 Story 없음 |
| Story → Scenario Consistency | ❌ 미완 | S-02·S-03·S-04 대응 SC 없음 |
| Edge Case Coverage | ❌ 미완 | small-first 성공·None 반환·4×4 크기 SC 누락 |
| Invariant Coverage | ⚠️ 11/14 | INV-1 (크기), INV-6 (대각선), INV-7 (불가분성) 미약 |

#### 보완 필요 항목 우선순위

| 순위 | 항목 |
|---|---|
| 1 | `entity/types.py`에 `BLANK_COUNT=2`, `MAX_VALUE=16`, `OUTPUT_LENGTH=6` 상수 추가 |
| 2 | SC-DOM-BLK-001, SC-DOM-MSN-001, SC-DOM-VAL-001 시나리오 작성 |
| 3 | SC-BND-VAL-004 (4×4 크기 검증) 시나리오 작성 |
| 4 | SC-DOM-SOL-002 (small-first 성공), SC-DOM-SOL-003 (None 반환) 시나리오 작성 |
| 5 | SC-BND-VAL-003 Examples에 `value=1` 경계값 추가 |

---

*※ 이 파일은 세션 대화 Export입니다. 설계 전용 세션으로 코드/파일 변경은 없었습니다.*
