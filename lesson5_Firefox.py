from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/add_remove_elements/')



for i in range(5):
    add_element2 = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    add_element2.click()

#print(len[driver.find_elements(By.CSS_SELECTOR, "button.added_manually")])

driver.get('http://uitestingplayground.com/dynamicid')
for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    blue_button.click()

#driver.get('http://uitestingplayground.com/classattr')
#for i in range(3):
#    blue_button2 = driver.find_element(By.CSS_SELECTOR, '[class="btn class2 btn-primary btn-test"]')
#    blue_button2.click()

#driver.get('https://the-internet.herokuapp.com/entry_ad')

#close_button = driver.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')
#close_button.click()

driver.get('https://the-internet.herokuapp.com/inputs')

input = driver.find_element(By.CSS_SELECTOR, 'input')
input.click()
input.send_keys("1000")
input.send_keys(Keys.BACKSPACE)
input.send_keys(Keys.BACKSPACE)
input.send_keys(Keys.BACKSPACE)
input.send_keys(Keys.BACKSPACE)
input.send_keys("999")

driver.get('https://the-internet.herokuapp.com/login')

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys('SuperSecretPassword!')
login = driver.find_element(By.CSS_SELECTOR, "button")
login.click()


sleep(10)