# HoloDuel Server
This is the server repo for HoloDuel.
This is a fan implementation of the Hololive card game.
I have no affiliation with Cover/Hololive. I own none of the assets/IP.

## 주요 변경사항 (v2.0)
- Azure Blob Storage 의존성 제거
- 로컬 파일 시스템 기반 데이터 저장
- Railway 배포 지원
- 헬스체크 엔드포인트 추가

## Setup
Install python 3.12.
Clone repo.
(preferably create a virtual environment "python -m venv venv" then activate it with active.cmd)
pip install -r requirements.txt
Run the server: runserver.cmd

## 데이터 저장
- 매치 로그: `data/match_logs/` 디렉토리에 JSON 파일로 저장
- 게임 패키지: `data/game_package/` 디렉토리에 저장
- 모든 데이터는 로컬 파일 시스템에 저장됩니다

## 유틸리티 스크립트
- `package_game_to_blob_storage.py`: 게임 패키지를 로컬 저장소에 업로드
- `download_match_logs.py`: 지정된 날짜 범위의 매치 로그 다운로드
- `test_local_storage.py`: 로컬 저장소 기능 테스트
- `deploy_to_railway.bat`: Railway 배포 스크립트

## Railway 배포
자세한 배포 가이드는 [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)를 참조하세요.

## 환경 변수
- `SKIP_HOSTING_GAME`: 게임 호스팅을 건너뛸지 여부 (기본값: false)
- `GAME_ZIP_FILE`: 게임 패키지 파일 경로
- `DAYS_BACK`: 매치 로그 다운로드 시 조회할 일수 (기본값: 7)

# Client Repo
https://github.com/daniel-k-taylor/holocardclient
