import pytest
from .pages.product_page import ProductPage

list_of_urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(x) for x in range(10)]


@pytest.mark.parametrize('link', [*[str(x) for x in range(10) if x != 7],
                                  pytest.param("7",
                                               marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_to_basket()
