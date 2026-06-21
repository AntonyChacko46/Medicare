from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv(
    "postgresql://medicare_db_imi6_user:tXbkN9bGaGMB7HlfOiNBjVY3I4nrMQtr@dpg-d8s26anavr4c73f7neeg-a.virginia-postgres.render.com/medicare_db_imi6",
    "postgresql://postgres:root@localhost/medicare"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"sslmode": "require"}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()