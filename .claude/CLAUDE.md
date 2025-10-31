# .claude/CLAUDE.md

이 파일은 **Claude Code Skills 개발 가이드**입니다.

## 개요

`.claude/` 디렉토리는 Claude Code의 프로젝트별 설정 및 Skills를 관리하는 공간입니다. 이 저장소에는 총 9개의 Skills가 설치되어 있습니다:

- **pdf-management** (1개): PDF 파일 관리
- **gochal-XX** (8개): 고고학 발굴조사보고서 고찰 작성

## 디렉토리 구조

```
.claude/
├── CLAUDE.md                    # 이 파일 (Skills 개발 가이드)
├── settings.local.json          # Claude Code 설정
├── output-styles/               # 출력 스타일 템플릿
└── skills/                      # Skills 디렉토리
    ├── README.md
    ├── pdf-management/          # PDF 관리 Skill
    ├── gochal-01-conclusion/    # 결론 작성 Skill
    ├── gochal-02-yugu-analysis/ # 유구 분석 Skill
    ├── gochal-03-yumul-analysis/# 유물 분석 Skill
    ├── gochal-04-pyeonnyeon/    # 편년 Skill
    ├── gochal-05-site-comparison/   # 주변 유적 비교 Skill
    ├── gochal-06-science-analysis/  # 자연과학 분석 Skill
    ├── gochal-07-culture-restoration/ # 문화 복원 Skill
    └── gochal-08-summary/       # 요약 작성 Skill
```

---

## Skill 아키텍처

### 표준 Skill 구조

각 Skill은 다음 구조를 따릅니다:

```
skill-name/
├── SKILL.md                 # [필수] Skill 정의 파일
├── assets/                  # [선택] 템플릿, 리소스
│   ├── template.md          # Markdown 출력 템플릿
│   └── schema.json          # 데이터 스키마
├── references/              # [선택] 참고 자료
│   ├── examples.md          # 실제 사용 예시
│   ├── terminology.md       # 전문 용어 사전
│   └── bibliography.md      # 참고 문헌
└── scripts/                 # [선택] 데이터 처리 스크립트
    ├── data_processor.py    # Python 스크립트
    └── validator.js         # Node.js 검증 스크립트
```

---

## SKILL.md 작성 가이드

### 필수 섹션

SKILL.md는 다음 섹션을 반드시 포함해야 합니다:

```markdown
# Skill Name

간단한 Skill 설명 (1-2문장)

## Description

상세한 Skill 설명 및 사용 사례

## Triggers

이 Skill이 자동 호출되는 트리거 키워드 목록

## Instructions

Claude Code가 이 Skill을 실행할 때 따라야 할 구체적인 지침

## Examples

사용 예시 및 입출력 샘플
```

### SKILL.md 예시

```markdown
# gochal-02-yugu-analysis

청동기시대 및 삼국시대 유적의 유구(주거지, 수혈 등) 분석 고찰 작성

## Description

발굴조사보고서의 유구 분석 고찰을 학술 논문 수준으로 자동 생성합니다.
주거지, 수혈, 구상유구 등의 형태, 배치, 시기별 변화를 분석합니다.

## Triggers

- "유구 분석", "주거지 분석", "수혈 분석"
- "유구 형태 고찰", "배치 양상 분석"
- "dwelling analysis", "pit analysis"

## Instructions

1. 입력 데이터 형식 확인 (Excel/CSV/JSON)
2. scripts/data_processor.py로 표준 JSON 변환
3. assets/template.md 기반으로 Markdown 생성
4. references/terminology.md의 표준 용어 사용
5. references/examples.md의 문체 참조
6. 출력 파일: 고찰/output/02-유구분석.md

## Examples

**입력 (Excel):**
| 유구번호 | 유구유형 | 평면형태 | 규모(m) |
|---------|---------|---------|---------|
| 1호 | 주거지 | 원형 | 5.2x5.0 |

**출력 (Markdown):**
```
## 유구 분석

### 주거지

조사 결과 주거지 20기가 확인되었다...
```
```

---

## Skill 개발 워크플로우

### 1. 새 Skill 생성

```bash
# 디렉토리 생성
mkdir -p .claude/skills/my-new-skill/{assets,references,scripts}

# SKILL.md 생성
touch .claude/skills/my-new-skill/SKILL.md
```

### 2. SKILL.md 작성

위의 "SKILL.md 작성 가이드" 참조하여 작성

### 3. 템플릿 및 참고자료 추가

```bash
# 출력 템플릿
touch .claude/skills/my-new-skill/assets/template.md

# 용어 사전
touch .claude/skills/my-new-skill/references/terminology.md

# 예시
touch .claude/skills/my-new-skill/references/examples.md
```

### 4. 데이터 처리 스크립트 (선택)

Python 스크립트 예시:
```python
# scripts/data_processor.py
import json
import pandas as pd

def process_excel(file_path):
    """Excel 파일을 표준 JSON으로 변환"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

def validate_data(data):
    """데이터 검증"""
    required_fields = ['유구번호', '유구유형', '평면형태']
    for item in data:
        for field in required_fields:
            if field not in item:
                raise ValueError(f"필수 필드 누락: {field}")
    return True
```

### 5. Skill 테스트

```
사용자: "새 Skill 테스트해줘"
→ Claude Code가 트리거 인식
→ SKILL.md의 Instructions 실행
→ 결과 확인
```

### 6. Git 커밋

```bash
# smithery-ai-github MCP 사용
git add .claude/skills/my-new-skill/
git commit -m "Add new skill: my-new-skill"
git push
```

---

## 고찰 Skills 상세

### gochal-01-conclusion (결론)
- **트리거**: "결론", "종합", "conclusion"
- **입력**: 이전 모든 고찰 섹션
- **출력**: `고찰/output/01-결론.md`
- **특징**: 전체 고찰 종합 및 학술적 의의 도출

### gochal-02-yugu-analysis (유구 분석)
- **트리거**: "유구 분석", "주거지 형태", "dwelling"
- **입력**: Excel/CSV/JSON (유구 목록)
- **출력**: `고찰/output/02-유구분석.md`
- **특징**: 형태, 배치, 시기별 변화 분석

### gochal-03-yumul-analysis (유물 분석)
- **트리거**: "유물 분석", "토기 분류", "pottery"
- **입력**: Excel/CSV/JSON (유물 목록)
- **출력**: `고찰/output/03-유물분석.md`
- **특징**: 형식 분류, 문양, 제작 기법 분석

### gochal-04-pyeonnyeon (편년)
- **트리거**: "편년", "시기 설정", "chronology"
- **입력**: 유물 형식 + AMS 연대 데이터
- **출력**: `고찰/output/04-편년.md`
- **특징**: 상대편년 + 절대편년 종합

### gochal-05-site-comparison (주변 유적 비교)
- **트리거**: "주변 유적", "지역 비교", "site comparison"
- **입력**: 비교 유적 목록 + 본 유적 특징
- **출력**: `고찰/output/05-주변유적비교.md`
- **특징**: 지역적 맥락 및 문화권 설정

### gochal-06-science-analysis (자연과학 분석)
- **트리거**: "자연과학", "AMS 연대", "scientific analysis"
- **입력**: AMS, 토양, 식물유체 분석 데이터
- **출력**: `고찰/output/06-자연과학분석.md`
- **특징**: 과학 분석 결과의 고고학적 해석

### gochal-07-culture-restoration (문화 복원)
- **트리거**: "생활상", "문화 복원", "cultural reconstruction"
- **입력**: 유구 배치 + 유물 조합 + 과학 분석
- **출력**: `고찰/output/07-문화복원.md`
- **특징**: 취락 구조, 생계 경제, 사회 조직 복원

### gochal-08-summary (요약)
- **트리거**: "요약", "초록", "summary", "abstract"
- **입력**: 전체 보고서 내용
- **출력**: `고찰/output/08-요약.md`
- **특징**: 한글 요약 + 영문 abstract

---

## Skill 관리 모범 사례

### DO (권장)

✅ **명확한 트리거**: 자연스러운 한국어 + 영어 키워드
✅ **표준 구조**: SKILL.md + assets/ + references/ + scripts/
✅ **용어 일관성**: references/terminology.md에 표준 용어 정의
✅ **예시 제공**: references/examples.md에 실제 출력 예시
✅ **버전 관리**: Git으로 변경 이력 관리
✅ **문서화**: SKILL.md에 상세한 Instructions 작성

### DON'T (피해야 할 사항)

❌ **모호한 트리거**: "분석" (너무 광범위)
❌ **복잡한 구조**: 5단계 이상 중첩된 디렉토리
❌ **하드코딩**: 스크립트에 파일 경로 하드코딩
❌ **한글 파일명**: `유구분석.md` → `yugu-analysis.md` (영문 권장)
❌ **거대한 SKILL.md**: 1000줄 이상 (분할 권장)

---

## 데이터 파이프라인

### 표준 데이터 흐름

```
입력 (Excel/CSV/JSON/Markdown)
    ↓
scripts/data_processor.py (Python)
    ↓
표준 JSON 데이터
    ↓
SKILL.md Instructions
    ↓
assets/template.md 적용
    ↓
고찰/output/XX-출력.md
```

### 데이터 스키마 예시

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "유구 데이터 스키마",
  "type": "object",
  "properties": {
    "유구목록": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "유구번호": {"type": "string"},
          "유구유형": {"type": "string"},
          "평면형태": {"type": "string"},
          "규모": {
            "type": "object",
            "properties": {
              "장축": {"type": "number"},
              "단축": {"type": "number"}
            }
          }
        },
        "required": ["유구번호", "유구유형"]
      }
    }
  }
}
```

---

## settings.local.json 설정

`.claude/settings.local.json`은 Claude Code의 프로젝트별 설정 파일입니다.

### 주요 설정 항목

```json
{
  "skills": {
    "autoDiscovery": true,
    "path": ".claude/skills"
  },
  "memory": {
    "enabled": true,
    "path": ".claude/CLAUDE.md"
  },
  "git": {
    "autoCommit": false,
    "useMCP": true
  }
}
```

---

## 문제 해결

### Q1: Skill이 인식되지 않아요
**A**: SKILL.md 파일 확인
- `.claude/skills/skill-name/SKILL.md` 경로 정확한지 확인
- SKILL.md 내 트리거 키워드 명확히 정의

### Q2: 출력 파일이 생성되지 않아요
**A**: Instructions 점검
- SKILL.md의 Instructions에 파일 경로 명시
- 출력 디렉토리 존재 여부 확인

### Q3: 데이터 변환 스크립트 오류
**A**: 스크립트 디버깅
```bash
# Python 스크립트 직접 실행
cd .claude/skills/skill-name/scripts
python data_processor.py
```

### Q4: Skill 충돌 (여러 Skill이 동시 호출)
**A**: 트리거 명확히 구분
- 각 Skill의 트리거를 더 구체적으로 정의
- 트리거 우선순위 설정

---

## 참고 자료

### 공식 문서
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills.md)
- [SKILL.md Specification](https://docs.claude.com/en/docs/claude-code/skill-md-spec.md)

### 프로젝트 문서
- `../CLAUDE.md` - 프로젝트 전체 가이드
- `../고찰/CLAUDE.md` - Skills 사용 가이드 (사용자용)
- `skills/README.md` - Skills 목록 및 개요

### 예제 Skills
- `skills/pdf-management/` - PDF 관리 Skill 참조
- `skills/gochal-02-yugu-analysis/` - 완전한 Skill 구조 예시

---

**마지막 업데이트**: 2025-10-31  
**Skills 개발 프레임워크**: Claude Code v1.0
