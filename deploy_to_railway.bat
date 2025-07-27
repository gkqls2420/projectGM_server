@echo off
echo ========================================
echo    HoloDuel Railway 배포 스크립트
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

REM 프로젝트 초기화 (필요한 경우)
echo [3/4] Railway 프로젝트 초기화...
if not exist .railway (
    echo 새로운 Railway 프로젝트를 생성합니다...
    railway init
) else (
    echo 기존 Railway 프로젝트를 사용합니다.
)

REM 배포
echo [4/4] Railway에 배포 중...
railway up
if errorlevel 1 (
    echo 배포 중 오류가 발생했습니다.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    배포 완료!
echo ========================================
echo.
echo 다음 명령어로 배포 상태를 확인하세요:
echo railway status
echo.
echo 다음 명령어로 로그를 확인하세요:
echo railway logs
echo.
pause 