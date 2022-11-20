# coding: utf-8 
# @Time    : 2022/10/13 下午11:03
# 让程序链接到浏览器  让浏览器完成各种复杂的操作 我们只接受最后结果
# selenium ：自动化测试工具
# 程序员可以从selenium中直接提取网页上的各种信息
# 环境搭建：1 下载selenium  2 下载浏览器驱动
# 让selenium启动浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 1.创建一个浏览器
web = Chrome()
# 2.打开一个浏览器
web.get('http://lagou.com')
# 找到某个元素点击他
el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[8]/a')
el.click()  #点击事件
time.sleep(1)
# 找到输入框 输入python 点回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)
# 查找存放的数据位置 进行数据提取
# 找到页面中所有的div
div_list = web.find_elements(By.XPATH,'/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')
for div in div_list:
    dirver = div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    price = div.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    print(dirver,price)
# /html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a
# /html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span
# 如何进入到窗口中进行提取 注意 在selenium的眼中  新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])

# 在新窗口中提取内容

# 关掉新窗口
web.close()
web.switch_to.window(web.window_handles[0])  #变更视角 回到原来的窗口中