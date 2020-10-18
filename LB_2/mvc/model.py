ID = {
    'user_id': 0,
    'blog_id': 0,
    'article_id': 0,
    'comment_id': 0
}


class User:
    user_id = None
    name = None
    mail = None
    
    def __init__(self, name, mail=None) -> None:
        if isinstance(name, str) and isinstance(mail, (str, None)):
            self.user_id = ID['user_id']
            ID['user_id'] += 1
            self.name = name
            self.mail = mail
        else:
            raise TypeError


class Blog:
    blog_id = None
    name = None
    description = None
    user_id = None

    def __init__(self, name, description, user_id) -> None:
        if isinstance(name, str) and isinstance(description, str) and isinstance(user_id,(int, User)):
            self.blog_id = ID['blog_id']
            ID['blog_id'] += 1
            self.name = name
            self.description = description
            self.user_id = user_id
        else:
            raise TypeError


class Article:
    article_id = None
    name = None
    text = None
    blog_id = None

    def __init__(self, name, text, blog_id) -> None:
        if isinstance(name, str) and isinstance(text, str) and isinstance(blog_id, (int, Blog)):
            self.article_id = ID['article_id']
            ID['article_id'] += 1
            self.name = name
            self.text = text
            self.blog_id = blog_id
        else:
            raise TypeError


class Comment:
    comment_id = None
    text = None
    article_id = None

    def __init__(self, text, article_id) -> None:
        if isinstance(text, str) and isinstance(article_id, (int, Article)):
            self.comment_id = ID['comment_id']
            ID['comment_id'] += 1
            self.text = text
            self.article_id = article_id
