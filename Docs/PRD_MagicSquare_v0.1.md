# Magic Square 4×4 — Product Requirements Document (PRD)

<!-- markdownlint-disable MD060 -->

| 항목 | 내용 |
| --- | --- |
| **문서 ID** | PRD-MSQ-001 |
| **버전** | v0.1 (Draft) |
| **작성일** | 2026-05-29 |
| **상태** | Draft — 구현 착수 전 검토용 |
| **작성 근거** | `Report/06_prd-reference-analysis_Report.md` 분석 결과 |
| **Primary Sources** | `Prompting/05_user-journey_Prompt.md`, `Report/01.problem-definition.md`, `Report/02.design.md`, `src/magic_square/entity/types.py` |

---

## 1. Document Control

### 1.1 문서 목적

본 PRD는 Magic Square 4×4 TDD Practice 프로젝트의 **구현 전 제품 요구사항**을 정의한다. 알고리즘 난이도보다 **불변식 기반 사고**, **계약 기반 테스트**, **Dual-Track TDD**, **리팩토링 훈련**을 목표로 하며, STEP 7(TDD 구현) 착수 전 팀·AI 에이전트가 공유할 단일 기준 문서이다.

### 1.2 참고 문서

| 문서 | 역할 |
| --- | --- |
| `Report/01.problem-definition.md` | Background, Why Chain, 문제 정의 |
| `Report/02.design.md` | `validate()` API, 7× 검증 함수, 테스트 명세 |
| `Prompting/05_user-journey_Prompt.md` | Epic, Journey, User Story, Gherkin (1차 참고) |
| `Report/05_user-journey_Report.md` | Verification 갭, 리스크 |
| `Report/06_prd-reference-analysis_Report.md` | PRD 섹션 매핑, 충돌 항목, 권장 목차 |
| `.cursor/rules/*.mdc` | Engineering Principles (부록 링크) |
| `src/magic_square/entity/types.py` | `ValidationResult`·도메인 상수 정본 |

### 1.3 변경 이력

| 버전 | 날짜 | 변경 내용 | 작성자 |
| --- | --- | --- | --- |
| v0.1 | 2026-05-29 | 초안 작성 — MVP/Phase 2 분리, 충돌 10건 해결안 반영 | PRD Agent |

### 1.4 용어 정의

| 용어 | 정의 |
| --- | --- |
| **불변 조건 (Invariant)** | 구현·입력 형태와 무관하게 항상 성립해야 하는 도메인 규칙 (INV-1~7) |
| **Dual-Track TDD** | Boundary(UI) 트랙과 Control(Logic) 트랙을 **독립 RED→GREEN→REFACTOR**로 진행하는 개발 방식. **GUI 개발이 아님** |
| **Git TDD 브랜치** | `red` / `green` / `refactoring` — 불변 조건 1개당 1사이클. Dual-Track과 별개 개념 |
| **빈칸 (Blank)** | 격자에서 아직 채워지지 않은 칸. 값 **`0`** 으로 표현 |
| **MVP** | `validate()` 기반 7개 불변 조건 검증 체계 |
| **Phase 2** | InputValidator, BlankFinder, MissingNumberFinder, Solver |

---

## 2. Executive Summary

Magic Square 4×4 프로젝트는 마방진을 **생성하는 알고리즘**이 아니라, **어떤 격자 상태가 유효한지를 일관되게 판정하는 기준 체계**를 구축하는 학습·훈련 프로젝트이다.

4×4 격자에 1~16이 중복 없이 배치되었을 때, 행·열·대각선 10개 합 조건이 동시에 34를 만족하는지를 **구현 이전에 명세하고**, TDD 사이클로 검증 가능한 계약으로 변환한다. Clean Architecture 관점의 ECB(Entity–Control–Boundary) 레이어 분리와 pytest 기반 RED-GREEN-REFACTOR를 통해, "구현 후 테스트"가 아닌 **"기준 먼저, 구현 나중"** 사고를 훈련한다.

**v0.1 범위 결정:** MVP는 `validate()` 7사이클(불변 조건 검증)에 집중하고, Solver·빈칸 채우기·입력 검증은 Phase 2로 분리한다.

---

## 3. Background & Context

### 3.1 관찰 (Observation)

현재 다루는 상황은 **4×4 격자 안에 숫자를 배치했을 때, 특정 규칙성(행·열·대각선 합의 균형)이 성립하는지 탐구**하는 것이다. 단순 나열이 아니라 **격자 구조, 숫자 배치, 합의 균형 관계**를 함께 다룬다.

4×4는 3×3보다 제약이 풍부하고, 5×5보다 복잡도가 급증하지 않아 **규칙 탐색과 검증 과정을 학습하기에 적절**하다.

### 3.2 학습·설계 맥락

| 맥락 | 설명 |
| --- | --- |
| 규칙 기반 문제 이해 | 숫자·격자를 통해 제약 충족 문제의 기초 학습 |
| 프로그램 구조화 | 입력, 계산, 검증, 결과 표현의 분리 연습 |
| 검증 중심 사고 | 정답 생성보다 **올바른 상태 판정**에 초점 |

### 3.3 Why Chain

#### Why #1 — 왜 마방진을 완성해야 하는가?

**숫자들이 배치된 4×4 격자가 일정한 균형 조건을 만족하는지 확인하고, 그 조건을 충족하는 완결된 상태를 얻기 위함.**

- 1~16 중복 없이 사용
- 각 행·열·대각선 합 동일 (34)
- 전체 격자가 하나의 일관된 규칙 체계로 검증 가능

**사용자 불편:**

1. 16칸, 중복 금지, 다방향 합 조건을 사람이 직접 판단하기 어렵다.
2. 부분적으로 맞아 보이는 상태가 전체적으로는 틀릴 수 있다.

**구조적 문제:** 핵심은 "칸을 채우는 것"이 아니라 **여러 제약이 얽힌 격자 상태를 일관되게 판단하고 완결 상태로 인식하는 방법**이다.

#### Why #2 — 왜 프로그램으로 구현하는가?

| 이유 | 설명 |
| --- | --- |
| 반복 가능성 | 동일 검증 절차를 다양한 격자에 반복 적용 |
| 검증 자동화 | 숫자 범위·중복·합 조건 누락 방지 |
| 오류 방지 | 부분 유효 vs 전체 무효를 명확히 구분 |
| 규칙 기반 사고 | "맞는 것 같다"가 아닌 **명시적 판단 기준** 필요 |

#### Why #3 — 왜 TDD로 설계하는가?

마방진은 **유효/무효 상태가 사전에 기술 가능**하여 TDD와 자연스럽게 맞닿는다. 검증 기준(허용 숫자, 합 비교 방식, 완성 판정)을 **구현 이전에 테스트로 고정**해야 한다. 입력·출력이 명확하지 않으면 경계 조건(빈 격자, 부분 채움, 중복 포함)을 테스트로 기술할 수 없다.

---

## 4. Problem Statement

### 4.1 표면 문제 (잘못된 정의)

> "1부터 16까지의 숫자를 4×4 격자에 배치하여, 모든 행·열·대각선의 합이 34가 되도록 만들어라."

→ **결과 형태**만 기술. 어떤 상태가 유효한지, 무엇을 판단하는 시스템을 만들 것인지 없음.

### 4.2 정확한 문제 정의

> **4×4 격자 상태가 주어졌을 때, 그 상태가 마방진의 불변 조건을 모두 만족하는지 일관되게 판정할 수 있는 기준 체계를 갖추어라. 단, 그 기준은 입력 형태나 구현 방식에 관계없이 동일하게 작동해야 한다.**

포함 요소:

- **무엇을** 판단하는가 — 격자 상태의 유효성
- **기준이 어디서** 오는가 — 불변 조건
- **기준의 성질** — 일관성, 독립성
- **완성 기준** — 모든 조건 동시 만족

### 4.3 훈련 목표 (사고 능력)

| 능력 | 설명 |
| --- | --- |
| 조건을 먼저 정의 | 결과 전에 올바른 상태를 언어로 기술 |
| 불변 조건 식별 | 변하지 않는 것 vs 변해도 되는 것 분리 |
| 상태 판정 | 부분 유효 vs 전체 유효 구분 |
| 경계 인식 | 유효·부분 유효·완전 오류 상태 각각 정의 |
| 기준의 독립성 | 판단 기준을 구현으로부터 분리 |

---

## 5. Vision & Goals

### 5.1 Epic

**Epic Title:** "불변식 기반 사고 훈련 시스템 구축"

4×4 마방진을 도메인 모델로 삼아, 구현 전에 불변식(Invariant)을 언어화하고 계약(Contract)으로 변환하는 사고 체계를 훈련한다.

### 5.2 Business Goal

TDD 학습 시 "무엇을 먼저 테스트해야 하는가"에 대한 기준이 없어 구현 후 역방향 테스트 작성이 반복되는 문제를 해결한다. 수학적으로 명확한 마방진 도메인으로 **Invariant-First Thinking**을 훈련한다.

### 5.3 Learning Goals

| ID | 내용 |
| --- | --- |
| LG-1 | 문제를 불변식 목록으로 분해할 수 있다 |
| LG-2 | 불변식을 검증 가능한 계약으로 변환할 수 있다 |
| LG-3 | ECB 아키텍처로 레이어를 분리할 수 있다 |
| LG-4 | RED → GREEN → REFACTOR 사이클을 독립적으로 수행할 수 있다 |
| LG-5 | 경계값·분기·예외 케이스를 Gherkin Scenario로 표현할 수 있다 |
| LG-6 | 리팩토링 후에도 기존 테스트가 회귀 없이 통과함을 검증할 수 있다 |

### 5.4 Success Criteria

| ID | 기준 | MVP | Phase 2 |
| --- | --- | :---: | :---: |
| SC-1 | 7개 불변 조건 각각 RED 테스트 1개 이상 | ✅ | ✅ |
| SC-2 | 모든 테스트 GREEN 상태로 커밋 | ✅ | ✅ |
| SC-3 | 커버리지 80% 이상 유지 | ✅ | ✅ |
| SC-4 | ECB 역방향 import 없음 | ✅ | ✅ |
| SC-5 | 타입힌트 없는 함수 없음 | ✅ | ✅ |
| SC-6 | 함수 본문 매직 넘버 없음 | ✅ | ✅ |
| SC-7 | 각 불변 조건·Story마다 Gherkin Scenario 1개 이상 | ⚠️ MVP는 validate 중심 | ✅ |
| SC-8 | Traceability Matrix 완성 | ✅ | ✅ |

### 5.5 Traceability Rule

```text
Concept → Invariant → Contract → Test → Implementation
```

---

## 6. Scope

### 6.1 MVP (v0.1 구현 범위)

| 포함 | 설명 |
| --- | --- |
| 4×4 격자 **완성 상태** 검증 | `validate(grid) -> ValidationResult` |
| 7개 불변 조건 검증 함수 | `_check_grid_size` ~ `_check_completeness` |
| Entity 타입 | `Grid`, `ConditionResult`, `ValidationResult`, 도메인 상수 |
| Control 레이어 | `control/validator.py` |
| TDD 7사이클 | 불변 조건 1개 = RED → GREEN → REFACTOR 1회 |
| pytest + AAA + 80% 커버리지 | `pyproject.toml` 설정 준수 |

### 6.2 Phase 2 (MVP 이후)

| 포함 | 설명 |
| --- | --- |
| Boundary / InputValidator | 빈칸 수·중복·범위 입력 검증 (S-01) |
| BlankFinder | 빈칸 좌표 탐색 (S-02) |
| MissingNumberFinder | 누락 숫자 탐색 (S-03) |
| Solver | small-first → large-first → None (S-05) |
| Dual-Track TDD | Boundary 트랙 + Control 트랙 병행 |
| 추가 Gherkin 6건 | §11.4 Planned 시나리오 |

### 6.3 Non-Scope (전 Phase 공통)

| 제외 | 이유 |
| --- | --- |
| N×N 일반화 | 4×4 학습 범위 고정 |
| GUI / Web UI | Boundary 레이어 테스트가 "UI 트랙"을 대체 |
| DB 저장, 파일 I/O | 도메인 검증에 불필요 |
| 성능 최적화 | 학습 목적과 무관 |
| 외부 API 연동 | 범위 외 |

### 6.4 범위 결정 근거 (충돌 해결 #1)

`Report/01`, `02`는 `validate()` 중심이고, `Prompting/05`는 Solver·BlankFinder까지 포함한다. **MVP = 검증 7 INV**, **Phase 2 = Solver·Blank·입력검증**으로 분리하여 AC 충돌을 방지한다.

---

## 7. Users & Journey

### 7.1 Persona

**TDD + ECB 학습 중인 소프트웨어 개발 학습자**

- 구현 중심 사고에서 "무엇을 먼저 정의해야 하는가"를 훈련하고자 함
- pytest, Python 타입힌트, Gherkin 작성 경험 초급~중급

### 7.2 Journey Goals

| ID | 목표 |
| --- | --- |
| JG-1 | 마방진 도메인 불변식을 언어로 명확히 정의 |
| JG-2 | 불변식을 계약으로 변환하고 레이어 분리 |
| JG-3 | 각 계약에 RED 테스트를 먼저 작성 |
| JG-4 | RED → GREEN → REFACTOR 사이클 완주 |
| JG-5 | 리팩토링 후 회귀 없음을 테스트로 증명 |

### 7.3 User Journey (5 Stage)

| Stage | 이름 | 핵심 행동 | MVP | Phase 2 |
| --- | --- | --- | :---: | :---: |
| 1 | Problem Recognition | INV-1~7 언어화 | ✅ | ✅ |
| 2 | Contract Definition | Gherkin·API 계약 작성 | ✅ (validate) | ✅ (전체 SC) |
| 3 | Domain Separation | ECB·컴포넌트 책임 분리 | ✅ (Entity+Control) | ✅ (+Boundary) |
| 4 | Dual-Track TDD Progress | RED→GREEN→REFACTOR | ✅ (Logic 트랙) | ✅ (+Boundary 트랙) |
| 5 | Regression Protection | 전체 GREEN·커버리지 확인 | ✅ | ✅ |

### 7.4 Dual-Track TDD (충돌 해결 #4, #5)

```text
Boundary Track (UI RED)  →  GREEN  →  REFACTOR
        ↑
Control Track (Logic RED)  →  GREEN  →  REFACTOR
```

- **UI RED** = Boundary 레이어(`InputValidator`) 테스트 RED. **실제 GUI 개발 아님** (Non-Scope와 충돌 없음).
- **Logic RED** = Control 레이어(`validate`, BlankFinder, Solver 등) 테스트 RED.
- **Git 브랜치** `red`/`green`/`refactoring`은 불변 조건 1개당 TDD 사이클을 의미하며, Dual-Track과 **별개 용어**이다.

### 7.5 User Stories

#### MVP User Stories

| ID | Story | Layer | Phase |
| --- | --- | --- | --- |
| US-04 | 시스템은 마방진 조건을 검증할 수 있다 | Control / `validate()` | MVP |
| US-11 | 리팩토링 후에도 기존 테스트가 회귀 없이 통과한다 | 전체 | MVP |

#### Phase 2 User Stories

| ID | Story | Layer | AC 수 |
| --- | --- | --- | --- |
| S-01 / US-06~09 | 입력 검증 — 빈칸 수·중복·범위 오류 | Boundary / InputValidator | 7 |
| S-02 / US-02 | 빈칸 좌표 탐색 | Control / BlankFinder | 5 |
| S-03 / US-03 | 누락 숫자 탐색 | Control / MissingNumberFinder | 5 |
| S-05 / US-05, US-10 | 두 가지 조합 시도 후 정답 또는 None | Control+Boundary / Solver | 8 |

> **Stage 5 전용 Story:** US-11(회귀 보호)이 Stage 5를 담당한다. 별도 Story 추가는 v0.2 검토 항목.

---

## 8. Domain Model

### 8.1 Key Invariants

| ID | 불변 조건 | 검증 함수 (MVP) |
| --- | --- | --- |
| INV-1 | 격자 크기: 4행 4열 | `_check_grid_size` |
| INV-2 | 숫자 집합: 1~16 정확히 한 번씩 | `_check_number_set` |
| INV-3 | 중복 금지 | `_check_no_duplicate` |
| INV-4 | 행 합 = 34 | `_check_row_sums` |
| INV-5 | 열 합 = 34 | `_check_col_sums` |
| INV-6 | 대각선 합 = 34 | `_check_diag_sums` |
| INV-7 | 10개 조건 중 하나라도 실패 시 전체 무효 | `_check_completeness` |

**파생 상수 (변하지 않음):**

- 16개 숫자 합 = **136** (1+2+…+16)
- 목표 합 = **34** (136 ÷ 4)
- 판정 기준 수 = **10** (행 4 + 열 4 + 대각선 2)

### 8.2 Data Dictionary

| 이름 | 타입 / 값 | 설명 | 상태 |
| --- | --- | --- | --- |
| `Grid` | `list[list[int]]` | 4×4 정수 격자, row-major | ✅ 구현됨 |
| `GRID_SIZE` | `4` | 행·열 크기 | ✅ `entity/types.py` |
| `TARGET_SUM` | `34` | 행·열·대각선 기준 합 | ✅ |
| `REQUIRED_NUMBERS` | `frozenset(1..16)` | 허용 숫자 집합 | ✅ |
| **Blank 값** | **`0`** | 빈칸 표현 (Gherkin Background 기준) | ✅ PRD 확정 |
| `BLANK_COUNT` | `2` | Solver 입력의 허용 빈칸 수 | 📋 Phase 2 추가 예정 |
| `MAX_VALUE` | `16` | 허용 최대 숫자 | 📋 Phase 2 추가 예정 |
| `OUTPUT_LENGTH` | `6` | Solver 출력 flat 길이 | 📋 Phase 2 추가 예정 |

> **충돌 해결 #6:** S-02는 "0 또는 None"을 언급하나, Gherkin Background와 Feature 정의는 **`0` 단일 표현**을 사용한다. Phase 2 구현 시 `0`만 허용.

### 8.3 Domain Components (Phase 2)

| 컴포넌트 | 레이어 | 책임 |
| --- | --- | --- |
| InputValidator | Boundary | 입력 형식·범위·빈칸 수 검증 |
| BlankFinder | Control | 빈칸 `(row, col)` 좌표 탐색 |
| MissingNumberFinder | Control | 미사용 1~16 숫자 목록 (오름차순) |
| MagicSquareValidator | Control | 행·열·대각선 합 검증 — MVP에서는 `validate()`가 담당 |
| Solver | Control + Boundary | small-first → large-first → `None` |

---

## 9. Functional Requirements

### 9.1 MVP — FR-VALID (격자 검증)

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| FR-V-01 | 시스템은 4×4 `Grid`를 입력받아 `ValidationResult`를 반환한다 | Must |
| FR-V-02 | 격자가 4행 4열이 아니면 "격자 크기" 조건을 실패로 보고한다 | Must |
| FR-V-03 | 1~16이 모두 포함되지 않으면 "숫자 집합" 조건을 실패로 보고한다 | Must |
| FR-V-04 | 중복 숫자가 있으면 "중복 금지" 조건을 실패로 보고한다 | Must |
| FR-V-05 | 행 합이 34가 아니면 "행 합" 조건을 실패로 보고한다 | Must |
| FR-V-06 | 열 합이 34가 아니면 "열 합" 조건을 실패로 보고한다 | Must |
| FR-V-07 | 대각선 합이 34가 아니면 "대각선 합" 조건을 실패로 보고한다 | Must |
| FR-V-08 | 6개 조건 중 하나라도 실패하면 `is_valid=False`이고 실패 목록에 포함한다 | Must |
| FR-V-09 | 7개 조건 모두 통과 시 `is_valid=True`, `failed_conditions=[]` | Must |
| FR-V-10 | 실패 시 `reason`에 사람이 읽을 수 있는 설명을 포함한다 | Must |

### 9.2 Phase 2 — FR-BND (입력 검증, S-01)

| ID | 요구사항 | AC |
| --- | --- | --- |
| FR-B-01 | 빈칸 0·1·3·4개이면 `"blank_count"` 오류 | AC-01-1~4 |
| FR-B-02 | 중복 숫자이면 `"duplicate"` 오류 | AC-01-5 |
| FR-B-03 | 17 이상 또는 0 이하(빈칸 제외)이면 `"out_of_range"` 오류 | AC-01-6~7 |

### 9.3 Phase 2 — FR-DOM (도메인 로직, S-02~S-05)

| ID | 요구사항 | Story |
| --- | --- | --- |
| FR-D-01 | 빈칸 2개 좌표를 `list[tuple[int,int]]`로 반환 | S-02 |
| FR-D-02 | 누락 숫자 2개를 오름차순 `list[int]`로 반환 | S-03 |
| FR-D-03 | small-first 실패 시 large-first 시도 | S-05 |
| FR-D-04 | 두 조합 모두 실패 시 `None` 반환 | S-05 |
| FR-D-05 | 반환 격자는 4×4, 빈칸 없음, `validate()` 통과 | S-05 |

---

## 10. Contracts & Interfaces

### 10.1 MVP Public API

```python
def validate(grid: Grid) -> ValidationResult:
    """7개 불변 조건을 순서대로 검증하고 통합 판정을 반환한다."""
```

### 10.2 MVP Internal API (Control, private)

| 함수 | 역할 |
| --- | --- |
| `_check_grid_size(grid) -> ConditionResult` | 4×4 구조 확인 |
| `_check_number_set(grid) -> ConditionResult` | 1~16 완전 포함 |
| `_check_no_duplicate(grid) -> ConditionResult` | 중복 없음 |
| `_check_row_sums(grid) -> ConditionResult` | 행 합 = TARGET_SUM |
| `_check_col_sums(grid) -> ConditionResult` | 열 합 = TARGET_SUM |
| `_check_diag_sums(grid) -> ConditionResult` | 대각선 합 = TARGET_SUM |
| `_check_completeness(results) -> ConditionResult` | 6개 전부 통과 시에만 완성 |

### 10.3 Entity Types (정본: `entity/types.py`)

```python
@dataclass(frozen=True)
class ConditionResult:
    name: str
    passed: bool
    reason: str | None = None

@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    failed_conditions: list[ConditionResult] = field(default_factory=list)
```

> **충돌 해결 #2:** S-04 AC-04-5는 `bool` 반환을 명시하나, MVP·Phase 2 공통 API는 **`ValidationResult`** 로 통일한다. `MagicSquareValidator`는 `validate()`를 래핑하거나 동일 시그니처를 사용한다.
>
> **충돌 해결 #8:** `magicsquare-ecb-architecture.mdc`의 `failed: list[str]` 예시는 **구식**이며 PRD·구현 정본은 `failed_conditions: list[ConditionResult]`이다.

### 10.4 Phase 2 API (예정)

| 함수 | 시그니처 | Layer |
| --- | --- | --- |
| InputValidator.validate | `(grid) -> InputValidationResult` | Boundary |
| BlankFinder.find | `(grid) -> list[tuple[int,int]]` | Control |
| MissingNumberFinder.find | `(grid) -> list[int]` | Control |
| Solver.solve | `(grid) -> Grid \| None` | Control |

### 10.5 TDD 실행 순서 (MVP)

| 순서 | 불변 조건 | 의존성 |
| ---: | --- | --- |
| 1 | 격자 크기 | 모든 검증의 전제 |
| 2 | 숫자 집합 | 중복·합의 전제 |
| 3 | 중복 금지 | 독립 위반 패턴 |
| 4 | 행 합 | 방향별 독립 |
| 5 | 열 합 | 행 합 구조 재사용 |
| 6 | 대각선 합 | 마지막 방향 |
| 7 | 완성의 불가분성 | 6개 결과 통합 |

---

## 11. Requirements ↔ Verification

### 11.1 Traceability Matrix (MVP)

| Invariant | Contract | Test (예시) | Implementation |
| --- | --- | --- | --- |
| INV-1 | `_check_grid_size` | `test_check_grid_size_rejects_non_4x4` | `control/validator.py` |
| INV-2 | `_check_number_set` | `test_check_number_set_rejects_missing` |同上 |
| INV-3 | `_check_no_duplicate` | `test_check_no_duplicate_rejects_dup` |同上 |
| INV-4 | `_check_row_sums` | `test_check_row_sums_fails_when_not_34` |同上 |
| INV-5 | `_check_col_sums` | `test_check_col_sums_fails_when_not_34` |同上 |
| INV-6 | `_check_diag_sums` | `test_check_diag_sums_fails_when_not_34` |同上 |
| INV-7 | `validate()` 통합 | `test_validate_accepts_valid_magic_square` |同上 |

### 11.2 Traceability Matrix (Phase 2)

| Story | Invariant | Scenario | Layer |
| --- | --- | --- | --- |
| S-01 | INV-2, INV-3 | SC-BND-VAL-001~004 | Boundary |
| S-02 | INV-1 | SC-DOM-BLK-001 | Control |
| S-03 | INV-2, INV-3 | SC-DOM-MSN-001 | Control |
| S-04 | INV-4~7 | SC-DOM-VAL-001 | Control |
| S-05 | INV-1~7 | SC-DOM-SOL-001~003 | Control+Boundary |

### 11.3 Gherkin Scenarios — Completed (4건)

| ID | 내용 | Story |
| --- | --- | --- |
| SC-DOM-SOL-001 | small-first 실패 → large-first 성공 (기대값 `[3,3,6,4,4,1]`) | S-05 |
| SC-BND-VAL-001 | 빈칸 0·1·3·4개 → `blank_count` | S-01 |
| SC-BND-VAL-002 | 중복 → `duplicate` | S-01 |
| SC-BND-VAL-003 | 17, -1, 100 → `out_of_range` | S-01 |

### 11.4 Gherkin Scenarios — Planned (6건)

| ID | 내용 | 상태 |
| --- | --- | --- |
| SC-DOM-BLK-001 | BlankFinder 좌표 반환 | 📋 Planned |
| SC-DOM-MSN-001 | MissingNumberFinder 누락 숫자 | 📋 Planned |
| SC-DOM-VAL-001 | MagicSquareValidator 행·열·대각선 | 📋 Planned |
| SC-BND-VAL-004 | 4×4 크기 검증 | 📋 Planned |
| SC-DOM-SOL-002 | small-first 성공 | 📋 Planned |
| SC-DOM-SOL-003 | 두 조합 모두 실패 → None | 📋 Planned |

> **충돌 해결 #7:** v0.1 PRD는 완성 Gherkin 4건 + Planned 6건으로 **Draft** 표기. SC-7(Success Criteria)은 Phase 2 완료 시 충족.

### 11.5 Verification Checklist (현재 7.5/10)

| 영역 | 결과 | 비고 |
| --- | --- | --- |
| Epic → Journey Consistency | ✅ | LG, SC, INV 매핑 완료 |
| Journey → Story Consistency | ⚠️ | Stage 5 = US-11로 대체 |
| Story → Scenario Consistency | ❌ → 📋 | S-02~04 SC Planned |
| Edge Case Coverage | ❌ → 📋 | SOL-002/003, BND-004 Planned |
| Invariant Coverage | ⚠️ 11/14 | MVP validate로 INV-4~7 보강 |

---

## 12. Architecture

### 12.1 Clean Architecture ↔ ECB 매핑 (충돌 해결 #10)

| Clean Architecture | ECB | 본 프로젝트 디렉토리 |
| --- | --- | --- |
| Entities | Entity | `src/magic_square/entity/` |
| Use Cases | Control | `src/magic_square/control/` |
| Interface Adapters | Boundary | `src/magic_square/boundary/` |
| Frameworks & Drivers | *(테스트·pytest)* | `tests/` |

### 12.2 ECB 레이어 규칙

```text
Boundary → Control → Entity

❌ Entity → Control
❌ Control → Boundary
```

| 레이어 | 역할 | 금지 |
| --- | --- | --- |
| Entity | 순수 데이터·타입·상수 | 로직, 다른 레이어 import |
| Control | 비즈니스 로직, 검증 흐름 | I/O 파싱, Boundary import |
| Boundary | 외부 입력 수신·포맷 변환 | 유효성 판정 (파싱 실패 외) |

### 12.3 디렉토리 구조 (정본 — 충돌 해결 #3)

`Report/02.design.md`의 flat 구조(`validator.py` at root) 대신 **ECB 트리를 정본**으로 한다.

```text
MagicSquare_021/
├── src/magic_square/
│   ├── entity/
│   │   └── types.py              # Grid, ValidationResult, 상수
│   ├── control/
│   │   └── validator.py          # validate(), _check_*  (MVP)
│   └── boundary/
│       ├── parser.py             # (Phase 2) 외부 입력 → Grid
│       └── input_validator.py    # (Phase 2) S-01
├── tests/
│   ├── conftest.py
│   ├── entity/test_types.py
│   ├── control/test_validator.py
│   └── boundary/                 # (Phase 2)
└── pyproject.toml
```

### 12.4 Git 브랜치 전략

```text
master ← GREEN만
 └── developer ← 통합
      ├── spec / red / green / refactoring
      └── (불변 조건 1개 = red → green → refactoring → developer)
```

커밋 접두사: `[RED]`, `[GREEN]`, `[REFACTOR]`

---

## 13. Development & Quality Approach

### 13.1 TDD Process

| 단계 | 규칙 |
| --- | --- |
| RED | `tests/`만 수정, 실패 테스트 작성, `src/` 수정 금지 |
| GREEN | 테스트 통과 최소 구현, 테스트 수정 금지 |
| REFACTOR | 동작 불변 구조 개선, 모든 테스트 GREEN 유지 |

### 13.2 Test Quality

- **AAA 패턴** 필수 (Arrange / Act / Assert 주석)
- 함수명: `test_<대상>_<조건>_<기대결과>`
- **하나의 테스트 = 하나의 동작**
- Fixture: `valid_magic_square` (`conftest.py`)
- **커버리지 ≥ 80%** (`pyproject.toml`)

### 13.3 Engineering Principles (요약)

| 원칙 | 내용 |
| --- | --- |
| Python 3.13 | 최신 union·match/case 활용 |
| Type hints | 모든 함수 인자·반환 필수 |
| Final 상수 | `TARGET_SUM`, `GRID_SIZE` 등 모듈 레벨 |
| Docstring | public API — Google 스타일 |
| Black | line-length 88 |
| 금지 | `print()` 디버그, bare except, 테스트 약화, ECB 역방향 import |

상세 규칙은 **Appendix A~E** (`.cursor/rules/*.mdc` 링크) 참조.

---

## 14. Risks, Gaps & Open Items

| 우선순위 | 항목 | 상태 | 조치 |
| --- | --- | --- | --- |
| P0 | MVP vs Phase 2 범위 | ✅ 해결 | §6 분리 |
| P0 | `bool` vs `ValidationResult` | ✅ 해결 | `ValidationResult` 통일 (§10.3) |
| P0 | flat vs ECB 디렉토리 | ✅ 해결 | ECB 트리 정본 (§12.3) |
| P1 | Gherkin 6건 미작성 | 📋 Open | Phase 2 착수 전 보완 |
| P1 | `BLANK_COUNT`, `OUTPUT_LENGTH` 상수 | 📋 Open | Phase 2 RED 전 `entity/types.py` 추가 |
| P2 | Stage 5 전용 Story | ⚠️ | US-11로 대체, v0.2 검토 |
| P2 | `ecb-architecture.mdc` 구식 예시 | 📋 Open | 별도 세션에서 `.mdc` 갱신 |
| P2 | SC-BND-VAL-003 `value=1` 경계값 | 📋 Open | Gherkin 보완 시 추가 |

---

## 15. Appendices

### Appendix A — TDD Process (원문)

→ `.cursor/rules/magicsquare-tdd-testing.mdc`

RED/GREEN/REFACTOR 단계 규칙, AAA 패턴, fixture scope, 커버리지 80%.

### Appendix B — Project Context & Branch Strategy

→ `.cursor/rules/magicsquare-project.mdc`

7 불변 조건, 브랜치 전략, 커밋 컨벤션, STEP 1~7 진행 상태.

### Appendix C — Prohibited Patterns

→ `.cursor/rules/magicsquare-forbidden.mdc`

`print()` 금지, bare except 금지, 테스트 약화 패턴, AI 코드 생성 규칙.

### Appendix D — Python Code Style

→ `.cursor/rules/magicsquare-python-code-style.mdc`

Python 3.13, type hints, Google docstring, Black 88, Final 상수.

### Appendix E — ECB Architecture Detail

→ `.cursor/rules/magicsquare-ecb-architecture.mdc`

> ⚠️ 해당 파일 내 `failed: list[str]` 예시는 구식. 정본은 §10.3 및 `entity/types.py`.

### Appendix F — Cursor Rules Index

→ `Report/03.cursor-rules.md`

| 파일 | alwaysApply | globs |
| --- | --- | --- |
| `magicsquare-project.mdc` | ✅ | — |
| `magicsquare-tdd-testing.mdc` | ✅ | `tests/**/*.py` |
| `magicsquare-forbidden.mdc` | ✅ | — |
| `magicsquare-ecb-architecture.mdc` | — | `src/**/*.py` |
| `magicsquare-python-code-style.mdc` | — | `**/*.py` |

### Appendix G — Feature Background (Gherkin)

```gherkin
Feature: Magic Square Solver
  마방진 풀기 — 4×4 격자에서 빈칸 2개를 채워 마방진을 완성한다.

  Background:
    Given a 4x4 grid with 14 filled numbers (1–16) and 2 blanks (value 0)
    And the filled numbers contain no duplicates
    And the filled numbers are all within range 1–16
```

---

## 16. Next Steps (Post-PRD)

1. PRD v0.1 리뷰 및 범위 확정
2. **MVP TDD 착수** — `red` 브랜치, INV-1(격자 크기) RED 테스트 작성
3. Phase 2 착수 전 — Gherkin 6건 보완, `BLANK_COUNT` 등 상수 추가
4. `ecb-architecture.mdc` 구식 예시 갱신 (선택)

---

*본 PRD는 `Report/06_prd-reference-analysis_Report.md` 분석 결과를 바탕으로 작성되었습니다.*
