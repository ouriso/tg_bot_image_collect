import traceback
from logging import getLogger

from telegram.constants import ParseMode
from telegram.ext import CallbackContext
from telegram.helpers import escape_markdown

from ersketch_assistant.config import ADMINS_IDS
from typing import Optional

MSG_ERROR = ('Что-то пошло не так. Попробуйте запросить данные позже.'
             ' Администраторы уведомлены о проблеме!')


async def error_handler(
        _update: Optional[object], context: CallbackContext) -> None:
    logger = getLogger()
    exc = context.error

    logger.error(msg="Во время работы бота возникло исключение:", exc_info=exc)

    # собираем трейс в единую строку
    tb_list = traceback.format_exception_only(type(exc), exc)
    tb_string = "".join(tb_list)

    message = (
        "Во время работы бота возникло исключение:\n"
        f"{escape_markdown(tb_string, 2)}"
    )

    # Finally, send the message
    await context.bot.send_message(
        chat_id=ADMINS_IDS[0], text=message, parse_mode=ParseMode.MARKDOWN_V2
    )
