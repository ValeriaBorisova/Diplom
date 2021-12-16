from fixtures.models.basket import BasketData


class TestBaskets:
    def test_baskets_with_valid_data(self, app):
        """
                Steps:
                1. Open start page
                2. Open choce page
                2. Click buy
                3. Check result

                """
        app.open_start_page()
        app.open_choices_page()
        data = BasketData
        app.baskets.add_baskets(data)
        assert 1 == 1