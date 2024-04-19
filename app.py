import pywhatkit
from selenium import webdriver
import os
from unidecode import unidecode

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome(options=options)

driver.get("https://google.com")

phone_number = '+5516992210406'
group = 'Hegk6ZpOcI0E3ptoCj9c40'
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 5

try:
    pywhatkit.sendwhatmsg_to_group_instantly(group, unidecode("teste"), waiting_time_to_send, close_tab,
                                             waiting_time_to_close)
except Exception as e:
    print(e)

print("Mensagem Enviada")

print("Finished!")
