from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

delay = driver.find_element(By.CSS_SELECTOR, '#delay')

delay.clear()

delay.send_keys('45')

seven = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)')

plus = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)')

eight = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)')

equals = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning')

screen = driver.find_element(By.CSS_SELECTOR, '[class = screen]')

seven.click()

plus.click()

eight.click()

equals.click()

sleep(45)

assert screen.text == '15'

driver.quit