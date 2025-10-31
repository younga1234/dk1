# 고고학 발굴조사보고서 고찰 작성 Skill 제작 계획서

**작성일**: 2025-10-31
**프로젝트명**: 고찰 섹션 자동 작성 Skill 시스템
**위치**: `/mnt/a/1030/.claude/skills/`

---

## 1. 프로젝트 개요

### 1.1 목적
한국 고고학 발굴조사보고서의 "고찰" 섹션을 효율적으로 작성하기 위한 AI 지원 시스템 구축

### 1.2 범위
고찰 섹션의 8개 항목 각각에 대한 독립적인 Claude Code Skill 개발

### 1.3 주요 기능
- 다양한 형식의 입력 데이터 지원 (Excel, CSV, Markdown, JSON, PDF)
- 학술 논문 수준의 Markdown 형식 출력
- 고고학 전문 용어 및 작성 규칙 적용
- 실제 보고서 예시 기반 작성

---

## 2. Skill 목록 및 우선순위

| 순번 | Skill명 | 항목명 | 우선순위 | 비고 |
|------|---------|--------|----------|------|
| 1 | `gochal-02-yugu-analysis` | 유구 분석 | ★★★ | 가장 기본적, 1차 개발 |
| 2 | `gochal-03-yumul-analysis` | 유물 분석 | ★★★ | 유구와 함께 핵심 |
| 3 | `gochal-04-pyeonnyeon` | 편년(編年) | ★★★ | 연대 설정 중요 |
| 4 | `gochal-05-site-comparison` | 주변 유적과의 비교 | ★★☆ | 비교 분석 |
| 5 | `gochal-01-conclusion` | 결론 및 종합 분석 | ★★☆ | 다른 항목 종합 |
| 6 | `gochal-06-science-analysis` | 자연과학 분석 종합 | ★☆☆ | 전문 분석 필요 |
| 7 | `gochal-07-culture-restoration` | 문화 양상 및 생활상 복원 | ★☆☆ | 해석적 내용 |
| 8 | `gochal-08-summary` | 요약 및 초록 | ★☆☆ | 전체 요약 |

---

## 3. 각 Skill 디렉토리 구조

```
gochal-XX-name/
├── SKILL.md                      # Skill 메타데이터 및 사용 가이드
│   ├── [YAML frontmatter]        # name, description
│   └── [Markdown body]           # 사용법, 입력/출력 형식
│
├── scripts/                      # 실행 스크립트
│   ├── data_processor.py         # 다중 형식 입력 처리
│   ├── excel_parser.py           # Excel/CSV → JSON
│   ├── markdown_parser.py        # Markdown → JSON
│   └── validator.py              # 입력 데이터 검증
│
├── references/                   # 참고 문서 (필요 시 로드)
│   ├── examples.md               # 실제 보고서 고찰 예시
│   ├── terminology.md            # 고고학 전문 용어 사전
│   ├── structure.md              # 해당 항목 작성 구조
│   └── citation-style.md         # 인용 및 참고문헌 형식
│
└── assets/                       # 출력 템플릿
    ├── template.md               # Markdown 출력 템플릿
    └── example-output.md         # 출력 예시
```

---

## 4. 입력 데이터 형식

### 4.1 표준 JSON 스키마

```json
{
  "site_info": {
    "name": "유적명",
    "region": "지역 (예: 나주, 순천)",
    "period": "시대 (예: 청동기시대, 삼국시대)",
    "excavation_year": "발굴연도",
    "organization": "발굴기관"
  },
  "data": {
    "유구목록": [
      {
        "번호": "주거지1",
        "형태": "방형",
        "크기": "4.5m × 4.2m",
        "구성요소": ["노지", "저장공", "기둥구멍"],
        "출토유물": ["무문토기", "석촉", "석도"]
      }
    ],
    "유물목록": [
      {
        "유구": "주거지1",
        "종류": "무문토기",
        "수량": 15,
        "특징": "구연부 파손"
      }
    ],
    "연대측정": [
      {
        "시료번호": "AMS-001",
        "측정값": "2850±50 BP",
        "보정연대": "BC 1100-950"
      }
    ],
    "주변유적": [
      {
        "유적명": "나주 오량동 유적",
        "거리": "3km",
        "시대": "청동기시대",
        "유사점": "주거지 형태 유사"
      }
    ]
  }
}
```

### 4.2 Excel/CSV 입력 형식

**Sheet 1: 유구목록**
| 번호 | 형태 | 크기 | 구성요소 | 출토유물 |
|------|------|------|----------|----------|
| 주거지1 | 방형 | 4.5×4.2m | 노지,저장공 | 무문토기,석촉 |

**Sheet 2: 유물목록**
| 유구 | 종류 | 수량 | 특징 |
|------|------|------|------|
| 주거지1 | 무문토기 | 15 | 구연부 파손 |

### 4.3 Markdown 입력 형식

```markdown
# 유적 정보
- 유적명: 나주 복암리 3지구
- 시대: 청동기시대
- 발굴연도: 2023

## 유구 목록
### 주거지1
- 형태: 방형
- 크기: 4.5m × 4.2m
- 구성요소: 노지, 저장공, 기둥구멍
```

---

## 5. 출력 형식

### 5.1 Markdown 표준 템플릿

```markdown
## 2. 유구 분석

### 2.1 주거지
조사 결과 총 15기의 주거지가 확인되었다. 주거지는 평면 형태에 따라 방형(10기),
원형(3기), 부정형(2기)으로 분류된다.

**표 1. 주거지 규모 현황**
| 구분 | 개수 | 평균 크기 | 비고 |
|------|------|-----------|------|
| 방형 | 10기 | 4.2×4.0m | 청동기시대 전기 |
| 원형 | 3기 | 직경 3.5m | 청동기시대 중기 |

방형 주거지는 장축 방향이 남북 방향으로 배치되어 있으며, 내부에는 중앙노지와
4개의 기둥구멍이 확인된다...

### 2.2 시간적·공간적 배치
...
```

---

## 6. 개발 단계별 세부 계획

### Phase 1: 환경 설정 및 초기화 (1일차)

**작업 내용**:
1. skill-creator의 `init_skill.py` 스크립트 사용
2. 8개 skill 디렉토리 구조 생성
3. 기본 템플릿 파일 배치

**명령어**:
```bash
cd /mnt/a/1030/.claude/skills
python /path/to/init_skill.py gochal-02-yugu-analysis --path .
python /path/to/init_skill.py gochal-03-yumul-analysis --path .
# ... 8개 반복
```

**예상 결과**:
```
.claude/skills/
├── gochal-01-conclusion/
├── gochal-02-yugu-analysis/
├── gochal-03-yumul-analysis/
├── gochal-04-pyeonnyeon/
├── gochal-05-site-comparison/
├── gochal-06-science-analysis/
├── gochal-07-culture-restoration/
└── gochal-08-summary/
```

---

### Phase 2: 우선순위 Skill 개발 (2-3일차)

#### gochal-02-yugu-analysis (유구 분석)

**SKILL.md 내용**:
```yaml
---
name: gochal-02-yugu-analysis
description: 한국 고고학 발굴조사보고서의 유구 분석 고찰 작성. 유구 형태, 규모, 특징, 시공간적 관계 분석. 청동기시대 및 삼국시대 유적 특화.
---

# 유구 분석 고찰 작성 Skill

## 목적
발굴된 유구(주거지, 수혈, 구상유구 등)의 형태, 규모, 특징을 종합하고
시간적·공간적 관계를 해석하여 학술적 고찰 작성

## 사용 시점
- "유구 분석 고찰 작성해줘"
- "주거지 형태 분석해줘"
- "유구 배치 양상 분석해줘"

## 입력 데이터
1. Excel/CSV 파일 (유구목록)
2. Markdown 텍스트
3. JSON 데이터
4. PDF에서 추출한 데이터

scripts/data_processor.py를 사용하여 모든 형식을 표준 JSON으로 변환

## 작성 프로세스
1. 입력 데이터 검증 (scripts/validator.py)
2. 유구 유형별 분류 및 통계
3. references/examples.md 참고하여 작성 스타일 학습
4. assets/template.md 기반 Markdown 생성
5. 전문 용어는 references/terminology.md 참조

## 출력
학술 논문 형식의 Markdown 문서
- 유구 유형별 분류
- 규모 및 형태 분석
- 시간적·공간적 배치 해석
- 표 및 목록 포함
```

**scripts/data_processor.py**:
```python
#!/usr/bin/env python3
"""
다중 형식 입력 데이터를 표준 JSON으로 변환
"""
import json
import pandas as pd
from pathlib import Path

def process_excel(filepath):
    """Excel/CSV → JSON"""
    df = pd.read_excel(filepath, sheet_name='유구목록')
    # ... 변환 로직
    return json_data

def process_markdown(text):
    """Markdown → JSON"""
    # ... 파싱 로직
    return json_data

def process_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# ... 나머지 함수
```

**references/examples.md**:
```markdown
# 유구 분석 고찰 작성 예시

## 예시 1: 나주 복암리 3지구 (2015)

### 2. 유구 분석

#### 2.1 주거지
조사 결과 청동기시대 주거지 12기가 확인되었다. 주거지는 평면 형태에 따라
방형 9기, 원형 3기로 구분된다.

방형 주거지는 장축 길이 4.2~5.8m, 단축 길이 3.8~4.5m 규모로,
평균 4.8×4.1m의 크기이다...

[출처: 나주 복암리유적 III (2015), p.245]

---

## 예시 2: 순천 덕암동 유적 (2018)
...
```

---

### Phase 3: 나머지 Skill 개발 (4-5일차)

동일한 구조로 나머지 7개 skill 개발:
- gochal-03-yumul-analysis
- gochal-04-pyeonnyeon
- gochal-05-site-comparison
- gochal-01-conclusion
- gochal-06-science-analysis
- gochal-07-culture-restoration
- gochal-08-summary

---

### Phase 4: 공통 자료 준비 (6일차)

#### 고고학 전문 용어 사전 (references/terminology.md)

```markdown
# 고고학 전문 용어

## 유구 관련
- **주거지**: 집터. 사람이 거주했던 흔적이 남아있는 유구
- **수혈**: 땅을 파서 만든 구덩이
- **노지**: 불을 때던 자리
- **저장공**: 곡물 등을 보관하던 구덩이
- **기둥구멍**: 기둥을 세웠던 자리

## 유물 관련
- **무문토기**: 문양이 없는 토기. 청동기시대 대표 유물
- **석촉**: 돌로 만든 화살촉
- **석도**: 돌로 만든 칼
- **방추차**: 실을 자을 때 사용하는 도구

## 편년 관련
- **AMS 연대**: 가속질량분석법을 이용한 방사성탄소연대측정
- **BP**: Before Present. 1950년 기준 과거 연대
- **cal BC**: 보정연대. 실제 달력 연대

## 시대 구분
- **청동기시대 전기**: BC 1500-1000
- **청동기시대 중기**: BC 1000-700
- **청동기시대 후기**: BC 700-400
```

---

### Phase 5: 테스트 및 검증 (7일차)

**테스트 데이터 준비**:
```
/mnt/a/1030/고찰/test-data/
├── sample-yugu.xlsx
├── sample-yumul.json
└── sample-site-info.md
```

**검증 항목**:
1. 각 skill의 YAML frontmatter 검증
2. 입력 데이터 형식 처리 테스트
3. 출력 Markdown 품질 확인
4. 전문 용어 사용 적절성 검토

**패키징**:
```bash
cd /mnt/a/1030/.claude/skills
python /path/to/package_skill.py gochal-02-yugu-analysis
# ... 8개 반복
```

---

### Phase 6: 문서화 및 배포 (8일차)

**메인 README 작성**:
```markdown
# 고고학 발굴조사보고서 고찰 작성 Skill

## 설치
각 skill을 `.claude/skills/` 디렉토리에 압축 해제

## 사용법
### 유구 분석 고찰 작성
1. 유구 데이터 준비 (Excel, CSV, JSON, Markdown)
2. Claude에게 "유구 분석 고찰 작성해줘" 요청
3. 데이터 파일 경로 제공
4. 생성된 Markdown 파일 확인

## Skill 목록
- gochal-02-yugu-analysis: 유구 분석
- gochal-03-yumul-analysis: 유물 분석
...
```

---

## 7. 예상 사용 시나리오

### 시나리오 1: 유구 분석 고찰 작성

**사용자 입력**:
```
"나주 복암리 유적의 유구 분석 고찰 작성해줘"
```

**Claude 동작**:
1. `gochal-02-yugu-analysis` skill 자동 트리거
2. "유구 데이터 파일을 제공해주세요 (Excel, CSV, JSON, Markdown)" 요청
3. 사용자가 `/mnt/a/1030/data/naju-bokam-yugu.xlsx` 제공
4. `scripts/data_processor.py`로 Excel → JSON 변환
5. `references/examples.md` 참고하여 작성 스타일 학습
6. `assets/template.md` 기반 Markdown 생성
7. `/mnt/a/1030/고찰/output/naju-bokam-yugu-analysis.md` 저장

**출력 파일 (일부)**:
```markdown
## 2. 유구 분석

### 2.1 주거지

나주 복암리 3지구에서는 청동기시대 주거지 총 12기가 조사되었다.
주거지는 평면 형태에 따라 방형 9기, 원형 3기로 구분되며...

**표 1. 주거지 형태별 현황**
| 형태 | 개수 | 평균 크기 | 비율 |
|------|------|-----------|------|
| 방형 | 9기 | 4.8×4.1m | 75% |
| 원형 | 3기 | 직경 3.5m | 25% |

방형 주거지는 장축 방향이 대체로 남북 방향(N-10°-E ~ N-20°-E)으로
배치되어 있으며, 이는 당시 일조량과 통풍을 고려한 것으로 판단된다...
```

---

### 시나리오 2: 편년 고찰 작성

**사용자 입력**:
```
"순천 덕암동 유적 편년 고찰 작성해줘. AMS 연대측정 결과도 포함해서."
```

**Claude 동작**:
1. `gochal-04-pyeonnyeon` skill 트리거
2. 연대측정 데이터 요청
3. JSON 데이터 입력 받음
4. `references/terminology.md`에서 연대 관련 용어 확인
5. Markdown 생성

---

## 8. 성공 기준 (Acceptance Criteria)

### 필수 요구사항
- [ ] 8개 skill 모두 독립적으로 작동
- [ ] 4가지 입력 형식 모두 지원 (Excel, Markdown, JSON, PDF)
- [ ] Markdown 출력 품질 (학술 논문 수준)
- [ ] `package_skill.py` 검증 통과
- [ ] 각 skill의 SKILL.md 완성도 (메타데이터 + 사용법)

### 품질 기준
- [ ] 고고학 전문 용어 정확성
- [ ] 실제 보고서와 유사한 작성 스타일
- [ ] 표, 목록, 인용 형식 일관성
- [ ] 한국어 학술 문장 자연스러움

### 성능 기준
- [ ] 입력 데이터 처리 속도 (1초 이내)
- [ ] Markdown 생성 속도 (5초 이내)
- [ ] 오류 처리 및 검증

---

## 9. 리스크 및 대응 방안

| 리스크 | 영향도 | 대응 방안 |
|--------|--------|-----------|
| PDF 텍스트 추출 품질 저하 | 중 | 수동 데이터 입력 옵션 제공 |
| 전문 용어 부정확 | 높음 | references/terminology.md 지속 업데이트 |
| 학술 작성 스타일 불일치 | 중 | 실제 보고서 예시 추가 수집 |
| 입력 데이터 형식 다양성 | 중 | 표준 JSON 스키마 강제 |

---

## 10. 향후 확장 계획

### 10.1 단기 (1개월 이내)
- 모든 8개 skill 완성 및 테스트
- 실제 보고서 예시 10개 이상 수집
- 사용자 피드백 수집

### 10.2 중기 (3개월 이내)
- Word 문서 (.docx) 출력 지원
- 도표 및 그래프 자동 생성
- 참고문헌 자동 정리 기능

### 10.3 장기 (6개월 이내)
- PDF 직접 출력
- 전남 지역 외 다른 지역 보고서 지원 확대
- 다른 시대(구석기, 신석기) 지원

---

## 11. 부록

### A. 참고 자료
- 문화재청 발굴조사보고서 작성 지침 (2019)
- 한국고고학회 학술 논문 작성법
- 전남 지역 청동기/삼국시대 보고서 150건

### B. 관련 문서
- `/mnt/a/1030/고찰/고찰.md` - 고찰 항목 정의
- `/mnt/a/1030/CLAUDE.md` - 프로젝트 전체 가이드
- `/mnt/a/1030/.claude/skills/pdf-management/` - 기존 PDF 관리 skill

### C. 연락처 및 지원
- GitHub Issues: 문제 보고 및 기능 요청
- 문서 업데이트: 지속적인 개선

---

**승인**: _________________
**작성자**: Claude Code
**검토일**: 2025-10-31
