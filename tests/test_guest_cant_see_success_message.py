from pages.product_page import ProductPage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        ]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product):
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()