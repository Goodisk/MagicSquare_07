"""Golden Master 시나리오 정의·직렬화·approve 패턴 (GM-2)."""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from magic_square.boundary.envelopes import FailureEnvelope, SuccessEnvelope
from magic_square.boundary.input_validator import ERROR_BLANK_COUNT, ERROR_DUPLICATE
from magic_square.boundary.ui_boundary import UIBoundary
from magic_square.control.missing_number_finder import find_not_exist_nums
from magic_square.control.solver import UnsolvableDomainError, solution
from magic_square.entity.types import GRID_SIZE, Grid

GOLDEN_MASTER_PATH: Final[Path] = (
    Path(__file__).resolve().parent.parent / "golden_master_expected.txt"
)

ERROR_UNSOLVABLE: Final[str] = "UNSOLVABLE"

SCENARIO_GRIDS: Final[dict[str, Grid]] = {
    "GM-TC-01": [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 0, 1],
    ],
    "GM-TC-02": [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ],
    "GM-TC-03": [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ],
    "GM-TC-04": [
        [16, 3, 2, 13],
        [5, 10, 5, 8],
        [9, 6, 0, 12],
        [4, 15, 0, 1],
    ],
    "GM-TC-05": [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 16],
    ],
}

SCENARIO_ORDER: Final[tuple[str, ...]] = tuple(SCENARIO_GRIDS.keys())

SECTION_HEADER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^\[GM-TC-\d{2}\]$")

ERROR_CONTRACT: Final[dict[str, str]] = {
    "GM-TC-03": ERROR_BLANK_COUNT,
    "GM-TC-04": ERROR_DUPLICATE,
    "GM-TC-05": ERROR_UNSOLVABLE,
}


@dataclass(frozen=True)
class ScenarioResult:
    """시나리오 실행 결과 — API result serialization."""

    kind: str
    body: str
    payload: list[int] | None = None


def blank_coords_row_major(grid: Grid) -> list[tuple[int, int]]:
    """0-index row-major 순서로 빈칸 좌표를 반환한다."""
    coords: list[tuple[int, int]] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            if grid[row_index][col_index] == 0:
                coords.append((row_index, col_index))
    return coords


def serialize_grid(grid: Grid) -> str:
    """격자를 Golden Master Input 블록 문자열로 변환한다."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def serialize_payload(payload: list[int]) -> str:
    """성공 payload를 Golden Master Output 형식으로 변환한다."""
    return "[" + ",".join(str(value) for value in payload) + "]"


def run_scenario(boundary: UIBoundary, grid: Grid) -> ScenarioResult:
    """시나리오 1건을 실행하고 직렬화 가능한 결과 DTO를 반환한다."""
    try:
        envelope = boundary.solve(grid)
    except UnsolvableDomainError:
        return ScenarioResult(kind="Error", body=ERROR_UNSOLVABLE)

    if isinstance(envelope, SuccessEnvelope):
        return ScenarioResult(
            kind="Output",
            body=serialize_payload(envelope.payload),
            payload=envelope.payload,
        )
    if isinstance(envelope, FailureEnvelope):
        return ScenarioResult(kind="Error", body=envelope.code)
    return ScenarioResult(kind="Error", body="UNKNOWN")


def format_scenario_section(
    scenario_id: str,
    grid: Grid,
    boundary: UIBoundary,
) -> str:
    """단일 GM-TC 블록 전체를 Golden Master 형식으로 포맷한다."""
    result = run_scenario(boundary, grid)
    lines = [
        f"[{scenario_id}]",
        "Input:",
        serialize_grid(grid),
        f"{result.kind}:",
        result.body,
    ]
    return "\n".join(lines)


def generate_golden_master_content(boundary: UIBoundary | None = None) -> str:
    """모든 GM-TC 시나리오의 Golden Master 기준 텍스트를 생성한다."""
    solver_boundary = boundary or UIBoundary()
    sections = [
        format_scenario_section(scenario_id, SCENARIO_GRIDS[scenario_id], solver_boundary)
        for scenario_id in SCENARIO_ORDER
    ]
    return "\n\n".join(sections) + "\n"


def normalize_section_body(body: str) -> str:
    """섹션 본문 비교용 공백·줄바꿈 정규화."""
    return body.rstrip()


def parse_sections(content: str) -> dict[str, str]:
    """Golden Master 파일을 섹션 ID → 본문 dict로 파싱한다."""
    sections: dict[str, str] = {}
    current_id: str | None = None
    body_lines: list[str] = []

    for line in content.splitlines():
        if SECTION_HEADER_PATTERN.match(line):
            if current_id is not None:
                sections[current_id] = "\n".join(body_lines)
            current_id = line[1:-1]
            body_lines = []
            continue
        if current_id is not None:
            body_lines.append(line)

    if current_id is not None:
        sections[current_id] = "\n".join(body_lines)

    return sections


def format_section_diff(expected: str, actual: str, scenario_id: str) -> str:
    """--- expected / +++ actual unified diff를 생성한다."""
    return "".join(
        difflib.unified_diff(
            expected.splitlines(keepends=True),
            actual.splitlines(keepends=True),
            fromfile=f"{scenario_id} (expected)",
            tofile=f"{scenario_id} (actual)",
        )
    )


def write_golden_master(path: Path | None = None) -> Path:
    """현재 Solver 출력으로 Golden Master 기준 파일을 기록한다."""
    target = path or GOLDEN_MASTER_PATH
    target.write_text(generate_golden_master_content(), encoding="utf-8")
    return target


def assert_section_matches_golden_master(
    scenario_id: str,
    *,
    path: Path | None = None,
    auto_create: bool = True,
    boundary: UIBoundary | None = None,
) -> ScenarioResult:
    """approve 패턴 — GM-TC 섹션 단위 actual vs expected 비교.

    기준 파일이 없으면 전체 파일을 생성한다.
    불일치 시 unified diff(--- expected / +++ actual) 후 FAIL.
    """
    target = path or GOLDEN_MASTER_PATH
    solver_boundary = boundary or UIBoundary()
    grid = SCENARIO_GRIDS[scenario_id]
    actual_section = format_scenario_section(scenario_id, grid, solver_boundary)
    actual_section_body = normalize_section_body(actual_section.split("\n", 1)[1])
    result = run_scenario(solver_boundary, grid)

    if not target.is_file():
        if not auto_create:
            raise AssertionError(f"Golden Master 기준 파일 없음: {target}")
        write_golden_master(target)
        return result

    expected_content = target.read_text(encoding="utf-8")
    expected_sections = parse_sections(expected_content)

    if scenario_id not in expected_sections:
        write_golden_master(target)
        return result

    expected_section_body = normalize_section_body(expected_sections[scenario_id])
    if actual_section_body == expected_section_body:
        return result

    diff_text = format_section_diff(
        expected_section_body,
        actual_section_body,
        scenario_id,
    )
    raise AssertionError(
        f"Golden Master [{scenario_id}] 출력 불일치 — Solver 회귀 감지\n\n"
        + diff_text
    )


def assert_int6_output_format(payload: list[int]) -> None:
    """성공 payload는 int 6개 tuple 형식이어야 한다."""
    assert len(payload) == 6
    assert all(isinstance(value, int) for value in payload)


def assert_one_index_rule(payload: list[int]) -> None:
    """좌표는 1-index이며 [1, GRID_SIZE] 범위여야 한다."""
    for index in (0, 1, 3, 4):
        assert 1 <= payload[index] <= GRID_SIZE


def assert_row_major_rule(grid: Grid, payload: list[int]) -> None:
    """빈칸 좌표는 row-major 순서로 payload에 반영되어야 한다."""
    blanks = blank_coords_row_major(grid)
    assert (payload[0] - 1, payload[1] - 1) == blanks[0]
    assert (payload[3] - 1, payload[4] - 1) == blanks[1]


def assert_small_first_combination_rule(grid: Grid, payload: list[int]) -> None:
    """작은 수 우선(sorted ascending) 조합이 적용되어야 한다."""
    missing = find_not_exist_nums(grid)
    ordered = sorted(missing)
    assert payload[2] == ordered[0]
    assert payload[5] == ordered[1]


def assert_small_first_fails(grid: Grid) -> None:
    """small-first 조합이 마방진을 완성하지 못함을 검증한다."""
    from magic_square.control.magic_square_validator import is_magic_square
    from magic_square.control.solver import _fill_grid

    missing = find_not_exist_nums(grid)
    ordered = sorted(missing)
    blanks = blank_coords_row_major(grid)
    filled = _fill_grid(grid, blanks, ordered)
    assert is_magic_square(filled) is False


def assert_reverse_fallback_rule(grid: Grid, payload: list[int]) -> None:
    """small-first 실패 후 reverse(sorted descending) fallback이 적용되어야 한다."""
    assert_small_first_fails(grid)
    missing = find_not_exist_nums(grid)
    ordered = sorted(missing)
    reversed_assignment = list(reversed(ordered))
    assert payload[2] == reversed_assignment[0]
    assert payload[5] == reversed_assignment[1]
    assert solution(grid) == payload


def assert_error_contract(scenario_id: str, error_code: str) -> None:
    """Error Contract — GM-TC별 기대 오류 코드를 검증한다."""
    expected = ERROR_CONTRACT[scenario_id]
    assert error_code == expected


def assert_matches_golden_master(
    *,
    path: Path | None = None,
    auto_create: bool = True,
) -> None:
    """전체 Golden Master 파일 approve — GM-TC-01~05 일괄 비교."""
    target = path or GOLDEN_MASTER_PATH
    actual = generate_golden_master_content()

    if not target.is_file():
        if not auto_create:
            raise AssertionError(f"Golden Master 기준 파일 없음: {target}")
        write_golden_master(target)
        return

    expected = target.read_text(encoding="utf-8")
    if actual == expected:
        return

    diff_text = format_section_diff(expected, actual, "golden_master_expected.txt")
    raise AssertionError(
        "Golden Master 출력 불일치 — Solver 회귀 감지\n\n" + diff_text
    )
