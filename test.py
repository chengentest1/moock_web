import time
from selenium import webdriver

from base.findelement import FindElement

driver=webdriver.Chrome()
driver.get('http://www.uelaw.cn:8002/')
get_ele=FindElement(driver,file_name=None,node=None)
#取消体验金
get_ele.get_elemnet('test_mk')[0].click()
time.sleep(2)
#点击按钮弹出登录输出框
get_ele.get_elemnet('login_img').click()
#输入手机号
get_ele.get_elemnet('login_ss')[0].send_keys('18311135605')
#输入密码
get_ele.get_elemnet('login_ss')[1].send_keys('asdf123')
#点击登录按钮
get_ele.get_elemnet('login_button').click()
time.sleep(2)
#点击UE服务
get_ele.get_elemnet('UEServise').click()
time.sleep(1)
#选择自动生成
get_ele.get_elemnet('auto_build')[1].click()
time.sleep(2)
#输入搜索框
get_ele1=FindElement(driver,file_name=None,node='Auto_service')
# get_ele1.get_elemnet('Search_input').send_keys('asdf123')
# get_ele1.get_elemnet('Search_button').click()
get_ele1.get_elemnet('filetype').click()
get_ele1.get_elemnet('fxptestfile').click()
time.sleep(2)
get_ele1.get_elemnet('goTo_buite').click()
# driver.find_element_by_css_selector('div.searchpanel > span').click()