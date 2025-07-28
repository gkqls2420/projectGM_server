@echo off
echo ========================================
echo    HoloDuel Server Status Checker
echo ========================================
echo.

echo Checking server status on port 8000...
echo.

REM 포트 8000 상태 확인
netstat -an | findstr :8000
if errorlevel 1 (
    echo.
    echo [STATUS] Server is NOT running on port 8000
    echo.
    echo To start the server, run: start_server.bat
) else (
    echo.
    echo [STATUS] Server is running on port 8000
    echo.
    echo Server URL: http://127.0.0.1:8000
    echo WebSocket URL: ws://127.0.0.1:8000/ws
    echo.
    echo To stop the server, run: stop_server.bat
)

echo.
pause 