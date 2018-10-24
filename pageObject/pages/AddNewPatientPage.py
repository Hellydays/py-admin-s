from pageObject import Locators
from pageObject.pages.BasePage import BasePage


class AddNewPatientPage(BasePage):
    def create_user(self, user, password):
        self.driver.find_element_by_id(Locators.patient_username).send_keys(user.username)
        self.driver.find_element_by_id(Locators.password_field).send_keys(password)
