from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.models import Base

load_dotenv(verbose=True)

engine_test = create_engine(os.environ['POSTGRES_URL_TEST'])

session_maker_test = sessionmaker(bind=engine_test)


def create_tables_test():
    Base.metadata.create_all(engine_test)


def drop_tables_test():
    Base.metadata.drop_all(engine_test)
