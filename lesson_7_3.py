from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.CSS_SELECTOR, '#user-name')

password = driver.find_element(By.CSS_SELECTOR, '#password')

button_1 = driver.find_element(By.CSS_SELECTOR, '#login-button')

username.send_keys('standard_user')

password.send_keys('secret_sauce')

button_1.click()

button_2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')

button_3 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')

button_4 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')

korzina_link = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

button_2.click()

button_3.click()

button_4.click()

korzina_link.click()

checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')

checkout.click()

first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')

last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')

postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')

button_5 = driver.find_element(By.CSS_SELECTOR, '#continue')

first_name.send_keys('egor')

last_name.send_keys('rakov')

postal_code.send_keys('18300')

button_5.click()

total = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]')

print(total.text)

assert total.text == 'Total: $58.29'

driver.quit()

