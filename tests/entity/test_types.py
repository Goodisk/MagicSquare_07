"""ConditionResult, ValidationResult 엔티티 타입 테스트.

[RED] 단계 — 구현 파일 없이 작성된 실패 테스트.
모든 테스트는 src/magic_square/entity/types.py 구현 전까지 ImportError로 실패한다.
"""
import pytest

from magic_square.entity.types import (
    GRID_SIZE,
    REQUIRED_NUMBERS,
    TARGET_SUM,
    ConditionResult,
    Grid,
    ValidationResult,
)


class TestDomainConstants:
    """도메인 상수 불변 조건 테스트."""

    def test_grid_size_is_4(self) -> None:
        # Arrange & Act & Assert
        assert GRID_SIZE == 4

    def test_target_sum_is_34(self) -> None:
        # Arrange & Act & Assert
        assert TARGET_SUM == 34

    def test_required_numbers_contains_1_to_16(self) -> None:
        # Arrange
        expected = frozenset(range(1, 17))

        # Act & Assert
        assert REQUIRED_NUMBERS == expected

    def test_required_numbers_count_is_16(self) -> None:
        # Arrange & Act & Assert
        assert len(REQUIRED_NUMBERS) == 16


class TestConditionResult:
    """ConditionResult 데이터클래스 테스트."""

    def test_passed_condition_reason_defaults_to_none(self) -> None:
        # Arrange & Act
        result = ConditionResult(name="격자 크기", passed=True)

        # Assert
        assert result.reason is None

    def test_passed_condition_stores_name_and_passed(self) -> None:
        # Arrange & Act
        result = ConditionResult(name="행 합", passed=True)

        # Assert
        assert result.name == "행 합"
        assert result.passed is True

    def test_failed_condition_stores_reason(self) -> None:
        # Arrange
        expected_reason = "행 또는 열의 수가 4가 아님"

        # Act
        result = ConditionResult(
            name="격자 크기",
            passed=False,
            reason=expected_reason,
        )

        # Assert
        assert result.passed is False
        assert result.reason == expected_reason

    def test_condition_result_is_immutable(self) -> None:
        # Arrange
        result = ConditionResult(name="격자 크기", passed=True)

        # Act & Assert
        with pytest.raises(AttributeError):
            result.passed = False  # type: ignore[misc]

    def test_condition_result_name_is_immutable(self) -> None:
        # Arrange
        result = ConditionResult(name="격자 크기", passed=True)

        # Act & Assert
        with pytest.raises(AttributeError):
            result.name = "다른 이름"  # type: ignore[misc]


class TestValidationResult:
    """ValidationResult 데이터클래스 테스트."""

    def test_valid_result_is_valid_is_true(self) -> None:
        # Arrange & Act
        result = ValidationResult(is_valid=True)

        # Assert
        assert result.is_valid is True

    def test_valid_result_failed_conditions_defaults_to_empty(self) -> None:
        # Arrange & Act
        result = ValidationResult(is_valid=True)

        # Assert
        assert result.failed_conditions == []

    def test_invalid_result_stores_failed_conditions(self) -> None:
        # Arrange
        failed = ConditionResult(
            name="행 합",
            passed=False,
            reason="1번 행의 합이 34가 아님 (실제: 33)",
        )

        # Act
        result = ValidationResult(is_valid=False, failed_conditions=[failed])

        # Assert
        assert result.is_valid is False
        assert len(result.failed_conditions) == 1
        assert result.failed_conditions[0].name == "행 합"

    def test_invalid_result_with_multiple_failures(self) -> None:
        # Arrange
        failures = [
            ConditionResult(name="행 합", passed=False, reason="1번 행의 합이 34가 아님"),
            ConditionResult(name="열 합", passed=False, reason="3번 열의 합이 34가 아님"),
        ]

        # Act
        result = ValidationResult(is_valid=False, failed_conditions=failures)

        # Assert
        assert len(result.failed_conditions) == 2

    def test_validation_result_is_immutable(self) -> None:
        # Arrange
        result = ValidationResult(is_valid=True)

        # Act & Assert
        with pytest.raises(AttributeError):
            result.is_valid = False  # type: ignore[misc]

    def test_single_failure_makes_result_invalid(self) -> None:
        """완성의 불가분성 — 조건 하나라도 실패하면 전체가 유효하지 않다."""
        # Arrange
        one_failure = [
            ConditionResult(name="대각선 합", passed=False, reason="반 대각선의 합이 34가 아님")
        ]

        # Act
        result = ValidationResult(is_valid=False, failed_conditions=one_failure)

        # Assert
        assert result.is_valid is False
        assert len(result.failed_conditions) == 1


class TestGridTypeAlias:
    """Grid 타입 별칭 사용 가능 여부 확인."""

    def test_grid_accepts_4x4_list(self) -> None:
        # Arrange & Act
        grid: Grid = [
            [16,  3,  2, 13],
            [ 5, 10, 11,  8],
            [ 9,  6,  7, 12],
            [ 4, 15, 14,  1],
        ]

        # Assert
        assert len(grid) == 4
        assert all(len(row) == 4 for row in grid)
