from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))


def test(): 
    driver.get("https://www.saucedemo.com/")

    driver.implicitly_wait(4)

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys('standard_user')

    driver.find_element(By.CSS_SELECTOR, "#password").send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    driver.find_element(By.ID, 'checkout').click()

    driver.find_element(By.ID, 'first-name').send_keys('Egor')

    driver.find_element(By.ID, 'last-name').send_keys('Rakov')

    driver.find_element(By.ID, 'postal-code').send_keys('18800')

    driver.find_element(By.ID, 'continue').click()


    total = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text

    assert 'Total: $58.29' in total


   