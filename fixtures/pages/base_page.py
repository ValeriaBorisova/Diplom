from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):


        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

        return element

    def click_element(self, locator, wait_time=10):
        element = self.find_element(locator, wait_time)
        element.click()


    def input_element(self, locator, input, wait_time=10):
        element = self.find_element(locator, wait_time)
        element.send_keys(input)


    def get_text(self, locator, wait_time=10):
        element = self.find_element(locator, wait_time)
        return element.text