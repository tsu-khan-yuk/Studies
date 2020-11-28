class User:
    user_id = None
    name = None
    mail = None

    def __init__(self, id: int, name: str, mail: str) -> None:
        if isinstance(id, int) and isinstance(name, str) and isinstance(mail, str):
            self.user_id = id
            self.name = name
            self.mail = mail
        else:
            raise TypeError('Invalid User field type')

    @staticmethod
    def fields():
        return ('user_id','name', 'e-mail')

    @staticmethod
    def creating_from_tuple(values: tuple):
        return User(values[0], values[1], values[2])

    def __str__(self):
        return '<User object[%(id)d]: %(name)20s|%(mail)15s>' % {
            'id': self.user_id,
            'name': self.name,
            'mail': self.mail
        }


class Blog:
    blog_id = None
    name = None
    description = None
    user_id = None

    def __init__(self, id: int, name: str, description: str, user_id) -> None:
        if isinstance(id, int) and isinstance(name, str) and \
            isinstance(description, str) and isinstance(user_id,(int, User)):
            self.blog_id = id
            self.name = name
            self.description = description
            self.user_id = user_id
        else:
            raise TypeError('Invalid Blog name, description or user_id values')

    @staticmethod
    def fields():
        return ('blog_id','name', 'description', 'user_id')

    @staticmethod
    def creating_from_tuple(values: tuple):
        return Blog(values[0], values[1], values[2], values[3])

    def __str__(self):
        return '<Blog object[%(id)d]: %(name)20s|%(description).20s... |%(fk_id)d>' % {
            'id': self.blog_id,
            'name': self.name,
            'description': self.description,
            'fk_id': self.user_id
        }


class Article:
    article_id = None
    name = None
    text = None
    blog_id = None

    def __init__(self, id: int, name: str, text: str, blog_id) -> None:
        if isinstance(id, int) and isinstance(name, str) and \
            isinstance(text, str) and isinstance(blog_id, (int, Blog)):
            self.article_id = id
            self.name = name
            self.text = text
            self.blog_id = blog_id
        else:
            raise TypeError('Invalid Article name, text or blog_id values')

    @staticmethod
    def fields():
        return ('article_id', 'name', 'text', 'blog_id')

    @staticmethod
    def creating_from_tuple(values: tuple):
        return Article(values[0], values[1], values[2], values[3])

    def __str__(self):
        return '<Article object[%(id)d]: %(name)30s|%(text).30s... |%(fk_id)d>' % {
            'id': self.article_id,
            'name': self.name,
            'text': self.text,
            'fk_id': self.blog_id
        }


class Comment:
    comment_id = None
    text = None
    article_id = None

    def __init__(self, id: int, text: str, article_id) -> None:
        if isinstance(id, int) and isinstance(text, str) and \
            isinstance(article_id, (int, Article)):
            self.comment_id = id
            self.text = text
            self.article_id = article_id

    @staticmethod
    def fields():
        return ('comment_id', 'text', 'article_id')

    @staticmethod
    def creating_from_tuple(values: tuple):
        return Comment(values[0], values[1], values[2])

    def __str__(self):
        return '<Comment object[%(id)d]: %(text).30s... |%(fk_id)d>' % {
            'id': self.comment_id,
            'text': self.text,
            'fk_id': self.article_id
        }


FIELD_TYPES = {
    'user_id': int,
    'blog_id': int,
    'article_id': int,
    'comment_id': int,
    'text': str,
    'description': str,
    'name': str,
    'e-mail': str
}
