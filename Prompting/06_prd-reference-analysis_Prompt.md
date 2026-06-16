# PRD 참고 문서 분석 — 세션 대화 전문

<!-- markdownlint-disable MD060 -->

> 날짜: 2026-05-29  
> 세션 설명: Magic Square 프로젝트 PRD 작성 전, Report/*.md 및 .cursor/rules/*.mdc 참고 문서를 분석하고 PRD 섹션 매핑을 수행한 설계·기획 세션 (PRD 본문·코드 미작성).

---

## Turn 1

### User (Turn 1)

당신은 PRD 작성 전문가이자 Dual-Track UI + Logic TDD 기반 제품 기획자입니다.

목표:
Magic Square 프로젝트 구현 전에 PRD를 작성하려고 합니다.

단, 지금은 PRD 본문을 바로 작성하지 마십시오.
먼저 PRD 작성에 참고해야 할 문서들을 분석하고,
각 문서의 어떤 내용을 PRD의 어떤 섹션에 반영해야 하는지 정리해 주세요.

프로젝트:

- Magic Square 4x4
- 목적: 알고리즘 난이도보다 불변식 기반 사고, 계약 기반 테스트, Dual-Track UI + Logic TDD, 리팩토링 훈련
- 아키텍처: Clean Architecture + ECB
- 테스트 방식: pytest, AAA 패턴, RED-GREEN-REFACTOR
- 핵심 산출물: 구현 전 PRD

참고 문서:

1. Report/*.md
2. .cursor/rules/*.mdc

각 문서별 참고 목적:

Report/1.ProblemDefinition_Report.md

- PRD의 Background
- Problem Definition
- Why are we doing this now
- Why Chain
- 제품 동기
- 사용자가 겪는 불편
- 무엇을 닫아야 하는가

Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md

- PRD의 Vision
- Epic Goal
- Persona
- User Journey
- User Story
- Acceptance Criteria
- Gherkin Scenario
- Verification Checklist
- Requirements와 Verification을 동시에 정리할 때 가장 중요한 1차 자료

Report/2.CleanArchitecture_DualTrack_TDD_Design_Report.md

- PRD의 Functional Scope
- Input / Output Contract
- Invariant Table
- Domain Concept
- Layer Boundary
- 사용자에게 보장할 동작
- 기능 명세 수준의 계약

Report/3.DevelopmentEnvironment_CursorRules_ECB_UserEntity_Report.md

- PRD의 Quality Requirements
- Development Method
- Engineering Principles
- Constraints
- ECB
- TDD 단계
- pytest / coverage
- prohibited patterns

.cursorrules + .cursor/rules/*.mdc

- 팀이 따라야 할 상세 개발 규칙 원문
- PRD의 Engineering Principles 또는 Appendix에 요약 반영
- 상세 규칙이 필요할 경우 부록으로 연결

작업 지시:

1. 각 문서를 읽고 핵심 내용을 요약하십시오.
2. 각 문서가 PRD의 어떤 섹션에 들어가야 하는지 매핑하십시오.
3. 중복되는 내용은 어느 문서를 우선 출처로 삼을지 정하십시오.
4. PRD 본문에 직접 넣을 내용과 부록으로 보낼 내용을 구분하십시오.
5. 구현 코드나 테스트 코드는 작성하지 마십시오.
6. 아직 PRD 본문 전체를 작성하지 마십시오.
7. 이번 단계는 “PRD 작성 전 참고 문서 분석 및 매핑”만 수행하십시오.

출력 형식 (사용자 지시 템플릿):

```markdown
# PRD Reference Document Analysis

## 1. Overall Judgment
- PRD 작성 가능 여부:
- 가장 중요한 1차 참고 문서:
- 보조 참고 문서:
- 누락된 정보:

## 2. Document Summary
(표)

## 3. PRD Section Mapping
(표)

## 4. Source Priority Rules
(표)

## 5. Directly Transfer to PRD Body
(표)

## 6. Move to Appendix or Engineering Principles
(표)

## 7. Conflicts / Ambiguities
(표)

## 8. Recommended PRD Outline
(권장 목차만)
```

주의:

- 구현 코드 작성 금지
- 테스트 코드 작성 금지
- 파일 수정 금지
- PRD 본문 작성 금지
- 참고 문서 분석과 매핑만 수행

### AI (Turn 1)

(참고: 저장소 실제 파일명은 사용자 지시명과 다름 — `Report/01.problem-definition.md`, `Report/02.design.md`, `Report/03.cursor-rules.md`, `Report/05_user-journey_Report.md` + User Journey 본문은 `Prompting/05_user-journey_Prompt.md`. `.cursorrules` 단일 파일 없음.)

---

## PRD Reference Document Analysis (AI 응답)

### 1. Overall Judgment

| 항목                         | 판단                                                                                                                                                                                                                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PRD 작성 가능 여부**       | **가능(조건부)** — 배경·불변식·계약·여정·품질 기준은 충분. 다만 **제품 범위(검증만 vs Solver/빈칸 채우기)**와 **API·레이어 구조**를 PRD 초안 전에 한 번 확정해야 함                                                                                                |
| **가장 중요한 1차 참고 문서** | `Prompting/05_user-journey_Prompt.md` (Epic → Journey → Story → Gherkin → Verification 전층)                                                                                                                                                                         |
| **보조 참고 문서**           | `Report/01.problem-definition.md`, `Report/02.design.md`, `.cursor/rules/*.mdc` (특히 `magicsquare-project.mdc`, `magicsquare-ecb-architecture.mdc`)                                                                                                               |
| **누락된 정보**              | (1) 누락 Gherkin 6건, (2) Stage 5 전용 User Story, (3) Dual-Track UI 구체 형태, (4) Clean Architecture↔ECB 매핑 표, (5) 릴리스 일정, (6) 운영 NFR, (7) `04_cursor-agents_Report`는 부록용 |

### 2. Document Summary

| Document                              | Main Content                                                                              | PRD Usage                                                              | Priority |
| ------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------- |
| `Report/01.problem-definition.md`     | STEP 1~5: 관찰, Why Chain, 문제 정의, 불변식, 훈련 목표                                  | Background, Problem Definition, Why now                                | **P1**   |
| `Report/02.design.md`                 | STEP 6: `validate()`·7×`_check_*`, 타입, RED/GREEN/경계, TDD 순서                         | Functional Scope, I/O Contract, Invariant                              | **P1**   |
| `Prompting/05_user-journey_Prompt.md` | Epic, Journey, S-01~05 AC, Gherkin 4건, Verification 7.5/10                             | Vision, Epic, Persona, Journey, Stories, AC, Gherkin                   | **P0**   |
| `Report/05_user-journey_Report.md`    | 설계 세션 메타 보고서                                                                     | Verification 갭, PRD 리스크                                            | **P2**   |
| `Report/03.cursor-rules.md`           | `.mdc` 5파일 체계, Dual-Track TDD 요약                                                    | Quality Requirements, Development Method                               | **P2**   |
| `magicsquare-project.mdc`             | 목적, 7 불변식, 브랜치·커밋                                                               | Goals, Invariants                                                      | **P1**   |
| `magicsquare-tdd-testing.mdc`         | RED/GREEN/REFACTOR, AAA, 커버리지 80%                                                     | Quality Requirements, Verification Method                              | **P1**   |
| `magicsquare-ecb-architecture.mdc`    | ECB 레이어·의존·디렉토리                                                                  | Architecture, Layer Boundary                                           | **P1**   |
| `magicsquare-python-code-style.mdc`   | Python 3.13, 타입힌트, Black 88                                                           | Engineering Principles                                                 | **P2**   |
| `magicsquare-forbidden.mdc`           | 금지 패턴, AI 행동 규칙                                                                   | Constraints, Appendix                                                  | **P2**   |
| `Report/04_cursor-agents_Report.md`   | Cursor Agent 14개 기록                                                                    | 팀 워크플로 부록 (선택)                                                | **P3**   |
| *(없음)* `.cursorrules`              | 단일 파일 미사용                                                                          | `Report/03` + `.mdc`로 대체                                            | —        |

### 3. PRD Section Mapping

| PRD Section                            | Primary Source                    | Secondary Source           | Content to Extract                                      |
| -------------------------------------- | --------------------------------- | -------------------------- | ------------------------------------------------------- |
| **Executive Summary / Vision**         | `Prompting/05`                    | `01.problem-definition`    | 불변식 우선 사고 훈련, 검증 체계 구축                   |
| **Background**                         | `01.problem-definition`           | `05`                       | 4×4 관찰, 사용자 불편, 구조적 문제                      |
| **Problem Definition**               | `01.problem-definition`           | `05`                       | 표면 vs 개선 정의; 유효성 판정 체계                     |
| **Why Now / Why Chain**                | `01.problem-definition`           | `05`                       | Why#1~#3                                                |
| **Goals & Success Metrics**            | `Prompting/05`                    | `magicsquare-project.mdc`  | SC-1~8, LG-1~6                                          |
| **Persona & Target Users**             | `Prompting/05`                    | `01`                       | TDD+ECB 학습자                                          |
| **Scope / Non-Scope**                  | `Prompting/05`                    | `02.design`                | 4×4, ECB, Solver vs N×N·GUI 제외                        |
| **Epic & User Journey**                | `Prompting/05`                    | `05_Report`                | 5 Stage, Dual-Track, US-01~11                           |
| **User Stories & AC**                  | `Prompting/05`                    | `05_Report`                | S-01~05, Future RED Test                                |
| **Functional Requirements**            | `Prompting/05`                    | `02.design`, ECB rules       | InputValidator, BlankFinder, Solver 등                  |
| **Input/Output Contract**              | `02.design`                       | `entity/types.py`, `05`    | `validate()`, `ValidationResult`, Solver I/O            |
| **Invariant Table**                    | `magicsquare-project.mdc`         | `01`, `02`, `05`           | INV-1~7, Traceability Rule                              |
| **Acceptance Criteria (검증)**         | `02.design`                       | `05`                       | RED/경계, reason, Gherkin                               |
| **Gherkin / BDD Scenarios**            | `Prompting/05`                    | `05_Report`                | SC 4건 완본 + 6건 보완 대기                             |
| **Verification Checklist**             | `05_Report` + `Prompting/05`      | `02`                       | 7.5/10, 5영역 점검                                      |
| **Architecture & Layer Boundary**      | `magicsquare-ecb-architecture.mdc`| `03`, `05`                 | Boundary→Control→Entity                                 |
| **Development Method**                 | `magicsquare-tdd-testing.mdc`     | `02`, `project.mdc`        | RED-GREEN-REFACTOR, Dual-Track                          |
| **Quality Requirements**               | `magicsquare-tdd-testing.mdc`     | `05`, `pyproject.toml`     | AAA, 80% cov                                            |
| **Engineering Principles**             | `forbidden.mdc`, `code-style.mdc` | `03.cursor-rules`          | 금지 패턴, 타입힌트, Final 상수                         |
| **Traceability Matrix**                | `Prompting/05`                    | `02`                       | Concept→Invariant→Contract→Test→Implementation          |
| **Risks / Open Issues**                | `05_Report`                       | `05` Level 5               | SC 누락, Stage 5 Story                                  |
| **Appendix: Rules 원문**               | `.cursor/rules/*.mdc`             | `03.cursor-rules`          | globs·통합 이력                                         |

### 4. Source Priority Rules

| Topic                         | Primary Source                    | Reason                                           |
| ----------------------------- | --------------------------------- | ------------------------------------------------ |
| 제품 비전·Epic·학습 목표      | `Prompting/05`                    | Epic/Journey/Story/Gherkin 계층 완본             |
| 문제 정의·Why Chain           | `01.problem-definition`           | STEP 1~5 전용                                    |
| 검증 코어 API·테스트 명세     | `02.design` + `entity/types.py`   | 구현과 일치하는 상세 계약                        |
| Solver·입력검증 범위·AC       | `Prompting/05`                    | `02.design`은 `validate()` 중심                  |
| 7개 불변 조건                 | `magicsquare-project.mdc`         | alwaysApply 정본                                 |
| ECB 레이어·디렉토리           | `magicsquare-ecb-architecture.mdc`| `02.design` flat 구조보다 최신                   |
| TDD·테스트 품질               | `magicsquare-tdd-testing.mdc`     | RED/GREEN/REFACTOR 원문                          |
| 금지 패턴                     | `magicsquare-forbidden.mdc`       | 통합 금지 목록                                   |
| Dual-Track 의미               | `Prompting/05`                    | UI/Logic 트랙; Git 브랜치와 용어 분리            |

### 5. Directly Transfer to PRD Body

| Source Document           | Content Type              | Target PRD Section                    |
| ------------------------- | ------------------------- | ------------------------------------- |
| `01.problem-definition`   | Why Chain, 문제 정의      | Background, Problem Definition        |
| `Prompting/05`            | Epic, Scope, Stories, AC  | Vision, Goals, User Stories           |
| `02.design`               | `validate()`, 7 checks    | I/O Contract, Functional Spec         |
| `magicsquare-project.mdc` | 7 불변식                  | Invariant Table                       |
| `magicsquare-ecb-architecture.mdc` | 레이어·컴포넌트  | Architecture                          |
| `05_Report`               | Verification 7.5/10       | Verification Checklist                |

### 6. Move to Appendix or Engineering Principles

| Source Document              | Content Type        | Target Appendix / Section      |
| ---------------------------- | ------------------- | ------------------------------ |
| `magicsquare-tdd-testing.mdc`| TDD 단계 규칙       | Appendix A: TDD Process        |
| `magicsquare-forbidden.mdc`  | 금지 패턴           | Appendix C: Prohibited Patterns|
| `magicsquare-python-code-style.mdc` | 스타일 규칙  | Appendix D: Python Style       |
| `magicsquare-project.mdc`    | 브랜치·커밋         | Appendix E: Git Workflow         |
| `03.cursor-rules`            | `.mdc` 인덱스       | Appendix F: Cursor Rules Index |
| `ecb-architecture.mdc`       | 구식 `failed` 예시  | PRD 미반영 (구식 예시)         |

### 7. Conflicts / Ambiguities

| Issue                                      | Related Document        | Decision Needed                              |
| ------------------------------------------ | ----------------------- | -------------------------------------------- |
| 검증만 vs Solver 포함                      | `01`, `02` vs `05`      | MVP vs Phase 2 분리                          |
| `bool` vs `ValidationResult`               | `05` S-04 vs `02`       | 단일 API 통일                                |
| flat vs ECB 디렉토리                       | `02` vs ECB rules       | ECB 트리 정본                                |
| Dual-Track vs Git 브랜치                   | `05` vs `project.mdc`   | 용어 분리                                    |
| GUI Non-Scope vs UI RED                    | `05` Scope              | UI 트랙 정의                                 |
| 빈칸 `0` vs `None`                         | `05` Gherkin vs S-02    | Data Dictionary 단일화                       |
| Gherkin 6건 미작성                         | `05`, `05_Report`       | Draft vs v1.0                                |

### 8. Recommended PRD Outline

```text
1. Document Control
2. Executive Summary
3. Background & Context
4. Problem Statement
5. Vision & Goals
6. Scope (MVP vs Phase 2)
7. Users & Journey
8. Domain Model
9. Functional Requirements
10. Contracts & Interfaces
11. Requirements ↔ Verification
12. Architecture
13. Development & Quality Approach
14. Risks, Gaps & Open Items
15. Appendices (A–G)
```

#### 작성 시 실무 메모

1. **PRD 본문 1차 축**은 `Prompting/05`, **검증 API**는 `02.design` + `entity/types.py`.
2. **§6 Scope**에서 MVP와 Phase 2를 분리하지 않으면 AC 충돌이 반복됩니다.
3. `ecb-architecture.mdc`의 `failed: list[str]` 예시는 PRD에 넣지 않습니다.

---

## Turn 2

### User (Turn 2)

/Report and Task Closer 이번 세션 대화를 정리해

### AI (Turn 2)

(본 Turn의 응답은 `Report/06_prd-reference-analysis_Report.md` 및 본 파일 Turn 2에 세션 Export 완료 보고로 기록됨.)

---

*이 파일은 Report and Task Closer Agent에 의해 생성·갱신되었습니다.*
