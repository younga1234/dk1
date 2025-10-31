# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

이 저장소는 한국 고고학 발굴 보고서 PDF 파일들을 관리하는 프로젝트입니다. 주로 전남 지역(나주, 순천, 광양, 무안, 함평, 해남 등)의 청동기시대 및 삼국시대 유적 보고서 약 150여 개를 포함합니다.

### 프로젝트 특성
- **문서 중심**: 애플리케이션 코드 없음, 순수 문서 관리
- **대용량 파일**: 개별 PDF 파일 100MB~1GB 규모
- **학술 자료**: 고고학 전문 용어 및 한국어 지명 포함

## Context 관리 전략 (Claude Code 개발자 노하우)

### 1. @ 참조로 효율적인 Context 제공

**파일 참조:**
```
@README.md              # README 전체 내용 포함
@.gitignore            # gitignore 규칙 확인
@.github/workflows/ci.yml  # CI 워크플로우 이해
```

**디렉토리 구조 참조:**
```
@.claude/skills/       # Skills 디렉토리 구조 나열
```

**여러 파일 동시 참조:**
```
@CLAUDE.md and @README.md  # 두 파일 동시에 컨텍스트 제공
```

### 2. Plan Mode 활용

복잡한 분석이나 계획 수립 시 Plan Mode 사용:
- **활성화**: `Shift+Tab` 키 또는 `--permission-mode plan`
- **용도**: 
  - 저장소 구조 심층 분석
  - 다단계 작업 계획 수립
  - PDF 파일 분류 전략 수립
- **특징**: 읽기 전용, 파일 수정 없음

### 3. Extended Thinking 활용

심층 분석이 필요한 경우:
- **활성화**: `Tab` 키로 토글
- **트리거 표현**: "think deeply about", "think hard"
- **사용 시기**:
  - 복잡한 분류 체계 설계
  - PDF 메타데이터 추출 전략
  - 대량 파일 관리 아키텍처

### 4. Skills 시스템 활용

#### 설치된 Project Skills

**pdf-management Skill**
- 위치: `.claude/skills/pdf-management/`
- 기능: PDF 파일 검색, 분류, 메타데이터 추출
- 자동 호출: "나주 지역 보고서 찾아줘" 같은 요청 시

#### Skills 사용 패턴

Skills는 **자동으로 호출**됩니다. 명시적 호출 불필요:
```
❌ "/pdf-management 실행"  (슬래시 명령어가 아님)
✅ "순천 지역 PDF 파일 목록 만들어줘"  (자동 호출됨)
```

### 5. Context Window 최적화

**대용량 파일 다루기:**
- pdf/ 디렉토리 직접 읽기 ❌ (context 낭비)
- ls 명령어로 파일명만 확인 ✅
- 필요한 파일만 선택적으로 분석 ✅

**메모리 계층 활용:**
- Project Memory (이 CLAUDE.md): 팀 전원 공유 지침
- User Memory (`~/.claude/CLAUDE.md`): 개인 선호도
- Session Memory: 현재 대화 컨텍스트

## 중요한 Git 워크플로우 규칙

### 절대 커밋하지 말아야 할 디렉토리

- `pdf/` - 대용량 PDF 파일들 (100MB 이상 파일 다수 포함)
- `data/` - 데이터 폴더

이 디렉토리들은 `.gitignore`에 의해 제외되며, **로컬에서만** 관리됩니다. 이 규칙을 절대 변경하지 마세요.

### Git 커밋 시 필수 사항

**항상 smithery-ai-github MCP를 사용하여 커밋하고 푸시하세요.**

로컬 git 명령어 대신 GitHub MCP 도구를 사용:
- `mcp__smithery-ai-github__create_or_update_file` - 파일 생성/업데이트
- `mcp__smithery-ai-github__push_files` - 여러 파일 한 번에 푸시

## MCP 서버 사용 우선순위

이 프로젝트에서는 다음 순서로 MCP 서버를 사용합니다:

### 1. waldzellai-clear-thought (복잡한 작업 시 최우선)
**사용 시기:**
- 복잡한 분류 체계 설계
- 다단계 작업 계획
- 문제 분석 및 해결 전략

**패턴:**
- Backward Thinking: 목표에서 시작점으로 (계획 수립)
- Forward Thinking: 탐색 및 발견
- Branching: 여러 접근법 비교

### 2. wonderwhy-er-desktop-commander (clear-thought 이후)
**사용 시기:**
- 파일 시스템 작업
- 로컬 터미널 명령 실행
- PDF 파일 메타데이터 확인

**주요 도구:**
- `list_directory`: 디렉토리 구조 확인
- `read_file`: 파일 읽기
- `start_process`: Python/Node REPL 시작

### 3. smithery-ai-github (Git 커밋 필수)
**사용 시기:**
- 모든 Git 커밋 및 푸시 작업
- GitHub 이슈/PR 관리

### 4. upstash-context-7-mcp (문서 수집)
**사용 시기:**
- 라이브러리/프레임워크 최신 문서
- 외부 API 레퍼런스

## 효율적인 작업 워크플로우

### 1. 새 작업 시작

```
1. Plan Mode로 분석 (Shift+Tab)
2. waldzellai-clear-thought로 계획 수립
3. wonderwhy-er-desktop-commander로 실행
4. smithery-ai-github로 커밋
```

### 2. PDF 파일 관리

```
# 파일 목록 확인 (context 효율적)
ls pdf/ | grep "나주"

# 특정 파일 상세 정보
stat pdf/나주복암리유적.pdf

# Python으로 메타데이터 추출 (필요 시)
python -c "import os; print(os.path.getsize('pdf/file.pdf'))"
```

### 3. 문서 분류 작업

**단계별 접근:**
1. @참조로 README와 CLAUDE.md 컨텍스트 제공
2. pdf-management Skill 자동 활용
3. 결과를 Markdown 문서로 정리
4. GitHub에 커밋

## 저장소 구조

```
.
├── pdf/                    # PDF 파일들 (Git 제외, 로컬 전용)
│   ├── 나주*.pdf          # 나주 지역 보고서
│   ├── 순천*.pdf          # 순천 지역 보고서
│   └── ...
├── data/                   # 데이터 폴더 (Git 제외, 로컬 전용)
├── .claude/
│   └── skills/
│       └── pdf-management/  # PDF 관리 Skill
│           └── SKILL.md
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions 워크플로우
├── .gitignore              # pdf/와 data/ 제외 설정
├── README.md               # 프로젝트 설명
└── CLAUDE.md               # 이 파일 (Project Memory)
```

## GitHub Actions 워크플로우

`.github/workflows/ci.yml`은 다음을 수행합니다:
- main 브랜치로 push 또는 PR 시 자동 실행
- 저장소 구조 확인
- .gitignore 설정 검증
- Python 3.11 환경 설정

워크플로우는 검증 목적이며, 빌드나 테스트를 실행하지 않습니다.

## 일반 워크플로우 패턴

### 코드베이스 탐색
```
"이 저장소의 구조를 설명해주세요" → 개요 시작
"@README.md 내용 기반으로 프로젝트 목적 설명" → 구체화
```

### 파일 검색
```
"@pdf/ 디렉토리에서 순천 관련 파일 찾기"
"100MB 이상 파일 목록 생성"
```

### 분석 작업
```
Plan Mode 활성화 → 전체 구조 분석
Extended Thinking → 심층 분류 전략
pdf-management Skill → 자동 처리
```

## 주의사항

- 현재 이 저장소에는 **애플리케이션 코드가 없습니다**
- 빌드, 테스트, 또는 배포 프로세스가 없습니다
- 주요 목적은 대용량 PDF 파일의 조직적 관리입니다
- 모든 대화와 응답은 **한국어로만** 작성하세요
- PDF 내용 읽기는 별도 PDF 처리 도구 필요 (이미지로 취급)

## 고급 기능

### Git Worktree (병렬 작업)
```bash
git worktree add ../dk1-feature -b feature-branch
cd ../dk1-feature
claude  # 격리된 환경에서 작업
```

### 커스텀 슬래시 명령어
`.claude/commands/` 디렉토리에 Markdown 파일로 생성:
```bash
# .claude/commands/analyze.md
PDF 파일 통계 분석 및 보고서 생성
```
사용: `> /analyze`

### 이미지 활용
- PDF 스크린샷 드래그 앤 드롭 → 내용 분석
- 유적 지도 이미지 → 위치 정보 추출

## 참고 자료

이 CLAUDE.md는 다음 공식 문서를 기반으로 작성되었습니다:
- [Claude Code Memory System](https://docs.claude.com/en/docs/claude-code/memory.md)
- [Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md)
- [Common Workflows](https://docs.claude.com/en/docs/claude-code/common-workflows.md)
- [Hooks Guide](https://docs.claude.com/en/docs/claude-code/hooks-guide.md)
