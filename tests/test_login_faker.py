import pytest 
from pages.login_page import LoginPage
from faker import Faker
from utils.logger import logger

fake = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar",[
    (fake.user_name(), fake.password(), False),
    (fake.user_name(), fake.password(), False),
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    driver = login_in_driver

    login_page = LoginPage(driver)

    login_page.login_completo(usuario, password)

    if debe_funcionar:
        logger.info(f"Login exitoso con usuario: {usuario}")
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        mensaje_error = login_page.obtener_error()
        logger.info(f"Login fallido con usuario: {usuario}, mensaje de error: {mensaje_error}")
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando"