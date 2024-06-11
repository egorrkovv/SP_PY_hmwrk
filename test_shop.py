from lesson_7_3 import shoptesting1
from lesson_7_3 import shoptesting2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_buy():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shoptesting1(driver).authorize("standard_user", "secret_sauce")
    shoptesting2.add_clothes_and_click_shopping_cart("self")
    shoptesting2.checkout()
    shoptesting2.information("Egor", "Rakov", "123456")
    total = shoptesting2.total()
    assert total == "Total: $58.29"
    
    driver.quit()