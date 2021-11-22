import  random
from datetime import datetime

from models import Author, Article, Tag, Blog
from database import DataBase, db_url

from sqlalchemy.sql.expression import func

if __name__ == '__main__':
    db = DataBase(db_url)


    with open('tags_info',  mode = 'r', encoding='utf-8') as file:
        tags_info = file.read().split('#')

    for tag in tags_info:
        tag = Tag(
            tag_text = tag
        )
        session = db.maker()
        session.add(tag)
        session.commit()
        session.close()

    with open('authors_info',  mode = 'r', encoding='utf-8') as file:
        authors_info = file.read().split('\n')

    session = db.maker()
    for author in authors_info:
        blog = Blog(
            heading = f'Мой блог~{author}',
            created_date = datetime.utcnow()
        )
        print('blog',blog.id, blog.heading)
        author = Author(
            name = author,
        )
        author.blog = blog

        session.add(blog)
        session.add(author)


        for text in range(random.randint(50, 100)):
            article = Article(
                heading = f'Моя публикация~{text}',
                article_text =  f'ТЕКСТ~{text}',
                p_date = datetime.utcnow(),
            )
            authors =  session.query(Author)
            rand_author = authors.order_by(func.random()).limit(1).first()
            print(rand_author)
            article.author = rand_author

            query = session.query(Tag)
            tags = query.order_by(func.random()).limit(random.randint(3, 5)).all()
            article.tag.extend(tags)
            session.add(article)
    session.commit()
    session.close()









