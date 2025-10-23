from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_page:

    URL = "https://www.saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    #Agregar cartel de error para login erroneo

    def __init__(self, driver):
        driver = self.driver
        self.wait = WebDriverWait(driver, 5)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def completar_user(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def completar_pass(self, password):
        input = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        input.clear()
        input.send_keys(password)
        return self
    
    def click_login(self):
        boton = self.wait.until(EC.element_to_be_clickable(*self._LOGIN_BUTTON)).click()
        return self
    
    def login_completo(self, usuario, password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.click_login()
        return self

#Agregar funcion para login erroneo