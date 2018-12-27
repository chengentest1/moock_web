from base.findelement import FindElement


class AutoBuitFile_Page():
    def __init__(self,driver):
        self.driver=driver
        self.find_e=FindElement(driver,file_name=None,node='Auto_service')
    #搜索输入框
    def search_input(self):
        return self.find_e.get_elemnet('Search_input')
    #搜索按钮
    def search_button(self):
        return self.find_e.get_elemnet('Search_button')
    #文件类型
    def get_file_type(self,n):
        return self.driver.find_element_by_id('tab-%s'%(n))
    #详细合同
    def detail_file(self,n,m):
        return self.driver.find_element_by_css_selector('#pane-1 > ul:nth-child(%d) > li > div:nth-child(2) > ol:nth-child(%d) > li'%(n,m))
    #去生成按钮
    def generate_button(self):
        return self.find_e.get_elemnet('generate_button')
    #我已阅读复选框
    def read_button(self):
        return self.find_e.get_elemnet('read_button')
    #下一步
    def next_button(self):
        return self.find_e.get_elemnet('next_button')[1]
    #选项ABCD
    def option_ABCD_button(self):
        return self.find_e.get_elemnet('option_ABCD_button')
    #选项下一步
    def option_next_button(self):
        return self.find_e.get_elemnet('option_next_button')
    #拖动滚动条
    def drag_scroll(self):
        self.find_e.get_elemnet('drag_scroll')