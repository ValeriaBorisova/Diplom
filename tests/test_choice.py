from fixtures.pages.constans import Constans


class TestChoices:
    def test_choices_with_valid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Input name product "bananas"
        3. Check result
        """
        app.open_start_page()
        item = "bananas"
        app.choice.search_item(data=item)
        result = app.choice.search_result()
        assert item in result

    def test_choices_with_invalid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Input invalid name "Cucumbers"
        3. Check result
        """
        app.open_start_page()
        item = "Cucumbers"
        app.choice.search_item(data=item)
        result = app.choice.not_result()[0]
        assert result == Constans.NOT_RESULT

    def test_add_item_to_basket(self, app):
        """
        Steps:
        1. Open start page
        2. Add item to basket
        3. Open basket
        4. Check item in basket
        """
        item = "bananas"
        app.open_start_page()
        app.choice.buy_bananas()
        app.basket.open_basket()
        basket_text = app.basket.get_basket_text()
        cart_title = basket_text[0]
        assert cart_title == Constans.BASKET
        add_goods = basket_text[1]
        assert item in add_goods
