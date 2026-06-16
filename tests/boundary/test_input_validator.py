"""Boundary 레이어 InputValidator 테스트 — S-01 / FR-B / SC-BND-VAL."""

from magic_square.boundary.input_validator import validate_input
from magic_square.entity.types import Grid


def test_validate_input_rejects_zero_blanks(valid_magic_square: Grid) -> None:
    """AC-01-1 / FR-B-01 / SC-BND-VAL-001: 빈칸 0개이면 blank_count 오류."""
    # Arrange
    grid = valid_magic_square

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "blank_count" in result.error_codes


def test_validate_input_rejects_one_blank(grid_one_blank: Grid) -> None:
    """AC-01-2 / FR-B-01: 빈칸 1개이면 blank_count 오류."""
    # Arrange
    grid = grid_one_blank

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "blank_count" in result.error_codes


def test_validate_input_rejects_three_blanks(grid_three_blanks: Grid) -> None:
    """AC-01-3 / FR-B-01: 빈칸 3개이면 blank_count 오류."""
    # Arrange
    grid = grid_three_blanks

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "blank_count" in result.error_codes


def test_validate_input_rejects_four_blanks(grid_four_blanks: Grid) -> None:
    """AC-01-4 / FR-B-01: 빈칸 4개이면 blank_count 오류."""
    # Arrange
    grid = grid_four_blanks

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "blank_count" in result.error_codes


def test_validate_input_rejects_duplicate_numbers(
    grid_with_duplicate_and_two_blanks: Grid,
) -> None:
    """AC-01-5 / FR-B-02 / SC-BND-VAL-002: 중복 숫자이면 duplicate 오류."""
    # Arrange
    grid = grid_with_duplicate_and_two_blanks

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "duplicate" in result.error_codes


def test_validate_input_rejects_value_above_max(
    grid_with_value_above_max: Grid,
) -> None:
    """AC-01-6 / FR-B-03 / SC-BND-VAL-003: 17 이상이면 out_of_range 오류."""
    # Arrange
    grid = grid_with_value_above_max

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "out_of_range" in result.error_codes


def test_validate_input_rejects_value_below_min(
    grid_with_value_below_min: Grid,
) -> None:
    """AC-01-7 / FR-B-03: 0 이하(빈칸 제외)이면 out_of_range 오류."""
    # Arrange
    grid = grid_with_value_below_min

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "out_of_range" in result.error_codes


def test_validate_input_rejects_non_4x4_grid(
    invalid_grid_wrong_row_count: Grid,
) -> None:
    """SC-BND-VAL-004: 4x4가 아닌 격자는 입력 검증을 실패한다."""
    # Arrange
    grid = invalid_grid_wrong_row_count

    # Act
    result = validate_input(grid)

    # Assert
    assert result.is_valid is False
    assert "grid_size" in result.error_codes
