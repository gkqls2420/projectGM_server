# GitHub 연동 Railway 배포 가이드

## 🚀 단계별 배포 과정

### 1단계: Railway 계정 생성 및 로그인

1. [Railway.app](https://railway.app) 접속
2. "Get Started" 클릭
3. GitHub 계정으로 로그인
4. Railway 대시보드로 이동

### 2단계: 새 프로젝트 생성

1. Railway 대시보드에서 **"New Project"** 클릭
2. **"Deploy from GitHub repo"** 선택
3. GitHub 저장소 목록에서 **`gkqls2420/holoduel`** 선택
4. **"Deploy Now"** 클릭

### 3단계: 환경 변수 설정

배포가 시작되면 다음 환경 변수를 설정하세요:

#### 필수 환경 변수
```
SKIP_HOSTING_GAME=false
```

#### 선택적 환경 변수
```
DAYS_BACK=7
LOG_LEVEL=INFO
```

**설정 방법:**
1. 프로젝트 대시보드에서 **"Variables"** 탭 클릭
2. **"New Variable"** 클릭
3. 변수명과 값을 입력
4. **"Add"** 클릭

### 4단계: 배포 확인

1. **"Deployments"** 탭에서 배포 상태 확인
2. 배포가 완료되면 **"View"** 클릭하여 서비스 URL 확인
3. 서비스 URL로 접속하여 정상 작동 확인

### 5단계: 도메인 설정 (선택사항)

1. **"Settings"** 탭에서 **"Domains"** 섹션 확인
2. **"Generate Domain"** 클릭하여 커스텀 도메인 생성
3. 또는 **"Custom Domain"** 추가

## 🔧 배포 후 확인사항

### 1. 헬스체크 확인
```
https://your-railway-url.railway.app/health
```
응답: `{"status": "healthy", "service": "holoduel-server"}`

### 2. 메인 페이지 확인
```
https://your-railway-url.railway.app/
```
게임 패키지가 있는 경우 게임 페이지로 리다이렉트

### 3. WebSocket 연결 확인
```
wss://your-railway-url.railway.app/ws
```

## 📊 모니터링

### 1. 로그 확인
- **"Deployments"** 탭에서 실시간 로그 확인
- **"View Logs"** 클릭하여 상세 로그 확인

### 2. 메트릭 확인
- **"Metrics"** 탭에서 CPU, 메모리, 네트워크 사용량 확인
- **"Usage"** 탭에서 리소스 사용량 확인

## 🚨 문제 해결

### 일반적인 문제들

#### 1. 배포 실패
- **로그 확인**: 배포 로그에서 오류 메시지 확인
- **의존성 문제**: `requirements.txt` 확인
- **포트 문제**: `railway.json` 설정 확인

#### 2. 서비스 시작 실패
- **환경 변수 확인**: 필수 환경 변수 설정 여부 확인
- **포트 바인딩**: `$PORT` 환경 변수 사용 확인
- **Python 버전**: `runtime.txt`에서 Python 3.12 확인

#### 3. 게임 패키지 누락
- 게임 패키지가 없는 경우 서버는 정상 작동하지만 게임 호스팅은 비활성화
- 게임 패키지를 포함하려면 `data/game_package/game.zip` 파일을 추가

### 로그 확인 명령어
```bash
# Railway CLI 사용 시
railway logs --follow
```

## 🔄 자동 배포 설정

### GitHub 연동 후 자동 배포
1. **"Settings"** 탭에서 **"GitHub"** 섹션 확인
2. **"Auto Deploy"** 활성화
3. main 브랜치에 푸시할 때마다 자동 배포

### 배포 브랜치 설정
- 기본: `main` 브랜치
- 변경하려면 **"Settings"** → **"GitHub"** → **"Branch"** 수정

## 💰 비용 관리

### 무료 플랜 제한
- 월 500시간 무료 사용
- 512MB 메모리
- 1GB 디스크 공간

### 사용량 모니터링
- **"Usage"** 탭에서 현재 사용량 확인
- **"Billing"** 탭에서 결제 정보 확인

## 🔐 보안 설정

### 환경 변수 보안
- 민감한 정보는 Railway 환경 변수로 설정
- `.env` 파일을 Git에 커밋하지 않음

### 접근 권한 관리
- **"Settings"** → **"Team"**에서 팀 멤버 권한 설정
- 프로젝트 접근 권한 관리

## 📞 지원

### 문제 발생 시
1. Railway 로그 확인
2. GitHub Issues에 문제 보고
3. Railway Discord 커뮤니티 참여

### 유용한 링크
- [Railway Documentation](https://docs.railway.app/)
- [Railway Discord](https://discord.gg/railway)
- [GitHub Repository](https://github.com/gkqls2420/holoduel) 