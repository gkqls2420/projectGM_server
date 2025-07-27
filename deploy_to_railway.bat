@echo off
echo ========================================
echo    HoloDuel Railway 배포 스크립트
echo ========================================
echo.

echo [1/4] Git 초기화 확인...
if not exist .git (
    echo Git 저장소를 초기화합니다...
    git init
    git add .
    git commit -m "Initial commit for Railway deployment"
    echo.
    echo GitHub에 저장소를 생성하고 다음 명령어를 실행하세요:
    echo git remote add origin https://github.com/yourusername/holoduel-server.git
    echo git push -u origin main
    echo.
    pause
    exit /b 1
) else (
    echo Git 저장소가 이미 초기화되어 있습니다.
)

echo [2/4] 변경사항 커밋...
git add .
git commit -m "Update for Railway deployment"

echo [3/4] Railway 배포 준비 완료!
echo.
echo 다음 단계를 따라하세요:
echo.
echo 1. https://railway.app 에서 GitHub 계정으로 로그인
echo 2. "New Project" 클릭
echo 3. "Deploy from GitHub repo" 선택
echo 4. 이 프로젝트의 GitHub 저장소 선택
echo 5. 환경 변수 설정: SKIP_HOSTING_GAME = true
echo 6. 배포 완료 후 제공되는 URL 확인
echo.
echo 배포된 서버 URL을 클라이언트 설정에 입력하세요:
echo - online_server_settings.gd 파일의 ONLINE_SERVER_URL 수정
echo.

echo [4/4] 배포 준비 완료!
echo.
pause 