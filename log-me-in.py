# логирование и классы для самых маленьких
# TODO: засовывать логи в файл

# минутка теории
# DEBUG: логи с информацией для отладки программы
# INFO: логи с информацией о том, что всё работает нормально
# WARNING: логи с информацией о том, что случилось что-то необычное, но всё работает нормально
# ERROR: из-за какой-то проблемы программа не смогла работать
# CRITICAL: из-за какой-то *очень* серьёзной проблемы программа больше не может работать

import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(lineno)s line ::: %(message)s')

a = int(input('Первое число: '))
b = int(input('Второе число: '))
logging.info(f'First number is {a}')
logging.info(f'Second number is {b}')


class Simplemath:           # и тут у нас появляется класс
    def __init__(self):     # а тут мы его инициализируем для использования
        self.a = a          # функциями ниже
        self.b = b
        logging.info('Successful class init')

    def add(self, a, b):
        plus = a + b
        logging.info(f'Add ans:{plus}')
        return plus

    def subs(self, a, b):
        minus = a - b
        logging.info(f'Substraction ans:{minus}')
        return minus

    def mult(self, a, b):
        mul = a * b
        logging.info(f'Multiplying ans:{mul}')
        return mul

    def div(self, a, b):
        divis = a / b
        logging.info(f'Division ans:{divis}')
        return divis


_a = Simplemath()                   # насколько я понял, _ возле переменной это просьба её не иcпользовать
print(_a.mult(a, b), _a.add(a, b))  # а сюда можно вписать любые методы. классы прекрасны 😀
