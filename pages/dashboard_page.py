import time

from pages.base_page import BasePage


class DashboardPage(BasePage):
    players_count_text = "//*[text()=\"Players count\"]"
    logo_scouts_panel = "//*[@title=\"Logo Scouts Panel\"]"
    button_main_page = "//*[text()=\"Main page\"]"
    button_players = "//*[text()=\"Players\"]"
    link_add_player = "//*[text()=\"Add player\"]"
    root_div = "//*[@id=\"__next\"]"
    text_shortcuts = "//*[text()=\"Shortcuts\"]"
    link_dev_team_contact = "//*[text()=\"Dev team contact\"]"
    text_last_created_players = "//*[text()=\"Last created player\"]"
    button_polski = "//*[text()=\"Polski\"]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    button_sign_out = "//*[text()=\"Sign out\"]"


    def get_title(self) -> str:
        self.wait_for_element_be_clickable(self.button_main_page)
        return self.get_page_title(self.dashboard_url)

    def click_add_player(self) -> None:
        self.wait_for_element_be_clickable(self.link_add_player)
        self.click_on_the_element(self.link_add_player)

    def click_sign_out(self) -> None:
        self.wait_for_element_be_clickable(self.button_sign_out)
        self.click_on_the_element(self.button_sign_out)



