from pages.base_page import BasePage


class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//input[@type='password']"
     sign_in_button_xpath = "//*[text()='Sign in']"
     login_url = ('https://scouts-test.futbolkolektyw.pl/login')
     # expected_title =
     # title_of_box =
     # header_of_box =


     def type_in_login(self, login):
       self.field_set_value(selector=self.login_field_xpath, value=login)

     def type_in_password(self, password):
       self.field_set_value(selector=self.password_field_xpath, value=password)

     def click_sign_in_button(self):
       self.click_on_the_element(selector=self.sign_in_button_xpath)
