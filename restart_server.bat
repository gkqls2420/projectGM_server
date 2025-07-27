@echo off
echo ========================================
echo    HoloDuel Server Restarter
echo ========================================
echo.

echo Stopping existing server...
call stop_server.bat

echo.
echo Waiting 3 seconds before starting new server...
timeout /t 3 /nobreak > nul

echo.
echo Starting new server...
call start_server.bat 