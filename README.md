# DK1 Project

이 저장소는 고고학 발굴 보고서 PDF 파일들을 관리하는 프로젝트입니다.

## 프로젝트 구조

```
.
├── pdf/          # PDF 파일들 (Git에서 제외됨)
├── data/         # 데이터 폴더 (Git에서 제외됨)
└── README.md     # 프로젝트 설명
```

## 주의사항

- `pdf/` 폴더와 `data/` 폴더는 .gitignore에 의해 Git 추적에서 제외됩니다.
- 대용량 파일은 로컬에서만 관리됩니다.

## GitHub Actions

이 저장소는 GitHub Actions를 사용하여 자동화된 워크플로우를 실행합니다.
