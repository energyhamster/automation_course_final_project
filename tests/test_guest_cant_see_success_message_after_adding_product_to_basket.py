from pages.product_page import ProductPage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        ]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product):
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_disappeared()