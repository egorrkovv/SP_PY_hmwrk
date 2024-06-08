from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
class forma_testing:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def fields(self, name, last, address, email, phone, city, country, job, company):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "first-name"]').send_keys(name)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys(last)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys(address)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys(email)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys(phone)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys(city)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys(country)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys(job)

        self._driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys(company)

        submit = self._driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")

        submit.click()


    def zip_code(self):        
        zip_code = self._driver.find_element(By.CSS_SELECTOR, 'div[id="zip-code"]').value_of_css_property("color")
        return zip_code

    def all_fields(self):  
        all_fields = ["#first-name, #last-name, #address, #e-mail, #phone, #city, #country, #job-position, #company"]
        for field in all_fields:
            color = self._driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("color")
            return color

def test_fields():
    testing = forma_testing(driver)

    testing.fields("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    
    assert testing.zip_code() == 'rgba(132, 32, 41, 1)' 
    
    assert testing.all_fields() == 'rgba(15, 81, 50, 1)' 

    driver.quit()