@echo off
echo Starting HoloDuel Server...
echo.

REM 가상환경 활성화 (존재하는 경우)
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Virtual environment activated.
)

REM 서버 시작
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
uvicorn server:app --reload --host 0.0.0.0 --port 8000