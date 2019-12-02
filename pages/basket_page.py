from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_url(self):
        # проверка на корректный url адрес
        assert "/basket/" in self.browser.current_url, "Incorrect basket URL"

    def basket_is_empty(self):
        # checking that basket is empty
        pass

    def basket_is_empty_text(self):
        # checking that basket is empty text presented
        pass