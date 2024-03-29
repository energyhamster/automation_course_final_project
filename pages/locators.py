from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    PRODUCT_PAGE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages > div.alert:nth-child(1) .alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "//div[@id='messages']//div[1]/div//strong//following-sibling::text()")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, ".btn-group a")