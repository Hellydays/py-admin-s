from pageObject import Locators
from pageObject.pages.BasePage import BasePage


class Login(BasePage):

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.login_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_field).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(Locators.login_button).click()
