from selenium.webdriver.common.by import By
from .base_page import BasePage


class SbisHomePage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")

    def go_to_contacts_page(self):
        self.find_to_click_element(self.CONTACTS_LINK).click()
