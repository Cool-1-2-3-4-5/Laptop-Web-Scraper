from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://www.bestbuy.ca/en-ca")

time.sleep(3)
enter = driver.find_element("name", "search")
enter.send_keys("Engineering Laptops")
enter.send_keys(Keys.RETURN)
time.sleep(10)
