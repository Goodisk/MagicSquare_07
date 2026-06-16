"""Track B — D-SOL-01~04 solution()."""

from __future__ import annotations

import pytest

from magic_square.control.solver import UnsolvableDomainError, solution

G1_GRID = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
G2_GRID = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 1]]
G3_GRID = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12], [13, 14, 0, 16]]


class TestDSol01G1StepA:
    """D-SOL-01 — G1 Step A 성공 [2,2,7,3,3,10] (I8)."""

    def test_d_sol_01_g1_returns_expected_six_tuple(self) -> None:
        # Arrange
        grid = G1_GRID

        # Act
        result = solution(grid)

        # Assert
        assert result == [2, 2, 10, 3, 3, 7]


class TestDSol02G2StepBFallback:
    """D-SOL-02 — G2 Step A 실패 · Step B 성공 (I9)."""

    def test_d_sol_02_g2_step_b_fallback_returns_six_tuple(self) -> None:
        # Arrange
        grid = G2_GRID

        # Act
        result = solution(grid)

        # Assert
        assert result == [3, 3, 7, 4, 3, 14]


class TestDSol03G3Unsolvable:
    """D-SOL-03 — G3 Step A·B 실패 → UnsolvableDomainError (I10)."""

    def test_d_sol_03_g3_raises_unsolvable_domain_error(self) -> None:
        # Arrange
        grid = G3_GRID

        # Act / Assert
        with pytest.raises(UnsolvableDomainError):
            solution(grid)


class TestDSol04PayloadShape:
    """D-SOL-04 — 성공 시 len==6, 좌표 1-index (I8, I9)."""

    def test_d_sol_04_g1_success_payload_length_six_one_index(self) -> None:
        # Arrange
        grid = G1_GRID

        # Act
        result = solution(grid)

        # Assert
        assert len(result) == 6
        assert result[0] in range(1, 5)
        assert result[3] in range(1, 5)
        assert result[1] in range(1, 5)
        assert result[4] in range(1, 5)
