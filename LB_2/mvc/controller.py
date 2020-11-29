from mvc.local import db_settings
from mvc.model import User, Blog, Article, Comment
from re import sub
from datetime import datetime
import psycopg2 as psql


push_timer_button = lambda: datetime.now()


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
    def __sql_search_query_generator(fields: list, conditions: list) -> dict:
        entities = list()
        attributes = list()
        sql_request = dict()
        for field in fields:
            for table in ['User', 'Blog', 'Article', 'Comment']:
                if field in string_to_type(table).fields():
                    entities.append(table)
                    attributes.append(field)
        condition_values = dict(zip(fields, conditions))
        string_search = str()
        integer_search = str()
        for entity, attribute in zip(entities, attributes):
            if isinstance(condition_values[attribute], str):
                string_search += 'SELECT %(attribute)s FROM "%(entity)s" '\
                                 'WHERE "%(entity)s"."%(attribute)s" ' % \
                {
                    'attribute': attribute,
                    'entity': entity
                }
                string_search += f"like '%{condition_values[attribute]}%' "
                string_search += 'union all '
            elif isinstance(condition_values[attribute], list):
                integer_search += 'SELECT %(attribute)s FROM "%(entity)s" '\
                                  'WHERE %(right)d < "%(entity)s"."%(attribute)s" '\
                                  'AND "%(entity)s"."%(attribute)s" < %(left)d ' % \
                {
                    'attribute': attribute,
                    'entity': entity,
                    'right': condition_values[attribute][0],
                    'left': condition_values[attribute][1]
                }
                integer_search += 'union all '
        sql_request['string_search'] = string_search[:-len('union all ')]
        sql_request['integer_search'] = integer_search[:-len('union all ')]
        return sql_request

    def find_items(self, fields: list, conditions: list) -> dict:
        data = dict()
        values = self.__sql_search_query_generator(fields, conditions)

        if values['string_search']:
            start1 = push_timer_button()
            self.__db.execute(values['string_search'])
            stop1 = push_timer_button()
            data['string'] = self.__db.fetchall()
            for raw_data, data_list_counter in zip(data['string'], range(len(data['string']))):
                data['string'][data_list_counter] = raw_data[0]

        if values['integer_search']:
            start2 = push_timer_button()
            self.__db.execute(values['integer_search'])
            stop2 = push_timer_button()
            data['integer'] = self.__db.fetchall()
            for raw_data, data_list_counter in zip(data['integer'], range(len(data['integer']))):
                data['integer'][data_list_counter] = raw_data[0]

        data['timer'] = ((stop1 - start1) + (stop2 - start2)).microseconds

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
