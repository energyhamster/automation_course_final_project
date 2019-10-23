from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_NAME_ON_PRODUCT_PAGE = (By.XPATH, '//h1[text()="The shellcoder\'s handbook"]')
    PRODUCT_PRICE_ON_PRODUCT_PAGE = (By.CLASS_NAME, "price_color")
    PRODUCT_PAGE_SUBMIT_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE_IN_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")