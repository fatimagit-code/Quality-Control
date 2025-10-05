from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def enter_text(self, by_locator, text):
        self.find_element(by_locator).send_keys(text)

    def click(self, by_locator):
        self.find_element(by_locator).click()

    def wait_for_element_visible(self, by_locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def is_visible(self, by_locator):
       return self.driver.find_element(*by_locator).is_displayed()

    def select_checklist(self, by_locator, value):
        # Find the dropdown element first
        dropdown_element = self.driver.find_element(*by_locator)

        # Now create a Select object with the found element
        select_option = Select(dropdown_element)

        # Select the desired option by visible text
        select_option.select_by_visible_text(value)

    def find_elements(self, by_locator):
        elements=self.driver.find_elements(*by_locator)
        return [element.text for element in elements]

    def find_element_prices(self, by_locator):
        elements=self.driver.find_elements(*by_locator)
        return [float(element.text.replace('$', '')) for element in elements]

    def get_text(self, by_locator):
        self.find_element(by_locator).text
