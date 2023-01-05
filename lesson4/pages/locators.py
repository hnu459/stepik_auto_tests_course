from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_IN_BASKET = (By.CLASS_NAME, "hidden-xs")
    NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) > .alertinner > strong")
    