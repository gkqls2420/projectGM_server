@echo off
echo ========================================
echo    HoloDuel Server Stopper
echo ========================================
echo.

echo Looking for server processes on port 8000...

REM 포트 8000을 사용하는 프로세스 찾기
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    echo Found process ID: %%a
    echo Stopping server process...
    taskkill /PID %%a /F
    if errorlevel 1 (
        echo Failed to stop process %%a
    ) else (
        echo Successfully stopped process %%a
    )
)

echo.
echo Server stopped.
pause 