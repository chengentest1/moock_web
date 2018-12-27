from util.read_ini import ReadIni
from selenium import webdriver
# file=ReadIni()
# h=file.get_value('user_email')
# h.split('>')[0]
# print(h.split('>')[0])
class FindElement(object):
    def __init__(self,driver,file_name=None,node=None):
        self.driver=driver
        self.file_name=file_name
        self.node=node
        self.file = ReadIni(self.file_name, self.node)
    def get_elemnet(self,value):

        h=self.file.get_value(value)
        by=h.split('<')[0]
        valu=h.split('<')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(valu)
            elif by=='name':
                return self.driver.find_element_by_name(valu)
            elif by=='class':
                return self.driver.find_element_by_class_name(valu)
            elif by=='xpath':
                return self.driver.find_element_by_xpath(valu)
            elif by=='css':
                return self.driver.find_element_by_css_selector(valu)
            elif by=='css_s':
                return  self.driver.find_elements_by_css_selector(valu)
            elif by=='classNames':
                return self.driver.find_elements_by_class_name(valu)
            elif by=='js':
                return self.driver.execute_script(valu)
            else:
                return self.driver.find_element_by_link_text(valu)
        except:
            return None
