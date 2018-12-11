from base.findelement import FindElement


class HomePage(object):
    def __init__(self,driver):
        self.find_e=FindElement(driver)
