from selenium.webdriver.common.by import By


class BasketLocators:
    BANANAS_BUY = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/div[3]/button')
    APPLES_BUY = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[2]/div[3]/button')
    TOMATE_BUY = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[3]/div[3]/button')
    POTATOES_BUY = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[4]/div[3]/button')