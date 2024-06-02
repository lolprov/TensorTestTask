from selenium.webdriver.common.by import By
from .base_page import BasePage


class TensorAboutPage(BasePage):
    WORK_IMAGES = (By.XPATH, "//div[contains(@class,'tensor_ru-About--col-md6')]//img")

    def check_size_of_work_images(self):
        images = self.find_elements(self.WORK_IMAGES)
        sizes = []
        for image in images:
            width = int(image.get_attribute("width"))
            height = int(image.get_attribute("height"))
            sizes.append((width, height))
        if sizes.count(sizes[0]) == len(sizes):
            return 1
        else:
            print(f"Sizes of images - {sizes}")
            return 0

