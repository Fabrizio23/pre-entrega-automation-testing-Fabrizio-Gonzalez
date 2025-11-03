from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login(login_in_driver, usuario, password, debe_funcionar):
    driver = login_in_driver
    print("Debe funcionar")
    if bool(debe_funcionar) == True:
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    elif bool(debe_funcionar) == False:
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, f"No se mostró el mensaje esperado. Se obtuvo: {mensaje_error}"