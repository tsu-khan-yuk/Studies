from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


FIELD_TYPES = {
    'user_id': int,
    'blog_id': int,
    'article_id': int,
    'comment_id': int,
    'text': str,
    'description': str,
    'name': str,
    'e_mail': str
}


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    e_mail = Column(String)
    blogs = relationship('Blog', cascade='all, delete')

    @staticmethod
    def fields():
        return 'user_id', 'name', 'e_mail'

    def __repr__(self):
        return '<User object[%(id)2d]: %(name)20s|%(mail)15s>' % {
            'id': self.user_id,
            'name': self.name,
            'mail': self.e_mail
        }


class Blog(Base):
    __tablename__ = 'Blog'
    blog_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    articles = relationship('Article', cascade='all, delete')

    @staticmethod
    def fields():
        return 'blog_id', 'name', 'description', 'user_id'

    def __repr__(self):
        return '<Blog object[%(id)2d]: %(name)20s|%(description).20s... |%(fk_id)d>' % {
            'id': self.blog_id,
            'name': self.name,
            'description': self.description,
            'fk_id': self.user_id
        }


class Article(Base):
    __tablename__ = 'Article'
    article_id = Column(Integer, primary_key=True)
    name = Column(String)
    text = Column(String)
    blog_id = Column(Integer, ForeignKey('Blog.blog_id'))
    comments = relationship('Comment', cascade='all, delete')

    @staticmethod
    def fields():
        return 'article_id', 'name', 'text', 'blog_id'

    def __repr__(self):
        return '<Article object[%(id)2d]: %(name)30s|%(text).30s... |%(fk_id)d>' % {
            'id': self.article_id,
            'name': self.name,
            'text': self.text,
            'fk_id': self.blog_id
        }


class Comment(Base):
    __tablename__ = 'Comment'
    comment_id = Column(Integer, primary_key=True)
    text = Column(String)
    article_id = Column(Integer, ForeignKey('Article.article_id'))

    @staticmethod
    def fields():
        return 'comment_id', 'text', 'article_id'

    def __repr__(self):
        return '<Comment object[%(id)2d]: %(text).30s... |%(fk_id)d>' % {
            'id': self.comment_id,
            'text': self.text,
            'fk_id': self.article_id
        }
