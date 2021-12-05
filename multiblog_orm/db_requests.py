import  random
from datetime import datetime

from models import Author, Article, Tag, Blog
from database import DataBase, db_url

db = DataBase(db_url)
session = db.maker()
print(Author.get_author_tags(session = session, name = 'Грувман Мотл'))
print(Tag.get_authors_with_tag(session = session, tag_text = 'fun'))
session.close()