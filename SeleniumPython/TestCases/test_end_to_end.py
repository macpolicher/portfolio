from selenium.webdriver.common.by import By
from TestCases import test_login

# CONSTANTS:
ITEM_NAME = 'Sauce Labs Backpack'
ITEM_PRICE = 29.99
FIRST_NAME = 'John'
LAST_NAME = 'Snow'
ZIP_CODE = '7777'
TAX = 2.40
TOTAL_PRICE = ITEM_PRICE + TAX


# dynamic functions:
def add_item_by_name_dynamic(item_name):
    test_login.driver.find_element(By.XPATH,
                                   f'//*[@class="inventory_item_name"][contains(text(), "{ITEM_NAME}")]'
                                   f'/ancestor::div[@class="inventory_item_description"]//button').click()


def find_element_using_xpath_dynamic(xpath):
    return test_login.driver.find_element(By.XPATH, xpath)


# --------------------------- TEST CASES: ---------------------------
def test_successful_transaction_end_to_end():
    # Login
    test_login.test_login_with_correct_credentials()

    # ----- HOME PAGE -----
    # Add item dynamically based on constant
    add_item_by_name_dynamic(ITEM_NAME)
    # View cart
    find_element_using_xpath_dynamic('//*[@class="shopping_cart_link"]').click()

    # ----- VIEW CART PAGE -----
    # Assert Added Item on cart
    item_on_cart_name = find_element_using_xpath_dynamic('//*[@class="inventory_item_name"]').text
    assert item_on_cart_name == ITEM_NAME
    # Assert Added Item on cart price
    price_of_item_on_cart = find_element_using_xpath_dynamic('//*[@class="inventory_item_price"]').text
    assert str(ITEM_PRICE) in price_of_item_on_cart
    # Proceed to checkout page
    find_element_using_xpath_dynamic('//*[@id="checkout"]').click()

    # ----- CHECK OUT PAGE -----
    # input First Name
    find_element_using_xpath_dynamic('//*[@id="first-name"]').send_keys(FIRST_NAME)
    # input Last Name
    find_element_using_xpath_dynamic('//*[@id="last-name"]').send_keys(LAST_NAME)
    # input Postal Code
    find_element_using_xpath_dynamic('//*[@id="postal-code"]').send_keys(ZIP_CODE)
    # click continue
    find_element_using_xpath_dynamic('//*[@id="continue"]').click()

    # ----- CHECK OUT OVERVIEW PAGE -----
    # assert item name on checkout overview page
    assert ITEM_NAME in find_element_using_xpath_dynamic('//*[@class="inventory_item_name"]').text
    # assert item price on checkout overview page
    assert str(ITEM_PRICE) in find_element_using_xpath_dynamic('//*[@class="inventory_item_price"]').text
    # assert total price
    assert str(TOTAL_PRICE) in find_element_using_xpath_dynamic('//*[@class="summary_total_label"]').text
    # proceed to FINISH
    find_element_using_xpath_dynamic('//*[@id="finish"]').click()

    # ----- ORDER COMPLETE COMPLETE PAGE -----
    # assert current url is of complete order
    assert test_login.driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    # assert logo is visible on complete order page
    assert find_element_using_xpath_dynamic('//*[@class="pony_express"]')




