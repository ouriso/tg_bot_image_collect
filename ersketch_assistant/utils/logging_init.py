import os
from logging import StreamHandler, Formatter, getLogger, INFO
from logging.handlers import TimedRotatingFileHandler
from string import Template
from sys import stdout

LOGS_FORMAT = '[%(asctime)s - %(levelname)s] %(module)s: %(message)s'
LOG_FILE_DATE_FORMAT = '%Y-%m-%d'

DEBUG_FLAG = os.getenv('DEBUG', False)
LOG_PATH = r'./logs'
LOG_LEVEL = INFO


def log_init(
    module_name: str, debug_flag: bool = DEBUG_FLAG, log_level: int = LOG_LEVEL,
    log_path: str = LOG_PATH, logger_name: str = None
):
    os.makedirs(log_path, exist_ok=True)
    start_msg = Template(f'{module_name} started in $mode mode!')

    if logger_name is None:
        logger = getLogger()
    else:
        logger = getLogger(logger_name)
        logger.propagate = False

    logger.setLevel(log_level)

    file_name = f'{log_path}/{module_name.lower()}.log'
    if not os.path.exists(file_name):
        file = open(file_name, 'w')
        file.close()

    # Write to file by default
    f_handler = TimedRotatingFileHandler(
        file_name, when='midnight', interval=1, encoding='utf-8')
    f_handler.setLevel(log_level)
    f_format = Formatter(LOGS_FORMAT)
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)

    # Output to screen in debug mode
    if debug_flag:
        c_handler = StreamHandler(stream=stdout)
        c_handler.setLevel(log_level)
        c_format = Formatter(LOGS_FORMAT)
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

    logger.info("-" * 80)
    logger.info(start_msg.substitute(mode='debug' if debug_flag else "regular"))
    logger.info("-" * 80)
