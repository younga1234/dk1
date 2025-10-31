# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

이 저장소는 **한국 고고학 발굴 보고서 작성 시스템**입니다. PDF 파일 관리뿐만 아니라, 고고학 발굴조사보고서의 고찰(考察) 섹션을 체계적으로 작성할 수 있는 Skills 시스템을 제공합니다.

### 프로젝트 범위
1. **PDF 관리**: 전남 지역(나주, 순천, 광양, 무안, 함평, 해남 등) 청동기시대 및 삼국시대 유적 보고서 약 150여 개 관리
2. **보고서 작성**: 8개의 전문 Skills를 활용한 학술 보고서 고찰 작성 자동화

### 프로젝트 특성
- **문서 중심**: 애플리케이션 코드 없음, 순수 문서 관리 및 작성
- **대용량 파일**: 개별 PDF 파일 100MB~1GB 규모
- **학술 자료**: 고고학 전문 용어 및 한국어 지명 포함
- **자동화 시스템**: Skills 기반 보고서 고찰 자동 생성

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

#### 설치된 Project Skills (9개)

**1. pdf-management Skill**
- **위치**: `.claude/skills/pdf-management/`
- **기능**: PDF 파일 검색, 분류, 메타데이터 추출
- **자동 호출**: "나주 지역 보고서 찾아줘" 같은 요청 시

**2. 고찰 작성 Skills (8개)**

발굴조사보고서의 고찰 섹션을 체계적으로 작성하는 전문 Skills:

| Skill 이름 | 설명 | 트리거 예시 |
|-----------|------|------------|
| `gochal-01-conclusion` | 결론 및 종합 분석 | "결론 작성", "종합 분석" |
| `gochal-02-yugu-analysis` | 유구(주거지, 수혈 등) 분석 | "유구 분석", "주거지 형태 분석" |
| `gochal-03-yumul-analysis` | 유물(토기, 석기 등) 분석 | "유물 분석", "토기 형식 분류" |
| `gochal-04-pyeonnyeon` | 편년(시기 설정) | "편년 고찰", "연대 분석" |
| `gochal-05-site-comparison` | 주변 유적 비교 | "주변 유적 비교", "지역 내 위치" |
| `gochal-06-science-analysis` | 자연과학 분석 종합 | "자연과학 분석", "AMS 연대 해석" |
| `gochal-07-culture-restoration` | 문화 양상 및 생활상 복원 | "생활상 복원", "문화 양상 분석" |
| `gochal-08-summary` | 요약 및 초록 작성 | "요약 작성", "영문 abstract" |

#### Skills 사용 패턴

Skills는 **자동으로 호출**됩니다. 명시적 호출 불필요:
```
❌ "/gochal-02-yugu-analysis 실행"  (슬래시 명령어가 아님)
✅ "주거지 형태 분석해줘"  (자동 호출됨)
```

#### Skills 입력 데이터 형식

고찰 Skills는 다양한 형식의 입력을 처리합니다:
- **Excel/CSV**: 유구/유물 목록 스프레드시트
- **JSON**: 표준화된 데이터 구조
- **Markdown**: 구조화된 텍스트
- **대화 입력**: 사용자가 직접 제공하는 정보

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

### 3. 보고서 고찰 작성 워크플로우 (NEW!)

**전체 프로세스:**
```
1. PDF 파일 수집 → pdf-management Skill 활용
2. 유구 데이터 준비 → Excel/CSV/JSON 형식
3. 고찰 작성 요청 → 해당 gochal Skill 자동 호출
4. 결과 검토 및 수정
5. GitHub에 커밋
```

**단계별 예시:**

**Step 1: 유구 분석**
```
"나주 복암리 유적의 주거지 데이터를 분석해서 유구 분석 고찰 작성해줘"
→ gochal-02-yugu-analysis 자동 호출
→ Excel 데이터 → JSON 변환 → Markdown 생성
```

**Step 2: 유물 분석**
```
"출토된 무문토기와 석기 분석해서 유물 분석 고찰 작성해줘"
→ gochal-03-yumul-analysis 자동 호출
```

**Step 3: 편년**
```
"AMS 연대측정 결과와 유물 형식 분석을 종합해서 편년 고찰 작성해줘"
→ gochal-04-pyeonnyeon 자동 호출
```

**Step 4: 결론**
```
"지금까지의 모든 고찰을 종합해서 결론 작성해줘"
→ gochal-01-conclusion 자동 호출
```

### 4. 문서 분류 작업

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
│   └── 주거지/            # 주거지 관련 자료
├── data/                   # 데이터 폴더 (Git 제외, 로컬 전용)
├── 고찰/                   # 고찰 작성 작업 디렉토리
│   ├── CLAUDE.md          # 고찰 작성 가이드
│   ├── skill-제작-계획서.md
│   └── 고찰.md
├── docs/                   # 문서 디렉토리
│   └── context-management-guide.md  # Context 관리 실전 가이드
├── .claude/
│   ├── skills/
│   │   ├── pdf-management/           # PDF 관리 Skill
│   │   ├── gochal-01-conclusion/     # 결론 작성 Skill
│   │   ├── gochal-02-yugu-analysis/  # 유구 분석 Skill
│   │   ├── gochal-03-yumul-analysis/ # 유물 분석 Skill
│   │   ├── gochal-04-pyeonnyeon/     # 편년 Skill
│   │   ├── gochal-05-site-comparison/  # 주변 유적 비교 Skill
│   │   ├── gochal-06-science-analysis/ # 자연과학 분석 Skill
│   │   ├── gochal-07-culture-restoration/ # 문화 양상 복원 Skill
│   │   └── gochal-08-summary/        # 요약 작성 Skill
│   └── settings.local.json
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions 워크플로우
├── .gitignore              # pdf/와 data/ 제외 설정
├── README.md               # 프로젝트 설명
└── CLAUDE.md               # 이 파일 (Project Memory)
```

## 고찰 작성 시스템 상세 (NEW!)

### 고찰 Skills 아키텍처

각 Skill은 다음 구조로 구성됩니다:

```
gochal-XX-name/
├── SKILL.md              # Skill 정의 및 프롬프트
├── assets/
│   └── template.md       # Markdown 출력 템플릿
├── references/
│   ├── examples.md       # 실제 보고서 예시
│   └── terminology.md    # 전문 용어 사전
└── scripts/
    └── data_processor.py # 데이터 변환 스크립트 (Python)
```

### 데이터 처리 파이프라인

```
Excel/CSV/JSON/Markdown 입력
    ↓
scripts/data_processor.py (표준화)
    ↓
표준 JSON 데이터
    ↓
Skill 프롬프트 + 템플릿
    ↓
학술 논문 수준 Markdown 고찰
```

### 고찰 작성 모범 사례

**DO:**
- Excel 파일로 유구/유물 데이터 정리 후 제공
- 한 번에 하나의 고찰 섹션씩 작성
- 생성된 Markdown 결과 검토 후 수정 요청
- 전문 용어는 references/terminology.md 참조

**DON'T:**
- 한 번에 모든 고찰 섹션 동시 작성 요청 ❌
- 데이터 없이 "상상으로" 고찰 작성 요청 ❌
- Skills 수동 호출 시도 ❌

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

### 보고서 작성 (NEW!)
```
데이터 준비 → 고찰 요청 → Skill 자동 호출 → 결과 검토
```

## 주의사항

- 현재 이 저장소에는 **애플리케이션 코드가 없습니다**
- 빌드, 테스트, 또는 배포 프로세스가 없습니다
- 주요 목적은:
  1. 대용량 PDF 파일의 조직적 관리
  2. 고고학 발굴조사보고서 고찰 자동 생성
- 모든 대화와 응답은 **한국어로만** 작성하세요
- PDF 내용 읽기는 별도 PDF 처리 도구 필요 (이미지로 취급)
- 고찰 작성 시 반드시 실제 데이터 기반으로 작성 (상상 금지)

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

### 프로젝트 문서 (CLAUDE.md 파일들)

이 프로젝트는 각 디렉토리별로 특화된 CLAUDE.md 파일을 관리합니다:

1. **`/CLAUDE.md`** (이 파일) - 프로젝트 전체 가이드
   - 프로젝트 개요 및 범위
   - Context 관리 전략
   - MCP 서버 사용 우선순위
   - 전체 워크플로우

2. **`고찰/CLAUDE.md`** - 고찰 작성 Skills 사용 가이드
   - 8개 고찰 Skills 사용법
   - 데이터 준비 가이드
   - 워크플로우 예시
   - 문제 해결

3. **`.claude/CLAUDE.md`** - Skills 개발 가이드
   - Skill 아키텍처 및 구조
   - SKILL.md 작성 가이드
   - Skills 개발 워크플로우
   - 데이터 파이프라인

4. **`docs/CLAUDE.md`** - 문서 작성 스타일 가이드
   - Markdown 컨벤션
   - 문서 유형별 가이드
   - 품질 체크리스트
   - 파일 명명 규칙

### 기타 프로젝트 문서
- `docs/context-management-guide.md` - Claude Code Context 관리 실전 가이드 (2025년 10월)
- `고찰/skill-제작-계획서.md` - Skills 제작 계획

### Claude Code 공식 문서
이 CLAUDE.md는 다음 공식 문서를 기반으로 작성되었습니다:
- [Claude Code Memory System](https://docs.claude.com/en/docs/claude-code/memory.md)
- [Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md)
- [Common Workflows](https://docs.claude.com/en/docs/claude-code/common-workflows.md)
- [Hooks Guide](https://docs.claude.com/en/docs/claude-code/hooks-guide.md)
