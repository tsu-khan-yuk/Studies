from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    e_mail = Column(String)

    def __repr__(self):
        return '<User object[%(id)d]: %(name)20s|%(mail)15s>' % {
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
    user = relationship('User')

    def __repr__(self):
        return '<Blog object[%(id)d]: %(name)20s|%(description).20s... |%(fk_id)d>' % {
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
    blog = relationship('Blog')

    def __repr__(self):
        return '<Article object[%(id)d]: %(name)30s|%(text).30s... |%(fk_id)d>' % {
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
    article = relationship('Article')

    def __repr__(self):
        return '<Comment object[%(id)d]: %(text).30s... |%(fk_id)d>' % {
            'id': self.comment_id,
            'text': self.text,
            'fk_id': self.article_id
        }
