"""Track A — U-FLOW-02 invalid 입력 시 Domain execute 0회 RED 스켈레톤 (확장).

@patch / @spy SolvePartialMagicSquare.execute — GREEN에서 call_count 검증.
"""

from __future__ import annotations

import pytest

import magic_square.boundary.ui_boundary as ui_boundary


class TestUFlow02ExecuteNeverCalledOnInvalid:
    """U-FLOW-02 — short-circuit: invalid 시 execute 0회 (AC-FR-01-06)."""

    def test_u_flow_02_invalid_size_never_calls_execute(self) -> None:
        # Given — 3×4 matrix (U-IN-02a 계열)
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12]]
        # boundary = UIBoundary()
        # @spy/mock SolvePartialMagicSquare.execute

        # When
        # envelope = boundary.solve(matrix)

        # Then — execute.call_count == 0; success is False
        pytest.fail("RED: U-FLOW-02 — INVALID_SIZE 시 execute 0회")

    def test_u_flow_02_three_blanks_never_calls_execute(self) -> None:
        # Given — 빈칸 3개 (E002)
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 0]]
        # @spy/mock SolvePartialMagicSquare.execute

        # When
        # envelope = boundary.solve(matrix)

        # Then — execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E002 빈칸 3개 시 execute 0회")

    def test_u_flow_02_out_of_range_never_calls_execute(self) -> None:
        # Given — E004 (값 17)
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 17]]
        # @spy/mock SolvePartialMagicSquare.execute

        # When
        # envelope = boundary.solve(matrix)

        # Then — execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E004 범위 위반 시 execute 0회")

    def test_u_flow_02_duplicate_never_calls_execute(self) -> None:
        # Given — E005
        # matrix = [[16, 3, 2, 13], [5, 10, 5, 8], [9, 6, 0, 12], [4, 15, 0, 1]]
        # @spy/mock SolvePartialMagicSquare.execute

        # When
        # envelope = boundary.solve(matrix)

        # Then — execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E005 중복 시 execute 0회")
