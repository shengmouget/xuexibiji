# coding: utf-8 
# @Time    : 2022/11/4 上午10:16
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
if __name__ == '__main__':
    data = pd.read_excel('data/皇帝年龄.xlsx',index_col=0)
    # print(data)
    # print(data.values)
    # print(data.index)
    # print(data.columns)
    # print(data.values[3])
    # print(data.index[3])
    # print(type(data.iloc[3]))
    # print(type(data))
    # print(data.dtypes)
    # print(data.describe())
    # print(plt.rcParams)  #输出plt所有参数
    # plt.rcParams['font.family'] = 'simHei'
    # plt.plot(data.iloc[:100,0],data.iloc[:100,1],'ro',ms=4)
    # plt.xticks(rotation=90,fontsize=6)
    # plt.show()
    # sel = data['年龄'] >= 70
    # print(np.mean(sel))
    # print(pd.value_counts(sel)) #统计隐码
    # print(data.loc[sel,'名'])
    # print(data.iloc[:1])
    # print(data.loc[sel])
    plt.rcParams['font.family'] = 'simHei'
    N = 10
    ages = data.iloc[:N,1].values
    x = np.arange(N)
    f = interp1d(x,ages,kind='cubic')
    xx = np.linspace(x.max(),x.min(),100)
    yy = f(xx)
    plt.plot(x,ages,'ko',ms=6)
    plt.plot(xx,yy,'r-',lw=2)
    plt.show()




