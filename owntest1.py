import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from base.findelement import FindElement
from page.autoBuitFile_page import AutoBuitFile_Page
from page.own_page import MY_Page

driver=webdriver.Chrome()
driver.get('http://www.uelaw.cn:8002/')
driver.implicitly_wait(20)
driver.maximize_window()
get_ele=FindElement(driver)
time.sleep(2)
#取消体验金
get_ele.get_elemnet('test_mk')[0].click()
time.sleep(2)
#点击按钮弹出登录输出框
get_ele.get_elemnet('login_img').click()
#输入手机号
get_ele.get_elemnet('login_ss')[0].send_keys('18311135605')
#输入密码
get_ele.get_elemnet('login_ss')[1].send_keys('asdf123')
get_ele.get_elemnet('login_button').click()
time.sleep(2)
h=MY_Page(driver)
h.Head_portrait().click()
h.my_order().click()
h.filter_condition().click()
h.status_condition().click()
h.waiting_payment().click()
time.sleep(1)
# h.submit_condition().click()