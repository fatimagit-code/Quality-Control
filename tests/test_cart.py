import pytest
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.product_details import ProductPage
from ..pages.cart_page import CartPage

@pytest.mark.cartsmanagement
@pytest.mark.major
def test_remove_item_from_cart(driver, standard_user_credentials):
    '''
        Add three different items, navigate to the cart, and verify all three items are listed with the correct names and total quantity (3).
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)

    expected_product1_name=inventory.get_product1_name()
    expected_product2_name=inventory.get_product2_name()

    inventory.cart_product1()
    inventory.cart_product2()

    inventory.click_cart_icon()

    cart = CartPage(driver)

    cart.click_remove_button()


    assert cart.get_all_products()==1
