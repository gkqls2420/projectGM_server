@echo off
echo ========================================
echo    Railway URL 확인 도구
echo ========================================
echo.

REM Railway CLI 설치 확인
echo [1/4] Railway CLI 확인...
railway --version >nul 2>&1
if errorlevel 1 (
    echo Railway CLI가 설치되지 않았습니다.
    echo 다음 명령어로 설치하세요: npm install -g @railway/cli
    pause
    exit /b 1
)
echo ✓ Railway CLI 확인 완료

REM 로그인 확인
echo [2/4] Railway 로그인 확인...
railway whoami >nul 2>&1
if errorlevel 1 (
    echo Railway에 로그인이 필요합니다.
    echo 다음 명령어로 로그인하세요: railway login
    pause
    exit /b 1
)
echo ✓ Railway 로그인 확인 완료

REM 프로젝트 상태 확인
echo [3/4] 프로젝트 상태 확인...
railway status
if errorlevel 1 (
    echo 프로젝트 상태 확인에 실패했습니다.
    pause
    exit /b 1
)

REM 서비스 URL 확인
echo [4/4] 서비스 URL 확인...
railway domain
if errorlevel 1 (
    echo 서비스 URL 확인에 실패했습니다.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    URL 확인 완료!
echo ========================================
echo.
echo 다음 명령어로 추가 정보를 확인할 수 있습니다:
echo - railway logs --follow
echo - railway status
echo - railway domain
echo.
pause 