from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseApp:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def wait_for_presence_of_all_elements_located(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def click_element_from_list_of_elements(
            self, locator, number_of_element, timeout=10):
        elements = self.find_elements(locator, timeout)
        elements[number_of_element].click()

    def write_into_input_field(
            self, locator, phrase, timeout=10, clear=False, with_enter=False):
        input_field = self.find_element(locator, timeout)
        if clear:
            input_field.clear()

        input_field.send_keys(phrase)

        if with_enter:
            input_field.send_keys(By.RETURN)
