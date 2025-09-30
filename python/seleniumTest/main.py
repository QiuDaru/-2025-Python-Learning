from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://tw.stock.yahoo.com/")
print("1")

"""search = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"ssb-search-input"))
)"""
search = driver.find_element(By.ID,"ssb-search-input")


search.send_keys("0050")
time.sleep(10)
search.send_keys(Keys.ENTER)
time.sleep(20)


print("抓文字")
print(driver.find_elements(By.TAG_NAME,"h3"))
#driver.quit()
