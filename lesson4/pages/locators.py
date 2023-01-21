from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group:nth-child(2) > a")
    REISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REISTER_BUTTON = (By.NAME, "registration_submit")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) > .alertinner")
    
class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket_summary")
    PRODUCT_IS_NOT_BASKET = (By.CSS_SELECTOR, "#content_inner p:nth-child(1) a")