from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from time import sleep
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

class calculator_testing:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        
    def delay(self):
        self._driver.find_element(By.ID, 'delay').clear()
        self._driver.find_element(By.ID, 'delay').send_keys("45")

    def click_buttons(self):
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[1]').click()
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[4]').click()
        self._driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[2]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').click()
    
    def wait_for_result(self):
        waiter = WebDriverWait(self._driver, 60) 
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
        

    
    def close_driver(self):
        self._driver.quit()

def test_calculator():
    calculator = calculator_testing(driver)
    calculator.delay()
    calculator.click_buttons()
    sleep(60)
    assert calculator.wait_for_result() == '15'


