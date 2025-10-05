import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="function")
def driver():
    """Setup and close webdriver"""
    firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    geckodriver_path = r"D:\Fatima\Learn\Testing\Selenium\Setup\geckodriver.exe"
    options = Options()
    options.binary_location = firefox_binary_path
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def standard_user_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture(scope="function")
def locked_user_credentials():
    return {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }
@pytest.fixture(scope="function")
def invalid_user_credentials():
    return {
        "username": "user",
        "password": "sauce"
    }
