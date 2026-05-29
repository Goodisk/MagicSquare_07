"""Track B — D-MIS-01 find_not_exist_nums RED 스켈레톤 (Report/09).

Domain Mock 금지.
"""

from __future__ import annotations

import pytest

import magic_square.control.missing_number_finder as missing_number_finder  # noqa: F401


class TestDMis01FindNotExistNums:
    """D-MIS-01 — G1 누락 {7, 10} 오름차순 (I7, I11)."""

    def test_d_mis_01_g1_returns_sorted_missing_seven_and_ten(self) -> None:
        # Given — G1
        # grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # When
        # missing = find_not_exist_nums(grid)

        # Then — [7, 10]; Domain Mock 없음
        pytest.fail("RED: D-MIS-01 — G1 누락 숫자 [7, 10] 오름차순")
