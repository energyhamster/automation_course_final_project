from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_url(self):
        # проверка на корректный url адрес
        assert "/basket/" in self.browser.current_url, "Incorrect basket URL"