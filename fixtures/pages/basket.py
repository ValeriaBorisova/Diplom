from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage


class Baskets(BasePage):
    def open_basket(self):
        self.click_element(locator=BasketLocators.CART_BUTTON)

    def get_basket_text(self):
        text = self.get_text(locator=BasketLocators.CART_TITLE)
        return text

    def add_item(self):
        self.click_element(locator=BasketLocators.CART_ADD_ITEM)

    def remove_item(self):
        self.click_element(locator=BasketLocators.CART_REMOVE_ITEM)

    def get_item_price(self, item):
        cart_text = self.get_text(locator=BasketLocators.CART_TITLE)
        product_price_string = ""
        for line in cart_text:
            if line.find(item) != -1:
                product_price_string = line
                break
        if product_price_string == "":
            assert False, f"В корзине не найден продукт {item}"
        product_total_price = product_price_string[
                              (product_price_string.find("= ") + 2): product_price_string.find(" руб")
                              ]
        return float(product_total_price)

    def delete(self) -> None:
        self.click_element(locator=BasketLocators.CART_DELETE_ITEM)

    def buy(self) -> None:
        self.click_element(locator=BasketLocators.CART_BUY_BUTTON)

    def get_basket_done_text(self):
        text = self.get_text(locator=BasketLocators.CART_DONE_POPUP)[0]
        return text
