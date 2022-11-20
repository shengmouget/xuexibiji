# coding: utf-8 
# @Time    : 2022/10/8 下午11:49
import re
# findall匹配字符串中所有符合正则的内容
list = re.findall(r'\d+',"我的电话号是：10086,我电话号码：11234")
print(list)

# finditer:匹配字符串中所有的内容 返回的是迭代器 从迭代器拿到内容
it = re.finditer(r'\d+',"我的电话号是：10086,我电话号码：11234")
print(it)
for i in it:
    print(i.group())
# search返回的结果是match对象 要想那数据.group() 找到一个结果就返回
s = re.search(r'\d+',"我的电话号是：10086,我电话号码：11234")
s.group()
# match 是从头开始匹配
s = re.match(r'\d+',"10086,我电话号码：11234")
print(s.group())
print('--------------------------------------')


# 预加载正则表达式
obj = re.compile(r'\d+')
ret = obj.finditer("我的电话号是：10086,我电话号码：11234")
for i in ret:
    print(i.group())


print('=====================================')
s = """
<div class='jay'><span id='1'>郭麒麟</span><div>
<div class='xay'><span id='2'>张麒麟</span><div>
<div class='say'><span id='3'>李麒麟</span><div>
<div class='fay'><span id='4'>王麒麟</span><div>
<div class='tay'><span id='5'>盛麒麟</span><div>
"""
# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<wahh>.*?)</span><div>",re.S) #re.S 匹配换行符
result = obj.finditer(s)
for it in result:
    print(it.group("wahh"))


