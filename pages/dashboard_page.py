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

    def get_title(self) -> str:
        time.sleep(4)
        return self.get_page_title(self.dashboard_url)

