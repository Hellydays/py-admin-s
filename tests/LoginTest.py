from pageObject.entity.User import User
from pageObject.pages.AddNewPatientPage import AddNewPatientPage
from pageObject.pages.LoginPage import Login
from pageObject.pages.MainPage import MainPage
from tests.BaseTest import BaseTest


class Main(BaseTest):

    user = User('username', 'qwerty', 'first', 'last', 'Spanish', '+375259991122', 'sense@sense.ly', '1234', 'TestOrg')

    def test(self):
        driver = self.driver
        driver.get(self.base_url)
        login = Login(driver)
        login.enter_username('testcli')
        login.enter_password('qwerty')
        login.click_sign_in()

        main_page = MainPage(driver)
        main_page.hover_over_patients_menu()
        main_page.add_new_patient()

        # add_new_patient_page = AddNewPatientPage(driver)
        # add_new_patient_page.create_user(user, 'qwerty')
