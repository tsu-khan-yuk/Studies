import datetime as date
from re import sub
from mvc.controller import Controller
from mvc.view import View
from mvc.model import User, Blog, Article, Comment, FIELD_TYPES


class MainConsole:
    ctrl = Controller()
    view = View()

    def __init__(self):
        print('PyPSQL console 0.9(Based on Python 3.6.9+) [%(date)s]' %
                {'date': str(date.datetime.now())[:-10]})
        hello_string = '+ ------------------------------------------- +\n'
        hello_string += '| "create" command to create item             |\n'
        hello_string += '| "get" command to get item from table        |\n'
        hello_string += '| "delete" command to delete item from table  |\n'
        hello_string += '| "quit" command to quit                      |\n'
        hello_string += '| "help" command to show this box             |\n'
        hello_string += '+ ------------------------------------------- +'
        print(hello_string)
        while True:
            input_string = input('/ >>> ')
            if input_string == 'quit':
                break
            elif input_string == 'help':
                print(hello_string)
            elif input_string in {'create', 'delete', 'get'}:
                self.command_manager(input_string)
            else:
                print('SyntaxError: Invalid command')

    def command_manager(self, cmd_name: str):
        if cmd_name == 'create':
            self.creating_commands()
        elif cmd_name == 'get':
            self.getter_commands()
        elif cmd_name == 'delete':
            self.deleting_commands()

    def getter_commands(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "table" to see table                |\n'
        rules += '| "items" to search items             |\n'
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
                        self.view.table_view(table_name, self.ctrl)
                    else:
                        print('Invalid table_name')
            elif string == 'items':
                print('Choose fields: user_id, blog_id, article_id, comment_id,\n'
                        '\ttext, description, name, e-mail')
                while True:
                    fields_name = input('/get/fields/ >>> ')
                    if fields_name == 'cancel':
                        break
                    fields_name = sub(',', ' ', fields_name).split()

                    invalid_name = False
                    for field in fields_name:
                        if not field in FIELD_TYPES.keys():
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
                                    left_limit = int(input('/get/fields({})/ >>> Input left limit: '.format(field)))
                                    right_limit = int(input('/get/fields({})/ >>> Input right limit: '.format(field)))
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

                    self.view.items_view(fields_name, conditions, self.ctrl)
            else:
                print('Invalid command')

    def creating_commands(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "help" command to show this box    |\n'
        rules += '| "cancel" command to go back        |\n'
        rules += '+ ----------------------------------- +\n'
        rules += 'Chose table: User, Blog, Article, Comment'
        print(rules)
        while True:
            string = input('/create/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string in {'User', 'Blog', 'Article', 'Comment'}:
                self.ctrl.insert_item(string, '')

    def deleting_commands(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "item" to search items              |\n'
        rules += '| "help" command to show this box    |\n'
        rules += '| "cancel" command to go back        |\n'
        rules += '+ ----------------------------------- +'
        rules += 'Chose table: User, Blog, Article, Comment'
        print(rules)
        while True:
            string = input('/delete/ >>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string in {'User', 'Blog', 'Article', 'Comment'}:
                pass


if __name__ == '__main__':
    MainConsole()
