# Проектируем базу данных мультиблога
# todo: Должен быть объект публикации
# todo: Должны быть теги
# todo: Объект Автора
# todo: Объект блога


# todo:  Заполнить базу минимум 100 авторами, у каждого автора от 50 до 100 статей, в которых от 3х тегов
# todo: Составить запрос и определить все теги использованые этим автором
# todo: Составить запрос и получить всех авторов которые использовали "Этот тег"

import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    Table,
)

Base = declarative_base()

_article_tags = Table(
    'article_tags',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String(32), unique=False)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=False)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False) #каждый автор ведет 1 блог
    blog = relationship(Blog, backref='author', uselist = False)

    def generate_authors(self):
        pass


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String(100), unique=False)
    article_text = Column(String(255), unique=False)
    p_date = Column(DateTime, unique=False)

    author_id = Column(Integer, ForeignKey("author.id"), nullable=False) #каждая статья имеет 1 автора
    author = relationship('Author', backref='article', uselist = False)

    tag_id = Column(Integer, ForeignKey("tag.id"), nullable=False)  #многие теги в разных статьях
    tag = relationship('Tag', backref='article')

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_text = Column(String(32), unique=True)

