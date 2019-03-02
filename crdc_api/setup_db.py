from sqlalchemy import create_engine, text
from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy.sql import exists, select
from utils import pretty_print


def connect_to_db(url):
    try:
        engine = create_engine(url)
        engine.connect()
        pretty_print("Connected to DB", True)
        return engine
    except Exception as e:
        print("ERROR! Unable to Connect to database with", url)
        print(e)
        return False


def setup_schema(engine, schema):
    with engine.connect() as conn:
        has_schema = conn.execute(text(
            f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{schema}';"))

        if not has_schema.scalar():
            conn.execute(CreateSchema(schema))

        conn.execute(DropSchema(schema, None, True))
        conn.execute(CreateSchema(schema))
        pretty_print(f"Created Schema {schema}", True)


def setup_db(config):
    pretty_print("SETUP DATABASE")
    engine = connect_to_db(config["url"])
    setup_schema(engine, config["schema"])

    return engine
