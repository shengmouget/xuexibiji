# coding: utf-8 
# @Time    : 2022/10/14 下午10:13
# 1.手动写头像识别
# 2.选择互联网上成熟的验证码破解工具
# 超级鹰 干 超级鹰
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time

web = Chrome()
web.get('https://www.chaojiying.com/user/login/')

# 处理验证码
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('17671148982', 'shengwei20001112', '940055')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 像页面中添加用户名 账号 密码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('17671148982')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('shengwei20001112')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)


time.sleep(4)
# 点击登陆
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
