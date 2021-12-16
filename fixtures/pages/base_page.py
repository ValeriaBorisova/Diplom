import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_elements(self, locator, wait_time=10):
        elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
        return elements

    def click_element(self, locator, wait_time=10):
        elements = self.find_elements(locator, wait_time)
        element = elements[0]
        time.sleep(2)
        element.click()

    def input_element(self, locator, input, wait_time=10):
        element = self.find_elements(locator, wait_time)[0]
        time.sleep(2)
        element.send_keys(input)

    def get_text(self, locator, wait_time=10):
        elements = self.find_elements(locator, wait_time)
        time.sleep(2)
        text = []
        for element in elements:
            text.append(element.text)
        return text
