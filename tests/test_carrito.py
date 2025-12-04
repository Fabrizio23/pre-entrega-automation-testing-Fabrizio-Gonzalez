import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from utils.logger import logger
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_carrito(login_in_driver, usuario, password):
    driver = login_in_driver
    LoginPage(driver).login_completo(usuario, password)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logger.info("Producto agregado al carrito")
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").is_displayed()