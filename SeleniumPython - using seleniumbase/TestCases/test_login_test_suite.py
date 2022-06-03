from seleniumbase import BaseCase


class TestLogin(BaseCase):
    def test_login_with_correct_credentials(self):
        # navigate to site
        self.open('https://www.saucedemo.com/')
        # maximize window
        self.maximize_window()
        # enter correct username for standard_user
        self.set_text('//*[@id="user-name"]', 'standard_user')
        # enter correct password
        self.set_text('//*[@id="password"]', 'secret_sauce')
        # click login
        self.click('//*[@id="login-button"]')
        # assert login successful
        current_url = self.get_current_url()
        assert current_url == 'https://www.saucedemo.com/inventory.html'
        # save screenshot
        self.wait_for_ready_state_complete(60)
        self.save_screenshot('successful login screenshot', 'screenshots/Login Screenshots')

    def test_login_with_locked_out_user(self):
        # navigate to site
        self.open('https://www.saucedemo.com/')
        # maximize window
        self.maximize_window()
        # enter correct username for standard_user
        self.set_text('//*[@id="user-name"]', 'locked_out_user')
        # enter correct password
        self.set_text('//*[@id="password"]', 'secret_sauce')
        # click login
        self.click('//*[@id="login-button"]')
        # assert login failed
        self.assert_element_visible('//*[@data-test="error"]')
        # assert element text of failed login
        self.assert_text('Epic sadface: Sorry, this user has been locked out.', '//*[@data-test="error"]')
        # save screenshot
        self.save_screenshot('locked out user - login screenshot', 'screenshots/Login Screenshots')

