# 🌐 HoloDuel 온라인 서버 배포 가이드

홀로라이브OCG 서버를 온라인에 배포하여 다른 플레이어들과 테스트할 수 있습니다.

## 🚀 추천 배포 방법

### **1. Railway (가장 간단) - 무료**

#### **단계별 배포 과정:**

1. **GitHub에 코드 업로드**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/holoduel-server.git
   git push -u origin main
   ```

2. **Railway 계정 생성**
   - https://railway.app 에서 GitHub 계정으로 로그인

3. **프로젝트 배포**
   - "New Project" 클릭
   - "Deploy from GitHub repo" 선택
   - GitHub 저장소 선택
   - 자동으로 배포 시작

4. **환경 변수 설정**
   - Railway 대시보드에서 "Variables" 탭
   - `SKIP_HOSTING_GAME` = `true` 추가

5. **도메인 확인**
   - 배포 완료 후 제공되는 URL 확인
   - 예: `https://holoduel-server-production.up.railway.app`

### **2. Render - 무료**

#### **배포 과정:**

1. **GitHub에 코드 업로드** (위와 동일)

2. **Render 계정 생성**
   - https://render.com 에서 GitHub 계정으로 로그인

3. **새 Web Service 생성**
   - "New +" → "Web Service"
   - GitHub 저장소 연결
   - 설정:
     - **Name**: `holoduel-server`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn server:app --host 0.0.0.0 --port $PORT`

4. **환경 변수 설정**
   - `SKIP_HOSTING_GAME` = `true`

5. **배포 완료**
   - 제공되는 URL 확인

### **3. Heroku - 무료 티어 종료됨**

#### **배포 과정:**

1. **Heroku CLI 설치**
   ```bash
   # Windows
   winget install --id=Heroku.HerokuCLI
   ```

2. **Heroku 로그인**
   ```bash
   heroku login
   ```

3. **앱 생성 및 배포**
   ```bash
   heroku create holoduel-server
   git push heroku main
   ```

4. **환경 변수 설정**
   ```bash
   heroku config:set SKIP_HOSTING_GAME=true
   ```

## 🔧 클라이언트 설정

### **온라인 서버 연결 설정:**

1. **`online_server_settings.gd` 파일 수정**
   ```gdscript
   const ONLINE_SERVER_URL = "wss://your-server-url.railway.app/ws"
   ```

2. **클라이언트에서 온라인 서버 사용**
   - `global_settings.gd`에서 `UseAzureServerAlways = true` 설정
   - 또는 온라인 서버 URL로 직접 연결

## 📋 배포 체크리스트

### **배포 전 확인사항:**
- [ ] `requirements.txt` 파일이 최신 상태
- [ ] `SKIP_HOSTING_GAME=true` 환경 변수 설정
- [ ] 서버 코드에서 포트 설정이 `$PORT` 사용
- [ ] WebSocket 엔드포인트 `/ws` 정상 작동

### **배포 후 확인사항:**
- [ ] 서버 URL 접속 가능 (`/` 엔드포인트)
- [ ] 헬스체크 엔드포인트 정상 (`/health`)
- [ ] WebSocket 연결 테스트
- [ ] 클라이언트에서 연결 테스트

## 🧪 테스트 방법

### **1. 서버 상태 확인**
```bash
curl https://your-server-url.railway.app/health
```

### **2. WebSocket 연결 테스트**
- 브라우저 개발자 도구에서:
```javascript
const ws = new WebSocket('wss://your-server-url.railway.app/ws');
ws.onopen = () => console.log('Connected!');
ws.onmessage = (event) => console.log('Message:', event.data);
```

### **3. 클라이언트 연결 테스트**
- Godot 클라이언트에서 온라인 서버 URL 설정
- 매치메이킹 큐 참여 테스트

## 🔒 보안 고려사항

### **프로덕션 환경에서 고려할 점:**
1. **HTTPS/WSS 사용** (대부분 클라우드 서비스에서 자동 제공)
2. **환경 변수로 민감한 정보 관리**
3. **CORS 설정** (필요시)
4. **Rate Limiting** (필요시)
5. **로깅 및 모니터링**

## 🐛 문제 해결

### **일반적인 문제들:**

1. **포트 충돌**
   - 환경 변수 `PORT` 확인
   - `$PORT` 사용 확인

2. **의존성 문제**
   - `requirements.txt` 업데이트
   - Python 버전 확인

3. **WebSocket 연결 실패**
   - HTTPS/WSS 사용 확인
   - 방화벽 설정 확인

4. **메모리 부족**
   - 무료 티어 제한 확인
   - 유료 플랜 고려

## 📞 지원

문제가 발생하면:
1. 클라우드 서비스 로그 확인
2. 서버 로그 확인
3. 네트워크 연결 테스트
4. 클라이언트 설정 확인

## 🎮 게임 테스트

온라인 서버 배포 후:
1. **단일 플레이어 테스트**: AI와 대전
2. **멀티플레이어 테스트**: 다른 플레이어와 대전
3. **매치메이킹 테스트**: 큐 시스템 작동 확인
4. **관전 테스트**: 다른 게임 관전 기능

---

**성공적으로 배포되면 전 세계 어디서든 홀로라이브OCG를 즐길 수 있습니다!** 🎮✨ 