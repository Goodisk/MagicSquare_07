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

## TDD 진행 체크리스트

> [Test Plan](Docs/TestPlan_MagicSquare_v0.1.md) · [defect_list.md](defect_list.md) (DL-MSQ-001) 기준.  
> **RED** = 테스트 작성·커밋 (`red` 브랜치) · **GREEN** = 최소 구현·커밋 (`green` 브랜치, G-번호 순).  
> GREEN은 Entity → Boundary(크기) → Boundary(S-01) → Control(INV) → Phase 2 → 회귀 순서를 따른다.

### RED 커밋 묶음 (테스트 작성)

묶음 단위로 `red`에 커밋하고, 하위 TC가 모두 체크되면 묶음도 체크한다.

- [x] **RED-1** `tests/entity/test_types.py` (16건) → `entity/types.py`
  - [x] G-001 `TestDomainConstants::test_grid_size_is_4`
  - [x] G-002 `…::test_target_sum_is_34`
  - [x] G-003 `…::test_required_numbers_contains_1_to_16`
  - [x] G-004 `…::test_required_numbers_count_is_16`
  - [x] G-005 `TestConditionResult::test_passed_condition_reason_defaults_to_none`
  - [x] G-006 `…::test_passed_condition_stores_name_and_passed`
  - [x] G-007 `…::test_failed_condition_stores_reason`
  - [x] G-008 `…::test_condition_result_is_immutable`
  - [x] G-009 `…::test_condition_result_name_is_immutable`
  - [x] G-010 `TestValidationResult::test_valid_result_is_valid_is_true`
  - [x] G-011 `…::test_valid_result_failed_conditions_defaults_to_empty`
  - [x] G-012 `…::test_invalid_result_stores_failed_conditions`
  - [x] G-013 `…::test_invalid_result_with_multiple_failures`
  - [x] G-014 `…::test_validation_result_is_immutable`
  - [x] G-015 `…::test_single_failure_makes_result_invalid`
  - [x] G-016 `TestGridTypeAlias::test_grid_accepts_4x4_list`

- [x] **RED-2** `tests/boundary/test_ac_fr_01_01_invalid_size.py` (8건) → `magic_square.boundary` · AC-FR-01-01
  - [x] G-017 `test_three_rows_grid_returns_invalid_size_error_code`
  - [x] G-018 `test_five_columns_grid_returns_invalid_size_error_code`
  - [x] G-019 `test_five_rows_grid_returns_invalid_size_error_code`
  - [x] G-020 `test_empty_grid_returns_invalid_size_error_code`
  - [x] G-021 `test_jagged_row_lengths_returns_invalid_size_error_code`
  - [x] G-022 `test_valid_4x4_grid_does_not_emit_invalid_size`
  - [x] G-023 `test_invalid_size_skips_blank_count_check`
  - [x] G-024 `test_pydantic_schema_rejects_non_4x4_flat_input`

- [ ] **RED-2b** `tests/boundary/test_ac_fr_01_01_input_validation.py` (예정) → `src/boundary/` · Dual-Track envelope
  - [ ] G-024a `TestNormalFailureReturn::test_none_grid_returns_failure_with_invalid_size_code`
  - [ ] G-024b~ AC-FR-01-02~05 (U-IN/U-OUT/U-FLOW, RED 미작성)

- [x] **RED-3** `tests/boundary/test_input_validator.py` (8건) → S-01 · `validate_input`
  - [x] G-025 TC-A-01 `test_validate_input_rejects_zero_blanks` (AC-01-1)
  - [x] G-026 TC-A-02 `test_validate_input_rejects_one_blank` (AC-01-2)
  - [x] G-027 TC-A-03 `test_validate_input_rejects_three_blanks` (AC-01-3)
  - [x] G-028 TC-A-04 `test_validate_input_rejects_four_blanks` (AC-01-4)
  - [x] G-029 TC-A-05 `test_validate_input_rejects_duplicate_numbers` (AC-01-5)
  - [x] G-030 TC-A-06 `test_validate_input_rejects_value_above_max` (AC-01-6)
  - [x] G-031 TC-A-07 `test_validate_input_rejects_value_below_min` (AC-01-7)
  - [x] G-032 TC-A-08 `test_validate_input_rejects_non_4x4_grid` (SC-BND-VAL-004)

- [x] **RED-4** `tests/control/test_validator.py` (9건) → MVP · INV-1~7
  - [x] G-033 TC-B-01 `test_check_grid_size_rejects_grid_with_three_rows` (INV-1)
  - [x] G-034 TC-B-02 `test_check_number_set_rejects_missing_number` (INV-2)
  - [x] G-035 TC-B-03 `test_check_no_duplicate_rejects_duplicate_number` (INV-3)
  - [x] G-036 TC-B-04 `test_check_row_sums_fails_when_first_row_not_34` (INV-4)
  - [x] G-037 TC-B-05 `test_check_col_sums_fails_when_third_col_not_34` (INV-5)
  - [x] G-038 TC-B-06 `test_check_diag_sums_fails_when_anti_diagonal_not_34` (INV-6)
  - [x] G-039 TC-B-07 `test_validate_accepts_valid_magic_square` (INV-7)
  - [x] G-040 TC-B-08 `test_validate_fails_when_row_sum_invalid` (FR-V-08)
  - [x] G-041 TC-B-09 `test_validate_includes_reason_when_condition_fails` (FR-V-10)

- [x] **RED-5** `tests/control/test_blank_finder.py` (4건) → S-02
  - [x] G-042 TC-B-10 `test_find_blanks_returns_two_coordinates`
  - [x] G-043 TC-B-11 `test_find_blanks_returns_row_col_tuples`
  - [x] G-044 TC-B-12 `test_find_blanks_returns_empty_list_when_no_blanks`
  - [x] G-045 TC-B-13 `test_find_blanks_returns_all_positions_when_more_than_two`

- [x] **RED-6** `tests/control/test_missing_number_finder.py` (4건) → S-03
  - [x] G-046 TC-B-14 `test_find_missing_returns_two_numbers`
  - [x] G-047 TC-B-15 `test_find_missing_returns_sorted_list`
  - [x] G-048 TC-B-16 `test_find_missing_returns_empty_when_complete`
  - [x] G-049 TC-B-17 `test_find_missing_returns_correct_numbers_with_duplicate_in_grid`

- [x] **RED-7** `tests/control/test_solver.py` (5건) → S-05
  - [x] G-050 TC-B-18 `test_solve_returns_small_first_when_small_first_succeeds`
  - [x] G-051 TC-B-19 `test_solve_returns_large_first_when_small_first_fails`
  - [x] G-052 TC-B-20 `test_solve_returns_none_when_both_combinations_fail`
  - [x] G-053 TC-B-21 `test_solve_returns_4x4_grid_without_blanks`
  - [x] G-054 TC-B-22 `test_solve_result_passes_validate`

- [x] **RED-8** `tests/regression/test_us11_regression_protection.py` (1건) → US-11
  - [x] G-055 TC-B-26 `test_us11_all_prd_usecase_test_files_exist`

### GREEN 처리 순서 (구현, G-번호 오름차순)

`green` 브랜치에서 **한 번에 G-번호 1건**(또는 동일 AC 묶음)만 구현한다. 통과 시 체크.

#### 0단계 — Entity (`entity/types.py`)

- [ ] G-001 ~ G-004 도메인 상수 (`GRID_SIZE`, `TARGET_SUM`, `REQUIRED_NUMBERS`)
- [ ] G-005 ~ G-015 `ConditionResult` / `ValidationResult` (`frozen=True`)
- [ ] G-016 `Grid` 타입 별칭

#### 1단계 — Boundary 크기 (`magic_square.boundary` · AC-FR-01-01)

- [ ] G-017 ~ G-021 비정형 격자 → `INVALID_SIZE`, `is_valid=False`
- [ ] G-022 정상 4×4 → `INVALID_SIZE` 미포함
- [ ] G-023 크기 위반 시 `_check_blank_count` 미호출
- [ ] G-024 `GridInputSchema` 16칸 Pydantic 검증

#### 1b단계 — Dual-Track Boundary (`src/boundary/` · 예정)

- [ ] G-024a `grid=None` → `FailureResponse` (`type=ERROR`, `code=INVALID_SIZE`, `message="Grid must be 4x4."`)
- [ ] G-024b~ AC-FR-01-02~05

#### 2단계 — Boundary S-01 (`validate_input` · RED-3 이후)

- [ ] G-025 ~ G-028 빈칸 수 → `blank_count` (AC-01-1~4)
- [ ] G-029 중복 → `duplicate` (AC-01-5)
- [ ] G-030 ~ G-031 범위 → `out_of_range` (AC-01-6~7)
- [ ] G-032 비 4×4 → `grid_size` / `INVALID_SIZE` (SC-BND-VAL-004)

#### 3단계 — Control MVP Validator (INV-1 → INV-7)

- [ ] G-033 INV-1 `_check_grid_size`
- [ ] G-034 INV-2 `_check_number_set`
- [ ] G-035 INV-3 `_check_no_duplicate`
- [ ] G-036 INV-4 `_check_row_sums`
- [ ] G-037 INV-5 `_check_col_sums`
- [ ] G-038 INV-6 `_check_diag_sums`
- [ ] G-039 ~ G-041 `validate()` 통합 · reason · 불가분성

#### 4단계 — Control Phase 2

- [ ] G-042 ~ G-045 BlankFinder (S-02)
- [ ] G-046 ~ G-049 MissingNumberFinder (S-03)
- [ ] G-050 ~ G-054 Solver (S-05)

#### 5단계 — 회귀

- [ ] G-055 US-11 회귀 보호 (G-001~054 완료 후 자동 해소 예상)

### 커버리지 목표

- [ ] Domain Logic: 95%+ (`pip install pytest-cov`)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결

- [x] [`defect_list.md`](defect_list.md) 생성 및 발견 결함 기록 (DL-MSQ-001, 23건)
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인 (G-055)

---

## 참고 문서

- [문제 정의 보고서](Report/01.problem-definition.md)
- [PRD v0.1](Docs/PRD_MagicSquare_v0.1.md)
- [Test Plan v0.1](Docs/TestPlan_MagicSquare_v0.1.md)
