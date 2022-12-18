from selenium.webdriver.common.by import By
      
def test_item(browser):  
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button, "Page has no button add to cart."