"""Track A — U-FLOW-02 invalid 입력 시 Domain execute 0회."""

from __future__ import annotations

from unittest.mock import patch

from magic_square.boundary.ui_boundary import UIBoundary


class TestUFlow02ExecuteNeverCalledOnInvalid:
    """U-FLOW-02 — short-circuit: invalid 시 execute 0회 (AC-FR-01-06)."""

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_flow_02_invalid_size_never_calls_execute(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12]]
        boundary = UIBoundary()

        # When
        envelope = boundary.solve(matrix)

        # Assert
        mock_execute.assert_not_called()
        assert envelope.success is False

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_flow_02_three_blanks_never_calls_execute(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 0]]
        boundary = UIBoundary()

        # When
        boundary.solve(matrix)

        # Assert
        mock_execute.assert_not_called()

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_flow_02_out_of_range_never_calls_execute(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 17]]
        boundary = UIBoundary()

        # When
        boundary.solve(matrix)

        # Assert
        mock_execute.assert_not_called()

    @patch("magic_square.boundary.ui_boundary.SolvePartialMagicSquare.execute")
    def test_u_flow_02_duplicate_never_calls_execute(
        self,
        mock_execute: object,
    ) -> None:
        # Given
        matrix = [[16, 3, 2, 13], [5, 10, 5, 8], [9, 6, 0, 12], [4, 15, 0, 1]]
        boundary = UIBoundary()

        # When
        boundary.solve(matrix)

        # Assert
        mock_execute.assert_not_called()
