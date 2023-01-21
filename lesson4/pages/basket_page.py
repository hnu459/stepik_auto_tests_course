from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product is presented, but should not be"
    
    def should_be_product_is_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IS_NOT_BASKET), "Product is presented, but should not be"