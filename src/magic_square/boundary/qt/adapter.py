"""Qt Boundary — 격자 문자열 변환 및 응답 메시지."""

from __future__ import annotations

import random
from typing import Final

from magic_square.entity.types import GRID_SIZE, Grid

BLANK_TOKEN: Final[frozenset[str]] = frozenset({"", "0"})
REQUIRED_BLANK_COUNT: Final[int] = 2

BASE_MAGIC_SQUARE: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

ERROR_MESSAGES: Final[dict[str, str]] = {
    "INVALID_SIZE": "격자는 4×4여야 합니다.",
    "E002": "빈칸은 정확히 2개여야 합니다.",
    "E004": "값은 1~16 범위여야 합니다.",
    "E005": "0이 아닌 숫자는 중복될 수 없습니다.",
    "PARSE_ERROR": "모든 칸에 0(빈칸) 또는 1~16 정수를 입력하세요.",
    "UNSOLVABLE": "두 가지 조합 모두 마방진을 완성할 수 없습니다.",
}


def format_error_message(code: str) -> str:
    """오류 코드를 사용자 메시지로 변환한다."""
    return ERROR_MESSAGES.get(code, f"오류 ({code})")


def parse_cell_text(text: str) -> int | None:
    """셀 텍스트를 정수로 파싱한다. 빈칸·0은 0, 잘못된 입력은 None."""
    stripped = text.strip()
    if stripped in BLANK_TOKEN:
        return 0
    if not stripped.isdigit():
        return None
    value = int(stripped)
    if value < 0 or value > 16:
        return None
    return value


def cells_to_grid(cells: list[list[str]]) -> Grid | None:
    """4×4 셀 텍스트를 Grid로 변환한다. 파싱 실패 시 None."""
    if len(cells) != GRID_SIZE:
        return None
    grid: Grid = []
    for row in cells:
        if len(row) != GRID_SIZE:
            return None
        parsed_row: list[int] = []
        for cell in row:
            parsed = parse_cell_text(cell)
            if parsed is None:
                return None
            parsed_row.append(parsed)
        grid.append(parsed_row)
    return grid


def apply_solution_payload(grid: Grid, payload: list[int]) -> Grid:
    """Solver 6-tuple payload를 격자에 반영한다 (1-index 좌표)."""
    filled = [row[:] for row in grid]
    filled[payload[0] - 1][payload[1] - 1] = payload[2]
    filled[payload[3] - 1][payload[4] - 1] = payload[5]
    return filled


def format_solution_message(payload: list[int]) -> str:
    """성공 payload를 사람이 읽을 수 있는 문자열로 변환한다."""
    return (
        f"({payload[0]},{payload[1]})={payload[2]}, "
        f"({payload[3]},{payload[4]})={payload[5]}"
    )


def grid_to_cell_texts(grid: Grid) -> list[list[str]]:
    """Grid를 Qt 셀 표시용 문자열 2차원 리스트로 변환한다."""
    return [["" if cell == 0 else str(cell) for cell in row] for row in grid]


def _rotate_grid_cw(grid: Grid) -> Grid:
    """격자를 시계 방향 90° 회전한다."""
    return [list(row) for row in zip(*grid[::-1], strict=True)]


def _reflect_grid_horizontal(grid: Grid) -> Grid:
    """격자를 좌우 반전한다."""
    return [row[::-1] for row in grid]


def _all_cell_coords() -> list[tuple[int, int]]:
    return [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE)]


def generate_random_puzzle(rng: random.Random | None = None) -> Grid:
    """완성 마방진에서 빈칸 2개를 랜덤으로 비운 퍼즐을 생성한다."""
    source = random.Random() if rng is None else rng
    grid = [row[:] for row in BASE_MAGIC_SQUARE]
    for _ in range(source.randint(0, 3)):
        grid = _rotate_grid_cw(grid)
    if source.choice((True, False)):
        grid = _reflect_grid_horizontal(grid)
    blanks = source.sample(_all_cell_coords(), REQUIRED_BLANK_COUNT)
    puzzle = [row[:] for row in grid]
    for row_index, col_index in blanks:
        puzzle[row_index][col_index] = 0
    return puzzle
