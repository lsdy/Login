# -*- coding: utf-8 -*-
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

firefox_options=Options()
firefox_options.add_argument('-headless')
driver=Firefox(firefox_options=firefox_options)
driver.get("https://passport.baidu.com/v2/?login")
driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()

# 输入账号密码
driver.find_element_by_name("userName").send_keys("账号")
driver.find_element_by_name("password").send_keys("密码")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='pass-button pass-button-submit']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("baidu.png")