from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.env import Env

def create_db_sessionLocal():
    env = Env()
    DB_URL = f'mysql+pymysql://{env.get("MYSQL_USER")}:{env.get("MYSQL_PASSWORD")}@{env.get("MYSQL_HOST")}:{env.get("MYSQL_PORT")}/{env.get("MYSQL_DATABASE")}'

    engine = create_engine(DB_URL)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal = create_db_sessionLocal()
DB_Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
