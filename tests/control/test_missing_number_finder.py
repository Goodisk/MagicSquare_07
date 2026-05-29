"""Control 레이어 MissingNumberFinder 테스트 — S-03 / SC-DOM-MSN-001."""

from magic_square.control.missing_number_finder import find_missing_numbers
from magic_square.entity.types import Grid


def test_find_missing_returns_two_numbers(grid_two_blanks: Grid) -> None:
    """AC-03-1 / SC-DOM-MSN-001: 빈칸 2개 격자에서 누락 숫자 2개를 반환한다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    missing = find_missing_numbers(grid)

    # Assert
    assert len(missing) == 2
    assert set(missing) == {7, 14}


def test_find_missing_returns_sorted_list(grid_two_blanks: Grid) -> None:
    """AC-03-2 / AC-03-3: 반환 목록은 오름차순 list[int]이다."""
    # Arrange
    grid = grid_two_blanks

    # Act
    missing = find_missing_numbers(grid)

    # Assert
    assert isinstance(missing, list)
    assert all(isinstance(n, int) for n in missing)
    assert missing == sorted(missing)


def test_find_missing_returns_empty_when_complete(
    valid_magic_square: Grid,
) -> None:
    """AC-03-4: 모든 숫자가 채워진 격자에서 빈 리스트를 반환한다."""
    # Arrange
    grid = valid_magic_square

    # Act
    missing = find_missing_numbers(grid)

    # Assert
    assert missing == []


def test_find_missing_returns_correct_numbers_with_duplicate_in_grid(
    grid_duplicate_for_missing_finder: Grid,
) -> None:
    """AC-03-5: 중복 숫자 격자에서도 누락 숫자를 정확히 반환한다."""
    # Arrange
    grid = grid_duplicate_for_missing_finder

    # Act
    missing = find_missing_numbers(grid)

    # Assert
    assert 11 in missing
    assert 7 in missing or 14 in missing
