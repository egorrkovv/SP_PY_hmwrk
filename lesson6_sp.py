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

driver.get('http://uitestingplayground.com/textinput')

askme = driver.find_element(By.CSS_SELECTOR, "input")

askme.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')

button.click()

textbutton = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(textbutton)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

third_pic = driver.find_element(By.CSS_SELECTOR, '[alt="calendar"]')

src = third_pic.get_attribute('src')

print(src)


driver.quit()