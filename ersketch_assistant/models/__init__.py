from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


pg_db = getenv('PG_DB')
pg_host = getenv('PG_HOST')
pg_port = getenv('PG_PORT')
pg_user = getenv('PG_USER')
pg_pass = getenv('PG_PASS')
pg_echo = getenv('PG_ECHO', False)

engine = create_engine(
    f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}',
    echo=pg_echo
)


def session(expire_on_commit=True) -> Session:
    return sessionmaker(engine, expire_on_commit=expire_on_commit)()
