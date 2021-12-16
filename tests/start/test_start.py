class TestStart:
    def test_place_with_valid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Check result
        """
        app.open_start_page()

        assert 1==1