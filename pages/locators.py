from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini > span:nth-child(2) > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REG_FORM_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketLocators:
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
