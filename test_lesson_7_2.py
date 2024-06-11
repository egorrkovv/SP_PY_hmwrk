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


def test(): 
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(4)
        

    driver.find_element(By.ID, 'delay').clear()
    driver.find_element(By.ID, 'delay').send_keys("45")

    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning').click()
    driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').click()
    
    result = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), "15"))
    
    result_text = driver.find_element(By.CLASS_NAME, 'screen').text

    assert result_text == "15"
        

    driver.quit()



