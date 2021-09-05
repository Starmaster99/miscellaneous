# автоматизированный гугл поиск для самых маленьких

from selenium import webdriver
from selenium.webdriver.chrome.options import Options       # !важно! перед работой устанавливаем chromewebdriver

print("Загрузка...")

chrome_options = Options()                                  # настройка запуска хрома в свёрнутом виде
chrome_options.add_argument("--headless")                   # подходит для всех версий

driver = webdriver.Chrome(options=chrome_options)           # непосредственно запуск

driver.get("https://www.google.com/")                       # переход на страницу поиска
pagetitle = driver.title                                    # получение заглавия

search = input("\nЧто будем искать?\n")                     # создаём переменную запроса
driver.get(f"https://www.google.com/search?q={search}")     # ищем информацию по запросу пользователя

div = driver.find_element_by_xpath("//div[@class='yuRUbf']")                # ищем контейнер нужных элементов
link = div.find_element_by_xpath(".//a").get_attribute("href")              # находим элемент со ссылкой
divtext = div.find_element_by_xpath(".//h3[@class='LC20lb DKV0Md']").text   # находим элемент с текстом

print(f"{divtext}\n{link}")     # выводим найденное


driver.quit()
