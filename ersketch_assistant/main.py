import logging

from telegram.ext import ApplicationBuilder

from config import TELEGRAM_BOT_TOKEN

from utils.logging_init import log_init
from handlers.error_handler import error_handler
from handlers import image_handlers


logger = logging.getLogger()


def main() -> None:
    # Создание объекта Updater и передача токена вашего бота
    app = ApplicationBuilder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    log_init(__name__)

    app.add_handler(image_handlers.msg_from_channel)
    app.add_handler(image_handlers.msg_from_chat)
    app.add_handler(image_handlers.msg_fw_from_chat)
    app.add_handler(image_handlers.msg_fw_from_channel)

    app.add_error_handler(error_handler)

    # Запуск бота
    app.run_polling()


if __name__ == "__main__":
    main()
