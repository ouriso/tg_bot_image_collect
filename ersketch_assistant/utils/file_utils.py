import hashlib


def get_md5(file_path: str) -> str:
    """
    Подсчет md5-суммы файла.

    :param file_path: Путь к файлу
    :return: md5-сумма.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as fp:
        while True:
            chunk = fp.read(4096)
            if not chunk:
                break
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
