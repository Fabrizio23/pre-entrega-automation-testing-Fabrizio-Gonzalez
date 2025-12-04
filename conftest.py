import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import pathlib
from datetime import datetime

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def encabezado():
    return {"x-api-key": "reqres-free-v1"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield

    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver",None)

        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = target / f"{report.when}_{item.name}_{timestamp}.png"
            driver.save_screenshot(str(file_name))