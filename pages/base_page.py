from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Основные методы взаимодействия с браузером"""

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.get(self.url)

    def open_browser(self):
        """Открыть браузер"""
        self.browser.get(self.url)

    def wait_until_clickable(self, locator: Tuple, timeout: int = 10) -> WebElement:
        """Ожидание, пока WebElement не станет кликабельным"""
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, locator: Tuple, timeout: int = 30) -> WebElement:
        """Ожидание, пока WebElement не станет видимым"""
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator: Tuple):
        """Действие - Клик по элементу"""
        self.wait_until_clickable(locator).click()

    def send_data(self, locator: Tuple, data: str):
        """Действие - Отправить данные"""
        self.wait_until_clickable(locator).send_keys(data)




