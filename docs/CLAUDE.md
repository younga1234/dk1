# docs/CLAUDE.md

이 파일은 **문서 작성 스타일 가이드**입니다.

## 개요

`docs/` 디렉토리는 프로젝트 관련 문서를 관리하는 공간입니다. 이 가이드는 일관된 문서 작성 스타일을 유지하기 위한 규칙과 권장 사항을 제공합니다.

## 디렉토리 구조

```
docs/
├── CLAUDE.md                        # 이 파일 (문서 작성 가이드)
├── context-management-guide.md      # Context 관리 실전 가이드
└── (향후 추가될 문서들)
```

---

## Markdown 컨벤션

### 1. 제목 (Headings)

```markdown
# H1: 문서 제목 (파일당 1개만)

## H2: 주요 섹션

### H3: 하위 섹션

#### H4: 세부 항목
```

**규칙:**
- H1은 문서 최상단에 1개만
- H2 이하부터 목차 구조 형성
- H5, H6는 가급적 사용 금지 (너무 깊은 중첩 방지)

### 2. 코드 블록

**인라인 코드:**
```markdown
`변수명`, `함수()`, `파일.md`
```

**코드 블록:**
````markdown
```python
def example():
    print("Hello")
```

```bash
git commit -m "message"
```
````

**규칙:**
- 언어 지정자 필수 (python, bash, json, markdown 등)
- 긴 코드는 30줄 이내로 분할

### 3. 리스트

**순서 없는 리스트:**
```markdown
- 항목 1
- 항목 2
  - 하위 항목 2.1
  - 하위 항목 2.2
- 항목 3
```

**순서 있는 리스트:**
```markdown
1. 첫 번째 단계
2. 두 번째 단계
3. 세 번째 단계
```

**규칙:**
- 들여쓰기는 공백 2칸
- 리스트 항목 간 빈 줄 없음
- 복잡한 항목은 각 항목 사이에 빈 줄 추가

### 4. 표 (Tables)

```markdown
| 열1 | 열2 | 열3 |
|-----|-----|-----|
| 값1 | 값2 | 값3 |
| 값4 | 값5 | 값6 |
```

**규칙:**
- 헤더 행 필수
- 정렬: 왼쪽 정렬 기본
- 복잡한 데이터는 CSV/Excel 사용

### 5. 링크 및 이미지

**내부 링크:**
```markdown
[Context 관리 가이드](./context-management-guide.md)
[루트 README](../README.md)
```

**외부 링크:**
```markdown
[Claude Code 공식 문서](https://docs.claude.com/en/docs/claude-code/)
```

**이미지:**
```markdown
![대체 텍스트](./images/screenshot.png)
```

**규칙:**
- 상대 경로 사용 권장
- 링크 텍스트는 명확하게 (~~"여기"~~, ✅"Context 관리 가이드")
- 이미지는 `docs/images/` 디렉토리에 저장

### 6. 인용 및 강조

**인용:**
```markdown
> 이것은 인용문입니다.
> 여러 줄에 걸쳐 작성할 수 있습니다.
```

**강조:**
```markdown
*이탤릭* 또는 _이탤릭_
**굵게** 또는 __굵게__
***굵은 이탤릭*** 또는 ___굵은 이탤릭___
```

**규칙:**
- 인용은 외부 자료 참조 시 사용
- 강조는 최소한으로 (너무 많으면 효과 감소)

### 7. 수평선

```markdown
---
```

**규칙:**
- 주요 섹션 구분 시 사용
- 3개의 하이픈 (`---`)

---

## 문서 작성 스타일

### 1. 어조 및 문체

**DO (권장):**
- ✅ 명확하고 간결한 문장
- ✅ 능동태 우선
- ✅ 기술 문서는 3인칭 또는 명령형
- ✅ 전문 용어는 처음 등장 시 설명

**DON'T (피해야 할 사항):**
- ❌ 모호한 표현 ("아마도", "대충")
- ❌ 수동태 남발
- ❌ 구어체 및 줄임말
- ❌ 불필요한 수식어

### 2. 한글 작문 규칙

**띄어쓰기:**
```
✅ 발굴 조사 보고서
❌ 발굴조사보고서 (맥락에 따라 붙여쓰기도 가능)
```

**외래어 표기:**
```
✅ 커밋, 푸시, 레포지토리
❌ commit, push, repository (코드 제외)
```

**괄호 사용:**
```
✅ PDF 파일 관리 (Portable Document Format)
✅ AMS 연대측정 (Accelerator Mass Spectrometry)
```

### 3. 구조화

**문서 구조:**
1. **제목** (H1)
2. **개요** (H2)
3. **목차** (선택, 긴 문서)
4. **본문** (H2, H3, H4)
5. **참고 자료** (H2, 문서 하단)
6. **메타데이터** (마지막 업데이트 날짜 등)

**예시:**
```markdown
# 문서 제목

간단한 소개 (1-2 문단)

## 목차 (선택)

- [섹션 1](#섹션-1)
- [섹션 2](#섹션-2)

## 섹션 1

내용...

## 섹션 2

내용...

## 참고 자료

- [링크1](URL)
- [링크2](URL)

---

**마지막 업데이트**: 2025-10-31
```

---

## 문서 유형별 가이드

### 1. 가이드 문서 (Tutorial)

**목적**: 초보자가 따라할 수 있는 단계별 안내

**구조:**
```markdown
# 제목: XX 가이드

## 개요
이 가이드에서 배울 내용

## 사전 준비
- 필요한 도구
- 사전 지식

## 단계별 안내

### 1단계: XX 하기
구체적인 지침...

### 2단계: YY 하기
구체적인 지침...

## 문제 해결
자주 발생하는 문제와 해결 방법

## 참고 자료
```

**예시**: `context-management-guide.md`

### 2. 참조 문서 (Reference)

**목적**: 기능, API, 명령어 등의 완전한 설명

**구조:**
```markdown
# 제목: XX 참조 문서

## 개요

## 구문 (Syntax)
```bash
command [options] <arguments>
```

## 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| -a | 설명 | 값 |

## 예시

## 관련 항목
```

### 3. 설명 문서 (Explanation)

**목적**: 개념, 배경, 아키텍처 설명

**구조:**
```markdown
# 제목: XX란?

## 개요

## 배경

## 주요 개념

### 개념 1
설명...

### 개념 2
설명...

## 실제 응용

## 참고 자료
```

### 4. 메모 (Notes)

**목적**: 간단한 메모, 회의록, 작업 일지

**구조:**
```markdown
# 날짜: 2025-10-31

## 주제

## 내용
- 항목 1
- 항목 2

## 다음 단계
- [ ] 할 일 1
- [ ] 할 일 2
```

---

## 파일 명명 규칙

### 1. 파일명 규칙

**일반 원칙:**
```
소문자-하이픈-구분.md
context-management-guide.md ✅
ContextManagementGuide.md ❌
컨텍스트_관리_가이드.md ❌
```

**특수 파일:**
- `README.md` - 대문자 (Git 컨벤션)
- `CLAUDE.md` - 대문자 (Claude Code 컨벤션)
- `CHANGELOG.md` - 대문자
- `LICENSE.md` - 대문자

### 2. 디렉토리 구조

```
docs/
├── guides/              # 가이드 문서
│   ├── getting-started.md
│   └── advanced-usage.md
├── reference/           # 참조 문서
│   ├── api-reference.md
│   └── command-reference.md
├── explanations/        # 설명 문서
│   └── architecture.md
├── notes/               # 메모 및 회의록
│   └── 2025-10-31-meeting.md
└── images/              # 이미지 파일
    └── diagram.png
```

---

## Git 커밋 메시지 (문서)

### 문서 관련 커밋 컨벤션

**형식:**
```
docs: <변경 사항 요약>

[선택] 상세 설명
```

**예시:**
```bash
git commit -m "docs: Context 관리 실전 가이드 추가"
git commit -m "docs: README 업데이트 - Skills 섹션 추가"
git commit -m "docs: 오타 수정 - context-management-guide.md"
```

**접두사:**
- `docs:` - 문서 추가/수정
- `fix(docs):` - 문서 오류 수정
- `refactor(docs):` - 문서 구조 개선

---

## 품질 체크리스트

문서 작성 후 다음을 확인하세요:

### 내용
- [ ] 제목이 명확한가?
- [ ] 개요가 1-2 문단으로 요약되었는가?
- [ ] 모든 섹션이 논리적 순서인가?
- [ ] 예시가 충분한가?
- [ ] 외부 링크가 모두 작동하는가?

### 형식
- [ ] Markdown 문법이 올바른가?
- [ ] 코드 블록에 언어 지정자가 있는가?
- [ ] 표가 올바르게 렌더링되는가?
- [ ] 이미지가 표시되는가?

### 스타일
- [ ] 어조가 일관적인가?
- [ ] 띄어쓰기가 올바른가?
- [ ] 전문 용어가 처음 등장 시 설명되었는가?
- [ ] 불필요한 수식어가 없는가?

### 메타데이터
- [ ] 마지막 업데이트 날짜가 있는가?
- [ ] 저자 또는 기여자 정보가 필요한가?

---

## 도구 및 리소스

### Markdown 편집기
- VS Code + Markdown Preview
- Typora
- Obsidian

### Lint 도구
```bash
# markdownlint 설치
npm install -g markdownlint-cli

# 문서 검사
markdownlint docs/**/*.md
```

### 참고 자료
- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Markdown Guide](https://www.markdownguide.org/)
- [한글 맞춤법 검사기](http://speller.cs.pusan.ac.kr/)

---

## 예시 템플릿

### 가이드 문서 템플릿

```markdown
# [주제] 가이드

[1-2 문단 소개]

## 사전 준비

- 항목 1
- 항목 2

## 단계별 안내

### 1단계: [제목]

[설명]

```bash
# 명령어 예시
```

### 2단계: [제목]

[설명]

## 문제 해결

### Q1: [질문]
**A**: [답변]

## 참고 자료

- [링크1](URL)
- [링크2](URL)

---

**마지막 업데이트**: YYYY-MM-DD
```

---

## 관련 문서

### 프로젝트 문서
- `../CLAUDE.md` - 프로젝트 전체 가이드
- `.claude/CLAUDE.md` - Skills 개발 가이드
- `고찰/CLAUDE.md` - 고찰 작성 가이드

### 공식 문서
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

**마지막 업데이트**: 2025-10-31  
**스타일 가이드 버전**: 1.0
