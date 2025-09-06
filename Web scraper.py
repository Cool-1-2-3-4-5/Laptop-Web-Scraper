#Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from google.oauth2.service_account import Credentials
import gspread

# Define the scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# JSON key file
SERVICE_ACCOUNT_FILE = r"c:\Users\elilt\OneDrive\Desktop\Projects\laptop-web-scraper-data-0cc293608455.json"

# Client
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=scope
)
gc = gspread.authorize(creds)

# Chrome driver setup
PATH = r"C:\Users\elilt\OneDrive\Desktop\Projects\Laptop-Web-Scraper\chromedriver-win64\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://www.bestbuy.ca/en-ca/search?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253ALaptops%2B%2526%2BMacBooks%253Bcustom0productcondition%253ABrand%2BNew%253Bcustom0ramsize%253A16%253Bcustom0harddrivecapacity%253A256%2BGB%2B-%2B511.9%2BGB%253Bcomputersoperatingsystem0enrchstring%253AWindows%2B11%2BHome%257CWindows%2B11%2BPro%253Blaptopbatterylife0enrchrange%253A9%2Bto%2B12%2BHours&search=Laptops")

# Filtering

time.sleep(3) # Delay to allow page to load
enter = driver.find_element("name", "search")
enter.send_keys("Laptops")
enter.send_keys(Keys.RETURN)
time.sleep(15) # Delay

# RAM
RAMcross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[9]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", RAMcross)
driver.execute_script("arguments[0].click();", RAMcross)
RAMw = driver.find_element(By.ID, "facetFilter-RAM(GB)_16")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", RAMw)
time.sleep(1)

# Operating System
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

# Storage
StorageCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[12]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", StorageCross)
driver.execute_script("arguments[0].click();", StorageCross)
time.sleep(0.5)
Storage = driver.find_element(By.ID, "facetFilter-TotalHardDriveCapacity_256GB-511.9GB")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", Storage)
time.sleep(1)

# Battery Life
BatteryCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[27]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", BatteryCross)
driver.execute_script("arguments[0].click();", BatteryCross)
time.sleep(0.5)
Battery = driver.find_element(By.ID, "facetFilter-BatteryLife_9to12Hours")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", Battery)
time.sleep(1)

# Condition
StateCross = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div[4]/button")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", StateCross)
driver.execute_script("arguments[0].click();", StateCross)
time.sleep(0.5)
state = driver.find_element(By.ID, "facetFilter-ProductCondition_BrandNew")
time.sleep(0.5)
driver.execute_script("arguments[0].click();", state)
time.sleep(6)


# Web Scraping
LaptopNamesRaw = driver.find_elements(By.CLASS_NAME, "productItemName_3IZ3c")
PricesRaw = driver.find_elements(By.CSS_SELECTOR, ".style-module_screenReaderOnly__4QmbS.style-module_large__g5jIz")
SavingRaw = driver.find_elements(By.CSS_SELECTOR, ".style-module_productSaving__g7g1G.style-module_right__Dvbyx")
# ReviewsRaw = driver.find_elements(By.CSS_SELECTOR, 'span[data-automation="rating-count"]')
LaptopNames = []
Prices = []
Savings = []
TruePrices = []
Reviews = []

# Data Processing
for num in range(0,len(LaptopNamesRaw)):
    LaptopNames.append(LaptopNamesRaw[num].text)
    Prices.append(PricesRaw[num].text)
    x = float(PricesRaw[num].text.replace("$",""))
    Savings.append(SavingRaw[num].text)
    SavingRawRand = SavingRaw[0].text.split(" ")
    y = float(SavingRawRand[1].replace("$",""))
    TruePrices.append(x+y)
    # Reviews.append(Reviews[num].text)

# Updating google sheets
spreadsheet = gc.open("Web Scraper").sheet1
spreadsheet.update_cell(1,1, "Laptop Names")
spreadsheet.update_cell(1,2, "Price")
spreadsheet.update_cell(1,3, "Savings")
spreadsheet.update_cell(1,4, "Original Value")
for i in range(len(LaptopNames)):
    spreadsheet.update_cell(i+2, 1, LaptopNames[i])
    spreadsheet.update_cell(i+2, 2, Prices[i])
    spreadsheet.update_cell(i+2, 3, Savings[i])
    spreadsheet.update_cell(i+2, 4, "$" + str(TruePrices[i]))