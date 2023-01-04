from selenium.webdriver.common.by import By
import time

def test_test(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    assert "accounts/logins/" in browser.current_url, "Login is not presented in link"
    time.sleep(5)