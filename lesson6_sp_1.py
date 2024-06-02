from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")

button.click()

content = driver.find_element(By.CSS_SELECTOR, '#content')

text = content.find_element(By.CSS_SELECTOR, '[class="bg-success"]').text

print(text)