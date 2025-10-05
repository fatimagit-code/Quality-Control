
import pytest
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage

@pytest.mark.login
@pytest.mark.critical
def test_successful_standard_login(driver, standard_user_credentials):

    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    inventory_page = login_page.login(standard_user_credentials)

    expected_path = InventoryPage.EXPECTED_URL_PATH
    assert expected_path in driver.current_url, \
        "Login Failed"

    assert inventory_page.is_on_inventory_page(), \
        "Inventory page wasn't displayed."

    product_count = inventory_page.get_product_count()
    assert product_count > 0, "Failed - No product is found"

@pytest.mark.login
@pytest.mark.critical
def test_Login_with_locked_out_user(driver, locked_user_credentials):
    '''
    Log in with locked_out_user, verify the specific error message for locked users is displayed, and the user is NOT redirected.

    '''
    login_page = LoginPage(driver)

    login_page.navigate_to_login()
    # 3. Verify the error message is displayed
    assert login_page.locked_login(locked_user_credentials), \
        "Failure: The 'User locked out' error message did not appear after login attempt."

    # 4.  Verify no redirection occurred (user stayed on the login URL)
    assert driver.current_url == login_page.base_url, \
        f"Failure: User was redirected to {driver.current_url} instead of staying on the login page ({login_page.base_url})."


@pytest.mark.login
@pytest.mark.critical
def test_Login_with_invalid_cred(driver, invalid_user_credentials):
    '''
    Attempt login with a non-existent username and password, verify the generic login error message is displayed.

    '''
    login_page = LoginPage(driver)


    login_page.navigate_to_login()
    # 3. Verify the error message is displayed

    assert login_page.invalid_login(invalid_user_credentials), \
        "Failure: The 'Non match user' error message did not appear after login attempt."

    # 4.  Verify no redirection occurred (user stayed on the login URL)
    assert driver.current_url == login_page.base_url, \
        f"Failure: User was redirected to {driver.current_url} instead of staying on the login page ({login_page.base_url})."


@pytest.mark.login
@pytest.mark.critical
def test_Login_with_missed_cred(driver):
    '''
    Attempt login with both username and password fields left empty, verify the "Username is required" error message appears.
    '''
    login_page = LoginPage(driver)


    login_page.navigate_to_login()
    # 3. Verify the error message is displayed

    assert login_page.required_missed(), \
        "Failure: The 'username is required' error message did not appear after login attempt."

    # 4.  Verify no redirection occurred (user stayed on the login URL)
    assert driver.current_url == login_page.base_url, \
        f"Failure: User was redirected to {driver.current_url} instead of staying on the login page ({login_page.base_url})."
