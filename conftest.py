import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.set_window_size(1400, 3000)
    yield browser
    browser.quit()
