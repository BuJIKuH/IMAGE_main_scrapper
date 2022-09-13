from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import DB_PATH


def create_dbsession(dp_path=None, **kwargs):
    dp_path = dp_path or DB_PATH
    engine = create_engine(dp_path)
    SessionClass = sessionmaker(bind=engine)
    return SessionClass()