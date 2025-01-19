from os import getenv
from pathlib import Path

# common settings
BASE_DIR = Path(__file__).resolve().parent
DEBUG_FLAG = getenv("DEBUG", False)

# TG settings
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = int(getenv("TELEGRAM_CHAT_ID", "0"))
TELEGRAM_CHANNEL_ID = int(getenv("TELEGRAM_CHANNEL_ID", "0"))
ADMINS_IDS = [int(aid) for aid in getenv("ADMINS_IDS").split(',')]


# DB settings
DB_NAME = getenv('DB_NAME')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_ECHO = getenv('DB_ECHO', False)

DB_CONNECTION_STRING = (
    f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
