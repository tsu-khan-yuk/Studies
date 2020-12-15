import datetime as date
from re import sub
from numpy import fabs
from mvc.controller import string_to_type
from mvc.view import View
from mvc.models import FIELD_TYPES
# todo: compile r'[)(]'


class MainConsole:
    view = View()

    def __init__(self):
        print('PyPSQL console 2.5(Based on Python 3.6.9+) [%(date)s]' %
              {'date': str(date.datetime.now())[:-10]})
        hello_string = '+ --------------------------------------------- +\n'
        hello_string += '| "insert" command to insert item               |\n'
        hello_string += '| "get" command to get item from table          |\n'
        hello_string += '| "update" command to update items from tables  |\n'
        hello_string += '| "delete" command to delete item from table    |\n'
        hello_string += '| "quit" command to quit                        |\n'
        hello_string += '| "help" command to show this box               |\n'
        hello_string += '+ --------------------------------------------- +'
        print(hello_string)
        while True:
            input_string = input('/ >>> ')
            if input_string == 'quit':
                break
            elif input_string == 'help':
                print(hello_string)
            elif input_string in {'insert', 'delete', 'get', 'update'}:
                self.command_manager(input_string)
            else:
                print('Invalid command')

    def command_manager(self, cmd_name: str):
        if cmd_name == 'insert':
            self.insert_menu()
        elif cmd_name == 'get':
            self.get_menu()
        elif cmd_name == 'update':
            self.update_menu()
        elif cmd_name == 'delete':
            self.delete_menu()

    def get_menu(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "table" to see table                |\n'
        rules += '| "item" to search item               |\n'
        rules += '| "help" command to show this box     |\n'
        rules += '| "cancel" command to go back         |\n'
        rules += '+ ----------------------------------- +'
        print(rules)
        while True:
            string = input('/get/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string == 'table':
                print('Choose table: User, Blog, Article, Comment')
                while True:
                    table_name = input('/get/table/ >>> ')
                    if table_name == 'cancel':
                        break
                    elif table_name in {'User', 'Blog', 'Article', 'Comment'}:
                        self.view.table_view(
                            table_name=table_name
                        )
                    else:
                        print('Invalid table_name')
            elif string == 'item':
                print('Choose fields: user_id, blog_id, article_id, comment_id,\n'
                      '\ttext, description, name, e-mail')
                while True:
                    fields_name = input('/get/fields/ >>> ')
                    if fields_name == 'cancel':
                        break
                    fields_name = sub(',', ' ', fields_name).split()

                    invalid_name = False
                    for field in fields_name:
                        if field not in FIELD_TYPES.keys():
                            print('Invalid field_name {}'.format(field))
                            invalid_name = True
                            break
                    if invalid_name:
                        continue

                    fields_name = list(set(fields_name))
                    conditions = list()
                    ret = None
                    for field in fields_name:
                        if FIELD_TYPES[field] == int:
                            while True:
                                try:
                                    left_limit = int(
                                        input('/get/fields({})/ >>> Input left limit: '.format(field))
                                    )
                                    right_limit = int(
                                        input('/get/fields({})/ >>> Input right limit: '.format(field))
                                    )
                                    break
                                except:
                                    print('Invalid type')
                                    continue
                            if left_limit > right_limit:
                                left_limit, right_limit = right_limit, left_limit
                            ret = [left_limit, right_limit]

                        elif FIELD_TYPES[field] == str:
                            ret = input('/get/fields({})/ >>> Input string pattern: '.format(field))
                        conditions.append(ret)

                    self.view.items_view(
                        fields=fields_name,
                        conditions=conditions
                    )
            else:
                print('Invalid command')

    def insert_menu(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "help" command to show this box    |\n'
        rules += '| "cancel" command to go back        |\n'
        rules += '+ ----------------------------------- +\n'
        rules += 'Chose table: User, Blog, Article, Comment'
        print(rules)
        while True:
            string = input('/insert/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string in {'User', 'Blog', 'Article', 'Comment'}:
                while True:
                    input_type = input('Create random row or manual input(random/manual)?\n'
                                       '/insert/"%s" >>> ' % string)
                    if input_type == 'manual':
                        new_data = {field: None for field in string_to_type(string).fields()}
                        new_data.pop(string.lower() + '_id')
                        for attribute in new_data.keys():
                            new_data[attribute] = self.input_processing(
                                string='>>> Input {}: '.format(attribute),
                                field_name=attribute
                            )
                        self.view.insert_item_view(
                            table_name=string,
                            new_data=new_data
                        )
                    elif input_type == 'random':
                        while True:
                            number_of_rows = input('>>> Input number of rows:')
                            try:
                                number_of_rows = int(number_of_rows)
                                break
                            except:
                                print('Invalid data type')
                        self.view.insert_random_items_view(
                            table_name=string,
                            rows_amount=fabs(number_of_rows)
                        )
                    elif input_type == 'cancel':
                        break
                    else:
                        print('Invalid option')
            else:
                print('Invalid command')

    def update_menu(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "help" command to show this box    |\n'
        rules += '| "cancel" command to go back        |\n'
        rules += '+ ----------------------------------- +\n'
        rules += 'Chose table: User, Blog, Article, Comment'
        print(rules)
        while True:
            string = input('/update/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string in {'User', 'Blog', 'Article', 'Comment'}:
                table_name = string
                execution_flag = True
                while execution_flag:
                    print('Choose: {}'.format(sub(r'[)(]', '', str(string_to_type(table_name).fields()))))
                    attribute = input('>>> Input name of attribute to be changed: ')
                    if attribute in string_to_type(string).fields():
                        while execution_flag:
                            new_value = input('>>> Input new value for {}: '.format(attribute))
                            if FIELD_TYPES[attribute] == int:
                                try:
                                    int(new_value)
                                except:
                                    print('Invalid type')
                                    continue
                            print('Choose attribute name: {}'.format(
                                sub(r'[)(]', '', str(string_to_type(table_name).fields())))
                            )
                            while execution_flag:
                                key_attribute = input('>>> Input key attribute to search: ')
                                if key_attribute in string_to_type(table_name).fields():
                                    key_value = input('>>> Input key value: ')
                                    if FIELD_TYPES[key_attribute] == int:
                                        try:
                                            int(key_value)
                                        except:
                                            print('Invalid type')
                                            continue
                                    self.view.update_items_view(
                                        table_name=table_name,
                                        attribute_to_change=attribute,
                                        new_value=new_value,
                                        key_attribute=key_attribute,
                                        key_value=key_value
                                    )
                                    execution_flag = False
                    else:
                        print('Invalid field name')
            else:
                print('Invalid command')

    def delete_menu(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "help" command to show this box    |\n'
        rules += '| "cancel" command to go back        |\n'
        rules += '+ ----------------------------------- +\n'
        rules += 'Chose table: User, Blog, Article, Comment'
        print(rules)
        while True:
            string = input('/delete/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string in {'User', 'Blog', 'Article', 'Comment'}:
                fields = string_to_type(string).fields()
                print('Choose field name: {}'.format(sub(r'[)(]', '', str(fields))))
                while True:
                    attribute = input('>>> Input field name: ')
                    if attribute in string_to_type(string).fields():
                        value = self.input_processing(
                            string='>>> Input value: ',
                            field_name=attribute
                        )
                        self.view.delete_item_view(
                            entity=string,
                            attribute=attribute,
                            value=value
                        )
                    elif attribute == 'cancel':
                        break
                    else:
                        print('Invalid attribute')
            else:
                print('Invalid command')

    @staticmethod
    def input_processing(string: str, field_name: str) -> str:
        while True:
            input_string = input(string)
            if FIELD_TYPES[field_name] == int:
                try:
                    int(input_string)
                except:
                    print('Invalid type')
                    continue
                return input_string
            if FIELD_TYPES[field_name] == str:
                return input_string


if __name__ == '__main__':
    MainConsole()
