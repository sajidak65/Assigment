import time
from asyncio import wait_for

import dec
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v141.cache_storage import CachedResponseType
from selenium.webdriver.common.keys import By
from numpy.f2py.rules import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from websocket import send

driver = webdriver.Chrome()
driver.get("https://ginandjuice.shop")

description_text = '/html/body/div[2]/section/div/section/div[2]/span[2]/p[1]'
ViewPro = '/html/body/div[2]/section/div/section[3]/a[1]/span[2]'
AllPro = '/html/body/div[2]/section/section/a'
d2_description='/html/body/div[2]/section/div/section/div[2]/span[2]/p[2]'
check_stock='//*[@id="stockCheckForm"]/button'

# Wait up to 10 seconds until the Login button is clickable
wait = WebDriverWait(driver, 10)
# Open a specific product page
driver.get("https://ginandjuice.shop/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)")

# Wait for description text and read it
# Wait for the description paragraph to appear and get its text
#open a view button

Element1 = wait.until(EC.visibility_of_element_located((By.XPATH, AllPro)))
Element1.click()
Element = wait.until(EC.visibility_of_element_located((By.XPATH, ViewPro)))
Element.click()
Add to CachedResponseType. wait.untill(//*[@id="addToCartForm"]/button)


d1 = "Originally a limited edition prototype, but back by popular demand, and now premixed with premium fruit juice, Pineapple Edition Gin is sure to rock your world. What doesn't taste better with a little pineapple added? Pizza? We'll let you fight that one out for yourselves. We think the gin is pretty good though."


desCheck = driver.find_element(By.XPATH,description_text).text
print(desCheck)
assert desCheck == d1
print("PASSED")
#open a view description
d2='250ML | 12 PACK | 8% ABV'
desccheck2 = driver.find_element(By.XPATH,d2_description).text
print(desccheck2)
assert desccheck2 == d2
print("PASSED")

chst = wait.until(EC.visibility_of_element_located((By.XPATH, check_stock)))
chst.click()



driver.quit()






