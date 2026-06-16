"""Control 레이어 BlankFinder 테스트 — S-02 / SC-DOM-BLK-001."""

from magic_square.control.blank_finder import find_blanks
from magic_square.entity.types import Grid


def test_find_blanks_returns_two_coordinates(grid_two_blanks: Grid) -> None:
    """AC-02-1 / SC-DOM-BLK-001: 빈칸 2개 격자에서 2개 좌표를 반환한다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    coordinates = find_blanks(grid)

    # Assert
    assert len(coordinates) == 2
    assert coordinates == [(2, 2), (3, 2)]


def test_find_blanks_returns_row_col_tuples(grid_two_blanks: Grid) -> None:
    """AC-02-2 / AC-02-3: 반환 타입은 (row, col) tuple 목록이다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    coordinates = find_blanks(grid)

    # Assert
    assert all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates)


def test_find_blanks_returns_empty_list_when_no_blanks(
    valid_magic_square: Grid,
) -> None:
    """AC-02-4: 빈칸이 없으면 빈 리스트를 반환한다."""
    # Arrange
    grid = valid_magic_square

    # Act
    coordinates = find_blanks(grid)

    # Assert
    assert coordinates == []


def test_find_blanks_returns_all_positions_when_more_than_two(
    grid_three_blanks_for_finder: Grid,
) -> None:
    """AC-02-5: 빈칸 2개 초과이면 모든 빈칸 좌표를 반환한다."""
    # Arrange
    grid = grid_three_blanks_for_finder

    # Act
    coordinates = find_blanks(grid)

    # Assert
    assert len(coordinates) == 3
    assert (2, 2) in coordinates
    assert (3, 1) in coordinates
    assert (3, 2) in coordinates
