"""US-11 / Stage 5 회귀 보호 — PRD use case 테스트 모듈 수집 전제."""

from pathlib import Path


def test_us11_all_prd_usecase_test_files_exist() -> None:
    """US-11: PRD use case별 RED 테스트 파일이 회귀 보호 대상으로 존재한다."""
    # Arrange
    test_files = [
        Path("tests/control/test_validator.py"),
        Path("tests/boundary/test_input_validator.py"),
        Path("tests/boundary/test_ac_fr_01_01_invalid_size.py"),
        Path("tests/control/test_blank_finder.py"),
        Path("tests/control/test_missing_number_finder.py"),
        Path("tests/control/test_solver.py"),
    ]

    # Act & Assert
    for test_file in test_files:
        assert test_file.is_file(), f"회귀 보호 대상 테스트 없음: {test_file}"

    # RED 단계: Entity GREEN 구현(도메인 상수)이 아직 없어야 한다
    from magic_square.entity import types as entity_types

    assert hasattr(entity_types, "GRID_SIZE"), (
        "RED 단계: GRID_SIZE 상수는 GREEN에서 구현한다"
    )
    assert entity_types.GRID_SIZE == 4
