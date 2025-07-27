# Railway 배포 가이드

## 개요
HoloDuel 서버를 Railway에 배포하는 방법을 설명합니다.

## 사전 준비

### 1. Railway CLI 설치
```bash
npm install -g @railway/cli
```

### 2. Railway 계정 생성 및 로그인
```bash
railway login
```

## 배포 방법

### 방법 1: 자동 배포 스크립트 사용 (Windows)
```bash
deploy_to_railway.bat
```

### 방법 2: 수동 배포
```bash
# 1. 프로젝트 초기화
railway init

# 2. 배포
railway up
```

### 방법 3: GitHub 연동
1. Railway 대시보드에서 "New Project" 클릭
2. "Deploy from GitHub repo" 선택
3. GitHub 저장소 연결
4. 자동 배포 설정

## 환경 변수 설정

Railway 대시보드에서 다음 환경 변수를 설정하세요:

### 필수 변수
- `SKIP_HOSTING_GAME`: `false` (게임 호스팅 활성화)

### 선택적 변수
- `DAYS_BACK`: `7` (매치 로그 조회 일수)
- `LOG_LEVEL`: `INFO` (로그 레벨)

## 배포 후 확인

### 1. 배포 상태 확인
```bash
railway status
```

### 2. 로그 확인
```bash
railway logs
```

### 3. 서비스 URL 확인
```bash
railway domain
```

## 문제 해결

### 일반적인 문제들

#### 1. 포트 바인딩 오류
- Railway는 `$PORT` 환경 변수를 자동으로 제공합니다
- `railway.json`에서 올바른 포트 설정 확인

#### 2. 의존성 설치 실패
- `requirements.txt`에 모든 의존성이 포함되어 있는지 확인
- Python 3.12 버전 사용 확인

#### 3. 게임 패키지 누락
- 게임 패키지가 없는 경우 서버는 정상 작동하지만 게임 호스팅은 비활성화됩니다
- 게임 패키지를 포함하려면 `data/game_package/game.zip` 파일을 추가하세요

### 로그 확인
```bash
# 실시간 로그 확인
railway logs --follow

# 특정 서비스 로그 확인
railway logs --service web
```

## 성능 최적화

### 1. 메모리 사용량
- Railway의 무료 플랜은 512MB 메모리 제한
- 매치 로그 파일이 많아지면 주기적으로 정리 필요

### 2. 디스크 공간
- `data/` 디렉토리의 파일들이 디스크 공간을 차지
- 주기적으로 오래된 매치 로그 정리 권장

## 모니터링

### 1. Railway 대시보드
- CPU, 메모리, 네트워크 사용량 모니터링
- 로그 실시간 확인

### 2. 헬스체크
- `/` 엔드포인트로 자동 헬스체크
- 서비스 상태 모니터링

## 백업 및 복구

### 1. 매치 로그 백업
```bash
# 로컬에서 매치 로그 다운로드
python download_match_logs.py
```

### 2. 환경 변수 백업
- Railway 대시보드에서 환경 변수 내보내기
- 설정 파일로 저장

## 보안 고려사항

### 1. 환경 변수
- 민감한 정보는 Railway 환경 변수로 설정
- `.env` 파일을 Git에 커밋하지 않음

### 2. 접근 제어
- Railway 프로젝트 접근 권한 관리
- 팀 멤버 권한 설정

## 비용 최적화

### 1. 무료 플랜 활용
- 월 500시간 무료 사용
- 개발/테스트 환경으로 활용

### 2. 프로덕션 환경
- 유료 플랜으로 업그레이드
- 더 많은 리소스와 기능 사용 가능 