import os
import zipfile
import json
import secrets
import string
import aiofiles
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

# 로컬 파일 시스템 경로 설정
LOCAL_DATA_DIR = "data"
MATCH_LOGS_DIR = os.path.join(LOCAL_DATA_DIR, "match_logs")
GAME_PACKAGE_DIR = os.path.join(LOCAL_DATA_DIR, "game_package")

def ensure_directories():
    """필요한 디렉토리들을 생성합니다."""
    os.makedirs(MATCH_LOGS_DIR, exist_ok=True)
    os.makedirs(GAME_PACKAGE_DIR, exist_ok=True)

def generate_short_alphanumeric_id(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def upload_match_to_local_storage(match_data):
    """매치 데이터를 로컬 파일 시스템에 저장합니다."""
    try:
        ensure_directories()
        
        # 고유한 파일명 생성
        uuid = generate_short_alphanumeric_id()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"match_{timestamp}_{uuid}_{match_data['player_info'][0]['username']}_VS_{match_data['player_info'][1]['username']}.json"
        file_path = os.path.join(MATCH_LOGS_DIR, filename)
        
        # 매치 데이터를 JSON 파일로 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(match_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Match data saved to local storage: {file_path}")
        
    except Exception as e:
        logger.error(f"Error saving match data to local storage: {e}")

def upload_game_package_local(game_zip_path):
    """게임 패키지를 로컬에 복사합니다."""
    try:
        ensure_directories()
        
        # 게임 패키지를 로컬 디렉토리에 복사
        import shutil
        destination_path = os.path.join(GAME_PACKAGE_DIR, "game.zip")
        shutil.copy2(game_zip_path, destination_path)
        
        logger.info(f"Game package copied to local storage: {destination_path}")
        
    except Exception as e:
        logger.error(f"Error copying game package to local storage: {e}")

async def download_and_extract_game_package_local(destination_path):
    """로컬에서 게임 패키지를 다운로드하고 압축을 해제합니다."""
    try:
        ensure_directories()
        
        # 로컬 게임 패키지 경로
        local_game_zip = os.path.join(GAME_PACKAGE_DIR, "game.zip")
        
        # 게임 패키지가 존재하는지 확인
        if not os.path.exists(local_game_zip):
            logger.warning(f"Game package not found at {local_game_zip}")
            return False
        
        # 압축 해제
        logger.info(f"Extracting game package from {local_game_zip} to {destination_path}")
        with zipfile.ZipFile(local_game_zip, 'r') as zip_ref:
            zip_ref.extractall(destination_path)
        
        logger.info(f"Game package extracted successfully to {destination_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error extracting game package: {e}")
        return False

def download_match_logs_between_dates(start_date, end_date, download_path):
    """지정된 날짜 범위의 매치 로그를 다운로드합니다."""
    try:
        ensure_directories()
        
        # 다운로드 디렉토리 생성
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        
        # 매치 로그 디렉토리의 모든 파일 검사
        if not os.path.exists(MATCH_LOGS_DIR):
            logger.warning(f"Match logs directory not found: {MATCH_LOGS_DIR}")
            return
        
        for filename in os.listdir(MATCH_LOGS_DIR):
            if filename.endswith('.json'):
                file_path = os.path.join(MATCH_LOGS_DIR, filename)
                file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                # 날짜 범위 확인
                if start_date <= file_modified_time <= end_date:
                    destination_path = os.path.join(download_path, filename)
                    import shutil
                    shutil.copy2(file_path, destination_path)
                    logger.info(f"Downloaded match log: {filename}")
        
        logger.info("Match logs download complete.")
        
    except Exception as e:
        logger.error(f"Error downloading match logs: {e}")

# 기존 Azure 함수들을 로컬 함수로 대체하는 래퍼 함수들
def upload_match_to_blob_storage(match_data):
    """Azure Blob Storage 대신 로컬 저장소를 사용합니다."""
    upload_match_to_local_storage(match_data)

def upload_game_package(game_zip_path):
    """Azure Blob Storage 대신 로컬 저장소를 사용합니다."""
    upload_game_package_local(game_zip_path)

async def download_and_extract_game_package(destination_path):
    """Azure Blob Storage 대신 로컬 저장소를 사용합니다."""
    return await download_and_extract_game_package_local(destination_path)

def download_blobs_between_dates(start_date, end_date, download_path):
    """Azure Blob Storage 대신 로컬 저장소를 사용합니다."""
    download_match_logs_between_dates(start_date, end_date, download_path)