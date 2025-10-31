---
name: gochal-08-summary
description: 한국 고고학 발굴조사보고서의 요약 및 초록 작성. 조사 내용, 주요 성과, 학술적 의의를 간결하게 요약하여 보고서 초록 또는 요약문을 생성. 한글 및 영문 초록 작성 지원. 사용자가 "요약 작성", "초록 작성", "abstract 작성"을 요청할 때 사용.
---

# 요약 및 초록 작성 Skill

## 목적

발굴조사 보고서의 전체 내용을 간결하게 요약하여 한글 초록 및 영문 abstract를 작성한다. 조사 배경, 주요 성과, 학술적 의의를 명확하게 전달한다.

## 사용 시점

다음과 같은 요청이 있을 때 이 skill을 사용한다:

- "요약 작성해줘"
- "초록 작성해줘"
- "영문 abstract 작성해줘"
- "보고서 요약문 작성해줘"

## 입력 데이터

- 조사 개요 (유적명, 위치, 기간)
- 주요 조사 성과 (유구, 유물)
- 시기 및 성격
- 학술적 의의

## 출력 형식

### 한글 초록
```markdown
## 요약

{유적명}은(는) {지역}에 위치하며, {조사기간}에 걸쳐 발굴조사가 실시되었다.

조사 결과 {시대} {유구종류} {개수}기, {유물종류} 등이 확인되었다. 
{주요특징_1}, {주요특징_2}의 특징을 보인다.

{편년결과}로, {시기}에 해당한다. 본 유적은 {학술적_의의}를 지닌다.

**주제어**: {키워드1}, {키워드2}, {키워드3}
```

### 영문 Abstract
```markdown
## Abstract

The {site name} is located in {region}, and excavation was conducted 
from {period}.

The excavation revealed {number} {feature type} from the {period}, 
along with {artifact types}. The features show characteristics of 
{feature1} and {feature2}.

Based on radiocarbon dating and typological analysis, the site dates 
to {period}. This site is significant for {scholarly significance}.

**Keywords**: {keyword1}, {keyword2}, {keyword3}
```

## 작성 요령

### 분량
- 한글 초록: 200-300자 (공백 포함)
- 영문 Abstract: 150-200 words

### 구성
1. 조사 배경 (1-2문장)
2. 주요 성과 (2-3문장)
3. 학술적 의의 (1-2문장)
4. 주제어 (3-5개)

### 문체
- 간결하고 명료한 문장
- 핵심 정보 위주
- 전문 용어 사용
