from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.lector_json import leer_json_productos
import time
from utils.logger import logger

RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver, usuario, password, nombre_producto):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario, password)
        
        inventory_page = InventoryPage(driver)
        inventory_page.agregar_producto_por_nombre(nombre_producto)
        inventory_page.abrir_carrito()

        time.sleep(1)

        cartPage = CartPage(driver)

        logger.info(f"Verificando que el producto {nombre_producto} esté en el carrito")
        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto, \
            f"El producto {nombre_producto} no coincide con el del carrito"
        
    except Exception as e:
        print(f"Error en test_cart_json: {e}")
        raise
    finally:
        driver.quit()