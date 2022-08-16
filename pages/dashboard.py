from pages.base_page import BasePage


class Dashboard(BasePage):
    players_count_text = "//*[contains(@class, 'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]/div[1]"
    players_count_value = "//*[contains(@class, 'MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded')]/div[2]/b"
    logo_scouts_panel = "//*[@title=\"Logo Scouts Panel\"]"
    button_main_page = "//*[text()=\"Main page\"]"
    button_players = "//*[text()=\"Players\"]"
    link_add_player = "//*[text()=\"Add player\"]"
    root_div = "//*[@id=\"__next\"]"
    text_shortcuts = "//*[text()=\"Shortcuts\"]"
    link_dev_team_contact = "//*[text()=\"Dev team contact\"]"
    text_last_created_players = "//*[text()=\"Last created player\"]"

    pass