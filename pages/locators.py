from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) p strong")
