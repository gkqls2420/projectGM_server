@echo off
REM ========================================
REM    HoloDuel Server Starter (Office)
REM ========================================

REM Change to the directory where this script resides, then move to project root
cd /d "%~dp0.."

REM ----------------------------------------
REM Environment preparation
REM ----------------------------------------

REM Inform the user which Python will be used
where python >nul 2>nul
if errorlevel 1 (
    echo ERROR: 'python' executable not found in PATH.
    echo        Please ensure Python is installed and added to PATH.
    pause
    exit /b 1
)

REM Set any required environment variables here
set "SKIP_HOSTING_GAME=true"

REM ----------------------------------------
REM Install Python dependencies
REM ----------------------------------------
echo.
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt

REM ----------------------------------------
REM Start the FastAPI / Uvicorn server
REM ----------------------------------------

echo Starting HoloDuel server at http://127.0.0.1:8000
python -m uvicorn server:app --reload --host 127.0.0.1 --port 8000

echo.
echo Server stopped.
pause 