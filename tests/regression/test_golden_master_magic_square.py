"""Golden Master 회귀 테스트 — Magic Square Solver (GM-2).

[TAG][GoldenMaster] pytest -m golden_master -v
"""

from __future__ import annotations

import pytest

from magic_square.boundary.ui_boundary import UIBoundary
from tests.golden_master.support import (
    SCENARIO_GRIDS,
    assert_error_contract,
    assert_int6_output_format,
    assert_one_index_rule,
    assert_reverse_fallback_rule,
    assert_row_major_rule,
    assert_section_matches_golden_master,
    assert_small_first_combination_rule,
)

pytestmark = pytest.mark.golden_master


@pytest.fixture
def boundary() -> UIBoundary:
    """Golden Master 테스트용 UIBoundary."""
    return UIBoundary()


class TestGoldenMasterMagicSquare:
    """GM-TC-01~05 — Solver 출력 Golden Master approve + 계약 검증."""

    def test_gm_tc_01_normal_combination_success(self, boundary: UIBoundary) -> None:
        """GM-TC-01: 정상 조합(small-first) 성공 — int[6]·row-major·1-index."""
        # Arrange
        grid = SCENARIO_GRIDS["GM-TC-01"]

        # Act
        result = assert_section_matches_golden_master("GM-TC-01", boundary=boundary)

        # Assert — Error Contract 외 성공 payload 계약
        assert result.kind == "Output"
        assert result.payload is not None
        assert_int6_output_format(result.payload)
        assert_one_index_rule(result.payload)
        assert_row_major_rule(grid, result.payload)
        assert_small_first_combination_rule(grid, result.payload)

    def test_gm_tc_02_reverse_combination_success(self, boundary: UIBoundary) -> None:
        """GM-TC-02: reverse fallback 조합 성공 — int[6]·reverse 규칙."""
        # Arrange
        grid = SCENARIO_GRIDS["GM-TC-02"]

        # Act
        result = assert_section_matches_golden_master("GM-TC-02", boundary=boundary)

        # Assert
        assert result.kind == "Output"
        assert result.payload is not None
        assert_int6_output_format(result.payload)
        assert_one_index_rule(result.payload)
        assert_row_major_rule(grid, result.payload)
        assert_reverse_fallback_rule(grid, result.payload)

    def test_gm_tc_03_invalid_blank_count(self, boundary: UIBoundary) -> None:
        """GM-TC-03: INVALID_BLANK_COUNT — Error Contract E002."""
        # Arrange
        # grid = SCENARIO_GRIDS["GM-TC-03"]

        # Act
        result = assert_section_matches_golden_master("GM-TC-03", boundary=boundary)

        # Assert
        assert result.kind == "Error"
        assert_error_contract("GM-TC-03", result.body)

    def test_gm_tc_04_duplicate_number(self, boundary: UIBoundary) -> None:
        """GM-TC-04: DUPLICATE_NUMBER — Error Contract E005."""
        # Arrange
        # grid = SCENARIO_GRIDS["GM-TC-04"]

        # Act
        result = assert_section_matches_golden_master("GM-TC-04", boundary=boundary)

        # Assert
        assert result.kind == "Error"
        assert_error_contract("GM-TC-04", result.body)

    def test_gm_tc_05_no_valid_magic_square(self, boundary: UIBoundary) -> None:
        """GM-TC-05: NO_VALID_MAGIC_SQUARE — Error Contract UNSOLVABLE."""
        # Arrange
        # grid = SCENARIO_GRIDS["GM-TC-05"]

        # Act
        result = assert_section_matches_golden_master("GM-TC-05", boundary=boundary)

        # Assert
        assert result.kind == "Error"
        assert_error_contract("GM-TC-05", result.body)
