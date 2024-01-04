from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def get_book_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_the_same_book_name(self, book_name):
        book_name_in_basket = self.browser.find_element(*BasketLocators.BOOK_IN_BASKET).text
        assert book_name_in_basket == book_name, f"{book_name_in_basket} should be the same as {book_name}"

    def should_be_the_same_price(self, price):
        price_in_basket = self.browser.find_element(*BasketLocators.PRICE_IN_BASKET).text
        assert price_in_basket == price, f"{price_in_basket} should be the same as {price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"


