from base.findelement import FindElement


class MY_Page(object):
    def __init__(self,driver):
        self.driver=driver
        self.find_e = FindElement(driver, file_name=None, node='my_page')
    #头像标签
    def Head_portrait(self):
        return self.find_e.get_elemnet('Head_portrait')
    #退出标签
    def quit_button(self):
        return self.find_e.get_elemnet('quit_button')
    #我的订单
    def my_order(self):
        return self.find_e.get_elemnet('my_order')[1]
    #筛选条件
    def filter_condition(self):
        return self.find_e.get_elemnet('filter')
    #状态条件
    def status_condition(self):
        return self.find_e.get_elemnet('status')
    #代付款条件
    def waiting_payment(self):
        return self.find_e.get_elemnet('waiting_payment')
    #搜索条件提交按钮
    def submit_condition(self):
        return self.find_e.get_elemnet('submit')
