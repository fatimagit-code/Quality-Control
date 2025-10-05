
import pytest
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.product_details import ProductPage
from ..pages.cart_page import CartPage
@pytest.mark.products
@pytest.mark.critical
def test_all_product_items_loaded(driver, standard_user_credentials):
    '''
        After successful login, verify that exactly 6 product items are displayed on the inventory page.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    inventory_page = login_page.login(standard_user_credentials)

    count=inventory_page.get_product_count()

    assert count == 6, f"Failed: Expected exactly 6 products, but found {count}."

@pytest.mark.sorts
@pytest.mark.critical
def test_sorting_by_name_a_to_z(driver, standard_user_credentials):
    '''
        Set the sort order to "Name (A to Z)" and verify the products are displayed in the correct alphabetical order.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)
    inventory.select_a_to_z()
    actual_products=inventory.get_products()
    expected_products=sorted(actual_products)
    assert actual_products==expected_products, \
        ("Product list wasn't sorted correctly")

@pytest.mark.sorts
@pytest.mark.critical
def test_sorting_by_price(driver, standard_user_credentials):
    '''
        Set the sort order to "Price (high to low)" and verify the top product has the highest price.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)
    inventory.select_price()
    actual_products_prices=inventory.get_products_price()
    expected_products=sorted(actual_products_prices, reverse=True)
    assert actual_products_prices==expected_products, \
        ("Product list wasn't sorted correctly")

@pytest.mark.Navigation
@pytest.mark.critical
def test_product_details_navigation(driver, standard_user_credentials):
    '''
        Click on a product name/image, verify redirection to the product detail page, and confirm the item name/price is correct.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)
    expected_product_name=inventory.get_product_name()
    expected_product_price=inventory.get_product_price()

    inventory.click_product()

    product=ProductPage(driver)

    actual_product_name=product.get_product_name()
    actual_product_price=product.get_product_price()

    assert actual_product_name == expected_product_name, \
        (f"Name Mismatch: Expected '{expected_product_name}', "
         f"but displayed name was '{actual_product_name}'.")

    assert actual_product_price == expected_product_price, \
        (f"Price Mismatch: Expected '{expected_product_price}', "
         f"but displayed price was '{actual_product_price}'.")

@pytest.mark.Navigation
@pytest.mark.major
def test_back_navigation(driver, standard_user_credentials):
    '''
        From the product detail page, click the "Back to products" button and verify return to the inventory page.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)

    inventory.click_product()

    product=ProductPage(driver)

    product.click_back_to_product()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL did not match expected inventory page URL"

@pytest.mark.cartstate
@pytest.mark.major
def test_ad_to_cart_from_product_details(driver, standard_user_credentials):
    '''
        Navigate to a product detail page, click "Add to Cart," and verify the shopping cart icon badge updates to 1.
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)

    inventory.click_product()

    product=ProductPage(driver)

    product.click_add_to_cart()
    assert product.get_cart_number() == 1, "shopping cart icon badge not updated to 1."

@pytest.mark.cartstate
@pytest.mark.major
def test_add_three_items_to_cart(driver, standard_user_credentials):
    '''
        Add three different items, navigate to the cart, and verify all three items are listed with the correct names and total quantity (3).
    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(standard_user_credentials)

    inventory = InventoryPage(driver)

    expected_product1_name=inventory.get_product1_name()
    expected_product2_name=inventory.get_product2_name()
    expected_product3_name=inventory.get_product3_name()

    inventory.cart_product1()
    inventory.cart_product2()
    inventory.cart_product3()

    inventory.click_cart_icon()

    cart = CartPage(driver)
    actual_product1_name=cart.get_product1_name()
    actual_product2_name=cart.get_product2_name()
    actual_product3_name=cart.get_product3_name()


    assert expected_product1_name == actual_product1_name, \
        (f"Name Mismatch: Expected '{expected_product1_name}', "
         f"but displayed name was '{actual_product1_name}'.")

    assert expected_product2_name == actual_product2_name, \
        (f"Name Mismatch: Expected '{expected_product2_name}', "
         f"but displayed name was '{actual_product2_name}'.")

    assert expected_product3_name == actual_product3_name, \
        (f"Name Mismatch: Expected '{expected_product3_name}', "
         f"but displayed name was '{actual_product3_name}'.")

    assert cart.get_all_products()==3
