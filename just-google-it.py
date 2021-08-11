# web scrapping (автоматизированное гугление и не только) для самых маленьких

from googlesearch import search

query = input('Что будем гуглить? ').strip()

try:
    n = int(input('Сколько будем гуглить? ').strip())
except ValueError:
    print('Ошибка! Введите целое положительное число!')
    n = 0

for i in search(query, tld='com', lang='ru', num=n, stop=n):
    print(i)
