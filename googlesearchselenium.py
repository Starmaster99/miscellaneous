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
driver.get(f"https://www.google.com/search?q={search}")     # ищём информацию запрос пользователя
ans = driver.find_element_by_class_name("yuRUbf").text      # получаем текст и адрес первой ссылки
print(ans)                                                  # выводим его


driver.quit()
