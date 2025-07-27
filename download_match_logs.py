import os
from app.dbaccess import download_blobs_between_dates
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# 날짜 범위 설정 (기본값: 최근 7일)
DAYS_BACK = int(os.getenv('DAYS_BACK', '7'))
END_DATE = datetime.now(timezone.utc)
START_DATE = END_DATE - timedelta(days=DAYS_BACK)

# 또는 특정 날짜 범위를 사용하려면 아래 주석을 해제하고 수정
# START_DATE = datetime(2024, 10, 10, tzinfo=timezone.utc)
# END_DATE = datetime(2024, 10, 20, tzinfo=timezone.utc)

logger.info(f"Downloading match logs from {START_DATE} to {END_DATE}")

# 다운로드 디렉토리 설정
current_directory = os.getcwd()
download_path = os.path.join(current_directory, "tests", "match_logs")

# 디렉토리가 없으면 생성
os.makedirs(download_path, exist_ok=True)

download_blobs_between_dates(START_DATE, END_DATE, download_path)

print("Match logs download completed!")