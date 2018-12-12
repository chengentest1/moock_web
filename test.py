import time
from selenium import webdriver

from base.findelement import FindElement

driver=webdriver.Chrome()
driver.get('http://www.uelaw.cn:8002/')
get_ele=FindElement(driver)
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
