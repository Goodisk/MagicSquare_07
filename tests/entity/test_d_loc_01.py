"""Track B — D-LOC-01 find_blank_coords."""

from __future__ import annotations

from magic_square.control.blank_finder import find_blank_coords


class TestDLoc01FindBlankCoords:
    """D-LOC-01 — G1 row-major 0-index [(1,1), (2,2)] (I6)."""

    def test_d_loc_01_g1_returns_row_major_zero_index_pairs(self) -> None:
        # Arrange
        grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # Act
        coords = find_blank_coords(grid)

        # Assert
        assert coords == [(1, 1), (2, 2)]
        assert len(coords) == 2
