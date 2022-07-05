from GeneralPackage.GeneralActions import GeneralActions
from GeneralPackage import GeneralInformation
from Locators import LoginPageLocators


class TestLogin(GeneralActions):

    def test_valid_credentials(self, valid_account_login):
        # self.test_log.info('testing')
        self.add_log.info('Verifying Title of Successful Login')
        assert self.driver.title == GeneralInformation.HOME_PAGE_TITLE
        self.add_log.info(f'Title: {GeneralInformation.HOME_PAGE_TITLE} is successfully verified')

    def test_locked_out_credentials(self):
        # NAVIGATE TO LOGIN PAGE
        self.add_log.info('Login with locked out credentials')
        self.driver.get(LoginPageLocators.HOME_URL)
        # ENTER LOCKED_OUT_USERNAME
        self.locate_and_send_keys(LoginPageLocators.USERNAME_FIELD, GeneralInformation.LOCKED_OUT_USERNAME)
        # ENTER VALID PASSWORD
        self.locate_and_send_keys(LoginPageLocators.PASSWORD_FIELD, GeneralInformation.VALID_PASSWORD)
        # CLICK LOGIN BUTTON
        self.locate_and_click(LoginPageLocators.LOGIN_BUTTON)
        # ASSERT ERROR LOGIN
        self.locate_and_assert_text(LoginPageLocators.ERROR_LOGIN_MESSAGE, GeneralInformation.LOCKED_OUT_MESSAGE)
        self.add_log.info(f'Successfully tested locked out user! with the message of: '
                          + GeneralInformation.LOCKED_OUT_MESSAGE)





























