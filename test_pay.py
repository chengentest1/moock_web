import time
from selenium import webdriver

from base.findelement import FindElement
from page.autoBuitFile_page import AutoBuitFile_Page

driver=webdriver.Chrome()
driver.get('http://www.uelaw.cn:8002/')
driver.implicitly_wait(20)
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
d=AutoBuitFile_Page(driver)
time.sleep(2)
d.get_file_type().click()
d.detail_file().click()
d.generate_button().click()
time.sleep(4)
# d.drag_scroll()
driver.execute_script('document.documentElement.scrollTop=600')
d.read_button().click()
time.sleep(3)
d.next_button().click()
time.sleep(4)
d.option_ABCD_button()[0].click()
d.option_next_button()[1].click()










# get_ele.get_elemnet('Search_input',file_name=None,node='Auto_service').send_keys('asdf123')
# get_ele.get_elemnet('Search_button',file_name=None,node='Auto_service').click()
# 文件类型-选择投资及公司运营管理类法律文件
# driver.find_element_by_css_selector('#tab-1').click()
# time.sleep(2)
#选择长期采购合同




# driver.find_element_by_css_selector('#pane-1 > ul:nth-child(1) > li > div:nth-child(2) > ol:nth-child(2) > li').click()
# time.sleep(1)
# #点击去生成
# driver.find_element_by_css_selector('.btn-generate.text-center').click()
# # driver.find_element_by_css_selector('.el-checkbox__inner').click()
# # driver.find_element_by_class_name('el-checkbox__inner').click()
# time.sleep(1)
# #拉动滚动条
# js="var q=document.documentElement.scrollTop=400"
# driver.execute_script(js)
# time.sleep(3)
# # hj="var u=document.getElementsByClassName('el-checkbox__input')[0].click()"
# # driver.execute(hj)
# #勾选我已阅读
# driver.find_element_by_class_name('el-checkbox__inner').click()
# #点击下一步
# driver.find_elements_by_css_selector('.btn_switch.cursor')[1].click()
# #选择A
# driver.find_elements_by_css_selector(".el-radio__inner")[0].click()
# time.sleep(2)
# #选择下一步
# driver.find_elements_by_css_selector('.btn_switch.cursor')[1].click()
# #选择A
# time.sleep(2)
# driver.execute_script("document.documentElement.scrollTop=40")
# driver.find_elements_by_css_selector(".el-radio__inner")[0].click()
# # driver.execute_script("document.getElementsByClassName('el-radio__input')[0].click()")
# #选择下一步
# time.sleep(2)
# driver.find_elements_by_css_selector('.btn_switch.cursor')[1].click()
#
# time.sleep(2)
# driver.find_elements_by_css_selector(".el-radio__inner")[1].click()
# driver.find_elements_by_css_selector(".btn_switch.cursor")[1].click()
# time.sleep(2)
# driver.find_elements_by_css_selector(".el-radio__inner")[1].click()
# driver.find_elements_by_css_selector(".btn_switch.cursor")[1].click()
# time.sleep(2)
# driver.find_elements_by_css_selector(".el-radio__inner")[1].click()
# driver.find_elements_by_css_selector(".btn_switch.cursor")[1].click()
#
# time.sleep(2)
# driver.find_elements_by_css_selector(".el-radio__inner")[1].click()
# driver.find_elements_by_css_selector(".btn_switch.cursor")[1].click()
# time.sleep(2)
# driver.find_element_by_css_selector(".btn-generate ").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".btn-orangeB").click()
# time.sleep(3)
# driver.find_element_by_id("input").send_keys("123456")
# time.sleep(1)
# driver.find_elements_by_css_selector(".el-button.btn-ToastConfirm")[0].click()