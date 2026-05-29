"""AC-FR-01-01 격자 크기(INVALID_SIZE) RED 테스트 — Boundary / InputValidator."""

from __future__ import annotations

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from magic_square.boundary.input_validator import validate_input
from magic_square.boundary.schemas import GridInputSchema
from magic_square.entity.types import Grid, InputValidationResult, ValidationErrorCode


class TestAcFr0101InvalidSize:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE"""

    def test_three_rows_grid_returns_invalid_size_error_code(
        self,
        invalid_grid_wrong_row_count: Grid,
    ) -> None:
        """행 수가 3이면 INVALID_SIZE 오류를 반환한다."""
        # Given
        grid = invalid_grid_wrong_row_count

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes

    def test_five_columns_grid_returns_invalid_size_error_code(
        self,
        invalid_grid_wrong_col_count: Grid,
    ) -> None:
        """열 수가 5이면 INVALID_SIZE 오류를 반환한다."""
        # Given
        grid = invalid_grid_wrong_col_count

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes

    def test_five_rows_grid_returns_invalid_size_error_code(
        self,
        invalid_grid_five_rows: Grid,
    ) -> None:
        """행 수가 5이면 INVALID_SIZE 오류를 반환한다."""
        # Given
        grid = invalid_grid_five_rows

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes

    def test_empty_grid_returns_invalid_size_error_code(
        self,
        invalid_grid_empty: Grid,
    ) -> None:
        """행이 0개이면 INVALID_SIZE 오류를 반환한다."""
        # Given
        grid = invalid_grid_empty

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes

    def test_jagged_row_lengths_returns_invalid_size_error_code(
        self,
        invalid_grid_jagged_rows: Grid,
    ) -> None:
        """행마다 열 수가 다르면 INVALID_SIZE 오류를 반환한다."""
        # Given
        grid = invalid_grid_jagged_rows

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes

    def test_valid_4x4_grid_does_not_emit_invalid_size(
        self,
        grid_two_blanks: Grid,
    ) -> None:
        """4행 4열이면 INVALID_SIZE 오류를 포함하지 않는다."""
        # Given
        grid = grid_two_blanks

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert ValidationErrorCode.INVALID_SIZE not in result.error_codes

    @patch("magic_square.boundary.input_validator._check_blank_count")
    def test_invalid_size_skips_blank_count_check(
        self,
        mock_check_blank_count: object,
        invalid_grid_wrong_row_count: Grid,
    ) -> None:
        """격자 크기 위반 시 빈칸 수 검증을 호출하지 않는다."""
        # Given
        grid = invalid_grid_wrong_row_count

        # When
        result: InputValidationResult = validate_input(grid)

        # Assert
        # AC-FR-01-01
        assert result.is_valid is False
        assert ValidationErrorCode.INVALID_SIZE in result.error_codes
        mock_check_blank_count.assert_not_called()

    def test_pydantic_schema_rejects_non_4x4_flat_input(self) -> None:
        """Pydantic 스키마가 16칸이 아닌 flat 입력을 거부한다."""
        # Given
        flat_cells = list(range(1, 13))

        # When / Then
        # AC-FR-01-01
        with pytest.raises(ValidationError) as exc_info:
            GridInputSchema.model_validate({"cells": flat_cells})

        assert "INVALID_SIZE" in str(exc_info.value)
