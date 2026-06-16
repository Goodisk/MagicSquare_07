# MagicSquare_021 — 결함 목록 (Defect List)

| 항목 | 내용 |
| --- | --- |
| **문서 ID** | DL-MSQ-001 |
| **작성일** | 2026-05-29 |
| **작성** | QA 리드 |
| **브랜치** | `red` (GREEN 미착수) |
| **기준 실행** | `pytest tests/ -v --tb=no --no-cov` |
| **연관 문서** | [Test Plan](Docs/TestPlan_MagicSquare_v0.1.md), [PRD](Docs/PRD_MagicSquare_v0.1.md) |

---

## 실행 요약

| 구분 | 수치 |
| --- | ---: |
| 수집·실행된 테스트 | 39 |
| 수집 오류 (Entity) | 1 파일 (`tests/entity/test_types.py`, 16건 미수집) |
| 실패 (FAILED) | 39 |
| 통과 (PASSED) | 0 |

> **참고:** RED 단계에서는 구현 스텁이 의도적으로 실패를 유발한다. 본 목록은 GREEN 착수 전 **기대 동작 대비 실제 동작**을 추적하기 위한 QA 기록이다.

---

## 결함 테이블

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEF-001 | Critical | TC-B-23~25 / FR-Entity | `pytest tests/entity/test_types.py` | `GRID_SIZE`, `TARGET_SUM`, `REQUIRED_NUMBERS` import 성공 | `ImportError: cannot import name 'GRID_SIZE'` | `entity/types.py`에 도메인 상수 미정의 | `Final` 상수 3종 export (`GRID_SIZE=4`, `TARGET_SUM=34`, `REQUIRED_NUMBERS=frozenset(range(1,17))`) |
| DEF-002 | High | TC-B-24 / PRD §8.2 | `ConditionResult(name="격자 크기", passed=True)` 후 `result.passed = False` | `AttributeError` (불변) | 필드 변경 성공 (mutable) | `@dataclass`만 사용, `frozen=True` 누락 | `ConditionResult`, `ValidationResult`를 `frozen=True` dataclass로 변경 |
| DEF-003 | Critical | AC-FR-01-01 | 3행 격자로 `validate_input(grid)` 호출 (`invalid_grid_wrong_row_count`) | `is_valid=False`, `INVALID_SIZE ∈ error_codes` | `is_valid=True`, `error_codes=[INVALID_SIZE]` | `validate_input` RED 스텁이 항상 `is_valid=True` 반환 | 4×4 검증 후 `is_valid=False` 및 오류 코드 설정 |
| DEF-004 | High | AC-FR-01-01 | 유효 4×4 격자로 `validate_input(valid_magic_square)` | `INVALID_SIZE ∉ error_codes` | `INVALID_SIZE ∈ error_codes` | 비정상 격자에도 동일 스텁 응답 | 정상 4×4일 때 `INVALID_SIZE` 미부여 |
| DEF-005 | High | AC-FR-01-01 | `@patch` 후 비정상 격자로 `validate_input` | `_check_blank_count` 미호출 | (호출 여부 검증 불가 — `is_valid` 선실패) | 격자 크기 선검증·조기 반환 미구현 | 크기 위반 시 `blank_count` 등 후속 검사 스킵 |
| DEF-006 | High | AC-FR-01-01 | `GridInputSchema.model_validate({"cells": list(range(1,13))})` | `ValidationError`, 메시지에 `INVALID_SIZE` | 예외 없음 (검증 통과) | `GridInputSchema` RED 스텁이 길이 제약 없음 | Pydantic `Field(min_length=16, max_length=16)` 등 16칸 고정 검증 |
| DEF-007 | Critical | AC-01-1~4 / SC-BND-VAL-001 | 완성 격자·빈칸 1·3·4개 각각 `validate_input` | `is_valid=False`, `"blank_count" in error_codes` | `is_valid=True`, `INVALID_SIZE`만 존재 | 빈칸 수 검증·오류 코드 미구현; `_check_blank_count`는 `NotImplementedError` | 빈칸(0) 개수 규칙(정확히 2개) 및 `blank_count` 코드 반환 |
| DEF-008 | High | AC-01-5 / SC-BND-VAL-002 | `grid_with_duplicate_and_two_blanks`로 `validate_input` | `"duplicate" in error_codes` | `INVALID_SIZE`만 반환 | 중복 검증 로직 없음 | 1~16 범위 내 중복 탐지 후 `duplicate` 코드 |
| DEF-009 | High | AC-01-6~7 / SC-BND-VAL-003 | 17 이상·0 이하 값 격자로 `validate_input` | `"out_of_range" in error_codes` | `INVALID_SIZE`만 반환 | 범위 검증 로직 없음 | 빈칸(0) 제외 1~16 범위 위반 시 `out_of_range` |
| DEF-010 | High | SC-BND-VAL-004 | `invalid_grid_wrong_row_count`로 `validate_input` | `"grid_size" in error_codes` (또는 `INVALID_SIZE`) | `INVALID_SIZE`만, `is_valid=True` | 4×4 판별과 S-01 오류 코드 매핑 미구현 | 비정형 격자 시 `grid_size`/`INVALID_SIZE` 및 `is_valid=False` |
| DEF-011 | Critical | FR-V-02 / INV-1 | 3행 격자로 `_check_grid_size(grid)` | `passed=False`, `name="격자 크기"`, `reason`에 크기 설명 | `passed=True`, `name="wrong"`, `reason=None` | Control validator RED 스텁이 항상 통과 | 행·열 수 4 검사 및 PRD reason 문자열 |
| DEF-012 | Critical | FR-V-03 / INV-2 | 숫자 7 누락·17 포함 격자로 `_check_number_set` | `passed=False`, `name="숫자 집합"` | `passed=True`, `name="wrong"` | 숫자 집합 검증 미구현 | `REQUIRED_NUMBERS` 대비 포함·누락 검사 |
| DEF-013 | Critical | FR-V-04 / INV-3 | 숫자 5 중복 격자로 `_check_no_duplicate` | `passed=False`, `reason="중복 숫자 존재: [5]"` | `passed=True`, `name="wrong"` | 중복 검증 미구현 | 중복 값 목록을 reason에 포함 |
| DEF-014 | Critical | FR-V-05 / INV-4 | 1행 합 33 격자로 `_check_row_sums` | `passed=False`, `name="행 합"`, 실제 합 in reason | `passed=True` | 행 합 검증 미구현 | 각 행 `TARGET_SUM` 비교 |
| DEF-015 | Critical | FR-V-06 / INV-5 | 3열 합 35 격자로 `_check_col_sums` | `passed=False`, `name="열 합"` | `passed=True` | 열 합 검증 미구현 | 열별 합 `TARGET_SUM` 비교 |
| DEF-016 | Critical | FR-V-07 / INV-6 | 반대각선 합 35 격자로 `_check_diag_sums` | `passed=False`, `name="대각선 합"` | `passed=True` | 대각선 합 검증 미구현 | 주·반대각선 합 검사 |
| DEF-017 | Critical | FR-V-09 / INV-7 | `validate(valid_magic_square)` | `is_valid=True`, `failed_conditions=[]` | `is_valid=True`, `failed_conditions=[ConditionResult(passed=False,...)]` | `validate()` 스텁이 유효 격자에 실패 항목 삽입 | 7개 조건 모두 통과 시 빈 실패 목록 |
| DEF-018 | Critical | FR-V-08 / INV-7 | 행 합 위반 격자로 `validate` | `is_valid=False`, `len(failed_conditions) >= 1` | `is_valid=False`, `failed_conditions=[]` (3행 등) 또는 `is_valid=True`+실패목록 (4×4 위반) | `validate()` 분기가 불변 조건 결과와 불일치 | `_check_*` 결과 집계·불가분성(`is_valid`) 반영 |
| DEF-019 | High | FR-V-10 | 행 합 위반 격자로 `validate` | 모든 `failed_conditions` 항목 `reason is not None` | `reason=None` | 실패 reason 미기록 | 각 `_check_*` 실패 시 PRD 형식 reason 생성 |
| DEF-020 | High | AC-02-1~5 / SC-DOM-BLK-001 | `find_blanks(grid_two_blanks)` | `[(2,2),(3,2)]`, 길이 2, `(row,col)` 2-tuple | `[(99,99,99)]`, 길이 1, 3-tuple | `blank_finder` RED 스텁 | `0` 셀 좌표를 `(row,col)`로 스캔 반환 |
| DEF-021 | High | AC-03-1~5 / SC-DOM-MSN-001 | `find_missing_numbers(grid_two_blanks)` | `{7,14}`, 오름차순 `[7,14]` | `[99,98,97]` (개수·값·정렬 모두 불일치) | `missing_number_finder` RED 스텁 | `REQUIRED_NUMBERS - 격자 값` 집합, 정렬 반환 |
| DEF-022 | Critical | AC-05-1~8 / SC-DOM-SOL-001~003 | `solve(grid_two_blanks)` 등 | small-first/large-first/None·4×4·`validate` 통과 | `[[0]]` (1×1, 빈칸 0 포함) | `solver` RED 스텁 | 조합 탐색·백트래킹 GREEN 구현 |
| DEF-023 | Medium | US-11 / TC-B-26 | `pytest tests/regression/test_us11_regression_protection.py` | `hasattr(entity_types, "GRID_SIZE")` 및 `== 4` | `hasattr` False → AssertionError | Entity GREEN(상수) 미완료로 회귀 전제 불충족 | DEF-001 해결 시 자동 해소 |

---

## 심각도 정의

| Severity | 기준 |
| --- | --- |
| **Critical** | 테스트 수집 불가, 핵심 API 전면 오동작, INV/FR 미충족 |
| **High** | 부분 시나리오 실패, 계약(필드·코드·reason) 불일치 |
| **Medium** | 회귀·문서화·전제 조건 불일치 (기능 스텁과 연동) |

---

## 결함 ↔ 테스트 매핑 (요약)

| 결함 ID | 대표 테스트 |
| --- | --- |
| DEF-001~002 | `tests/entity/test_types.py` (16건, 수집 오류 포함) |
| DEF-003~006 | `tests/boundary/test_ac_fr_01_01_invalid_size.py` (8건) |
| DEF-007~010 | `tests/boundary/test_input_validator.py` (8건) |
| DEF-011~019 | `tests/control/test_validator.py` (9건) |
| DEF-020 | `tests/control/test_blank_finder.py` (4건) |
| DEF-021 | `tests/control/test_missing_number_finder.py` (4건) |
| DEF-022 | `tests/control/test_solver.py` (5건) |
| DEF-023 | `tests/regression/test_us11_regression_protection.py` (1건) |

---

## GREEN 착수 우선순위 (권장)

1. **Entity** — DEF-001, DEF-002 (다른 레이어 상수·타입 의존)
2. **Boundary** — DEF-003~010, DEF-006 (입력 게이트)
3. **Control Validator** — DEF-011~019 (MVP INV-1~7)
4. **Control Phase 2** — DEF-020~022
5. **회귀** — DEF-023

---

## 변경 이력

| 날짜 | 변경 |
| --- | --- |
| 2026-05-29 | 초판 작성 — RED 스텁 대비 23건 결함 등록 (`pytest` 39 FAILED + Entity 수집 오류) |
