from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_in_basket(self):
        self.should_be_product_page()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_correct_product_in_basket()
        self.should_be_correct_price_in_basket()

    def should_be_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "Product page doesn't open"

    def add_product_to_basket(self):
        submit_button = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_SUBMIT_BUTTON)
        submit_button.click()

    def should_be_correct_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name in add_product_in_basket, "Incorrect product in basket after adding"

    def should_be_correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, "Incorrect product price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"

    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"


