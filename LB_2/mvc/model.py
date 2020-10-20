ID = {
    'user_id': 0,
    'blog_id': 0,
    'article_id': 0,
    'comment_id': 0
}    


# STRUCTURE = {
#         'User': {
#             'user_id',
#             'name',
#             'mail'
#         },
#         'Blog': {
#             'blog_id',
#             'name',
#             'description',
#             'user_id'
#         },
#         'Article': {
#             'article_id',
#             'name',
#             'text',
#             'blog_id'
#         },
#         'Comment': {
#         'comment_id',
#         'text',
#         'article_id'
#     }
# }


class User:
    user_id = None
    name = None
    mail = None
    
    def __init__(self, name, mail=None) -> None:
        if isinstance(name, str) and isinstance(mail, (str, type(None))):
            self.user_id = ID['user_id']
            ID['user_id'] += 1
            self.name = name
            self.mail = mail
        else:
            raise TypeError('Invalid User name or mail values')

    @staticmethod
    def fields():
        return ('user_id', 'name', 'mail')
    
    @staticmethod
    def model_type():
        return 'User'

    def __str__(self):
        return '<User object[{}]: {}|{}>'.format(self.user_id, self.name, self.mail)


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
            raise TypeError('Invalid Blog name, description or user_id values')

    @staticmethod
    def fields():
        return ('blog_id', 'name', 'description', 'user_id')

    @staticmethod
    def model_type():
        return 'Blog'

    def __str__(self):
        output = '<Blog object[{}]: ['.format(self.user_id)
        output += ' name: "{}" |'.format(self.name)
        output += ' description: "{}" |'.format(self.description)
        output += ' ' # TODO: !!!
        return output


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
            raise TypeError('Invalid Article name, text or blog_id values')

    @staticmethod
    def fields():
        return ('article_id', 'name', 'text', 'blog_id')

    @staticmethod
    def model_type():
        return 'Article'

    def __str__(self):
        output = '<Article object[{}]: ['.format(self.article_id)
        output += 'name: "{}" | '.format(self.name)
        output += 'text: "{}" | '.format(self.text)
        output += 'fk_blog_id: "{}">'.format(self.text)


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

    @staticmethod
    def fields():
        return ('comment_id', 'text', 'article_id')

    @staticmethod
    def model_type():
        return 'Comment'


if __name__ == '__main__':
    pass


