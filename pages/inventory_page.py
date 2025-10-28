from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import login_page

class InventoryPage:
    _MENU_HAMBURGUESA = (By.ID, "react-burger-menu-btn")
    _CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")
    _ADD_TO_CART= (By.ID, "add-to-cart-sauce-labs-backpack")
    _REMOVE_FROM_CART = (By.ID, "remove-sauce-labs-backpack")
    _CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def agregar_producto_al_carrito(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._ADD_TO_CART)).click()
        return self
    
    def obtener_conteo_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._CONTADOR_CARRITO))
            print("✅ Mensaje de error detectado correctamente")
            return True
        except:
            print("❌ No se detectó mensaje de error")
            return False

    def eliminar_producto_del_carrito(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._REMOVE_FROM_CART)).click()
        return self
    
    def menu_hamburguesa(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._MENU_HAMBURGUESA)).click()
        return self
    
    def filtro(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._FILTRO)).click()
        return self
    
    def carrito(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._CARRITO)).click()
        return self