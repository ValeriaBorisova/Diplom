import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from fixtures.pages.application import Application


def pytest_addoption(parser):
    parser.addoption(
        "--url", 
        action="store", 
        default="https://berpress.github.io/online-grocery-store/", 
        help="Store url"),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    )
    
    
@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    app = Application(driver, url)
    yield app
    app.quit()
