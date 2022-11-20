# coding: utf-8 
# @Time    : 2022/10/11 下午3:40
"""
线程：执行单位
进程：资源单位 每一个进程至少要有一个线程
"""
# 启动一个程序 默认都会有一个主线程
"""python实现多线程需要导入threading包"""
from threading import Thread  #线程类
from multiprocessing import Process #进程
# # 第一套写法
# def fun():
#     for i in range(1000):
#         print("fun",i)
#
# if __name__ == '__main__':
#     t = Thread(target=fun)  #创建多线程 并安排任务
#     t.start() #多线程状态为开始工作状态 具体执行时间由CPU决定
#     for i in range(1000):
#         print('main',i)

# 第二套写法
# class MyThead(Thread):
#     def run(self): #固定的
#        for i in range(1000):
#            print('子线程',i)
#
# if __name__ == '__main__':
#     t1 = MyThead() #传参数 必需是元组
#     t1.start() #开启线程
#     for i in range(1000):
#         print('主线程',i)

# 进程
# def func():
#     for i in range(1000):
#         print('子进程',i)
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(1000):
#         print('主进程',i)
