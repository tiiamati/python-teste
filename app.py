from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service

print("GOOGLE_CHROME_BIN>>>>>>")
print(os.environ.get("GOOGLE_CHROME_BIN"))
print("CHROMEDRIVER_PATH>>>>>>")
print(os.environ.get("CHROMEDRIVER_PATH"))

service = Service(executable_path='./chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://medium.com")

print(driver.page_source)
print("Finished!")
