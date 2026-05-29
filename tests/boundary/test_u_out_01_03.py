"""Track A — U-OUT-01~03 출력 계약 RED 스켈레톤 (Report/09).

Control mock/spy는 GREEN 단계에서 연동 — 아래 주석만 표시.
"""

from __future__ import annotations

import pytest

import magic_square.boundary.ui_boundary as ui_boundary


class TestUOut01SolutionLength:
    """U-OUT-01 — 성공 payload 길이 6 (AC-FR-02-01, I8)."""

    def test_u_out_01_valid_g1_returns_six_element_payload(self) -> None:
        # Given — G1
        # matrix = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
        # boundary = UIBoundary()
        # @spy/mock SolvePartialMagicSquare.execute — 호출 허용

        # When
        # envelope = boundary.solve(matrix)

        # Then — success True; len(payload) == 6; list[int]
        pytest.fail("RED: U-OUT-01 — G1 성공 시 int[6] payload 반환")


class TestUOut02OneIndexedCoordinates:
    """U-OUT-02 — 좌표 1-index, r,c ∈ [1,4] (AC-FR-02-02)."""

    def test_u_out_02_payload_coordinates_are_one_indexed_in_range(self) -> None:
        # Given — G1
        # matrix = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
        # boundary = UIBoundary()

        # When
        # envelope = boundary.solve(matrix)

        # Then — payload[0,2,4] and payload[1,3,5] each in [1, 4]
        pytest.fail("RED: U-OUT-02 — payload 좌표 1-index [1,4] 범위")


class TestUOut03ExpectedSolutionValues:
    """U-OUT-03 — G1 기대 solution [2,2,7,3,3,10] (AC-FR-02, I8)."""

    def test_u_out_03_g1_payload_matches_expected_six_tuple(self) -> None:
        # Given — G1; expected [2, 2, 7, 3, 3, 10]
        # boundary = UIBoundary()

        # When
        # envelope = boundary.solve(matrix)

        # Then — payload == [2, 2, 7, 3, 3, 10]
        pytest.fail("RED: U-OUT-03 — G1 payload [2,2,7,3,3,10] 일치")
