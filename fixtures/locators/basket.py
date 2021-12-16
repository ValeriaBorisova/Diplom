from selenium.webdriver.common.by import By


class BasketLocators:
    CART_BUTTON = (By.CSS_SELECTOR, "i.material-icons")
    CART_TITLE = (By.CSS_SELECTOR, "li.collection-item")
    CART_ADD_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and contains(text(),'add')]",
    )
    CART_REMOVE_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and contains(text(),'remove')]",
    )
    CART_DELETE_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-delete' and contains(text(),'close')]",
    )
    CART_BUY_BUTTON = (
        By.XPATH,
        ".//li/button[@class = 'btn red btn-small' and contains(text(),'Buy')]",
    )
    CART_DONE_POPUP = (
        By.XPATH,
        ".//div[@class = 'toast' and contains(text(),'Pay done!')]",
    )


