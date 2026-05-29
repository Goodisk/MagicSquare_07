"""Control 레이어 Solver 테스트 — S-05 / SC-DOM-SOL-001~003."""

from magic_square.control.solver import solve
from magic_square.control.validator import validate
from magic_square.entity.types import Grid


def test_solve_returns_small_first_when_small_first_succeeds(
    grid_two_blanks: Grid,
) -> None:
    """AC-05-1 / SC-DOM-SOL-002: small-first로 완성되면 그 결과를 반환한다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    result = solve(grid)

    # Assert
    assert result is not None
    assert 0 not in [cell for row in result for cell in row]


def test_solve_returns_large_first_when_small_first_fails(
    grid_two_blanks: Grid,
) -> None:
    """AC-05-2 / AC-05-3 / SC-DOM-SOL-001: small-first 실패 후 large-first 성공."""
    # Arrange
    grid = grid_two_blanks

    # Act
    result = solve(grid)

    # Assert
    assert result is not None
    assert result[2][2] == 14
    assert result[3][2] == 7


def test_solve_returns_none_when_both_combinations_fail(
    grid_unsolvable_two_blanks: Grid,
) -> None:
    """AC-05-4 / SC-DOM-SOL-003: 두 조합 모두 실패하면 None을 반환한다."""
    # Arrange
    grid = grid_unsolvable_two_blanks

    # Act
    result = solve(grid)

    # Assert
    assert result is None


def test_solve_returns_4x4_grid_without_blanks(grid_two_blanks: Grid) -> None:
    """AC-05-5 / AC-05-6 / AC-05-7: 반환 격자는 4x4이며 빈칸이 없다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    result = solve(grid)

    # Assert
    assert result is not None
    assert len(result) == 4
    assert all(len(row) == 4 for row in result)
    assert 0 not in [cell for row in result for cell in row]


def test_solve_result_passes_validate(grid_two_blanks: Grid) -> None:
    """AC-05-8: 반환된 격자는 validate()를 통과한다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    result = solve(grid)

    # Assert
    assert result is not None
    validation = validate(result)
    assert validation.is_valid is True
