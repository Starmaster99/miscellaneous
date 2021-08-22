# selenium для самых маленьких
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # для печатания

driver = webdriver.Chrome()

driver.get("https://www.reddit.com/")
print(driver.title)

search = driver.find_element_by_id("header-search-bar")
search.send_keys("r/cats")
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
