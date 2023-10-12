import pytest
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
# import time
# from selenium.webdriver.common.by import By

# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# class TestProductPage:
    
#     def test_button_add_to_basket_is_visible(self, browser):
#         browser.get(link)
#         time.sleep(10)
#         assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
