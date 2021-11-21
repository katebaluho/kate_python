import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from multiblog_orm import models


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


if __name__ == '__main__':
    db_url = "sqlite:///multiblog_db.db"
    db = DataBase(db_url)
    print(1)

