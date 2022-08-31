import os
import time
import unittest
from selenium import webdriver

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, USER_LOGIN, USER_PASSWORD


def print_nice_words() -> None:
    print("WELL DONE!!!!!!!!!")


class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get(LoginPage.login_url)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_logout(self) -> None:
        login_page = LoginPage(self.driver)
        login_page.login(USER_LOGIN, USER_PASSWORD)

        login_page.wait_for_element_be_clickable(DashboardPage.button_polski)

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_sign_out()

        assert self.driver.current_url == login_page.login_url


    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print_nice_words()




