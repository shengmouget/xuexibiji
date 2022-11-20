# coding: utf-8 
# @Time    : 2022/10/14 下午9:43
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select  #下拉列表
from selenium.webdriver.chrome.options import Options #无头浏览器
# 准备好配置
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disbale-gpu')
web = Chrome(options=opt)
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# 定位到下拉列表
sel_el = web.find_element(By.XPATH,'//*[@id="OptionDate"]')
# 对元素进行包装
sel = Select(sel_el)
# 让浏览器进行调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    table = web.find_element(By.XPATH,'//*[@id="TableList"]/table/tbody')
    print(table.text)
    print('................')
print('运行完毕')
web.close()

# 如何拿到页面代码Elements(经过数据加载以及js执行之后的结果的html内容)
print(web.page_source)
