import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
# driver.find_element_by_css_selector('.ml-20.fz14.cursor').click()
#输入用户名
# driver.find_elements_by_css_selector('.el-input__inner')[0].send_keys('kk')
#修改用户名，点击确认
# driver.find_element_by_css_selector('.el-button--default.el-button--mini').click()
#点击修改手机号
# driver.find_element_by_css_selector('ul.myul > li:nth-child(1) > div > span.cursor').click()
#输入手机号
# jk='#app > div > div > div.personalIndex_all > div > div.router-nav.fl > div > div.forprivate > div:nth-child(2) > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input'
# driver.find_element_by_css_selector(jk).send_keys('18311135605')
# #点击获取验证码
# driver.find_element_by_css_selector('.spanCode').click()
# #填写验证码
# driver.find_element_by_css_selector(jk).send_keys(Keys.TAB).click()
# ml='#app > div > div > div.personalIndex_all > div > div.router-nav.fl > div > div.forprivate > div:nth-child(2) > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input'
# driver.find_element_by_css_selector(ml).send_keys('sdfgh')



# #点击修改登录密码
# driver.find_element_by_css_selector('ul.myul  > li:nth-child(2) > div > span.cursor').click()
# #输入旧密码
# driver.find_elements_by_css_selector('[autocomplete="off"]')[0].send_keys('jhdj')
# #输入新密码
# driver.find_elements_by_css_selector('[autocomplete="off"]')[1].send_keys('jhdje')
# #输入重复密码
# driver.find_elements_by_css_selector('[autocomplete="off"]')[2].send_keys('jhwdj')
# #点击确定
# driver.find_elements_by_css_selector('button.el-button.btn-ToastConfirm.el-button--default.el-button--mini>span')[0].click()

#点击我的订单
driver.find_elements_by_css_selector('.luyouspan')[1].click()
time.sleep(3)
driver.find_element_by_css_selector('.screen_title>span:nth-child(2)').click()
driver.find_element_by_css_selector('.screen_content>li>div>div>span').click()
driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2) > span').click()