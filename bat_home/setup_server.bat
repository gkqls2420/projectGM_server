@echo off
echo ========================================
echo    HoloDuel Server Setup
echo ========================================
echo.

REM Python 버전 확인
echo [1/5] Checking Python version...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.10 or higher.
    pause
    exit /b 1
)

REM 가상환경 생성
echo [2/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists.
    set /p choice="Do you want to recreate it? (y/N): "
    if /i "%choice%"=="y" (
        echo Removing existing virtual environment...
        rmdir /s /q venv
        python -m venv venv
    )
) else (
    python -m venv venv
)

REM 가상환경 활성화
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)

REM 패키지 설치
echo [4/5] Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install packages!
    pause
    exit /b 1
)

REM 설정 완료
echo [5/5] Setup completed successfully!
echo.
echo You can now run start_server.bat to start the server.
echo.
pause 