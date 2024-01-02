import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('number', [*[str(x) for x in range(10) if x != 7],
                                  pytest.param("7",
                                               marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    basket = ProductPage(browser, link)
    basket.open()
    book = basket.get_book_name()
    price = basket.get_book_price()
    basket.add_to_basket()
    basket.should_be_the_same_book_name(book)
    basket.should_be_the_same_price(price)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_to_basket()
    basket.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser, link)
    basket.open()
    basket.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_to_basket()
    basket.should_disappeared_success_message()




