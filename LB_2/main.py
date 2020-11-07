"""
    -> Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній     роботі №1, засобами консольного інтерфейсу.
    -> Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
    -> Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
    -> Програмний код виконати згідно шаблону MVC (модель-подання-контролер)
"""
import datetime as date
from re import sub
from mvc.controller import Controller
from mvc.view import View
from mvc.model import User, Blog, Article, Comment


class MainConsole:
    ctrl = Controller()
    view = View()

    def __init__(self):
        print('PyPSQL console 0.9(Based on Python 3.6.9+) [%(date)s]' %
                {'date': str(date.datetime.now())[:-10]})
        hello_string = '+ ------------------------------------------- +\n'
        hello_string += '| "create" commmand to create item            |\n'
        hello_string += '| "get" commmand to get item from table       |\n'
        hello_string += '| "delete" commmand to delete item from table |\n'
        hello_string += '| "quit" commmand to quit                     |\n'
        hello_string += '| "help" commmand to show this box            |\n'
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
        rules += '| "items" to search items              |\n'
        rules += '| "help" commmand to show this box    |\n'
        rules += '| "cancel" commmand to go back        |\n'
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
                    if table_name in {'User', 'Blog', 'Article', 'Comment'}:
                        self.view.table_output(table_name, self.ctrl)
                    elif table_name == 'cancel':
                        break
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
                    print(fields_name)


    def creating_commands(self):
        rules = '+ ----------------------------------- +\n'
        rules += '| "help" commmand to show this box    |\n'
        rules += '| "cancel" commmand to go back        |\n'
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
        rules += '| "help" commmand to show this box    |\n'
        rules += '| "cancel" commmand to go back        |\n'
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
