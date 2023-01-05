from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        Add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        Add_button.click()
        
    def test_poduct_name_is_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text, "Product name is not in basket"        
    
    def test_product_price_is_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text, "Product price is not in basket"        
    