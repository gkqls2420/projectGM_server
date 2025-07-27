@echo off
echo ========================================
echo    HoloDuel Server Starter
echo ========================================
echo.

REM 가상환경 활성화
echo [1/4] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment!
    echo Please run setup_server.bat first.
    pause
    exit /b 1
)

REM 환경 변수 설정
echo [2/4] Setting environment variables...
set SKIP_HOSTING_GAME=true

REM 서버 시작
echo [3/4] Starting server...
echo Server will be available at: http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo.

uvicorn server:app --reload --host 127.0.0.1 --port 8000

echo.
echo Server stopped.
pause 