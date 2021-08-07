# логирование и классы для самых маленьких

# минутка теории
# DEBUG: логи с информацией для отладки программы
# INFO: логи с информацией о том, что всё работает нормально
# WARNING: логи с информацией о том, что случилось что-то необычное, но всё работает нормально
# ERROR: из-за какой-то проблемы программа не смогла работать
# CRITICAL: из-за какой-то *очень* серьёзной проблемы программа больше не может работать

import logging

logging.basicConfig(level=logging.DEBUG)

a = int(input('Первое число: '))
b = int(input('Второе число: '))
logging.info(f'16:First number is {a}')
logging.info(f'17:Second number is {b}')


class Simplemath:           # и тут у нас появляется класс
    def __init__(self):     # а тут мы его инициализируем для использования
        self.a = a          # функциями ниже
        self.b = b
        logging.info('24:Successful class init')

    def add(self, a, b):
        plus = a + b
        logging.info(f'28:Add ans:{plus}')
        return plus

    def subs(self, a, b):
        minus = a - b
        logging.info(f'32:Substraction ans:{minus}')
        return minus

    def mult(self, a, b):
        mul = a * b
        logging.info(f'38:Multiplying ans:{mul}')
        return mul

    def div(self, a, b):
        divis = a / b
        logging.info(f'43:Division ans:{divis}')
        return divis


_a = Simplemath()                   # насколько я понял, _ возле переменной это просьба её не иcпользовать
print(_a.mult(a, b), _a.add(a, b))  # а сюда можно вписать любые методы. классы прекрасны 😀
