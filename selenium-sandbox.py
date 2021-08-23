# selenium для самых маленьких

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.cnet.com/tech/computing/")
print(driver.title)

asset = driver.find_elements_by_class_name("o-linkOverlay")


for asset_link in asset:
    links = asset_link.get_attribute('href')
    print(links)
    # link = links.split("/")[-2]           # опционально. будет выводиться конец ссылки по типу
    # print(link)                           # best-laptop

driver.quit()
