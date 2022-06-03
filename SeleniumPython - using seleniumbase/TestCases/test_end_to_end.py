from TestCases.test_login_test_suite import TestLogin


# VARIABLES
ITEM_NAME = 'Sauce Labs Onesie'
ITEM_PRICE = 7.99
FIRST_NAME = 'Tony'
LAST_NAME = 'Stark'
ZIP_POSTAL_CODE = '7777'


# Inherit from test_login_test_suite to avoid code repetition
class EndToEndTest(TestLogin):
    # Dynamic Functions
    def add_product_dynamic(self):
        self.click('//*[@class="inventory_item_name"][contains(text(), '
                   f'"{ITEM_NAME}")]/ancestor::div[@class="inventory_item_description"]//button')

    def assert_current_url(self, url):
        # assert current url is correct
        current_url = self.get_current_url()
        assert current_url == url

    # ----- START OF TEST CASES -----
    def test_successful_end_to_end_test(self):
        # Login Successfully
        self.test_login_with_correct_credentials()

        # ----- HomePage -----
        # Add product to cart
        self.add_product_dynamic()
        # click button to view cart page
        self.click('//*[@id="shopping_cart_container"]')

        # ----- View Cart Page -----
        # assert current url is correct
        self.assert_current_url('https://www.saucedemo.com/cart.html')
        # assert item name is correct and added successfully
        self.assert_text(ITEM_NAME, '//*[@class="inventory_item_name"]')
        # assert item price is correct and visible
        self.assert_text_visible(ITEM_PRICE, '//*[@class="inventory_item_price"]')
        # click button to view checkout information page
        self.click('//*[@id="checkout"]')

        # ----- Checkout Information Page -----
        # assert current url is correct
        self.assert_current_url('https://www.saucedemo.com/checkout-step-one.html')
        # Enter First Name
        self.set_text('//*[@id="first-name"]', FIRST_NAME)
        # Enter Last Name
        self.set_text('//*[@id="last-name"]', LAST_NAME)
        # Enter ZipCode
        self.set_text('//*[@id="postal-code"]', ZIP_POSTAL_CODE)
        # click continue to proceed to checkout overview page
        self.click('//*[@id="continue"]')

        # ----- Checkout Overview Page -----
        # assert current url is correct
        self.assert_current_url('https://www.saucedemo.com/checkout-step-two.html')
        # assert ITEM NAME is visible and correct
        self.assert_text_visible(ITEM_NAME, '//*[@class="inventory_item_name"]')
        # assert ITEM PRICE is visible and correct
        self.assert_text_visible(ITEM_PRICE, '//*[@class="inventory_item_price"]')
        # click button finish - to proceed to Check Out Complete page
        self.click('//*[@id="finish"]')

        # ----- Checkout Complete Page -----
        # assert current url is correct
        self.assert_current_url('https://www.saucedemo.com/checkout-complete.html')
        # assert PONY LOGO is visible
        self.assert_element_visible('//*[@class="pony_express"]')
        # save screenshot to verify successful end to end test
        self.save_screenshot('Successful End to End Test', 'screenshots/End to End Screenshots')





