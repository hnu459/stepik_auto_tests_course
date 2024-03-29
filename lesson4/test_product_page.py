from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.guest_basket
class TestGuestAddToBasketFromProductPage():    
    @pytest.mark.xfail   
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_guest_can_add_product_to_basket()
        page.should_not_be_success_message()
        
    def test_guest_cant_see_success_message(self, browser):
         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
         page = ProductPage(browser, link)
         page.open()
         page.should_not_be_success_message()      
    
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_guest_can_add_product_to_basket()
        page.should_product_price_is_in_basket()
        page.should_poduct_name_is_in_basket()            
        
    @pytest.mark.xfail    
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_guest_can_add_product_to_basket()
        page.should_is_disappeared()
        
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        
    @pytest.mark.need_review    
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.should_go_to_basket_page()
        page.should_be_product_in_basket()
        page.should_be_product_is_basket()
        
@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)    
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = 'sdgtyhiklp'
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_guest_can_add_product_to_basket()
        page.should_product_price_is_in_basket()
        page.should_poduct_name_is_in_basket()
