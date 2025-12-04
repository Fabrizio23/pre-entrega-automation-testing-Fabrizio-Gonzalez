from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver, usuario, password):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario, password)
        inventory_page = InventoryPage(driver)
        logger.info("Verificando elementos en la página de inventario")
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario está vacío"
        logger.info("Verificando el conteo del carrito")
        assert inventory_page.obtener_conteo_carrito() == 0
        inventory_page.agregar_primer_producto()
        logger.info("Verificando el conteo del carrito después de agregar un producto")
        assert inventory_page.obtener_conteo_carrito() == 1
    except Exception as e:
        logger.error(f"Error en test_inventory: {e}")
        print(f"Error en test_inventory: {e}")
        raise