from selenium.webdriver.common.by import By
from ..pages.base import BasePage


class InventoryPage(BasePage):

    EXPECTED_URL_PATH = "/inventory.html"
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_TITLES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES= (By.CLASS_NAME, "inventory_item_price")
    sort= (By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select")
    product_name = (By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
    product_price = (By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
    product1=(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div")
    product2=(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div")
    product3=(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div")
    product1_cart=(By.ID,"add-to-cart-sauce-labs-bike-light")
    product2_cart=(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
    product3_cart=(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
    cart_icon=(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")


    def is_on_inventory_page(self) -> bool:
        try:
            self.wait_for_element_visible(self.INVENTORY_CONTAINER)
            return self.EXPECTED_URL_PATH in self.driver.current_url
        except:
            return False

    def get_product_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_TITLES))

    def select_a_to_z(self):
        self.select_checklist(self.sort, "Name (A to Z)")

    def get_products(self):
        return self.find_elements(self.PRODUCT_TITLES)

    def select_price(self):
        self.select_checklist(self.sort, "Price (high to low)")

    def get_products_price(self):
         return self.find_element_prices(self.PRODUCT_PRICES)

    def get_product_name(self):
        return self.get_text(self.product_name)

    def get_product_price(self):
        return self.get_text(self.product_price)

    def click_product(self):
        self.click(self.product_name)

    def get_product1_name(self):
        return self.get_text(self.product1)

    def get_product2_name(self):
        return self.get_text(self.product2)

    def get_product3_name(self):
        return self.get_text(self.product3)

    def cart_product1(self):
        self.click(self.product1_cart)

    def cart_product2(self):
        self.click(self.product2_cart)

    def cart_product3(self):
        self.click(self.product3_cart)

    def click_cart_icon(self):
        self.click(self.cart_icon)
