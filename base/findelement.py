from util.read_ini import ReadIni
from selenium import webdriver
# file=ReadIni()
# h=file.get_value('user_email')
# h.split('>')[0]
# print(h.split('>')[0])
class FindElement(object):
    def __init__(self,driver):
        self.driver=driver
    def get_elemnet(self,value,file_name=None,node=None):

        file=ReadIni(file_name,node)
        h=file.get_value(value)
        by=h.split('<')[0]
        value=h.split('<')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
            elif by=='class':
                return self.driver.find_element_by_name(value)
            elif by=='xpath':
                return self.driver.find_element_by_xpath(value)
            elif by=='css':
                return self.driver.find_element_by_css_selector(value)
            elif by=='classNames':

                return self.driver.find_elements_by_class_name(value)
            else:
                return self.driver.find_element_by_link_text(value)
        except:
            return None
