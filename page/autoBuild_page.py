from base.findelement import FindElement
class AutoBuild(object):
    def __init__(self,driver):
        self.find_e = FindElement(driver)
    def search_input(self):
        return self.find_e.get_elemnet('Search_input')
    def search_button(self):

        return self.find_e.get_elemnet('Search_button')