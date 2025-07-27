from app.dbaccess import upload_game_package
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# 게임 패키지 파일 경로 (환경 변수로 설정 가능)
GAME_ZIP_FILE = os.getenv('GAME_ZIP_FILE', r"D:\Projects\godot\holocardclient\export\game.zip")

if os.path.exists(GAME_ZIP_FILE):
    upload_game_package(GAME_ZIP_FILE)
    print("Game package uploaded to local storage successfully!")
else:
    print(f"Game package file not found at: {GAME_ZIP_FILE}")
    print("Please set the GAME_ZIP_FILE environment variable or update the path in this script.")