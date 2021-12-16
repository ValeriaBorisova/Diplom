from selenium.webdriver.common.by import By


class ChoiceLocators:
    BANANAS_BUY = (By.XPATH, ".//div/span[@class = 'card-title' and contains(text(), "
                             "'bananas')]/following::div[1]/button")
    APPLES_BUY = (By.XPATH, ".//div/span[@class = 'card-title' and contains(text(), "
                            "'apples')]/following::div[1]/button")
    BREAD_BUY = (By.XPATH, ".//div/span[@class = 'card-title' and contains(text(), "
                            "'bread')]/following::div[1]/button")

