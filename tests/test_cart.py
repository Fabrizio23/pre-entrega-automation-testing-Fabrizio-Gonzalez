from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from utils.logger import logger
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario, password)
        inventory_page = InventoryPage(driver)
        inventory_page.agregar_primer_producto()
        inventory_page.abrir_carrito()
        cartPage = CartPage(driver)
        productos_en_carrito = cartPage.obtener_productos_carrito()
        logger.info(f"Productos en el carrito: {productos_en_carrito}")      
        assert len(productos_en_carrito) == 1, "El producto no se agregó al carrito"
    except Exception as e:
        logger.error(f"Error en test_cart: {e}")
        print(f"Error en test_cart: {e}")
        raise