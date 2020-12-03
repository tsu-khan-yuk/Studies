from sqlalchemy import create_engine
from mvc.local import DATABASE_URI
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker
from mvc.models import User, Blog, Article, Comment


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
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def __del__(self):
        self.__session.close()

    def get_all_table_items(self, table_name: str) -> None:
        table_data = self.__session.query(string_to_type(table_name)).all()
        return table_data

    def find_items(self, fields: list, conditions: list):
        pass

    def insert_item(self, table_name: str):
        pass

    def insert_random_item(self, table_name: str, rows_amount: int):
        pass

    def update_item(self, table_name: str, attribute_to_change: str, new_value: str, key_attribute: str, key_value: str):
        pass

    def delete_item(self, entity: str, attribute: str, value: str):
        # todo: add eval(f'self.__session.query(string_to_type({entity})).filter(...)')
        query = self.__session.query(string_to_type(entity)).filter()
        filter_group = Column.in_()
        # query = query.filter(and_(*filter_group))
