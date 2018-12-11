from base.findelement import FindElement


class HomePage(object):
    def __init__(self,driver):
        self.find_e=FindElement(driver)

    #取消体验金
    def Experience_gold(self):
        return self.find_e.get_elemnet('test_mk')
    #点击按钮弹出登录输出框
    def Login_img(self):
        return self.find_e.get_elemnet('login_img')
    #输入手机号
    def input_phone(self):
        return self.find_e.get_elemnet('login_ss')[0]
    #输入密码
    def input_password(self):
        return self.find_e.get_elemnet('login_ss')[1]
    #点击登录按钮
    def click_login_button(self):
        return self.find_e.get_elemnet('login_button')
    #点击UE服务
    def click_UEservice(self):
        return self.find_e.get_elemnet('UEServise')
    #选择自动生成
    def auto_file(self):
        return self.find_e.get_elemnet('auto_build')[1]
