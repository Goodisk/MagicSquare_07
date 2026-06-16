"""Qt Boundary adapter — 격자 변환 및 메시지."""

from __future__ import annotations

import random

from magic_square.boundary.qt.adapter import (
    apply_solution_payload,
    cells_to_grid,
    format_error_message,
    format_solution_message,
    generate_random_puzzle,
    grid_to_cell_texts,
    parse_cell_text,
)
from magic_square.boundary.ui_boundary import UIBoundary
from magic_square.entity.types import GRID_SIZE


class TestParseCellText:
    """셀 텍스트 파싱."""

    def test_parse_cell_text_empty_returns_zero(self) -> None:
        # Arrange
        text = ""

        # Act
        result = parse_cell_text(text)

        # Assert
        assert result == 0

    def test_parse_cell_text_zero_token_returns_zero(self) -> None:
        # Arrange
        text = "0"

        # Act
        result = parse_cell_text(text)

        # Assert
        assert result == 0

    def test_parse_cell_text_valid_number_returns_int(self) -> None:
        # Arrange
        text = "16"

        # Act
        result = parse_cell_text(text)

        # Assert
        assert result == 16

    def test_parse_cell_text_invalid_returns_none(self) -> None:
        # Arrange
        text = "abc"

        # Act
        result = parse_cell_text(text)

        # Assert
        assert result is None


class TestCellsToGrid:
    """4×4 셀 → Grid 변환."""

    def test_cells_to_grid_valid_4x4_returns_grid(self) -> None:
        # Arrange
        cells = [
            ["16", "3", "2", "13"],
            ["5", "0", "11", "8"],
            ["9", "6", "", "12"],
            ["4", "15", "14", "1"],
        ]

        # Act
        grid = cells_to_grid(cells)

        # Assert
        assert grid == [
            [16, 3, 2, 13],
            [5, 0, 11, 8],
            [9, 6, 0, 12],
            [4, 15, 14, 1],
        ]

    def test_cells_to_grid_wrong_row_count_returns_none(self) -> None:
        # Arrange
        cells = [["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"]]

        # Act
        grid = cells_to_grid(cells)

        # Assert
        assert grid is None


class TestApplySolutionPayload:
    """Solver payload 격자 반영."""

    def test_apply_solution_payload_fills_blank_cells(self) -> None:
        # Arrange
        grid = [
            [16, 3, 2, 13],
            [5, 0, 11, 8],
            [9, 6, 0, 12],
            [4, 15, 14, 1],
        ]
        payload = [2, 2, 10, 3, 3, 7]

        # Act
        filled = apply_solution_payload(grid, payload)

        # Assert
        assert filled[1][1] == 10
        assert filled[2][2] == 7


class TestFormatMessages:
    """오류·성공 메시지 포맷."""

    def test_format_error_message_known_code(self) -> None:
        # Arrange
        code = "E002"

        # Act
        message = format_error_message(code)

        # Assert
        assert "빈칸" in message

    def test_format_solution_message_returns_coordinate_string(self) -> None:
        # Arrange
        payload = [2, 2, 10, 3, 3, 7]

        # Act
        message = format_solution_message(payload)

        # Assert
        assert message == "(2,2)=10, (3,3)=7"


class TestGridToCellTexts:
    """Grid → Qt 셀 문자열."""

    def test_grid_to_cell_texts_blank_becomes_empty_string(self) -> None:
        # Arrange
        grid = [[0, 1], [2, 3]]

        # Act
        texts = grid_to_cell_texts(grid)

        # Assert
        assert texts[0][0] == ""
        assert texts[0][1] == "1"


class TestGenerateRandomPuzzle:
    """랜덤 퍼즐 생성."""

    def test_generate_random_puzzle_has_exactly_two_blanks(self) -> None:
        # Arrange
        rng = random.Random(42)

        # Act
        puzzle = generate_random_puzzle(rng)

        # Assert
        blank_count = sum(1 for row in puzzle for cell in row if cell == 0)
        assert blank_count == 2

    def test_generate_random_puzzle_nonzero_values_are_unique(self) -> None:
        # Arrange
        rng = random.Random(99)

        # Act
        puzzle = generate_random_puzzle(rng)

        # Assert
        values = [cell for row in puzzle for cell in row if cell != 0]
        assert len(values) == len(set(values))
        assert all(1 <= value <= 16 for value in values)

    def test_generate_random_puzzle_is_solvable(self) -> None:
        # Arrange
        rng = random.Random(7)
        boundary = UIBoundary()

        # Act
        puzzle = generate_random_puzzle(rng)
        envelope = boundary.solve(puzzle)

        # Assert
        assert envelope.success is True
        assert len(envelope.payload) == 6

    def test_generate_random_puzzle_varies_blank_positions(self) -> None:
        # Arrange
        rng = random.Random(0)

        # Act
        puzzles = [generate_random_puzzle(rng) for _ in range(5)]
        blank_sets = {
            tuple(
                (row_index, col_index)
                for row_index, row in enumerate(puzzle)
                for col_index, cell in enumerate(row)
                if cell == 0
            )
            for puzzle in puzzles
        }

        # Assert
        assert len(blank_sets) > 1

