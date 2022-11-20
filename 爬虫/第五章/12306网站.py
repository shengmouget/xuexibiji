# coding: utf-8 
# @Time    : 2022/10/14 下午10:47
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
# 滑块解决方案

# chrome的版本大于88 固定写法
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')

# 定位 输入账号密码
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('17671148982')
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('shengwei20001112')
web.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(5)

# 拉滑块


btn = web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()


