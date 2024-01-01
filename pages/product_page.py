from .base_page import BasePage
from .locators import BasketLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*BasketLocators.ADD_TO_BASKET_BTN)
        book_name = self.browser.find_element(*BasketLocators.BOOK_NAME).text
        price = self.browser.find_element(*BasketLocators.PRICE).text
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_the_same_book_name(book_name)
        self.should_be_the_same_price(price)

    def should_be_the_same_book_name(self, book_name):
        book_name_in_basket = self.browser.find_element(*BasketLocators.BOOK_IN_BASKET).text
        assert book_name_in_basket == book_name, f"{book_name_in_basket} should be the same as {book_name}"

    def should_be_the_same_price(self, price):
        price_in_basket = self.browser.find_element(*BasketLocators.PRICE_IN_BASKET).text
        assert price_in_basket == price, f"{price_in_basket} should be the same as {price}"