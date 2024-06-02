import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class SbisContactsPage(BasePage):
    TENSOR_BANNER = (By.XPATH, '//a[@title="tensor.ru"]')
    REGION_BANNER = (By.XPATH, '//div[contains(@class, "sbisru-Contacts__relative")]//span[contains(@class, '
                               '"Region-Chooser__text")]')
    CONTACTS_LIST = (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__name")]')
    REGION_41 = (By.XPATH, '//ul[@class="sbis_ru-Region-Panel__list-l"]//span[@title="Камчатский край"]')
    REGIONS = (By.XPATH, '//ul[@class="sbis_ru-Region-Panel__list-l"]')

    def click_tensor_banner(self):
        self.find_element(self.TENSOR_BANNER).click()

    def take_contacts_list(self):
        contacts = self.find_elements(self.CONTACTS_LIST)
        return [contact.get_attribute("title") for contact in contacts]

    def click_region_banner(self):
        self.find_to_click_element(self.REGION_BANNER).click()

    def change_region(self):
        self.vision_element(self.REGIONS)
        self.vision_element(self.REGION_41)
        time.sleep(1)
        self.find_to_click_element(self.REGION_41).click()
        self.wait_for_elements_staleness(self.CONTACTS_LIST)

    def wait_for_elements_staleness(self, locator, time=10):
        elements = self.find_elements(locator)
        WebDriverWait(self.driver, time).until(
            lambda driver: all(EC.staleness_of(element)(driver) for element in elements),
            message="Elements did not become stale in time"
        )

    def get_region_name(self):
        return self.find_element(self.REGION_BANNER).text

