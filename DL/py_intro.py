# coding: utf-8 
# @Time    : 2022/11/3 下午10:09
import re
import pandas as pd
with open('data/皇帝年龄.txt','r',encoding='utf-8') as f:
    text = f.readlines()
    result = pd.DataFrame(columns=['名','年龄','出生','崩'])
    age_c = re.compile('(\d+)岁', re.S)
    birth_pass_c = re.compile('(前?\d+)年', re.S)
    name_c = re.compile('\d*[黄祖宗]*(.*?)\d+岁')
    for line in text:
        age = age_c.findall(line)
        birth_pass = birth_pass_c.findall(line)
        name = name_c.findall(line)
        if age and len(birth_pass) == 2 and name:
            result.loc[f'第%d位'% (len(result)+1)] = [name[0],age[0],birth_pass[0],birth_pass[1]]
    print(result)
    print(result.to_excel('data/皇帝年龄.xlsx'))



