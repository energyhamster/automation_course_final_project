from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, '//h1[text()="The shellcoder\'s handbook"]')
    PRODUCT_PAGE_SUBMIT_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//strong[contains(text(), "The shellcoder\'s handbook")]')
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")