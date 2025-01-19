import logging

from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext

from ersketch_assistant.config import (TELEGRAM_CHAT_ID, ADMINS_IDS,
                                       TELEGRAM_CHANNEL_ID)

# from ersketch_assistant.utils.file_utils import get_md5
# from ersketch_assistant.models import session, engine
# from ersketch_assistant.models.tables import ImageMessage, Base

logger = logging.getLogger()

FW_CHANNEL_FILTER = filters.ForwardedFrom(TELEGRAM_CHANNEL_ID)
PRIVATE_USERS = filters.Chat()
PRIVATE_USERS.add_chat_ids(ADMINS_IDS)

FILTERS_PHOTO_CHANNEL = (filters.PHOTO & filters.Chat(TELEGRAM_CHAT_ID)
                         & ~filters.REPLY & ~filters.FORWARDED)
FILTERS_PHOTO_CHAT = (filters.PHOTO & filters.Chat(TELEGRAM_CHAT_ID)
                      & filters.REPLY)
FILTERS_PHOTO_FW_CHANNEL = filters.PHOTO & FW_CHANNEL_FILTER
FILTERS_PHOTO_FW_CHAT = (
    PRIVATE_USERS
    & filters.FORWARDED
    & filters.REPLY)


async def handle_from_channel(update: Update, _context: CallbackContext):
    logger.info(handle_from_channel.__name__)
    ...


async def handle_from_chat(update: Update, _context: CallbackContext):
    logger.info(handle_from_chat.__name__)
    ...


async def handle_forward_from_channel(
        update: Update, _context: CallbackContext):
    logger.info(handle_forward_from_channel.__name__)
    ...


async def handle_forward_from_chat(update: Update, _context: CallbackContext):
    logger.info(handle_forward_from_chat.__name__)
    ...


msg_from_channel = MessageHandler(
    FILTERS_PHOTO_CHANNEL, handle_from_channel
)
msg_from_chat = MessageHandler(
    FILTERS_PHOTO_CHAT, handle_from_chat
)
msg_fw_from_channel = MessageHandler(
    FILTERS_PHOTO_FW_CHANNEL, handle_forward_from_channel
)
msg_fw_from_chat = MessageHandler(
    FILTERS_PHOTO_FW_CHAT, handle_forward_from_chat
)
