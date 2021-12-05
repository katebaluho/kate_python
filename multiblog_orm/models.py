# Проектируем базу данных мультиблога
# : Должен быть объект публикации
# : Должны быть теги
# : Объект Автора
# : Объект блога


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
    Column('articles_id', Integer, ForeignKey('articles.id')),
    Column('tags_id', Integer, ForeignKey('tags.id'))
)

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String(32), unique=False)
    created_date = Column(DateTime, unique=False)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=False)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False) #каждый автор ведет 1 блог
    blog = relationship(Blog, backref='authors', uselist = False)

    @staticmethod
    def get_author_tags(session, name):
        author = session.query(Author).filter(Author.name == name).first()
        author_articles = author.articles
        tags = []
        for article in author_articles:
            tags.extend(list(article.tag))
        return list(set(tags))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String(100), unique=False)
    article_text = Column(String(255), unique=False)
    p_date = Column(DateTime, unique=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False) #каждая статья имеет 1 автора
    author = relationship('Author', backref='articles', uselist = False)

    tag = relationship('Tag', secondary = _article_tags ,backref='articles')

    def __str__(self):
        return self.article_text

    def __repr__(self):
        return self.article_text



class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_text = Column(String(32), unique=False)

    @staticmethod
    def get_authors_with_tag(session, tag_text):
        tag = session.query(Tag).filter(Tag.tag_text == tag_text).first()
        articles_with_tag = tag.articles
        authors_list = [article.author for article in articles_with_tag]
        return list(set(authors_list))

    def __str__(self):
        return self.tag_text

    def __repr__(self):
        return self.tag_text
