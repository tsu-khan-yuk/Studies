from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
from re import sub
import psycopg2 as psql
import random
import time


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

    def get_all_table_items(self, table_name: str) -> list:
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

    def find_items(self, fields: list, conditions: list):
        """
            fields: ['user_id', 'name']
            conditions: [[0, 10], 'Ivan']
        """
        self.__sql_request_generator(fields, conditions)
        return []

    @staticmethod
    def __sql_request_generator(fields: list, conditions: list) -> str:
        entities = list()
        attributes = list()
        sql_request = 'SELECT * FROM '
        for field in fields:
            for table in ['User', 'Blog', 'Article', 'Comment']:
                if field in string_to_type(table).fields():
                    entities.append(table)
                    attributes.append(field)
        entities_set = set(entities)
        entities_str = sub("'", '"', str(entities_set))
        entities_str = sub(r'{|}', '', entities_str)
        sql_request += entities_str
        sql_request += ' WHERE '
        condition_part = str()
        condition_values = dict(zip(fields, conditions))
        for entity, attribute in zip(entities, attributes):
            print(attribute)
            if isinstance(condition_values[attribute], str):
                condition_part += f'"{entity}"."{attribute}"'
                condition_part += f" like '%{condition_values[attribute]}%'"
            elif isinstance(condition_values[attribute], list):
                condition_part += f'{condition_values[attribute][0]} < "{entity}"."{attribute}"'
                condition_part += ' AND '
                condition_part += f'"{entity}"."{attribute}" < {condition_values[attribute][1]}'
            condition_part += ' AND '
        sql_request += condition_part[:-5]
        print(sql_request)

    @staticmethod
    def input_processing(string: str) -> "int, str":
        """
        Функция принимает сторку и преобразовывает ее
        в тип соотвецтвенно указаниям полсе ':'
        <значение нужного типа>:<тип данных>
        """
        # # TODO: date ???
        input_string = input(string)
        if ":" in input_string:
            string_parts = input_string.split(":")
            if string_parts[1] == "int":
                try:
                    string_parts = int(string_parts[0])
                except ValueError:
                    print("Something went wrong")
                return string_parts
            elif string_parts[1] == "str":
                return string_parts[0]
            else:
                print("Something went wrong")
        else:
            return input_string


    def insert_item(self, table_name, data):
        data_dict = dict()
        print('You using formating input: ')
        for field in string_to_type(table_name).fields():
            data_dict[field] = self.input_processing('>>> Input {}: '.format(field))
        fields = tuple(data_dict.keys())
        values = tuple(data_dict.values())

        fields = sub("'", '"', str(fields))

        # # TODO: add check for types in db table ['blog_id']
        sql_request = 'INSERT INTO "%(table_name)s" %(fields)s VALUES %(values)s;' % {
            'table_name': table_name,
            'fields': fields,
            'values': str(tuple(data_dict.values()))
        }

        self.__db.execute(sql_request)
        self.__db_connection.commit()

    def delete_item(self, name):
        pass
