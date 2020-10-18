# Реалізувати функції внесення, редагування та вилучення даних у таблицях бази даних, створених у лабораторній роботі №1, засобами консольного інтерфейсу.
# Передбачити автоматичне пакетне генерування «рандомізованих» даних у базі.
# Забезпечити реалізацію пошуку за декількома атрибутами з двох та більше сутностей одночасно: для числових атрибутів – у рамках діапазону, для рядкових – як шаблон функції LIKE оператора SELECT SQL, для логічного типу – значення True/False, для дат – у рамках діапазону дат.
# Програмний код виконати згідно шаблону MVC (модель-подання-контролер)

import datetime as date 
import psycopg2


if __name__ == '__main__':

    # TODO: функції внесення, редагування та вилучення даних

    print('PyPSQL console 0.9(Based on Python 3.6.9+) [{}]'.format(date.datetime.now()))
    try:
        connection = psycopg2.connect(
            database="lab_1", 
            user="ivan",
            password="0000", 
            host="localhost", 
            port=5432
        )
        flag = True
    except Exception as ex:
        connection = None
        flag = False
    print('Connecting to DB:', ('SUCCESS' if flag else 'FAILED'))

    while flag:
        command = input('>>> ')
        if command == 'quit()':
            connection.close()
            break

