from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "accounts/login/" in self.browser.current_url, "Login is not presented in link" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        enter_email = self.browser.find_element(*BasePageLocators.REISTER_EMAIL)
        enter_email.send_keys(email)
        enter_pass1 = self.browser.find_element(*BasePageLocators.REISTER_PASS1)
        enter_pass1.send_keys(password)
        enter_pass2 = self.browser.find_element(*BasePageLocators.REISTER_PASS2)
        enter_pass2.send_keys(password)
        button = self.browser.find_element(*BasePageLocators.REISTER_BUTTON)
        button.click()


        