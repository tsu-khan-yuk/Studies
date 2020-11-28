from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
from re import sub
import psycopg2 as psql
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
            return []
        buffer = list()
        table_type = string_to_type(table_name)
        for i in data:
            buffer.append(table_type.creating_from_tuple(i))
        return buffer

    @staticmethod
    def __sql_request_generator(fields: list, conditions: list) -> dict:
        entities = list()
        attributes = list()
        sql_request = str()
        for field in fields:
            for table in ['User', 'Blog', 'Article', 'Comment']:
                if field in string_to_type(table).fields():
                    entities.append(table)
                    attributes.append(field)
        entities_set = set(entities)
        entities_str = sub(r"'", '"', str(entities_set))
        entities_str = sub(r'{|}', '', entities_str)
        condition_values = dict(zip(fields, conditions))
        string_conditions = str()
        integer_conditions = str()
        for entity, attribute in zip(entities, attributes):

            if isinstance(condition_values[attribute], str):
                string_conditions += 'SELECT %(attribute)s FROM "%(entity)s" '\
                                     'WHERE "%(entity)s"."%(attribute)s" ' % \
                {
                    'attribute': attribute,
                    'entity': entity
                }
                string_conditions += "like '%%(value)s%' union all" % {
                    'value': condition_values[attribute]
                }
            elif isinstance(condition_values[attribute], list):
                integer_conditions += f'{condition_values[attribute][0]} < "{entity}"."{attribute}"'
                integer_conditions += ' AND '
                integer_conditions += f'"{entity}"."{attribute}" < {condition_values[attribute][1]}'
                integer_conditions += ' AND '

        sql_request += string_conditions + ' AND ' + integer_conditions
        ret = dict()
        ret['entities'] = entities
        ret['sql_request'] = sql_request
        print(sql_request)
        return ret

    def find_items(self, fields: list, conditions: list):
        values = self.__sql_request_generator(fields, conditions)
        self.__db.execute(values['sql_request'])
        data = self.__db.fetchall()
        return data

    @staticmethod
    def input_processing(string: str) -> "int, str":
        """
        Функция принимает сторку и преобразовывает ее
        в тип соотвецтвенно указаниям полсе ':'
        <значение нужного типа>:<тип данных>
        """
        # TODO: date ???
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
        print('You are using formatting input: ')
        # todo: change fields *_id [*]
        fields_set = string_to_type(table_name).fields()
        for i in range(1, len(fields_set)):
            data_dict[fields_set[i]] = self.input_processing('>>> Input {}: '.format(fields_set[i]))
        fields = tuple(data_dict.keys())
        values = tuple(data_dict.values())

        fields = sub("'", '"', str(fields))

        # TODO: add check for types in db table ['blog_id']
        sql_request = 'INSERT INTO "%(table_name)s" %(fields)s VALUES %(values)s;' % {
            'table_name': table_name,
            'fields': fields,
            'values': str(tuple(data_dict.values()))
        }

        self.__db.execute(sql_request)
        self.__db_connection.commit()

    def delete_item(self, name):
        pass
