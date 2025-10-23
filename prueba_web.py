from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    #login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url
    print("El URL es correcto ✅")
except AssertionError:
    print("El URL es incorrecto ❌")

    #Corroborar titulo
try:
    assert driver.title == "Swag Labs"
    print("Swag Labs es el titulo ✅")
except AssertionError:
    print("Titulo incorrecto ❌")

#Corroborar elementos en pagina
try:
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
    print("Se muestra el carrito de compras ✅")
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    print("Se muestra el filtro de productos ✅")
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    print("Se muestra el menu de hamburguesa ✅")
except AssertionError:
    print("No se muestran todos los elementos de la pagina ❌")

    #Corroborar que haya productos en lista
try:
    assert driver.find_elements(By.CLASS_NAME, "inventory_list")
    print("Se muestran productos en el inventario ✅")
except AssertionError:
    print("No se muestran productos en el inventario ❌")

    #Sumar elemento a carrito
try:
    productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"
    print("Se sumo correctamente el producto ✅")
except AssertionError:
    print("No se pudo sumar el producto al carrito ❌")

#Comprobacion de producto en carrito
try:
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    productos.find_element(By.CLASS_NAME, "inventory_item").is_displayed()
    print("Se encuentra el producto en el carrito ✅")
except AssertionError:
    print("No se encuentra el producto en el carrito ❌")
    #REVISAR ESTE ULTIMO ASSERT

finally:
    driver.quit()