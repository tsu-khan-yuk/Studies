"""
    -> Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній     роботі №1, засобами консольного інтерфейсу.
    -> Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
    -> Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
    -> Програмний код виконати згідно шаблону MVC (модель-подання-контролер)
"""
import datetime as date
from mvc.controller import Controller
from mvc.model import User, Blog, Article, Comment


class MainConsole:
    """
    Commands:
        CRATE model:
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

    def __init__(self):
        print('PyPSQL console 0.9(Based on Python 3.6.9+) [%(date)s]' % {'date': str(date.datetime.now())[:-10]})
        while True:
            input_string = input('>>> ')
            if input_string == 'quit':
                break
            self.command_manager(input_string)

    def command_manager(self, cmd_name: str):
        cmd_name = cmd_name.split()
        print(cmd_name)
        if cmd_name[0] == 'show':
            self.table_getter(cmd_name[1])

    def table_getter(self, table_name: str):
        for i in self.ctrl.get_all_table_items(table_name):
            print(i)


if __name__ == '__main__':
    MainConsole()
