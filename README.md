# MagicSquare_021

**4x4 Magic Square — TDD 기반 문제 정의 및 구현 프로젝트**

---

## 프로젝트 개요

이 프로젝트는 4x4 마방진(Magic Square)을 주제로, **문제를 올바르게 정의하고 검증 기준을 먼저 세우는 사고 훈련**을 목적으로 합니다.

단순히 마방진을 만드는 것이 목표가 아닙니다. 어떤 격자 상태가 유효한지를 일관된 기준으로 판정할 수 있는 체계를 구축하는 것이 핵심입니다.

---

## 문제 정의 (핵심 요약)

### 표면적 정의 (잘못된 관점)

> "1부터 16까지의 숫자를 4x4 격자에 배치하여, 모든 행, 열, 대각선의 합이 34가 되도록 만들어라."

### 정확한 정의

> "4x4 격자 상태가 주어졌을 때, 그 상태가 마방진의 불변 조건을 모두 만족하는지 일관되게 판정할 수 있는 기준 체계를 갖추어라.  
> 단, 그 기준은 입력 형태나 구현 방식에 관계없이 동일하게 작동해야 한다."

---

## 핵심 Invariant (불변 조건)

| 불변 조건 | 내용 |
|---|---|
| **숫자 집합** | 1부터 16까지의 정수가 정확히 한 번씩 사용되어야 한다 |
| **격자 크기** | 반드시 4행 4열의 정방형 구조여야 한다 |
| **전체 합** | 16개 숫자의 합은 항상 136이며, 이는 변하지 않는다 |
| **목표 합** | 136을 4등분한 값인 34가 각 행, 열, 대각선의 기준 합이다 |
| **판정 기준 수** | 행 4개 + 열 4개 + 대각선 2개, 총 10개의 합 조건이 동시에 성립해야 한다 |
| **중복 금지** | 어떤 숫자도 두 번 이상 등장할 수 없다 |
| **완성의 불가분성** | 10개의 조건 중 하나라도 실패하면 전체가 유효하지 않다 |

---

## 왜 TDD 방식인가

마방진 문제는 정답의 형태가 구현 이전에 완전히 정의될 수 있습니다. 이 특성이 TDD 방식과 자연스럽게 맞닿습니다.

- **불변 조건이 사전에 확정 가능하다** — 검증 기준이 구현보다 먼저 존재한다
- **판단 기준이 통제되어야 한다** — 기준이 구현의 변화에 흔들리면 신뢰할 수 없다
- **입출력이 명확히 정의될 수 있다** — 어떤 상태를 받아 무엇을 돌려줄지 사전에 선언 가능하다

따라서 **먼저 기준을 세우고 나중에 채우는 흐름**이 이 문제의 본질적인 구조와 일치합니다.

---

## 이 프로젝트에서 훈련하는 사고 능력

| 사고 능력 | 설명 |
|---|---|
| **조건을 먼저 정의하는 사고** | 결과를 만들기 전에 올바른 상태의 기준을 언어로 기술한다 |
| **불변 조건을 식별하는 사고** | 변할 수 없는 것과 변해도 되는 것을 분리해 인식한다 |
| **상태를 판정하는 사고** | 부분적으로 맞아 보이는 것과 전체적으로 유효한 것을 구분한다 |
| **경계를 인식하는 사고** | 유효/부분 유효/완전히 잘못된 상태를 각각 명확히 정의한다 |
| **기준의 독립성을 유지하는 사고** | 판단 기준이 구현으로부터 분리되어 흔들리지 않도록 한다 |

---

## 프로젝트 구조

```
MagicSquare_021/
└── Report/
    └── 01.problem-definition.md   # 문제 정의 보고서 (STEP 1~5)
```

---

## 진행 단계

| 단계 | 내용 | 상태 |
|---|---|---|
| STEP 1 | Observation — 상황 관찰 | 완료 |
| STEP 2 | Why #1 — 마방진을 완성해야 하는 이유 | 완료 |
| STEP 3 | Why #2 — 프로그램으로 구현해야 하는 이유 | 완료 |
| STEP 4 | Why #3 — TDD 방식으로 설계해야 하는 이유 | 완료 |
| STEP 5 | 진짜 문제 정의 (Invariant + 사고 능력) | 완료 |
| STEP 6 | 설계 | 예정 |
| STEP 7 | 구현 | 예정 |

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 [Test Plan](Docs/TestPlan_MagicSquare_v0.1.md) 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트

`tests/boundary/test_input_validator.py` · S-01 · `InputValidator.validate_input`

- [x] TC-A-01: 빈칸 0개 격자 → `is_valid=False`, `"blank_count"` 오류 (SC-BND-VAL-001)
- [x] TC-A-02: 빈칸 1개 격자 → `is_valid=False`, `"blank_count"` 오류 (AC-01-2)
- [x] TC-A-03: 빈칸 3개 격자 → `is_valid=False`, `"blank_count"` 오류 (AC-01-3)
- [x] TC-A-04: 빈칸 4개 격자 → `is_valid=False`, `"blank_count"` 오류 (AC-01-4)
- [x] TC-A-05: 중복 숫자 포함 격자 → `is_valid=False`, `"duplicate"` 오류 (SC-BND-VAL-002)
- [x] TC-A-06: 17 이상 값 포함 → `is_valid=False`, `"out_of_range"` 오류 (SC-BND-VAL-003)
- [x] TC-A-07: 0 이하 값 포함(빈칸 제외) → `is_valid=False`, `"out_of_range"` 오류 (AC-01-7)
- [x] TC-A-08: 4×4가 아닌 격자 → `is_valid=False`, `"grid_size"` 오류 (SC-BND-VAL-004)

### Track B — Domain / Logic 테스트

#### B-1. MVP Validator · `tests/control/test_validator.py` · US-04 · INV-1~7

- [x] TC-B-01: 3행 격자 → `_check_grid_size` 실패, `name="격자 크기"` (INV-1)
- [x] TC-B-02: 숫자 7 누락·17 포함 → `_check_number_set` 실패 (INV-2)
- [x] TC-B-03: 숫자 5 중복 → `_check_no_duplicate` 실패, `reason="중복 숫자 존재: [5]"` (INV-3)
- [x] TC-B-04: 1행 합 33 → `_check_row_sums` 실패 (INV-4)
- [x] TC-B-05: 3열 합 35 → `_check_col_sums` 실패 (INV-5)
- [x] TC-B-06: 반대각선 합 35 → `_check_diag_sums` 실패 (INV-6)
- [x] TC-B-07: 유효 마방진 → `validate()` `is_valid=True`, `failed_conditions=[]` (INV-7)
- [x] TC-B-08: 행 합 위반 격자 → `validate()` `is_valid=False` (FR-V-08)
- [x] TC-B-09: 실패 조건 → 모든 `failed_conditions`에 `reason` 포함 (FR-V-10)

#### B-2. BlankFinder · `tests/control/test_blank_finder.py` · S-02

- [x] TC-B-10: 빈칸 2개 → 좌표 2개 `[(2,2), (3,2)]` 반환 (AC-02-1)
- [x] TC-B-11: 반환값 → `(row, col)` tuple 목록 (AC-02-2, AC-02-3)
- [x] TC-B-12: 빈칸 없음 → 빈 리스트 반환 (AC-02-4)
- [x] TC-B-13: 빈칸 3개 → 모든 빈칸 좌표 반환 (AC-02-5)

#### B-3. MissingNumberFinder · `tests/control/test_missing_number_finder.py` · S-03

- [x] TC-B-14: 빈칸 2개 → 누락 숫자 `{7, 14}` 반환 (AC-03-1)
- [x] TC-B-15: 반환값 → 오름차순 `list[int]` (AC-03-2, AC-03-3)
- [x] TC-B-16: 완성 격자 → 빈 리스트 반환 (AC-03-4)
- [x] TC-B-17: 중복 포함 격자 → 누락 숫자 정확히 반환 (AC-03-5)

#### B-4. Solver · `tests/control/test_solver.py` · S-05

- [x] TC-B-18: small-first 성공 → 완성 격자 반환, 빈칸(0) 없음 (SC-DOM-SOL-002)
- [x] TC-B-19: small-first 실패 → large-first `(14, 7)` 배치 성공 (SC-DOM-SOL-001)
- [x] TC-B-20: 두 조합 모두 실패 → `None` 반환 (SC-DOM-SOL-003)
- [x] TC-B-21: 반환 격자 → 4×4, 빈칸 없음 (AC-05-5, AC-05-6)
- [x] TC-B-22: 반환 격자 → `validate()` 통과 (AC-05-8)

#### B-5. Entity (선행) · `tests/entity/test_types.py`

- [x] TC-B-23: 도메인 상수 — `GRID_SIZE`, `TARGET_SUM`, `REQUIRED_NUMBERS` (GREEN)
- [x] TC-B-24: `ConditionResult` — frozen, name, passed, reason (GREEN)
- [x] TC-B-25: `ValidationResult` — is_valid, failed_conditions, 불가분성 (GREEN)

#### B-6. 회귀 보호 · `tests/regression/test_us11_regression_protection.py` · US-11

- [x] TC-B-26: PRD Use Case 테스트 파일 5개 존재 확인

### 커버리지 목표

- [ ] Domain Logic: 95%+ (`pip install pytest-cov`)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결

- [x] [`defect_list.md`](defect_list.md) 생성 및 발견 결함 기록 (DL-MSQ-001, 23건)
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## 참고 문서

- [문제 정의 보고서](Report/01.problem-definition.md)
- [PRD v0.1](Docs/PRD_MagicSquare_v0.1.md)
- [Test Plan v0.1](Docs/TestPlan_MagicSquare_v0.1.md)
