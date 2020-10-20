from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
import psycopg2 as psql


STRINGS = {
    'output': {
        'User': ' %(user_id)s | %(name)17s | %(mail)s',
        'Blog': ' %(blog_id)s | %(name)s | %(description)s | %(user_id)s',
        'Article': ' %(article_id)s | %(name)s | %(text)s | %(blog_id)s',
        'Comment': ' %(comment_id)s | %(text)s | %(article_id)s'
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

    def output_dict_formating(self, table: str, values: tuple) -> str:
        fields = string_to_type(table).fields()
        j = 0
        ret = dict()
        for i in fields:
            ret[i] = values[j]
            j += 1
        return STRINGS['output'][table] % ret

    def show_items(self, table_name: str) -> None:
        if table_name in {'User', 'Blog', 'Article', 'Comment'}:
            self.db.execute('SELECT * FROM "%(table)s"' % {'table': table_name})
            data = self.db.fetchall()
            if not data:
                print('Table is empty')
                return None
            for i in data:
                print(self.output_dict_formating(table_name, i))
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
