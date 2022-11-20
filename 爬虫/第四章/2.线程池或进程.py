# coding: utf-8 
# @Time    : 2022/10/11 下午4:11
# 线程池 一次性开辟一些线程  用户直接给线程池提交任务 线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f"线程{i}")
    #      等线程结束后在执行   守护
    print('123')