from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('lin', ["0","1","2","3","4","5","6", pytest.param("7", marks=pytest.mark.xfail),"8","9"])

def test_guest_can_add_product_to_basket(browser, lin):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{lin}"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.test_product_price_is_in_basket()
    page.test_poduct_name_is_in_basket()
    time.sleep(1)