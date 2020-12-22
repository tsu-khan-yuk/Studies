from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker
from mvc.local import DATABASE_URI
from mvc.models import User, Blog, Article, Comment
import sqlalchemy.exc as error


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
    __engine = create_engine(DATABASE_URI)
    __session = None

    def __init__(self):
        self.__set_session()

    def __set_session(self):
        try:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
        except Exception as ex:
            print('DATABASE NOT FOUND:')
            raise ex

    def __del__(self):
        self.__session.close()

    def get_all_table_items(self, **kwargs) -> list:
        """
        :param table_name:
        :return:
        """
        table_data = self.__session.query(string_to_type(kwargs['table_name'])).all()
        return table_data

    def find_items(self, **kwargs):
        """
        :param fields:
        :param conditions:
        :return:
        """
        entities = list()
        attributes = list()
        for field in kwargs['fields']:
            for table in ['User', 'Blog', 'Article', 'Comment']:
                if field in string_to_type(table).fields():
                    entities.append(table)
                    attributes.append(field)

        found_data = list()
        condition_values = dict(zip(kwargs['fields'], kwargs['conditions']))
        for attribute, entity in zip(attributes, entities):
            if isinstance(condition_values[attribute], str):
                query = self.__session.query(string_to_type(entity))
                query = eval(
                    f'query.filter({entity}.{attribute}=="{condition_values[attribute]}")'
                )
                found_data += query.all()
            elif isinstance(condition_values[attribute], list):
                query = self.__session.query(string_to_type(entity))
                query = eval(
                    f'query.filter({entity}.{attribute}'
                    f'.between({condition_values[attribute][0]}, {condition_values[attribute][1]}))'
                )
                found_data += query.all()
        if found_data == []:
            return None
        return found_data

    def insert_item(self, **kwargs):
        """
        :param table_name:
        :param new_data:
        :return:
        """
        object_type = string_to_type(kwargs['table_name'])
        object_content = object_type()
        for attr in kwargs['new_data'].keys():
            setattr(object_content, attr, kwargs['new_data'][attr])
        try:
             self.__session.add(object_content)
             self.__session.commit()
             return str(object_content)
        except error.IntegrityError as ex:
            error_detail = str(ex).split('\n')[1]
            print('STDERR: Integrity Error \n' + error_detail)
            self.__set_session()
        except error.DataError as ex:
            error_detail = str(ex).split('\n')[0]
            error_detail = error_detail[len('(psycopg2.errors.NumericValueOutOfRange) v'):]
            error_detail = 'DETAIL: V' + error_detail
            print('STDERR: Data Error: \n' + error_detail)
            self.__set_session()
        except Exception as ex:
            print(ex)
            self.__set_session()
        return None

    def update_item(self, **kwargs):
        """
        :param table_name:
        :param attribute_to_change:
        :param new_value:
        :param key_attribute:
        :param key_value:
        :return:
        """
        query_data = self.__session.query(string_to_type(kwargs['table_name'])).filter()
        query_data = eval(
            f'query_data.filter({kwargs["table_name"]}.{kwargs["key_attribute"]}=="{kwargs["key_value"]}")'
        )
        query_data = query_data.all()
        update_limit = 1

        if query_data == []:
            return None
        elif len(query_data) > 1:
            while True:
                answer = input(
                    '>>> Several options were found. Change (all/first) or'
                    'choose other key attribute: '
                )
                if answer == 'all':
                    update_limit = len(query_data)
                    break
                elif answer == 'first':
                    update_limit = 1
                    break
                else:
                    print('Invalid answer')

        ret = list()
        for index in range(update_limit):
            eval(
                f'setattr(query_data[{index}], '
                f'"{kwargs["attribute_to_change"]}", '
                f'"{kwargs["new_value"]}")'
            )
            ret.append(query_data[index])

        try:
            self.__session.commit()
            return ret
        except Exception as err:
            print(err)
            self.__set_session()
        return None

    def delete_item(self, **kwargs):
        """
        :param entity:
        :param attribute:
        :param value:
        :return:
        """
        query = self.__session.query(string_to_type(kwargs['entity'])).filter()
        query_data = eval(
            f'query.filter({kwargs["entity"]}.{kwargs["attribute"]}=="{kwargs["value"]}")'
        )
        query_data = query_data.all()
        delete_limit = 1

        if query_data == []:
            return None
        elif len(query_data) > 1:
            while True:
                answer = input(
                    '>>> Several options were found. Change (all/first) or'
                    'choose other key attribute: '
                )
                if answer == 'all':
                    delete_limit = len(query_data)
                    break
                elif answer == 'first':
                    delete_limit = 1
                    break
                else:
                    print('Invalid answer')

        try:
            for index in range(delete_limit):
                self.__session.delete(query_data[index])
            self.__session.commit()
        except Exception as ex:
            print(ex)
            self.__set_session()
            return None
        return query_data
