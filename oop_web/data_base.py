import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from oop_web.models import Base
from oop_web.settings import DATABASES


class DataBase:

    def __init__(self):
        db_url = DATABASES['promo_url']
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


if __name__ == '__main__':
    db = DataBase()
    print(1)
