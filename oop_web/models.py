from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
)

Base = declarative_base()


class PromoLink(Base):
    __tablename__ = 'promo_link'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), unique=False)
    label = Column(String(50), unique=False)
