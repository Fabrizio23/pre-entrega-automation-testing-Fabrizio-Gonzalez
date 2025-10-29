from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

def test_login(login_in_driver):
    try:
        driver = login_in_driver
        assert "/inventory.html" in driver.current_url, "Login exitoso"
    except Exception as e:
        print(f"Error en login. {e}")
        raise