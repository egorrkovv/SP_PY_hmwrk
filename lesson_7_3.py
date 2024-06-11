from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

class shoptesting1:
    def __init__(self, driver): 
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        self._driver = driver

        self._driver.get("https://www.saucedemo.com/")

        self._driver.implicitly_wait(4)

    def authorize(self, name, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)

        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
class shoptesting2:

    def __init__(self, driver): 
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self._driver = driver

        self._driver.implicitly_wait(4)

    def add_clothes_and_click_shopping_cart(self):
        self._driver = driver

        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    def checkout (self):
        self._driver.find_element(By.ID, 'checkout').click()

    def information(self, first_name, last_name, postal_code):
        self._driver.find_element(By.ID, 'first-name').send_keys(first_name)

        self._driver.find_element(By.ID, 'last-name').send_keys(last_name)

        self._driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

        self._driver.find_element(By.ID, 'continue').click()
    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        print(total)


   