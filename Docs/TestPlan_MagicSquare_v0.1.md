# Magic Square 4×4 — Test Plan

<!-- markdownlint-disable MD060 -->

| 항목 | 내용 |
| --- | --- |
| **문서 ID** | TP-MSQ-001 |
| **버전** | v0.1 |
| **작성일** | 2026-05-29 |
| **상태** | RED 완료 — GREEN 미착수 |
| **연관 PRD** | `Docs/PRD_MagicSquare_v0.1.md` (PRD-MSQ-001 v0.1) |
| **브랜치** | `red` |
| **테스트 프레임워크** | pytest 8.x, AAA 패턴, 커버리지 ≥ 80% |

---

## 1. 문서 목적

본 Test Plan은 PRD v0.1에 정의된 **모든 Use Case**(User Story, Functional Requirement, Gherkin Scenario)를 pytest 테스트로 검증하기 위한 계획·매핑·실행 가이드이다.

Traceability Rule을 따른다.

```text
Concept → Invariant → Contract → Test → Implementation
```

---

## 2. 테스트 전략

### 2.1 TDD 단계

| 단계 | 테스트 | 구현 | 본 문서 상태 |
| --- | --- | --- | --- |
| **RED** | `tests/` 작성, 실패 확인 | `src/` 수정 금지 | ✅ 완료 |
| **GREEN** | 수정 금지 | 최소 구현 | ⬜ 미착수 |
| **REFACTOR** | GREEN 유지 | 구조 개선 | ⬜ 미착수 |

### 2.2 품질 규칙

- **AAA 패턴** — `# Arrange` / `# Act` / `# Assert` 주석 필수
- **함수명** — `test_<대상>_<조건>_<기대결과>`
- **하나의 테스트 = 하나의 동작**
- **Fixture** — 반복 Arrange는 `tests/conftest.py`에 정의
- **금지** — 테스트 조건 완화, `pass` 본문, 불변 조건 혼합 검증

### 2.3 범위 구분

| 구분 | PRD § | 테스트 파일 | 테스트 수 | 구현 대상 |
| --- | --- | --- | ---: | --- |
| **MVP** | §6.1, §9.1 | `tests/control/test_validator.py` | 9 | `control/validator.py` |
| **Phase 2 — Boundary** | §6.2, §9.2 | `tests/boundary/test_input_validator.py` | 8 | `boundary/input_validator.py` |
| **Phase 2 — Control** | §6.2, §9.3 | `tests/control/test_blank_finder.py` | 4 | `control/blank_finder.py` |
| | | `tests/control/test_missing_number_finder.py` | 4 | `control/missing_number_finder.py` |
| | | `tests/control/test_solver.py` | 5 | `control/solver.py` |
| **회귀 보호** | §7.5 US-11 | `tests/regression/test_us11_regression_protection.py` | 1 | — |
| **선행 Entity** | §8.2 | `tests/entity/test_types.py` | 16 | `entity/types.py` ✅ |
| **합계 (Use Case)** | | | **31** | |
| **합계 (전체)** | | | **47** | |

> **S-04** (마방진 검증)는 Phase 2 Story이나 API가 MVP `validate()`와 동일하므로 `test_validator.py`에서 커버한다.

---

## 3. Traceability Matrix (요약)

| PRD ID | Story / FR | Invariant | Gherkin | 테스트 파일 | 테스트 함수 |
| --- | --- | --- | --- | --- | --- |
| FR-V-02 | US-04 | INV-1 | — | `test_validator.py` | `test_check_grid_size_rejects_grid_with_three_rows` |
| FR-V-03 | US-04 | INV-2 | — | `test_validator.py` | `test_check_number_set_rejects_missing_number` |
| FR-V-04 | US-04 | INV-3 | — | `test_validator.py` | `test_check_no_duplicate_rejects_duplicate_number` |
| FR-V-05 | US-04 | INV-4 | — | `test_validator.py` | `test_check_row_sums_fails_when_first_row_not_34` |
| FR-V-06 | US-04 | INV-5 | — | `test_validator.py` | `test_check_col_sums_fails_when_third_col_not_34` |
| FR-V-07 | US-04 | INV-6 | — | `test_validator.py` | `test_check_diag_sums_fails_when_anti_diagonal_not_34` |
| FR-V-01, FR-V-08~10 | US-04 | INV-7 | — | `test_validator.py` | `test_validate_*` (3건) |
| AC-01-1~4, FR-B-01 | S-01 | INV-2 | SC-BND-VAL-001 | `test_input_validator.py` | `test_validate_input_rejects_*_blanks` (4건) |
| AC-01-5, FR-B-02 | S-01 | INV-3 | SC-BND-VAL-002 | `test_input_validator.py` | `test_validate_input_rejects_duplicate_numbers` |
| AC-01-6~7, FR-B-03 | S-01 | INV-2 | SC-BND-VAL-003 | `test_input_validator.py` | `test_validate_input_rejects_value_*` (2건) |
| — | S-01 | INV-1 | SC-BND-VAL-004 | `test_input_validator.py` | `test_validate_input_rejects_non_4x4_grid` |
| AC-02-1~5 | S-02 | INV-1 | SC-DOM-BLK-001 | `test_blank_finder.py` | `test_find_blanks_*` (4건) |
| AC-03-1~5 | S-03 | INV-2,3 | SC-DOM-MSN-001 | `test_missing_number_finder.py` | `test_find_missing_*` (4건) |
| AC-05-1~8 | S-05 | INV-1~7 | SC-DOM-SOL-001~003 | `test_solver.py` | `test_solve_*` (5건) |
| — | US-11 | — | — | `test_us11_regression_protection.py` | `test_us11_all_prd_usecase_test_files_exist` |

---

## 4. MVP — Control / Validator (9건)

**파일:** `tests/control/test_validator.py`  
**대상 API:** `magic_square.control.validator`  
**구현 예정:** `src/magic_square/control/validator.py`  
**TDD 순서:** PRD §10.5 — INV-1 → INV-7

| # | 테스트 함수 | FR | INV | Fixture | 기대 결과 (Assert) |
| ---: | --- | --- | --- | --- | --- |
| 1 | `test_check_grid_size_rejects_grid_with_three_rows` | FR-V-02 | INV-1 | `invalid_grid_wrong_row_count` | `passed=False`, `name="격자 크기"`, `reason="행 또는 열의 수가 4가 아님"` |
| 2 | `test_check_number_set_rejects_missing_number` | FR-V-03 | INV-2 | `invalid_grid_missing_number` | `passed=False`, `name="숫자 집합"`, `reason="허용되지 않는 숫자 포함 또는 필수 숫자 누락"` |
| 3 | `test_check_no_duplicate_rejects_duplicate_number` | FR-V-04 | INV-3 | `invalid_grid_duplicate_number` | `passed=False`, `name="중복 금지"`, `reason="중복 숫자 존재: [5]"` |
| 4 | `test_check_row_sums_fails_when_first_row_not_34` | FR-V-05 | INV-4 | `invalid_grid_wrong_row_sum` | `passed=False`, `name="행 합"`, `reason="1번 행의 합이 34가 아님 (실제: 33)"` |
| 5 | `test_check_col_sums_fails_when_third_col_not_34` | FR-V-06 | INV-5 | `invalid_grid_wrong_col_sum` | `passed=False`, `name="열 합"`, `reason="3번 열의 합이 34가 아님 (실제: 35)"` |
| 6 | `test_check_diag_sums_fails_when_anti_diagonal_not_34` | FR-V-07 | INV-6 | `invalid_grid_wrong_diagonal_sum` | `passed=False`, `name="대각선 합"`, `reason="반 대각선의 합이 34가 아님 (실제: 35)"` |
| 7 | `test_validate_accepts_valid_magic_square` | FR-V-01, FR-V-09 | INV-7 | `valid_magic_square` | `is_valid=True`, `failed_conditions=[]` |
| 8 | `test_validate_fails_when_row_sum_invalid` | FR-V-08 | INV-7 | `invalid_grid_wrong_row_sum` | `is_valid=False`, `len(failed_conditions) >= 1` |
| 9 | `test_validate_includes_reason_when_condition_fails` | FR-V-10 | — | `invalid_grid_wrong_row_sum` | `is_valid=False`, 모든 failed 항목에 `reason is not None` |

---

## 5. Phase 2 — Boundary / InputValidator (8건)

**파일:** `tests/boundary/test_input_validator.py`  
**대상 API:** `magic_square.boundary.input_validator.validate_input`  
**구현 예정:** `src/magic_square/boundary/input_validator.py`

| # | 테스트 함수 | AC | FR | Gherkin | Fixture | 기대 결과 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `test_validate_input_rejects_zero_blanks` | AC-01-1 | FR-B-01 | SC-BND-VAL-001 | `valid_magic_square` | `is_valid=False`, `"blank_count" in error_codes` |
| 2 | `test_validate_input_rejects_one_blank` | AC-01-2 | FR-B-01 | SC-BND-VAL-001 | `grid_one_blank` | 동일 |
| 3 | `test_validate_input_rejects_three_blanks` | AC-01-3 | FR-B-01 | SC-BND-VAL-001 | `grid_three_blanks` | 동일 |
| 4 | `test_validate_input_rejects_four_blanks` | AC-01-4 | FR-B-01 | SC-BND-VAL-001 | `grid_four_blanks` | 동일 |
| 5 | `test_validate_input_rejects_duplicate_numbers` | AC-01-5 | FR-B-02 | SC-BND-VAL-002 | `grid_with_duplicate_and_two_blanks` | `"duplicate" in error_codes` |
| 6 | `test_validate_input_rejects_value_above_max` | AC-01-6 | FR-B-03 | SC-BND-VAL-003 | `grid_with_value_above_max` | `"out_of_range" in error_codes` |
| 7 | `test_validate_input_rejects_value_below_min` | AC-01-7 | FR-B-03 | SC-BND-VAL-003 | `grid_with_value_below_min` | `"out_of_range" in error_codes` |
| 8 | `test_validate_input_rejects_non_4x4_grid` | — | — | SC-BND-VAL-004 | `invalid_grid_wrong_row_count` | `"grid_size" in error_codes` |

---

## 6. Phase 2 — Control / BlankFinder (4건)

**파일:** `tests/control/test_blank_finder.py`  
**대상 API:** `magic_square.control.blank_finder.find_blanks`  
**구현 예정:** `src/magic_square/control/blank_finder.py`

| # | 테스트 함수 | AC | Gherkin | Fixture | 기대 결과 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `test_find_blanks_returns_two_coordinates` | AC-02-1 | SC-DOM-BLK-001 | `grid_two_blanks` | `len==2`, `[(2,2), (3,2)]` |
| 2 | `test_find_blanks_returns_row_col_tuples` | AC-02-2, AC-02-3 | SC-DOM-BLK-001 | `grid_two_blanks` | 각 요소가 `(row, col)` tuple |
| 3 | `test_find_blanks_returns_empty_list_when_no_blanks` | AC-02-4 | SC-DOM-BLK-001 | `valid_magic_square` | `[]` |
| 4 | `test_find_blanks_returns_all_positions_when_more_than_two` | AC-02-5 | SC-DOM-BLK-001 | `grid_three_blanks_for_finder` | `len==3`, 3개 좌표 포함 |

---

## 7. Phase 2 — Control / MissingNumberFinder (4건)

**파일:** `tests/control/test_missing_number_finder.py`  
**대상 API:** `magic_square.control.missing_number_finder.find_missing_numbers`  
**구현 예정:** `src/magic_square/control/missing_number_finder.py`

| # | 테스트 함수 | AC | Gherkin | Fixture | 기대 결과 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `test_find_missing_returns_two_numbers` | AC-03-1 | SC-DOM-MSN-001 | `grid_two_blanks` | `len==2`, `{7, 14}` |
| 2 | `test_find_missing_returns_sorted_list` | AC-03-2, AC-03-3 | SC-DOM-MSN-001 | `grid_two_blanks` | `list[int]`, 오름차순 |
| 3 | `test_find_missing_returns_empty_when_complete` | AC-03-4 | SC-DOM-MSN-001 | `valid_magic_square` | `[]` |
| 4 | `test_find_missing_returns_correct_numbers_with_duplicate_in_grid` | AC-03-5 | SC-DOM-MSN-001 | `grid_duplicate_for_missing_finder` | `11 in missing` |

---

## 8. Phase 2 — Control / Solver (5건)

**파일:** `tests/control/test_solver.py`  
**대상 API:** `magic_square.control.solver.solve`  
**구현 예정:** `src/magic_square/control/solver.py`

| # | 테스트 함수 | AC | Gherkin | Fixture | 기대 결과 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `test_solve_returns_small_first_when_small_first_succeeds` | AC-05-1 | SC-DOM-SOL-002 | `grid_two_blanks` | `result is not None`, 빈칸(0) 없음 |
| 2 | `test_solve_returns_large_first_when_small_first_fails` | AC-05-2, AC-05-3 | SC-DOM-SOL-001 | `grid_two_blanks` | `result[2][2]==14`, `result[3][2]==7` |
| 3 | `test_solve_returns_none_when_both_combinations_fail` | AC-05-4 | SC-DOM-SOL-003 | `grid_unsolvable_two_blanks` | `result is None` |
| 4 | `test_solve_returns_4x4_grid_without_blanks` | AC-05-5, AC-05-6 | — | `grid_two_blanks` | 4×4, `0` 없음 |
| 5 | `test_solve_result_passes_validate` | AC-05-7, AC-05-8 | SC-DOM-SOL-001 | `grid_two_blanks` | `validate(result).is_valid is True` |

**SC-DOM-SOL-001 수치 검증 (참고):**

- 입력 격자: `grid_two_blanks` (빈칸 `(2,2)`, `(3,2)`, 누락 숫자 `{7, 14}`)
- small-first `(7, 14)` → 행 합 41 ❌
- large-first `(14, 7)` → 마방진 완성 ✅
- solve() flat 출력 기대값: `[3, 3, 6, 4, 4, 1]`

---

## 9. 회귀 보호 — US-11 (1건)

**파일:** `tests/regression/test_us11_regression_protection.py`  
**Story:** US-11 / Stage 5 Regression Protection

| # | 테스트 함수 | 목적 | 기대 결과 |
| ---: | --- | --- | --- |
| 1 | `test_us11_all_prd_usecase_test_files_exist` | PRD Use Case별 RED 테스트 파일 존재 확인 | 5개 테스트 파일 `Path.is_file()` |

**검증 대상 파일:**

1. `tests/control/test_validator.py`
2. `tests/boundary/test_input_validator.py`
3. `tests/control/test_blank_finder.py`
4. `tests/control/test_missing_number_finder.py`
5. `tests/control/test_solver.py`

---

## 10. 선행 Entity 테스트 (16건)

**파일:** `tests/entity/test_types.py`  
**대상:** `src/magic_square/entity/types.py`  
**상태:** ✅ GREEN (Entity 선행 구현 완료)

| 클래스 | 테스트 수 | 검증 대상 |
| --- | ---: | --- |
| `TestDomainConstants` | 4 | `GRID_SIZE`, `TARGET_SUM`, `REQUIRED_NUMBERS` |
| `TestConditionResult` | 5 | frozen, name, passed, reason |
| `TestValidationResult` | 6 | is_valid, failed_conditions, 불가분성 |
| `TestGridTypeAlias` | 1 | 4×4 Grid 타입 수용 |

---

## 11. Fixture 목록

**파일:** `tests/conftest.py`

### 11.1 MVP / 공통

| Fixture | 용도 |
| --- | --- |
| `valid_magic_square` | 완전한 4×4 마방진 (모든 INV 충족) |
| `invalid_grid_wrong_row_count` | 3행 격자 (INV-1, SC-BND-VAL-004) |
| `invalid_grid_wrong_col_count` | 5열 격자 (INV-1) |
| `invalid_grid_missing_number` | 숫자 7 누락·17 포함 (INV-2) |
| `invalid_grid_duplicate_number` | 숫자 5 중복 (INV-3) |
| `invalid_grid_wrong_row_sum` | 1행 합 33 (INV-4, INV-7) |
| `invalid_grid_wrong_col_sum` | 3열 합 35 (INV-5) |
| `invalid_grid_wrong_diagonal_sum` | 반대각선 합 35 (INV-6) |
| `passed_condition` | 통과 `ConditionResult` |
| `failed_condition` | 실패 `ConditionResult` |
| `valid_validation_result` | `is_valid=True` |
| `invalid_validation_result` | `is_valid=False` + failed 목록 |

### 11.2 Phase 2 전용

| Fixture | 용도 |
| --- | --- |
| `grid_two_blanks` | 빈칸 2개 — BlankFinder, MissingNumberFinder, Solver |
| `grid_one_blank` | 빈칸 1개 — AC-01-2 |
| `grid_three_blanks` | 빈칸 3개 — AC-01-3 |
| `grid_four_blanks` | 빈칸 4개 — AC-01-4 |
| `grid_with_duplicate_and_two_blanks` | 중복 + 빈칸 2 — AC-01-5 |
| `grid_with_value_above_max` | 17 포함 — AC-01-6 |
| `grid_with_value_below_min` | -1 포함 — AC-01-7 |
| `grid_three_blanks_for_finder` | 빈칸 3개 — AC-02-5 |
| `grid_duplicate_for_missing_finder` | 중복 + 빈칸 2 — AC-03-5 |
| `grid_unsolvable_two_blanks` | 해 불가 격자 — SC-DOM-SOL-003 |

---

## 12. 테스트 실행

### 12.1 명령어

```bash
# Use Case RED 테스트 전체 (현재: collection ERROR = RED)
python -m pytest tests/control tests/boundary tests/regression -v --no-cov

# MVP만
python -m pytest tests/control/test_validator.py -v --no-cov

# Entity (GREEN)
python -m pytest tests/entity -v --no-cov

# 커버리지 포함 (GREEN 단계 이후)
python -m pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80
```

### 12.2 RED 단계 검증 결과 (2026-05-29)

| 구분 | 결과 | 원인 |
| --- | --- | --- |
| Use Case 31건 | **5 errors (collection)** | `ModuleNotFoundError: magic_square.control` / `magic_square.boundary` |
| Entity 16건 | **17 passed** | `entity/types.py` 구현 완료 |
| US-11 1건 | **passed** | 테스트 파일 존재 검증 (import 불필요) |

→ Use Case 테스트는 **구현 부재로 인한 RED** 상태가 정상이다.

---

## 13. GREEN 진입 순서

PRD §10.5 TDD 실행 순서 및 ECB 의존 방향에 따라 아래 순서로 GREEN을 진행한다.

| 순서 | 구현 파일 | 통과 목표 테스트 | 테스트 수 |
| ---: | --- | --- | ---: |
| 1 | `control/validator.py` | `test_validator.py` | 9 |
| 2 | `boundary/input_validator.py` | `test_input_validator.py` | 8 |
| 3 | `control/blank_finder.py` | `test_blank_finder.py` | 4 |
| 4 | `control/missing_number_finder.py` | `test_missing_number_finder.py` | 4 |
| 5 | `control/solver.py` | `test_solver.py` | 5 |

각 단계: `red` → `green` 브랜치 → 최소 구현 → pytest GREEN → `refactoring` → `developer` 머지.

---

## 14. 미커버 / 후속 항목

| 항목 | PRD 참조 | 비고 |
| --- | --- | --- |
| 경계 케이스 추가 | `Report/02.design.md` §6-3 | 5×5, 빈 리스트, 행 길이 불일치 등 — GREEN 후 REFACTOR 단계에서 보강 |
| `BLANK_COUNT`, `OUTPUT_LENGTH` 상수 | PRD §8.2 | Phase 2 GREEN 전 `entity/types.py` 추가 |
| SC-BND-VAL-003 `value=1` 경계값 | PRD §14 | Gherkin·테스트 보강 예정 |
| Stage 5 전용 Story | PRD §7.5 | US-11로 대체, v0.2 검토 |

---

## 15. 디렉토리 구조 (테스트)

```text
tests/
├── conftest.py                          # 공유 fixture
├── entity/
│   └── test_types.py                    # Entity 16건 (GREEN)
├── control/
│   ├── test_validator.py                # MVP 9건 (RED)
│   ├── test_blank_finder.py             # S-02 4건 (RED)
│   ├── test_missing_number_finder.py    # S-03 4건 (RED)
│   └── test_solver.py                   # S-05 5건 (RED)
├── boundary/
│   └── test_input_validator.py          # S-01 8건 (RED)
└── regression/
    └── test_us11_regression_protection.py  # US-11 1건
```

---

*본 Test Plan은 PRD v0.1 및 `red` 브랜치 RED 테스트 작성 결과를 바탕으로 작성되었습니다.*
