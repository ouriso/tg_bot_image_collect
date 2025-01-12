from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from ersketch_assistant.config import DB_CONNECTION_STRING, DB_ECHO

pg_db = getenv('PG_DB')
pg_host = getenv('PG_HOST')
pg_port = getenv('PG_PORT')
pg_user = getenv('PG_USER')
pg_pass = getenv('PG_PASS')
pg_echo = getenv('PG_ECHO', False)

engine = create_engine(DB_CONNECTION_STRING, echo=DB_ECHO)

Base = declarative_base()


def initialize_database():
    Base.metadata.create_all(engine)


def session(expire_on_commit=True) -> Session:
    return sessionmaker(engine, expire_on_commit=expire_on_commit)()
