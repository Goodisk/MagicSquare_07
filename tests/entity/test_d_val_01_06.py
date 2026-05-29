"""Track B — D-VAL-01~06 is_magic_square."""

from __future__ import annotations

from magic_square.control.magic_square_validator import is_magic_square


class TestDVal01CompleteGrid:
    """D-VAL-01 — G0 완전 격자 True (I1~I5)."""

    def test_d_val_01_g0_complete_grid_returns_true(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is True


class TestDVal02RowSum:
    """D-VAL-02 — 행 합 ≠ M(34) → False (I1)."""

    def test_d_val_02_row_sum_mismatch_returns_false(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 12], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is False


class TestDVal03ColSum:
    """D-VAL-03 — 열 합 ≠ M(34) → False (I2)."""

    def test_d_val_03_col_sum_mismatch_returns_false(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 8, 12], [4, 15, 14, 1]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is False


class TestDVal04DiagonalSum:
    """D-VAL-04 — 대각 합 ≠ M(34) → False (I3)."""

    def test_d_val_04_diagonal_sum_mismatch_returns_false(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 2]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is False


class TestDVal05Duplicate:
    """D-VAL-05 — 1~16 중복 → False (I4)."""

    def test_d_val_05_duplicate_in_one_to_sixteen_returns_false(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 10, 5, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is False


class TestDVal06ZeroInCompleteGrid:
    """D-VAL-06 — 완전 격자에 0 포함 → False (I4)."""

    def test_d_val_06_zero_in_complete_grid_returns_false(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # Act
        result = is_magic_square(grid)

        # Assert
        assert result is False
