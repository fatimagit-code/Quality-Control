from selenium.webdriver.common.by import By
from ..pages.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):


    product_name = (By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")
    product_price = (By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[3]")
    back_to_product=(By.ID,"back-to-products")
    add_to_cart=(By.ID,"add-to-cart")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_product_name(self):
        return self.get_text(self.product_name)

    def get_product_price(self):
        return self.get_text(self.product_price)

    def click_back_to_product(self):
        self.click(self.back_to_product)

    def click_add_to_cart(self):
        self.click(self.add_to_cart)

    def get_cart_number(self):
        try:
            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.cart_badge)
            )
            cart_text = self.get_text(self.cart_badge)
            return int(cart_text)
        except TypeError:
            return 0  # No badge means nothing in cart
        except Exception as e:
            raise AssertionError(f"Failed to get cart number: {e}")
