import os
import time
import unittest
from selenium import webdriver

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, USER_LOGIN, USER_PASSWORD


def print_nice_words() -> None:
    print("WELL DONE!!!!!!!!!")


class DashboardTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get(LoginPage.login_url)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_correct_title(self) -> None:
        login_page = LoginPage(self.driver)
        login_page.login(USER_LOGIN, USER_PASSWORD)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page_title = dashboard_page.get_title()

        assert dashboard_page_title == dashboard_page.expected_title

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print_nice_words()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"



