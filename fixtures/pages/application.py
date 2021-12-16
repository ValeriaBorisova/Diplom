from fixtures.pages.basket import Baskets
from fixtures.pages.choice import Choices
from fixtures.pages.start import  StartPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.start = StartPage(self)
        self.choice = Choices(self)
        self.basket = Baskets(self)



    def quit(self):
        self.driver.quit()

    def open_start_page(self):
        self.driver.get(self.url)

    def open_choices_page(self):
        self.driver.get("https://berpress.github.io/online-grocery-store/")
