import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

@pytest.mark.parametrize("username,password", [
    ("satanda_user", "secret_sauce"), #Error en usuario
    ("standard_user", "Secret_sauce"), #Error en contrasseña
    ("", "secret_sauce"), #Usuario vacio
    ("standard_user", ""), #Contraseña vacia
    ])
def test_login_incorrecto(username, password):
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        mensaje = driver.find_element(By.CLASS_NAME, "error-button")

        assert mensaje.is_displayed(), "El login fallo exitosamente :D ✅"

    except Exception as e:
        print(f"No fallo el login. {e}")
        raise