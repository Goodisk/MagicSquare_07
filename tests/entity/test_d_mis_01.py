"""Track B — D-MIS-01 find_not_exist_nums."""

from __future__ import annotations

from magic_square.control.missing_number_finder import find_not_exist_nums


class TestDMis01FindNotExistNums:
    """D-MIS-01 — G1 누락 {7, 10} 오름차순 (I7, I11)."""

    def test_d_mis_01_g1_returns_sorted_missing_seven_and_ten(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # Act
        missing = find_not_exist_nums(grid)

        # Assert
        assert missing == [7, 10]
