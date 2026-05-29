"""Track B — D-LOC-01 find_blank_coords RED 스켈레톤 (Report/09).

Domain Mock 금지.
"""

from __future__ import annotations

import pytest

import magic_square.control.blank_finder as blank_finder  # noqa: F401


class TestDLoc01FindBlankCoords:
    """D-LOC-01 — G1 row-major 0-index [(1,1), (2,2)] (I6)."""

    def test_d_loc_01_g1_returns_row_major_zero_index_pairs(self) -> None:
        # Given — G1
        # grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # When
        # coords = find_blank_coords(grid)

        # Then — [(1, 1), (2, 2)] length 2; Domain Mock 없음
        pytest.fail("RED: D-LOC-01 — G1 빈칸 0-index [(1,1), (2,2)]")
