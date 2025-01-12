from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.functions import current_timestamp

from ersketch_assistant.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    fullname = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=current_timestamp)


class ImageMessage(Base):
    __tablename__ = 'image_messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_md5 = Column(String, nullable=False, unique=True,
                       comment="MD5-сумма изображения")
    message_id = Column(Integer, primary_key=True,
                        comment="Идентификатор сообщения пользователя")
    username = Column(String(50), nullable=False)
    user_id = Column(Integer, nullable=False,
                     comment="Идентификатор пользователя в ТГ")
    channel_id = Column(Integer, nullable=False,
                        comment="Идентификатор канала")
    chat_id = Column(Integer, nullable=False,
                     comment="Идентификатор чата")
    message_date = Column(DateTime, nullable=False)
    image_url = Column(String, nullable=False,
                       comment="Ссылка на изображение")
    image_path = Column(String, nullable=False,
                        comment="Локальный путь к изображению")
    text = Column(String, nullable=True,
                  comment="Сообщение к картинке")
    original_message_id = Column(
        Integer, nullable=True,
        comment="Идентификатор сообщения, на которое отвечал пользователь")
    is_reply_message = Column(Boolean, nullable=True,
                              comment="Является ли сообщение ответом")
