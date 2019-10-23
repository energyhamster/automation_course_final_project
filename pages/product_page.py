from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_in_basket(self):
        self.should_be_product_page()
        self.add_product_to_basket()
        # self.should_be_correct_product_in_basket()
        # self.should_be_correct_price_in_basket()

    def should_be_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PRODUCT_PAGE), "Product page doesn't open"

    def add_product_to_basket(self):
        submit_button = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_SUBMIT_BUTTON)
        submit_button.click()

    def should_be_correct_product_in_basket(self):
        product_name_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PRODUCT_PAGE).text
        product_name_in_busket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_on_product_page == product_name_in_busket, "Incorrect product in basket after adding"



    #
    # def should_be_correct_price_in_basket(self):
    #     pass

