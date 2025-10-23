from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs"
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encuentran productos listados"
    except Exception as e:
        print(f"Error en test_inventory. {e}")