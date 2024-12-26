# app/db/database.py

from sqlmodel import SQLModel, create_engine, Session
from models.models import Note  # Import your models here

# Configure your database URL here
DATABASE_URL = "sqlite:///./test.db"
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
