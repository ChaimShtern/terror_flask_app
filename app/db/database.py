from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.models import Base

load_dotenv(verbose=True)

engine = create_engine(os.environ['POSTGRES_URL'])

session_maker = sessionmaker(bind=engine)


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)

# drop_tables()
# create_tables()
