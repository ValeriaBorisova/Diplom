import logging

from selenium.webdriver.common.by import By

from fixtures.locators.choice import ChoiceLocators
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class Choices(BasePage):

    """
    Поиск товара
    """

    def search_item(self, data):
        logger.info(f"Найден товар{data}")
        self.input_element(locator=(By.ID, 'email_inline'), input=data)
        self.click_element(locator=(By.XPATH, "//button[text()='Search']"))

    def search_result(self):
        text = self.get_text(locator=(By.CLASS_NAME, "card-title"))
        return text

    def not_result(self):
        text = self.get_text(locator=(By.CSS_SELECTOR, 'h3'))
        return text

    def buy_bananas(self):
        self.click_element(locator=ChoiceLocators.BANANAS_BUY)

    def buy_apples(self):
        self.click_element(locator=ChoiceLocators.APPLES_BUY)

    def buy_bread(self):
        self.click_element(locator=ChoiceLocators.BREAD_BUY)