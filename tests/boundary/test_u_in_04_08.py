"""Track A — U-IN-04~08 입력 검증 RED 스켈레톤 (Report/09).

U-IN-01~03은 Report/08 `test_ac_fr_01_01_*.py`에 Full RED로 존재 — 중복 금지.
"""

from __future__ import annotations

import pytest

import magic_square.boundary.input_validator as input_validator  # noqa: F401


class TestUIn04ValueBelowRange:
    """U-IN-04 — 값 < 1 → E004 (AC-FR-01-04)."""

    def test_u_in_04_value_below_range_returns_e004(self) -> None:
        # Given
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, -1]]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — Failure envelope E004; SolvePartialMagicSquare.execute 0회
        pytest.fail("RED: U-IN-04 — 값 -1 포함 시 E004 envelope, Domain execute 0회")


class TestUIn05ValueAboveRange:
    """U-IN-05 — 값 > 16 → E004 (AC-FR-01-04)."""

    def test_u_in_05_value_above_range_returns_e004(self) -> None:
        # Given
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 17]]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — Failure envelope E004; execute 0회
        pytest.fail("RED: U-IN-05 — 값 17 포함 시 E004 envelope, Domain execute 0회")


class TestUIn06NonzeroDuplicate:
    """U-IN-06 — non-zero 중복 → E005 (AC-FR-01-05)."""

    def test_u_in_06_nonzero_duplicate_returns_e005(self) -> None:
        # Given
        # matrix = [[16, 3, 2, 13], [5, 10, 5, 8], [9, 6, 0, 12], [4, 15, 0, 1]]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — Failure envelope E005; execute 0회
        pytest.fail("RED: U-IN-06 — non-zero 5 중복 시 E005 envelope, Domain execute 0회")


class TestUIn07ValueHundredOutOfRange:
    """U-IN-07 — 값 100 → E004 (SC-BND-VAL-003 확장)."""

    def test_u_in_07_value_hundred_returns_e004(self) -> None:
        # Given
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 100]]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — Failure envelope E004; execute 0회
        pytest.fail("RED: U-IN-07 — 값 100 포함 시 E004 envelope, Domain execute 0회")


class TestUIn08DuplicateSixteenWithBlanks:
    """U-IN-08 — 빈칸 2개 유지·16 중복 → E005."""

    def test_u_in_08_duplicate_sixteen_returns_e005(self) -> None:
        # Given
        # matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 0, 12], [4, 15, 0, 16]]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — Failure envelope E005; execute 0회
        pytest.fail("RED: U-IN-08 — 16 중복(빈칸 2개) 시 E005 envelope, Domain execute 0회")
