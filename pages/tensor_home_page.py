from selenium.webdriver.common.by import By
from .base_page import BasePage


class TensorHomePage(BasePage):
    ABOUT_BLOCK = "//div[@class='tensor_ru-Index__block4-bg']"
    POWER_IN_PEOPLE = (By.XPATH, ABOUT_BLOCK + "/descendant::p[contains(@class, 'card-title')]")
    ABOUT_BLOCK_MORE_LINK = (By.XPATH, ABOUT_BLOCK + "/descendant::a")

    def get_power_in_people(self):
        return self.find_element(self.POWER_IN_PEOPLE)

    def click_more_link_in_about_block(self):
        element = self.find_to_click_element(self.ABOUT_BLOCK_MORE_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
