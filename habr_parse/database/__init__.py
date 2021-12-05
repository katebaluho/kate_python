from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from habr_parse.database.meta import Base
from habr_parse.database.settings import DATABASES


class DB:

    def __init__(self):
        db_url = DATABASES['URL']
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


db_url = DATABASES['URL']
db = DB()
start_session = db.maker()