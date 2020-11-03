from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
import psycopg2 as psql


STRING_TEMPLATE = {
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
    __db_connection = None
    __db = None

    def __init__(self) -> None:
        self.__set_cursor()

    def __del__(self) -> None:
        self.__db.close()
        self.__db_connection.close()

    def __set_cursor(self) -> None:
        try:
            self.__db_connection = psql.connect(
                database=db_settings['database'],
                user=db_settings['user'],
                password=db_settings['password'],
                host=db_settings['host'],
                port=db_settings['port']
            )
            flag = True
        except Exception as ex:
            self.__db_connection = None
            flag = False

        if flag:
            self.__db = self.__db_connection.cursor()
        else:
            raise Exception('DB not found')

    def output_dict_formating(self, table: str, values: tuple) -> str:
        fields = string_to_type(table).fields()
        j = 0
        fields_values = dict()
        for i in fields:
            fields_values[i] = values[j]
            j += 1
        return STRING_TEMPLATE['output'][table] % fields_values

    def get_all_table_items(self, table_name: str) -> None:
        if table_name in {'User', 'Blog', 'Article', 'Comment'}:
            # # TODO: try/except
            self.__db.execute('SELECT * FROM "%(table)s"' % {'table': table_name})
            data = self.__db.fetchall()
            if not data:
                print('Table is empty')
                return
            buffer = list()
            table_type = string_to_type(table_name)
            for i in data:
                buffer.append(table_type.creating_from_tuple(i))
            return buffer
        else:
            raise TypeError('Invalid table_name')

    def show_item(self, table: str, field: str, condition: str) -> None:
        if table in {'User', 'Blog', 'Article', 'Comment'}:
            self.__db.execute(
                'SELECT * FROM "%(table)s" WHERE %(condition)s' %
                {
                'table': table,
                'condition': condition
                }
            )
            data = self.__db.fetchall()
            if not data:
                print('Not found')
                return
            buffer = list()
            for i in data:
                buffer.append(table_type.creating_from_tuple(i))
            return buffer
            
    def insert_item(self, name, price, quantity):
        pass

    def update_item(self, name, price, quantity):
        pass

    def update_item_type(self, new_item_type):
        pass

    def delete_item(self, name):
        pass
