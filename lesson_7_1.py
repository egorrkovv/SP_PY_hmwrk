from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(4)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')

first_name.send_keys('Иван')

last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')

last_name.send_keys('Петров')

address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')

address.send_keys('Ленина, 55-3')

city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')

city.send_keys('Москва')

country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')

country.send_keys('Россия')

email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')

email.send_keys('test@skypro.com')

phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')

phone.send_keys('+7985899998787')

jobposition = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')

jobposition.send_keys('QA')

company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')

company.send_keys('test@skypro.com')

submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

submit.click()

company = driver.find_element(By.CSS_SELECTOR, '[id="company"]')

phone = driver.find_element(By.CSS_SELECTOR, '[id="phone"]')

email = driver.find_element(By.CSS_SELECTOR, '[id="e-mail"]')

country = driver.find_element(By.CSS_SELECTOR, '[id="country"]')

city = driver.find_element(By.CSS_SELECTOR, '[id="city"]')

address = driver.find_element(By.CSS_SELECTOR, '[id="address"]')

last_name = driver.find_element(By.CSS_SELECTOR, '[id="last-name"]')

first_name = driver.find_element(By.CSS_SELECTOR, '[id="first-name"]')

ZipCode = driver.find_element(By.CSS_SELECTOR, '[id="zip-code"]')

jobposition = driver.find_element(By.CSS_SELECTOR, '[id="job-position"]')

assert 'rgba(132, 32, 41, 1)' in ZipCode.value_of_css_property("color")

assert 'rgba(15, 81, 50, 1)' in jobposition.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in first_name.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in last_name.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in address.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in city.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in country.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in email.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in phone.value_of_css_property('color')

assert 'rgba(15, 81, 50, 1)' in company.value_of_css_property('color')