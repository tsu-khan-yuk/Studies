from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment, STRUCTURE
import psycopg2 as psql


STRINGS = {
    'output': {
        'User': [
            '%(id)s | %(user)17s | %(mail)s',
            ['id', 'user', 'mail']
        ]
    }
}


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

    def show_items(self, table_name: str) -> None:
        if table_name in STRUCTURE.keys():
            self.db.execute('SELECT * FROM "%(table)s"' % {'table': table_name})
            # TODO: rewrite for other models !!!
            for i in self.db.fetchall():
                print('%(id)s | %(user)16s | %(mail)s' % {
                    'id': i[0],
                    'user': i[1],
                    'mail': i[2]
                })
        else:
            raise TypeError('Invalid table_name')

    def show_item(self, table: str, field: str, condition: str) -> None:
        if table in STRUCTURE.keys() and field in STRUCTURE[table]:
            self.db.execute(
                'SELECT * FROM "%(table)s" WHERE %(condition)s' % 
                {
                'table': table,
                'field': field,
                'condition': condition
                }    
            )
            # TODO: rewrite for other models !!!
            item = self.db.fetchall()
            print(STRINGS['output'][table] % {
                'id': item[0][0],
                'user': item[0][1],
                'mail': item[0][2]
            })

    def insert_item(self, name, price, quantity):
        pass

    def update_item(self, name, price, quantity):
        pass

    def update_item_type(self, new_item_type):
        pass

    def delete_item(self, name):
        pass
