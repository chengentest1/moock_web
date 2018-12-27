import time
from selenium import webdriver

from base.findelement import FindElement
from page.autoBuitFile_page import AutoBuitFile_Page

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
#点击我的
driver.find_element_by_css_selector('.dis_inline.el-dropdown-selfdefine').click()
time.sleep(2)
#点击退出
# driver.find_element_by_css_selector('.el-dropdown-menu__item.c3').click()
#点击修改用户名
driver.find_element_by_css_selector('.ml-20.fz14.cursor').click()
#输入用户名
driver.find_elements_by_css_selector('.el-input__inner')[0].send_keys('神')
driver.find_element_by_css_selector('.el-button--default.el-button--mini').click()