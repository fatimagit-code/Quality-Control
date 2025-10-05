from selenium.webdriver.common.by import By
from ..pages.base import BasePage


class CartPage(BasePage):

    product1=(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div")
    product2=(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div")
    product3=(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div[5]/div[2]/a/div")
    all_products=(By.CLASS_NAME,"inventory_item_name")
    remove_button=(By.ID,"remove-sauce-labs-bike-light")



    def get_product1_name(self):
        return self.get_text(self.product1)

    def get_product2_name(self):
        return self.get_text(self.product2)

    def get_product3_name(self):
        return self.get_text(self.product3)

    def get_all_products(self):
        return len(self.find_elements(self.all_products))

    def click_remove_button(self):
        self.click(self.remove_button)
