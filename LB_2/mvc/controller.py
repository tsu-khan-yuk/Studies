from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
import psycopg2 as psql


STRINGS = {
    'output': {
        'User': ' %(id)s | %(user)17s | %(mail)s',
        'Blog': ' %(id)s | %(name)s | %(description)s | %(fk_user_id)s',
        'Article': ' %(id)s | %(name)s | %(text)s | %(fk_blog_id)s',
        'Comment': ' %(id)s | %(text)s | %(fk_article_id)s'
    }
}

def string_to_type(model_name: str):

    if model_name == 'User':
        return User
    elif model_name == 'Blog':
        return Blog
    elif model_name == 'Article':
        return Article
    elif model_name == 'Comment':
        return Comment


class Controller:
    db = None
    
    def __init__(self) -> None:
        self.set_cursor()

    def set_cursor(self) -> None:
        try:
            connection = psql.connect(
                database=db_settings['database'], 
                user=db_settings['user'],
                password=db_settings['password'], 
                host=db_settings['host'], 
                port=db_settings['port']
            )
            flag = True
        except Exception as ex:
            connection = None
            flag = False

        if flag:
            self.db = connection.cursor()
        else:
            raise Exception('DB not found')

    def output_dict_formating(self) -> dict:
        # TODO: returns dict for print
        pass

    def show_items(self, table_name: str) -> None:
        if table_name in {'User', 'Blog', 'Article', 'Comment'}:
            self.db.execute('SELECT * FROM "%(table)s"' % {'table': table_name})
            # TODO: rewrite for other models !!!
            for i in self.db.fetchall():
                print(STRINGS['output'][table_name] % {
                    'id': i[0],
                    'user': i[1],
                    'mail': i[2]
                })
        else:
            raise TypeError('Invalid table_name')

    def show_item(self, table: str, field: str, condition: str) -> None:
        if table in {'User', 'Blog', 'Article', 'Comment'} and field in string_to_type(table).fields():
            self.db.execute(
                'SELECT * FROM "%(table)s" WHERE %(condition)s' % 
                {
                'table': table,
                'field': field,
                'condition': condition
                }    
            )
            # TODO: rewrite for other models !!!
            items = self.db.fetchall()

            for i in items:
                print(STRINGS['output'][table] % {
                    'id': i[0],
                    'user': i[1],
                    'mail': i[2]
                })

    def insert_item(self, name, price, quantity):
        pass

    def update_item(self, name, price, quantity):
        pass

    def update_item_type(self, new_item_type):
        pass

    def delete_item(self, name):
        pass
