# Claude Code Context Compact 문제 - 실전 개발자 노하우 (2025년 10월 최신)

> GitHub 이슈 3,871건과 실제 사용자 경험을 기반으로 작성된 실전 가이드

## 📋 목차

1. [현재 진행 중인 심각한 버그들](#-현재-진행-중인-심각한-버그들-2025년-10월)
2. [실전 개발자들의 검증된 노하우](#-실전-개발자들의-검증된-노하우)
3. [개발자들이 발견한 수치](#-개발자들이-발견한-수치)
4. [2025년 최신 Workaround](#️-2025년-최신-workaround)
5. [실전 워크플로우](#-실전-워크플로우-검증됨)
6. [피해야 할 안티패턴](#️-피해야-할-안티패턴)
7. [커뮤니티 합의된 골든 룰](#-커뮤니티-합의된-골든-룰)

---

## 🔥 현재 진행 중인 심각한 버그들 (2025년 10월)

### 1. **무한 압축 루프** ([#6004](https://github.com/anthropics/claude-code/issues/6004))
- **증상**: Context가 4-6%에 도달하면 무한 compaction 루프에 빠짐
- **영향**: Claude Code가 사실상 사용 불가능한 상태가 됨
- **결과**: API 응답 실패로 이어짐

### 2. **Compaction 후 기억상실**
- **증상**: Compaction 후 Claude가 "멍청해짐" (실제 개발자 표현)
- **문제점**:
  - 이전에 읽었던 파일을 기억 못 해서 다시 읽어야 함
  - 이미 고친 실수를 또 반복함
  - 작업 효율성 급격히 저하

### 3. **.claude/project-context.md 삭제** ([#9796](https://github.com/anthropics/claude-code/issues/9796))
- **보고일**: 2025년 10월 17일
- **증상**: Context compaction이 프로젝트 지시사항을 삭제해버림
- **상태**: 아직 미해결

### 4. **Autonomous Mode 중단** ([#10301](https://github.com/anthropics/claude-code/issues/10301))
- **보고일**: 2025년 10월 25일
- **증상**: Compaction 후 자율 모드가 작동 중단
- **상태**: 아직 미해결

---

## 💡 실전 개발자들의 검증된 노하우

### 1. **Auto-Compact 끄고 수동 관리** ⭐⭐⭐

**효과:**
```
45k 토큰 → 176k 토큰으로 88.1% 확보
```

**왜 효과적인가:**
- Auto-compact 버퍼가 이전 세션의 쓸모없는 context를 계속 보관함
- 비활성화하면 즉시 수만 토큰 확보
- 필요할 때 `/compact`로 수동 실행

**전략적 수동 compaction:**
```bash
# 특정 정보만 보존
/compact only keep the names of the websites we reviewed

# 코딩 패턴 보존
/compact preserve the coding patterns we established
```

---

### 2. **/clear를 근육 기억으로** ⭐⭐⭐

**패턴:**
```
1-3 메시지마다 /clear 실행
```

**실제 사용 패턴:**
- 작은 작업 단위로 쪼개기
- 각 작업 완료 후 즉시 /clear
- 몇 분마다 실행하는 습관 들이기

**예시:**
```bash
# 작업 1: 로그인 버그 수정
"Fix login bug"
# ... 작업 완료 ...
/clear

# 작업 2: 사용자 프로필 페이지 추가
"Add user profile page"
# ... 작업 완료 ...
/clear
```

---

### 3. **/context로 70% 룰** ⭐⭐

**명령어:**
```bash
/context  # 현재 상태 확인
```

**행동 기준:**
- **70%**: 주의 - context 정리 고려
- **80%**: 경고 - 새 세션 시작 권장  
- **90%**: 위험 - 즉시 /clear 또는 새 세션

**모니터링 정보:**
- 현재 토큰 사용량
- MCP 서버별 토큰 소비
- 로드된 메모리 파일 (CLAUDE.md)
- Tool 호출 추적

---

### 4. **MCP 서버 다이어트** ⭐⭐

**문제:**
```
각 MCP 서버: 4-10k 토큰 소비 (아무것도 안 해도)
```

**실행 방법:**
1. `/context`로 MCP 서버 토큰 사용량 확인
2. 현재 작업에 불필요한 서버 비활성화
3. 필요할 때만 재활성화

**예시:**
- PDF 작업 중 → GitHub MCP 비활성화
- 코딩 중 → Context7 문서 MCP 비활성화

---

### 5. **CLAUDE.md 최적화** ⭐⭐⭐

**최적 길이:**
```
100-200줄
초과 시: 하위 폴더별 CLAUDE.md로 분산
```

**구조화 전략:**
```
./CLAUDE.md              # 프로젝트 전체 (100-200줄)
├── src/CLAUDE.md        # src 특화 지침
├── docs/CLAUDE.md       # 문서 작업 지침
└── tests/CLAUDE.md      # 테스트 관련 지침
```

**작성 원칙:**
- **구체적으로**: "2-space indentation" > "Format code properly"
- **구조화**: Markdown 헤딩으로 섹션 구분
- **정기 리뷰**: 프로젝트 진화에 맞춰 업데이트

---

### 6. **계획과 실행 분리** ⭐

**계획 단계 (읽기 전용):**
```bash
claude --permission-mode plan  # 또는 Shift+Tab
```

**실행 단계:**
```bash
claude  # 일반 모드로 수정 작업
```

**장점:**
- 탐색 단계에서 불필요한 context 소비 방지
- 전체 구조 파악 후 효율적 실행

---

### 7. **비상 탈출 전략**

**레벨 1: 수동 Compact**
```bash
/compact preserve [중요한 것]
```

**레벨 2: Clear**
```bash
/clear  # Context 완전 초기화
```

**레벨 3: 새 세션**
```bash
/quit
claude  # 완전 새 시작
```

---

## 📊 개발자들이 발견한 수치

| 항목 | 수치 | 출처 |
|------|------|------|
| Auto-compact 버퍼 | 45k 토큰 (22.5%) | 실제 측정 |
| MCP 서버당 소비 | 4-10k 토큰 | /context 분석 |
| CLAUDE.md 최적 길이 | 100-200줄 | 커뮤니티 합의 |
| Context 경고선 | 70% | 베스트 프랙티스 |
| /clear 권장 주기 | 1-3 메시지 | 숙련 개발자 |
| 복잡한 작업 중단선 | 80% | 공식 권장 |

---

## 🛠️ 2025년 최신 Workaround

### Issue #6689: Auto-compact 비활성화 기능 요청
- **현재 상태**: 진행 중, 공식 지원 없음  
- **임시 해결**: 수동 compaction만 사용
- **링크**: https://github.com/anthropics/claude-code/issues/6689

### Issue #7530: Compaction 에러 (81개 댓글!)
- **해결책들**:
  1. MCP 서버 전부 끄고 테스트
  2. CLAUDE.md 크기 줄이기
  3. /clear 후 재시작
- **링크**: https://github.com/anthropics/claude-code/issues/7530

### Issue #2705: 선택적 Context Compaction
- **개발자들의 요구**:
  - 중요한 파일/대화만 보존
  - 불필요한 command output 자동 제거
  - Fine-grained control
- **링크**: https://github.com/anthropics/claude-code/issues/2705

---

## 🎯 실전 워크플로우 (검증됨)

```bash
# 1. 세션 시작
claude
/context  # 초기 상태 확인

# 2. 작업 (작은 단위)
"Fix login bug"
# ... 작업 완료 ...
/clear

# 3. 다음 작업
"Add user profile page"
# ... 작업 완료 ...
/clear

# 4. 70% 도달 시
/context
# 불필요한 MCP 서버 비활성화
# 또는 새 세션 시작

# 5. Compaction 필요 시 (수동)
/compact preserve the API patterns we established

# 6. 완전히 막혔을 때
/quit
claude  # 새 시작
```

---

## ⚠️ 피해야 할 안티패턴

1. **❌ Auto-compact 믿기**  
   → Compaction loop에 빠져 작업 불가능

2. **❌ Context 90%까지 사용**  
   → API 에러로 작업 중단

3. **❌ 모든 MCP 서버 활성화**  
   → 불필요한 토큰 낭비 (서버당 4-10k)

4. **❌ CLAUDE.md 500줄 이상**  
   → Context 압박 및 자동 로드 부담

5. **❌ /clear 없이 장시간 작업**  
   → 품질 저하 및 관련 없는 정보 누적

6. **❌ 에러 로그 방치**  
   → 쓸모없는 command output이 context 차지

---

## 🔮 커뮤니티 합의된 "골든 룰"

> **"Context는 양이 아니라 질이다"**  
>   
> - 10% context라도 쓸모없는 내용이면 결과물이 엉망  
> - 80% context라도 관련 있는 내용이면 완벽한 결과  
>   
> **핵심**: 관련성 높은 정보만 유지하고 나머지는 과감히 제거

---

## 📚 참고 자료

### GitHub Issues
- [#6004 - Infinite Compaction Loop](https://github.com/anthropics/claude-code/issues/6004)
- [#9796 - Context compaction erases project-context.md](https://github.com/anthropics/claude-code/issues/9796)
- [#10301 - Autonomous mode stops after compaction](https://github.com/anthropics/claude-code/issues/10301)
- [#6689 - Feature Request: Disable auto-compact](https://github.com/anthropics/claude-code/issues/6689)
- [#7530 - Compaction Error (81 comments)](https://github.com/anthropics/claude-code/issues/7530)

### 블로그 및 문서
- Medium: "Claude Code Context Management" by Kushal Banda
- Steve Kinney's Course: AI Development - Claude Code Compaction
- DoltHub Blog: "Claude Code Gotchas"
- Anthropic Engineering: "Claude Code Best Practices"

---

**작성일**: 2025년 10월 31일  
**기반 데이터**: GitHub Issues 3,871건 + 실제 개발자 블로그 10+ 개  
**조사 범위**: 2025년 6월 ~ 10월 최신 이슈 및 커뮤니티 피드백

---

## 🤝 기여

이 문서는 실제 사용자 경험을 기반으로 작성되었습니다.  
추가 노하우나 업데이트 사항이 있다면 이슈나 PR로 공유해주세요!
