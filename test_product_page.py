import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
from random import choices
import string

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        registration = LoginPage(browser, link)
        registration.open()
        registration.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = ''.join(choices(string.ascii_uppercase + string.digits, k=15))
        registration.register_new_user(email, password)
        registration.should_be_registered()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        basket = ProductPage(browser, link)
        basket.open()
        book = basket.get_book_name()
        price = basket.get_book_price()
        basket.add_to_basket()
        basket.should_be_the_same_book_name(book)
        basket.should_be_the_same_price(price)

    def test_user_cant_see_success_message(self, browser):
        basket = ProductPage(browser, link)
        basket.open()
        basket.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('number', [*[str(x) for x in range(10) if x != 7],
                                  pytest.param("7",
                                               marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, number):
    promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    basket = ProductPage(browser, promo_link)
    basket.open()
    book = basket.get_book_name()
    price = basket.get_book_price()
    basket.add_to_basket()
    basket.solve_quiz_and_get_code()
    basket.should_be_the_same_book_name(book)
    basket.should_be_the_same_price(price)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_to_basket()
    basket.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    basket = ProductPage(browser, link)
    basket.open()
    basket.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_to_basket()
    basket.should_disappeared_success_message()




