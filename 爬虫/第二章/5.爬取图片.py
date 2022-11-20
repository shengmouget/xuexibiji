# coding: utf-8 
# @Time    : 2022/10/9 下午10:04
# 拿到主页面源代码 提取到子页面的链接地址
# 通过href拿到子页面类容 从子页面中找到图片的下载地址
import requests
import bs4
import time
url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
resp = requests.get(url)
resp.encoding = 'utf-8' #处理乱码
# print(resp.text)
# 把源代码交给bs
main_page = bs4.BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("div",class_='Clbc_Game_l_a').find_all('a')
# print(alist)
list_herf = []
for a in alist:
    herf = 'https://www.umei.cc' + a.get('href')
    list_herf.append(herf)
set_herf = set(list_herf)
for herf_child in set_herf:
    # print(herf_child)
    # 拿到子页面源代码
    child_page_resp = requests.get(herf_child)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
# #     从子页面拿到图片下载路径
    child_page = bs4.BeautifulSoup(child_page_text,"html.parser")
    img = child_page.find('div',class_='big-pic')
    img_im = img.find('img')
    img_src = img_im.get("src")
    # print(img_src)
#     下载图片
    img_resp = requests.get(img_src)
    img_resp.content #这里拿到的是字节
    img_name = img_src.split('/')[-1] #以/为分届劈开
    with open('img/'+img_name,'wb') as f:
        f.write(img_resp.content)
    print("over",img_name)
    time.sleep(1)

print("all over")
f.close()
resp.close()


