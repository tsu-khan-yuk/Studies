"""
    -> Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній     роботі №1, засобами консольного інтерфейсу.
    -> Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
    -> Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
    -> Програмний код виконати згідно шаблону MVC (модель-подання-контролер)
"""
import datetime as date 
from mvc.controller import Controller
from mvc.model import User, Blog, Article, Comment



print('PyPSQL console 0.9(Based on Python 3.6.9+) [%(date)s]' % {'date': str(date.datetime.now())[:-10]})

var = Controller()
buf = var.get_all_table_items(table_name='User')
for i in buf:
    print(i)
