from page.home_page import HomePage


class HomeHandle(object):
    def __init__(self,driver):
        self.home_p=HomePage(driver)
    def clickExperience_gold(self):
        self.home_p.Experience_gold().click()
    def clickLogin_img(self):
        self.home_p.Login_img().click()
    def send_inputHone(self,phone):
        self.home_p.input_phone().send_keys(phone)
    def send_input_password(self,password):
        self.home_p.input_password().send_keys(password)
    def click_login_button(self):
        self.home_p.Login_img().click()
    def click_UEservice(self):
        self.home_p.UEservice().click()
    def select_auto_file(self):
        self.home_p.auto_file().click()