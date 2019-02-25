from sqlalchemy import create_engine, text
from sqlalchemy.schema import CreateSchema, DropSchema
from constants import (
    DATABASE_URL,
    DB_SCHEMA
)
from sqlalchemy.sql import exists, select
from utils import pretty_print


def connect_to_db():
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        pretty_print("Connected to DB", True)
        return engine
    except Exception as e:
        print("ERROR! Unable to Connect to database with", DATABASE_URL)
        print(e)
        return False


def setup_schema(engine):
    with engine.connect() as conn:
        has_schema = conn.execute(text(
            f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{DB_SCHEMA}';"))

        if not has_schema.scalar():
            conn.execute(CreateSchema(DB_SCHEMA))

        conn.execute(DropSchema(DB_SCHEMA, None, True))
        conn.execute(CreateSchema(DB_SCHEMA))
        pretty_print(f"Created Schema {DB_SCHEMA}", True)


def setup_db():
    pretty_print("SETUP DATABASE")
    engine = connect_to_db()
    setup_schema(engine)

    return engine
