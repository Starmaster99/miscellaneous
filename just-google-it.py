# web scrapping (автоматизированное гугление и не только) для самых маленьких

from googlesearch import search

query = input('Что будем гуглить? ').strip()
num = int(input('Сколько будем гуглить? ').strip())


for i in search(query, tld='com', lang='ru', stop=num):
    print(i)
