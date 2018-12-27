from base.findelement import FindElement


class AutoBuitFile_Page():
    def __init__(self,driver):
        self.find_e=FindElement(driver,file_name=None,node='Auto_service')
    def search_input(self):
        return self.find_e.get_elemnet('Search_input')
    def search_button(self):
        return self.find_e.get_elemnet('Search_button')
    def get_file_type(self):
        return self.find_e.get_elemnet('auto_file')
    def detail_file(self):
        return self.find_e.get_elemnet('life2')
    def generate_button(self):
        return self.find_e.get_elemnet('generate_button')
    def read_button(self):
        return self.find_e.get_elemnet('read_button')
    def next_button(self):
        return self.find_e.get_elemnet('next_button')[1]
    def option_ABCD_button(self):
        return self.find_e.get_elemnet('option_ABCD_button')
    def option_next_button(self):
        return self.find_e.get_elemnet('option_next_button')
    def drag_scroll(self):
        self.find_e.get_elemnet('drag_scroll')