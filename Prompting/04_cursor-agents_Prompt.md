# cursor-agents — 세션 대화 전문
> 날짜: 2026-05-28  
> 세션 설명: `.cursor/agents/` 폴더에 역할별 Agent 파일 14개 생성 (code-reviewer 포함 + report-and-task-closer)

---

## Turn 1

### User
`.cursor/agents/code-reviewer.md` 파일을 만들어 줘. YAML frontmatter에 name, description, model: inherit, readonly: true 를 넣고, 본문에는 코드 리뷰 지침을 적어 줘. 코드 리뷰어: 코드를 읽고 버그는 없는지, 코딩 규칙에 따라 올바르게 작성되었는지를 점검하고 성능 최적화를 제안하는 전문 코드 품질 검토자.

### AI
`.cursor/agents/` 디렉토리를 생성하고 `code-reviewer.md` 파일을 작성했다.

파일 구성:
- YAML frontmatter: `name: Code Reviewer`, `description`, `model: inherit`, `readonly: true`
- 본문 구성 (5개 리뷰 항목): 버그 탐지, 코딩 규칙, ECB 아키텍처, 테스트 품질, 성능 최적화
- 리뷰 결과는 🔴 CRITICAL / 🟡 WARNING / 🔵 SUGGESTION 심각도로 분류, 마지막에 PASS / NEEDS REVISION 판정 출력

생성 파일: `.cursor/agents/code-reviewer.md` (210줄)

---

## Turn 2

### User
```json
[{
  "resource": "/c:/DEV/MagicSquare_021/.cursor/agents/code-reviewer.md",
  "owner": "markdownlint",
  "code": { "value": "MD040" },
  "severity": 4,
  "message": "MD040/fenced-code-language: Fenced code blocks should have a language specified",
  "startLineNumber": 195
}]
```

### AI
195번째 줄 코드 펜스에 `text` 언어 태그를 추가해 MD040 경고를 해소했다.

수정 내용: ` ``` ` → ` ```text `

---

## Turn 3

### User
(긴 프롬프트 — 공통 Agent 안전 규칙 + A-1~A-9 Agent 정의 전문 제공)  
아래의 지침을 참고하여 code-reviewer 와 같이 역할 별 agent들을 만들어 줘

### AI
12개 Agent 파일을 `.cursor/agents/` 폴더에 생성했다.

생성된 파일 목록:

| 파일명 | Agent 이름 | readonly |
|---|---|:---:|
| `system-optimization-engineer.md` | System Optimization Engineer | false |
| `ux-design-advisor.md` | UX Design Advisor | false |
| `multi-agent-collaboration.md` | Multi-Agent Collaboration | false |
| `app-runner.md` | App Runner | false |
| `backup-snapshot.md` | Backup Snapshot | false |
| `backup-restore.md` | Backup Restore | false |
| `product-planning-manager.md` | Product Planning Manager | false |
| `backend-developer.md` | Backend Developer | false |
| `frontend-developer.md` | Frontend Developer | false |
| `quality-assurance-engineer.md` | Quality Assurance Engineer | true |
| `ai-integration-expert.md` | AI Integration Expert | false |
| `backup-report-github-manager.md` | Backup / Report / GitHub Manager | false |

설계 원칙:
- 읽기 전용 분석 Agent(code-reviewer, quality-assurance-engineer)는 `readonly: true`
- 파일 생성·수정·Git 명령 실행 Agent는 `readonly: false`
- 모든 Agent 하단에 공통 안전 규칙 6개 항목 통일 적용
- backend-developer, quality-assurance-engineer에는 이 프로젝트의 TDD/ECB 컨텍스트 추가 반영

---

## Turn 4

### User
보고서 작성 및 스크립트 export 에이전트도 추가해줘
- Name : report and task closer
- 동작 : 현재 세션을 마무리하기 전에 사용되면 Agent가 현재 대화의 모든 AI답변 전체를 Export하고, 작업 내용을 보고서로 작성하는 역할을 수행

### AI
`.cursor/agents/report-and-task-closer.md`를 생성했다.

동작 방식 (4단계):
- STEP 1: Report/, Prompting/ 폴더의 기존 파일 번호를 확인해 다음 번호 결정
- STEP 2: 현재 세션 전체 대화를 `Prompting/NN_작업명_Prompt.md`에 원문 그대로 Export
- STEP 3: 수행 작업 요약 보고서를 `Report/NN_작업명_Report.md`에 작성
- STEP 4: 생성된 파일 경로, 기록된 Turn 수, 누락 여부, 다음 작업 제안을 보고

핵심 설계 원칙:
- AI 응답은 요약 없이 원문 전체 저장 (코드 블록, 표, 목록 서식 보존)
- 기존 Report/03_..., Prompting/03_...이 있으므로 다음 호출 시 04_번호로 자동 시작
- 기존 파일을 절대 덮어쓰지 않음
- 누락된 Turn이 있으면 "누락: Turn N (이유)" 형태로 명시

---

## Turn 5

### User
/Report and Task Closer

(세션 종료 요청 — 이번 세션의 전체 대화를 Export하고 보고서 작성 지시)

### AI
`Prompting/04_cursor-agents_Prompt.md` 및 `Report/04_cursor-agents_Report.md` 두 파일을 생성하여 세션 Export를 완료했다.
