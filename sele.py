from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.ENTER)

driver.close()