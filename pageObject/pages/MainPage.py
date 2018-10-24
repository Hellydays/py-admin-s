from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObject import Locators
from pageObject.pages.BasePage import BasePage


class MainPage(BasePage):
    def hover_over_patients_menu(self):
        patient_menu = self.driver.find_element(By.CSS_SELECTOR, Locators.patients_menu_css_selector)
        hover = ActionChains(self.driver).move_to_element(patient_menu)
        hover.perform()

    def add_new_patient(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.add_new_patient).click()
