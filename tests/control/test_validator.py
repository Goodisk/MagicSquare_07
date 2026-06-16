"""Control 레이어 validator 테스트 — MVP FR-V / INV-1~7 / US-04."""

from magic_square.control.validator import (
    _check_col_sums,
    _check_diag_sums,
    _check_grid_size,
    _check_no_duplicate,
    _check_number_set,
    _check_row_sums,
    validate,
)
from magic_square.entity.types import ConditionResult, Grid, ValidationResult


def test_check_grid_size_rejects_grid_with_three_rows(
    invalid_grid_wrong_row_count: Grid,
) -> None:
    """FR-V-02 / INV-1: 3행 격자는 격자 크기 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_wrong_row_count

    # Act
    result: ConditionResult = _check_grid_size(grid)

    # Assert
    assert result.passed is False
    assert result.name == "격자 크기"
    assert result.reason == "행 또는 열의 수가 4가 아님"


def test_check_number_set_rejects_missing_number(
    invalid_grid_missing_number: Grid,
) -> None:
    """FR-V-03 / INV-2: 필수 숫자 누락 시 숫자 집합 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_missing_number

    # Act
    result: ConditionResult = _check_number_set(grid)

    # Assert
    assert result.passed is False
    assert result.name == "숫자 집합"
    assert result.reason == "허용되지 않는 숫자 포함 또는 필수 숫자 누락"


def test_check_no_duplicate_rejects_duplicate_number(
    invalid_grid_duplicate_number: Grid,
) -> None:
    """FR-V-04 / INV-3: 중복 숫자가 있으면 중복 금지 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_duplicate_number

    # Act
    result: ConditionResult = _check_no_duplicate(grid)

    # Assert
    assert result.passed is False
    assert result.name == "중복 금지"
    assert result.reason == "중복 숫자 존재: [5]"


def test_check_row_sums_fails_when_first_row_not_34(
    invalid_grid_wrong_row_sum: Grid,
) -> None:
    """FR-V-05 / INV-4: 행 합이 34가 아니면 행 합 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_wrong_row_sum

    # Act
    result: ConditionResult = _check_row_sums(grid)

    # Assert
    assert result.passed is False
    assert result.name == "행 합"
    assert result.reason == "1번 행의 합이 34가 아님 (실제: 33)"


def test_check_col_sums_fails_when_third_col_not_34(
    invalid_grid_wrong_col_sum: Grid,
) -> None:
    """FR-V-06 / INV-5: 열 합이 34가 아니면 열 합 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_wrong_col_sum

    # Act
    result: ConditionResult = _check_col_sums(grid)

    # Assert
    assert result.passed is False
    assert result.name == "열 합"
    assert result.reason == "3번 열의 합이 34가 아님 (실제: 35)"


def test_check_diag_sums_fails_when_anti_diagonal_not_34(
    invalid_grid_wrong_diagonal_sum: Grid,
) -> None:
    """FR-V-07 / INV-6: 대각선 합이 34가 아니면 대각선 합 조건을 실패로 판정한다."""
    # Arrange
    grid = invalid_grid_wrong_diagonal_sum

    # Act
    result: ConditionResult = _check_diag_sums(grid)

    # Assert
    assert result.passed is False
    assert result.name == "대각선 합"
    assert result.reason == "반 대각선의 합이 34가 아님 (실제: 35)"


def test_validate_accepts_valid_magic_square(
    valid_magic_square: Grid,
) -> None:
    """FR-V-01 / FR-V-09 / US-04: 유효한 마방진은 is_valid=True를 반환한다."""
    # Arrange
    grid = valid_magic_square

    # Act
    result: ValidationResult = validate(grid)

    # Assert
    assert result.is_valid is True
    assert result.failed_conditions == []


def test_validate_fails_when_row_sum_invalid(
    invalid_grid_wrong_row_sum: Grid,
) -> None:
    """FR-V-08 / INV-7: 하나의 조건이라도 실패하면 is_valid=False이다."""
    # Arrange
    grid = invalid_grid_wrong_row_sum

    # Act
    result: ValidationResult = validate(grid)

    # Assert
    assert result.is_valid is False
    assert len(result.failed_conditions) >= 1


def test_validate_includes_reason_when_condition_fails(
    invalid_grid_wrong_row_sum: Grid,
) -> None:
    """FR-V-10: 실패 조건에는 사람이 읽을 수 있는 reason이 포함된다."""
    # Arrange
    grid = invalid_grid_wrong_row_sum

    # Act
    result: ValidationResult = validate(grid)

    # Assert
    assert result.is_valid is False
    assert all(f.reason is not None for f in result.failed_conditions)
