from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    leg_xpath = "//*[@name=\"leg\"]"
    submit_button_xpath = "//button[@type=\"submit\"]"
    leg_wrapper_xpath = "//*[@id=\"mui-component-select-leg\"]"
    right_leg_xpath = "//*[@id=\"menu-leg\"]/div[3]/ul/li[1]"
    left_leg_xpath = "//*[@id=\"menu-leg\"]/div[3]/ul/li[2]"
    player_name = "//input[@name=\"name\"]"
    player_surname = "//input[@name=\"surname\"]"
    player_age = "//input[@name=\"age\"]"
    player_main_position = "//input[@name=\"mainPosition\"]"
    button_submit = "//*[text()=\"Submit\"]"
    add_player_edit_url = 'https://scouts-test.futbolkolektyw.pl/en/players/630e329f62fd50f9620fdc36/edit'

    def get_title(self) -> str:
        self.wait_for_element_be_clickable(self.button_main_page)
        return self.get_page_title(self.dashboard_url)

    def set_leg_value(self, value: str) -> None:
        self.wait_for_element_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.leg_wrapper_xpath)
        if value == "right":
            self.click_on_the_element(self.right_leg_xpath)
        if value == "left":
            self.click_on_the_element(self.left_leg_xpath)

    def click_button_submit(self):
        self.click_on_the_element(selector=self.button_submit)

    def filling_the_required_fields(self, name: str, surname: str, age: str, main_position: str):
        self.field_set_value(selector=self.player_name, value=name)
        self.field_set_value(selector=self.player_surname, value=surname)
        self.field_set_value(selector=self.player_age, value=age)
        self.field_set_value(selector=self.player_main_position, value=main_position)
        self.click_button_submit()
