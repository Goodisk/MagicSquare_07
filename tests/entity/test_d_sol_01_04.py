"""Track B — D-SOL-01~04 solution() RED 스켈레톤 (Report/09).

Domain Mock 금지.
"""

from __future__ import annotations

import pytest

import magic_square.control.solver as solver  # noqa: F401


class TestDSol01G1StepA:
    """D-SOL-01 — G1 Step A 성공 [2,2,7,3,3,10] (I8)."""

    def test_d_sol_01_g1_returns_expected_six_tuple(self) -> None:
        # Given — G1; missing {7, 10}
        # grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # When
        # result = solution(grid)

        # Then — [2, 2, 7, 3, 3, 10]; r,c ∈ [1,4]; Domain Mock 없음
        pytest.fail("RED: D-SOL-01 — G1 solution [2,2,7,3,3,10]")


class TestDSol02G2StepBFallback:
    """D-SOL-02 — G2 Step A 실패 · Step B 성공 (I9)."""

    def test_d_sol_02_g2_step_b_fallback_returns_six_tuple(self) -> None:
        # Given — G2 (Report/02 부록 TBD)
        # grid = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 1]]

        # When
        # result = solution(grid)

        # Then — int[6] SSOT G2 Appendix (interim TBD)
        pytest.fail("RED: D-SOL-02 — G2 TBD")


class TestDSol03G3Unsolvable:
    """D-SOL-03 — G3 Step A·B 실패 → UnsolvableDomainError (I10)."""

    def test_d_sol_03_g3_raises_unsolvable_domain_error(self) -> None:
        # Given — G3
        # grid = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12], [13, 14, 0, 16]]

        # When / Then — UnsolvableDomainError; Domain Mock 없음
        pytest.fail("RED: D-SOL-03 — G3 UnsolvableDomainError")


class TestDSol04PayloadShape:
    """D-SOL-04 — 성공 시 len==6, 좌표 1-index (I8, I9)."""

    def test_d_sol_04_g1_success_payload_length_six_one_index(self) -> None:
        # Given — G1
        # grid = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]

        # When
        # result = solution(grid)

        # Then — len(result) == 6; coords 1-index ∈ [1, 4]
        pytest.fail("RED: D-SOL-04 — G1 성공 payload 길이 6·1-index 좌표")
