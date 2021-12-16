import time

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
        time.sleep(10)
        result = app.choice.search_result()
        assert item in result

    def test_settings_with_invalid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Input invalid name "Cucumbers"
        3. Check result

        """
        app.open_place_page()
        item = "Cucumbers"
        app.choice.search_item(data=item)
        time.sleep(10)
        result = app.choice.not_result()
        assert result == Constans.NOT_RESULT
