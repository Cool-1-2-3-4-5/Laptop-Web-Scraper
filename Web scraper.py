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
RAMcross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[9]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", RAMcross)
driver.execute_script("arguments[0].click();", RAMcross)
RAMw = driver.find_element(By.ID, "facetFilter-RAM(GB)_16")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", RAMw)
time.sleep(1)

OperSysCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[14]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", OperSysCross)
driver.execute_script("arguments[0].click();", OperSysCross)
time.sleep(0.5)
OperSys1 = driver.find_element(By.ID, "facetFilter-OperatingSystem_Windows11Pro")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", OperSys1)
time.sleep(10)
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", OperSysCross)
OperSys2 = driver.find_element(By.ID, "facetFilter-OperatingSystem_Windows11Home")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", OperSys2)
time.sleep(1)

StorageCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[12]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", StorageCross)
driver.execute_script("arguments[0].click();", StorageCross)
time.sleep(0.5)
Storage = driver.find_element(By.ID, "facetFilter-TotalHardDriveCapacity_256GB-511.9GB")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", Storage)
time.sleep(1)

BatteryCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[27]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", BatteryCross)
driver.execute_script("arguments[0].click();", BatteryCross)
time.sleep(0.5)
Battery = driver.find_element(By.ID, "facetFilter-BatteryLife_9to12Hours")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", Battery)
time.sleep(1)

StateCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[4]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", StateCross)
driver.execute_script("arguments[0].click();", StateCross)
time.sleep(0.5)
state = driver.find_element(By.ID, "facetFilter-ProductCondition_BrandNew")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", state)
time.sleep(20)

print("Good")
