# Golden Master Approve 패턴 설계

Magic Square Solver의 회귀를 방지하기 위해 **Golden Master(Approval) 테스트**를 적용한다.
현재 Solver(`UIBoundary`)의 실제 출력을 기준 파일과 비교한다.

## 목적

- Solver·Boundary 출력 계약이 의도치 않게 변경되면 CI에서 즉시 감지
- 5개 대표 시나리오의 **입력 → 출력** 스냅샷을 버전 관리
- 기준 파일 갱신은 **명시적 approve**(생성 스크립트 실행)로만 수행

## 아키텍처

```text
scripts/generate_golden_master.py
        │
        ▼
tests/golden_master/support.py  ──►  tests/golden_master_expected.txt
        ▲                                    │
        │                                    │ compare
tests/regression/test_golden_master_magic_square.py ◄─────┘
```

| 구성 요소 | 역할 |
| --- | --- |
| `tests/golden_master/support.py` | 시나리오 정의, DTO 직렬화, approve 비교 |
| `tests/golden_master_expected.txt` | 버전 관리되는 기준 출력 |
| `scripts/generate_golden_master.py` | 기준 파일 (재)생성 CLI |
| `tests/regression/test_golden_master_magic_square.py` | `@pytest.mark.golden_master` GM-TC 테스트 |

## 출력 캡처 방식

**Result DTO serialize** 방식을 사용한다.

`UIBoundary.solve(grid)` 호출 결과를 `SuccessEnvelope` / `FailureEnvelope`로 받아
Golden Master 텍스트 블록으로 직렬화한다. `UnsolvableDomainError`는 Qt Boundary와
동일하게 `Error: UNSOLVABLE`로 기록한다.

## 시나리오 (5건)

| 섹션 키 | 설명 | 기대 결과 종류 |
| --- | --- | --- |
| `GM-TC-01` | small-first 조합 즉시 성공 (G2 격자) | `Output:` 6-tuple |
| `GM-TC-02` | small-first 실패 · reverse fallback 성공 | `Output:` 6-tuple |
| `GM-TC-03` | 빈칸 1개 (INVALID_BLANK_COUNT) | `Error:` E002 |
| `GM-TC-04` | 중복 숫자 (DUPLICATE_NUMBER) | `Error:` E005 |
| `GM-TC-05` | 두 조합 모두 실패 (NO_VALID_MAGIC_SQUARE) | `Error:` UNSOLVABLE |

## 기준 파일 형식

섹션은 `[scenario_key]` 헤더로 구분한다. 섹션 간은 빈 줄 1개.

```text
[normal_success]
Input:
16 2 3 13
5 11 10 8
9 7 0 12
4 14 15 0
Output:
[3,3,6,4,4,1]

[reverse_success]
Input:
...
Output:
[3,3,7,4,3,14]
```

- **Input**: 공백 구분 정수, 행마다 한 줄
- **Output**: `[r1,c1,v1,r2,c2,v2]` (쉼표, 공백 없음)
- **Error**: Boundary 오류 코드 (`E002`, `E005`, `UNSOLVABLE`)

## Approve 패턴 동작

### 1. 기준 파일 없음

`assert_matches_golden_master(auto_create=True)` 호출 시:

1. 현재 Solver 출력을 생성
2. `tests/golden_master_expected.txt`에 **자동 기록**
3. 테스트 **PASS** (초기 bootstrap)

### 2. 기준 파일 있음

1. 현재 Solver 출력(actual) 생성
2. 기준 파일(expected)과 **전체 문자열 비교**
3. 일치 → **PASS**
4. 불일치 → `difflib.unified_diff` 출력 후 **FAIL**

### 3. 의도적 변경 승인 (approve)

Solver 출력 변경이 올바른 경우:

```bash
python scripts/generate_golden_master.py
git add tests/golden_master_expected.txt
git commit -m "[REFACTOR] test: Golden Master 기준 갱신"
```

## pytest 실행

```bash
pytest -m golden_master -v
```

개별 GM-TC 테스트 파일:

```bash
pytest tests/regression/test_golden_master_magic_square.py -v
```

전체 회귀 스위트:

```bash
pytest tests/regression/ -v
```

## GM-2 테스트 케이스

| ID | 테스트 함수 | 검증 대상 |
| --- | --- | --- |
| GM-TC-01 | `test_gm_tc_01_normal_combination_success` | int[6]·row-major·1-index·small-first |
| GM-TC-02 | `test_gm_tc_02_reverse_combination_success` | int[6]·reverse fallback |
| GM-TC-03 | `test_gm_tc_03_invalid_blank_count` | Error Contract E002 |
| GM-TC-04 | `test_gm_tc_04_duplicate_number` | Error Contract E005 |
| GM-TC-05 | `test_gm_tc_05_no_valid_magic_square` | Error Contract UNSOLVABLE |

모든 GM-TC 테스트는 `@pytest.mark.golden_master` 마커가 적용된다.

## 실패 시 diff 출력 예시

```
AssertionError: Golden Master [GM-TC-01] 출력 불일치 — Solver 회귀 감지

--- GM-TC-01 (expected)
+++ GM-TC-01 (actual)
@@ -4,4 +4,4 @@
 4 14 15 0
 Output:
-[3,3,6,4,4,1]
+[3,3,6,4,4,2]
```

## ECB 레이어 준수

- 테스트는 **Boundary**(`UIBoundary`) 진입점을 사용 — 실제 사용자 흐름과 동일
- Control(`solution()`) 직접 호출 대신 Envelope DTO 직렬화로 Track A 계약 검증
- Entity/Control 레이어 코드 변경 없음 (테스트·스크립트만 추가)

## 실패 시 해석

| diff 위치 | 가능 원인 |
| --- | --- |
| `Output:` 줄 | Solver 조합 순서·payload 변경 |
| `Error:` E002/E005 | InputValidator 오류 코드 변경 |
| `Error:` UNSOLVABLE | UnsolvableDomainError 처리·메시지 변경 |

불일치 diff를 확인한 뒤, **버그**이면 Solver를 수정하고, **의도된 변경**이면
생성 스크립트로 기준 파일을 갱신한다.
