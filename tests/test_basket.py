from fixtures.pages.constans import Constans


class TestBaskets:
    def test_add_item(self, app):
        """
        Steps:
        1. Open start page
        2. Add item to basket
        3. Open basket
        4. Add item (increase qty)
        """
        item = "bananas"
        app.open_start_page()
        app.choice.buy_bananas()
        app.basket.open_basket()
        price = app.basket.get_item_price(item)
        app.basket.add_item()
        new_price = app.basket.get_item_price(item)
        assert new_price == price * 2

    def test_remove_item(self, app):
        """
        Steps:
        1. Open start page
        2. Add item to basket
        3. Open basket
        4. Remove item (decrease qty)
        """
        pass

    def test_delete(self, app):
        """
        Steps:
        1. Open start page
        2. Add item to basket
        3. Open basket
        4. Delete item
        """
        pass

    def test_buy(self, app):
        """
        Steps:
        1. Open start page
        2. Add item to basket
        3. Open basket
        4. Buy
        """
        app.open_start_page()
        app.choice.buy_bananas()
        app.basket.open_basket()
        app.basket.buy()
        text = app.basket.get_basket_done_text()
        assert text == Constans.CART_BUY
