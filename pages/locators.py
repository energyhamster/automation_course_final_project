from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_PAGE = (By.XPATH, '//h1[text()="The shellcoder\'s handbook"]')
    PRODUCT_PRICE = (By.CLASS_NAME, '[class="price_color"]')