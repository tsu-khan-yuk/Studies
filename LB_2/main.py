"""
    -> Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній     роботі №1, засобами консольного інтерфейсу.
    -> Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
    -> Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
    -> Програмний код виконати згідно шаблону MVC (модель-подання-контролер)
"""
import datetime as date
from mvc.controller import Controller
from mvc.view import View
from mvc.model import User, Blog, Article, Comment


class MainConsole:
    """
    Commands:
        CREATE model:
            'create User(id, name, mail)',
            'create Blog(id, name, description, user_id)',
            'create Article(id, name, text, blog_id)',
            'create Comment(id, text, article_id)'
        GET model:
            'show User table',
            ...
        DELETE model:
    """
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
            input_string = input('>>> ')
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
        rules += '| "item" to search items              |\n'
        rules += '| "help" commmand to show this box    |\n'
        rules += '| "cancel" commmand to go back        |\n'
        rules += '+ ----------------------------------- +'
        print(rules)
        while True:
            string = input('>>> ')
            if string == 'cancel':
                return
            elif string == 'help':
                print(rules)
            elif string == 'table':
                print('Chose table: User, Blog, Article, Comment')
                while True:
                    
                    self.view.table_output(self.ctrl.get_all_table_items())

    def creating_commands(self):
        pass

    def deleting_commands(self):
        pass


if __name__ == '__main__':
    MainConsole()
