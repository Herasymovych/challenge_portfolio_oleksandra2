import os
import time
import unittest
from selenium import webdriver

from pages.add_player import AddPlayerPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, USER_LOGIN, USER_PASSWORD, NAME, SURNAME, AGE, MAIN_POSITION


def print_nice_words() -> None:
    print("WELL DONE!!!!!!!!!")


class AddPlayerTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get(LoginPage.login_url)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_redirects(self) -> None:
        login_page = LoginPage(self.driver)
        login_page.login(USER_LOGIN, USER_PASSWORD)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_add_player()

        assert self.driver.current_url == AddPlayerPage.add_player_url

    def test_leg_input_sets_value(self) -> None:
        expected_leg_value = "right"
        login_page = LoginPage(self.driver)
        login_page.login(USER_LOGIN, USER_PASSWORD)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_add_player()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.set_leg_value(expected_leg_value)
        actual_leg_value = add_player_page.get_element_value(AddPlayerPage.leg_xpath)

        assert expected_leg_value == actual_leg_value

    def test_required_fields_add_player(self):
        login_page = LoginPage(self.driver)
        login_page.login(USER_LOGIN, USER_PASSWORD)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_add_player()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.filling_the_required_fields(NAME, SURNAME, AGE, MAIN_POSITION)
        time.sleep(5)

        assert self.driver.current_url.__contains__("edit")





    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print_nice_words()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"



