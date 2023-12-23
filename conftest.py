import pytest
import allure

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    attach = browser.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG) 
    browser.quit()
    