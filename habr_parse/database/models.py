import datetime
from sqlalchemy.orm import relationship
from habr_parse.database.meta import Base


from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table
)

_publication_tag = Table(
    'publication_tag',
    Base.metadata,
    Column("publication_id", Integer, ForeignKey("publications.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String, unique=True, nullable=False)


class Publication(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    url = Column(String, unique=True, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", backref="publications")

    tags = relationship("Tag", secondary=_publication_tag, backref="publications")


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)





