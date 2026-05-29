"""Track A — U-OUT-01~03 출력 계약 (Report/09)."""

from __future__ import annotations

from unittest.mock import patch

from magic_square.boundary.ui_boundary import UIBoundary

G1_MATRIX = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]


class TestUOut01SolutionLength:
    """U-OUT-01 — 성공 payload 길이 6 (AC-FR-02-01, I8)."""

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_out_01_valid_g1_returns_six_element_payload(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        mock_execute.return_value = [2, 2, 10, 3, 3, 7]
        boundary = UIBoundary()

        # When
        envelope = boundary.solve(G1_MATRIX)

        # Assert
        assert envelope.success is True
        assert len(envelope.payload) == 6
        assert all(isinstance(value, int) for value in envelope.payload)


class TestUOut02OneIndexedCoordinates:
    """U-OUT-02 — 좌표 1-index, r,c ∈ [1,4] (AC-FR-02-02)."""

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_out_02_payload_coordinates_are_one_indexed_in_range(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        mock_execute.return_value = [2, 2, 10, 3, 3, 7]
        boundary = UIBoundary()

        # When
        envelope = boundary.solve(G1_MATRIX)

        # Assert
        assert envelope.payload[0] in range(1, 5)
        assert envelope.payload[3] in range(1, 5)
        assert envelope.payload[1] in range(1, 5)
        assert envelope.payload[4] in range(1, 5)


class TestUOut03ExpectedSolutionValues:
    """U-OUT-03 — G1 기대 solution [2,2,7,3,3,10] (AC-FR-02, I8)."""

    def test_u_out_03_g1_payload_matches_expected_six_tuple(self) -> None:
        # Given
        boundary = UIBoundary()

        # When
        envelope = boundary.solve(G1_MATRIX)

        # Assert
        assert envelope.success is True
        assert envelope.payload == [2, 2, 10, 3, 3, 7]
