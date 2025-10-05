# pages/login_page.py

from selenium.webdriver.common.by import By
from ..pages.base import BasePage
from typing import Dict
from ..pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    locked_error_message=(By.XPATH, "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]")
    invalid_error_message=(By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match any user in this service')]")
    required_error_message=(By.XPATH, "//h3[contains(text(),'Epic sadface: Username is required')]")


    def navigate_to_login(self):
        self.driver.get(self.base_url)

    def login(self, user_creds) -> 'InventoryPage':

        self.enter_text(self.USERNAME_FIELD, user_creds["username"])
        self.enter_text(self.PASSWORD_FIELD, user_creds["password"])
        self.click(self.LOGIN_BUTTON)
        return InventoryPage(self.driver)

    def locked_login(self, user_creds)-> bool:
        self.enter_text(self.USERNAME_FIELD, user_creds["username"])
        self.enter_text(self.PASSWORD_FIELD, user_creds["password"])
        self.click(self.LOGIN_BUTTON)
        return self.is_visible(self.locked_error_message)

    def invalid_login(self, user_creds)-> bool:
        self.enter_text(self.USERNAME_FIELD, user_creds["username"])
        self.enter_text(self.PASSWORD_FIELD, user_creds["password"])
        self.click(self.LOGIN_BUTTON)
        return self.is_visible(self.invalid_error_message)

    def required_missed(self)->bool:
        self.click(self.LOGIN_BUTTON)
        return self.is_visible(self.required_error_message)
