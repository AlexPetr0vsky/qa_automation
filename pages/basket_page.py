from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_message = self.browser.find_element(*BasketLocators.SUCCESS_MESSAGE).text
        assert "empty" in basket_message, "The basket should be empty"
