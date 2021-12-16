from selenium.webdriver.common.by import By

from fixtures.pages.base_page import BasePage


class Choices(BasePage):

    def search_item(self, data):
        self.input_element(locator=(By.ID, 'email_inline'), input=data)
        self.click_element(locator=(By.XPATH, "//button[text()='Search']"))


    def search_result(self):
        self.get_text(locator=(By.CLASS_NAME, 'card-title'))


    def not_result(self):
        self.get_text(locator=(By.CSS_SELECTOR, 'h3'))
