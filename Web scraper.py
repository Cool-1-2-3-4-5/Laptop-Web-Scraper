from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://www.bestbuy.ca/en-ca")

time.sleep(3)
enter = driver.find_element("name", "search")
enter.send_keys("Laptops")
enter.send_keys(Keys.RETURN)
time.sleep(15)
# OperSys = driver.find_element(By.CLASS_NAME, "productName_3Ikre")
# OperSys.click()

RAMcross = driver.find_element(By.CLASS_NAME, "style-module_icon__L3Rjc")
RAMcross.click()
RAMw = driver.find_element(By.ID, "facetFilter-RAM(GB)_16")
driver.execute_script("arguments[0].scrollIntoView(true);", RAMw)
time.sleep(0.5)
RAMcross = driver.find_element(By.CLASS_NAME, "style-module_darkGrey__ailJw -mt-[2px] style-module_icon__JRetG")
RAMcross.click()
RAMw.click()


# OperSyss = driver.find_element(By.ID, "facetFilter-OperatingSystem_Windows11Pro")
# OperSyss.click()
# OperSyss = driver.find_element(By.ID, "facetFilter-OperatingSystem_Windows11Home")
# OperSyss.click()
time.sleep(20)