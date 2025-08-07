@echo off
echo HoloDuel Client - Quick Push
echo ============================

REM 클라이언트 디렉토리로 이동
cd /d "D:\OneDrive\OneDrive - KRAFTON\cursor_study\projectGM\holocardclient-main"

REM 모든 변경사항 추가 및 커밋
git add .
git commit -m "Update client files - %date% %time%"

REM GitHub에 push (클라이언트 저장소)
git push origin master

echo.
echo Client Push 완료!
pause 