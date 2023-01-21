from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest

def test(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    email = str(time.time()) + "@fakemail.org"
    password = 'sdgtyhiklp'
    page.register_new_user(email=email, password=password)
    page.should_be_authorized_user()
    time.sleep(3)





















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def test_register_new_user():
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # browser = webdriver.Chrome()
    # browser.get(link)
    # email = str(time.time()) + "@fakemail.org"
    # password = str(time.time()) + "plkjg,uth"
    # enter_email = browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
    # enter_email.send_keys(email)
    # enter_pass1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
    # enter_pass1.send_keys(password)
    # enter_pass2 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
    # enter_pass2.send_keys(password)
    # button = browser.find_element(By.NAME, "registration_submit")
    # button.click()
    # time.sleep(10)