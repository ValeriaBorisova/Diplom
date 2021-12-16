from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage


class Baskets(BasePage):
    def add_basket(self):
        self.click_element(locator=BasketLocators.BANANAS_BUY)
        self.click_element(locator=BasketLocators.APPLES_BUY)
        self.click_element(locator=BasketLocators.TOMATE_BUY)
        self.click_element(locator=BasketLocators.POTATOES_BUY)
