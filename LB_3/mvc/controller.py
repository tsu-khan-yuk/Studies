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
        pass

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
        # todo: add validation for data?
        # todo: need to upgrade try/except
        #   psycopg2.errors.ForeignKeyViolation sqlalchemy.exc.IntegrityError
        #   psycopg2.errors.NumericValueOutOfRange sqlalchemy.exc.DataError
        try:
             self.__session.add(object_content)
             self.__session.commit()
        except error.IntegrityError as ex:
            print('Int Err')
            self.__set_session()
        except error.DataError as ex:
            print('Data Err')
            self.__set_session()
        except Exception as ex:
            print(type(ex))
            self.__set_session()

    def insert_random_item(self, **kwargs):
        """
        :param table_name:
        :param rows_amount:
        :return:
        """
        pass

    def update_item(self, **kwargs):
        """
        :param table_name:
        :param attribute_to_change:
        :param new_value:
        :param key_attribute:
        :param key_value:
        :return:
        """
        pass

    def delete_item(self, **kwargs):
        """
        :param entity:
        :param attribute:
        :param value:
        :return:
        """
        query = self.__session.query(string_to_type(kwargs['entity'])).filter()
        query_data = eval(f'query.filter({kwargs["entity"]}.{kwargs["attribute"]}=={kwargs["value"]})')
        query_data = query_data.all()
        # todo: check in view
        # todo: create new session if crush
        # todo: need to upgrade try/except
        try:
            for item in query_data:
                self.__session.delete(item)
            self.__session.commit()
        except Exception as ex:
            self.__set_session()
            print(ex)
