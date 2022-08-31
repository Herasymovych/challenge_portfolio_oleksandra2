from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT

class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_set_value(self, selector, value, locator_type=By.XPATH):
        self.wait_for_element_be_clickable(selector)
        element = self.driver.find_element(locator_type, selector)
        return element.send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url: str) -> str:
        self.driver.get(url)
        return self.driver.title

    def wait_for_element_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def get_element_value(self, selector, selector_type=DEFAULT_LOCATOR_TYPE) -> str:
        return self.driver.find_element(selector_type, selector).get_attribute("value")