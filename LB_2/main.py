"""
    -> Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній     роботі №1, засобами консольного інтерфейсу.
    -> Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
    -> Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
    -> Програмний код виконати згідно шаблону MVC (модель-подання-контролер)
"""
from mvc.local import db_settings
import datetime as date 
import psycopg2 as psql


print('PyPSQL console 0.9(Based on Python 3.6.9+) [%(date)s]' % {'date': str(date.datetime.now())[:-10]})
# try:
#     connection = psql.connect(
#         database=db_settings['database'], 
#         user=db_settings['user'],
#         password=db_settings['password'], 
#         host=db_settings['host'],   
#         port=db_settings['port']
#     )
#     flag = True
# except Exception as ex:
#     connection = None
#     flag = False
# print('Connecting to DB: %(status)s' % {'status': 'SUCCESS' if flag else 'FAILED'})

from mvc.controller import Controller
from mvc.model import User, Blog, Article, Comment

var = Controller()
var.show_item(
    table='User',
    field='user_id',
    condition='"user_id" = 2'
)
