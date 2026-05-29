"""Track B — D-VAL-01~06 is_magic_square RED 스켈레톤 (Report/09).

Domain Mock 금지.
"""

from __future__ import annotations

import pytest

import magic_square.control.magic_square_validator as magic_square_validator


class TestDVal01CompleteGrid:
    """D-VAL-01 — G0 완전 격자 True (I1~I5)."""

    def test_d_val_01_g0_complete_grid_returns_true(self) -> None:
        # Given — G0
        # grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # When
        # result = is_magic_square(grid)

        # Then — True; Domain Mock 없음
        pytest.fail("RED: D-VAL-01 — G0 완전 마방진 is_magic_square True")


class TestDVal02RowSum:
    """D-VAL-02 — 행 합 ≠ M(34) → False (I1)."""

    def test_d_val_02_row_sum_mismatch_returns_false(self) -> None:
        # Given
        # grid = [[16, 3, 2, 12], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # When
        # result = is_magic_square(grid)

        # Then — False
        pytest.fail("RED: D-VAL-02 — 행 합 불일치 시 False")


class TestDVal03ColSum:
    """D-VAL-03 — 열 합 ≠ M(34) → False (I2)."""

    def test_d_val_03_col_sum_mismatch_returns_false(self) -> None:
        # Given
        # grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 8, 12], [4, 15, 14, 1]]

        # When
        # result = is_magic_square(grid)

        # Then — False
        pytest.fail("RED: D-VAL-03 — 열 합 불일치 시 False")


class TestDVal04DiagonalSum:
    """D-VAL-04 — 대각 합 ≠ M(34) → False (I3)."""

    def test_d_val_04_diagonal_sum_mismatch_returns_false(self) -> None:
        # Given
        # grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 2]]

        # When
        # result = is_magic_square(grid)

        # Then — False
        pytest.fail("RED: D-VAL-04 — 대각 합 불일치 시 False")


class TestDVal05Duplicate:
    """D-VAL-05 — 1~16 중복 → False (I4)."""

    def test_d_val_05_duplicate_in_one_to_sixteen_returns_false(self) -> None:
        # Given
        # grid = [[16, 3, 2, 13], [5, 10, 5, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

        # When
        # result = is_magic_square(grid)

        # Then — False
        pytest.fail("RED: D-VAL-05 — 1~16 중복 시 False")


class TestDVal06ZeroInCompleteGrid:
    """D-VAL-06 — 완전 격자에 0 포함 → False (I4)."""

    def test_d_val_06_zero_in_complete_grid_returns_false(self) -> None:
        # Given
        # grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # When
        # result = is_magic_square(grid)

        # Then — False
        pytest.fail("RED: D-VAL-06 — 완전 격자에 0 포함 시 False")
