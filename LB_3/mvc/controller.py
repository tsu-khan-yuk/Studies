from sqlalchemy import create_engine
from mvc.local import DATABASE_URI
from sqlalchemy.orm import sessionmaker


class Controller:
    __engine = create_engine(DATABASE_URI)
    __session = None

    def __init__(self):
        self.__session = sessionmaker(bind=self.engine)()

    def __del__(self):
        self.__session.close()

    def get_all_table_items(self, table_name: str) -> None:
        pass

    def find_items(self, fields: list, conditions: list):
        pass

    def insert_item(self, table_name: str):
        pass

    def insert_random_item(self, table_name: str, rows_amount: int):
        pass

    def update_item(self, table_name: str, attribute_to_change: str, new_value: str, key_attribute: str, key_value: str):
        pass

    def delete_item(self, entity: str, attribute: str, value: str):
        pass
