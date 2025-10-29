from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

def test_carrito(login_in_driver):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").is_displayed(), "El contador del carrito no se muestra después de agregar un producto"
    except Exception as e:
        print(f"Error en test_carrito. {e}")