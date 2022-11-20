# coding: utf-8 
# @Time    : 2022/10/11 下午5:17
# 一般情况下  当程序处于IO状态的时候 线程都处于阻塞状态
# 协程当程序遇见IO操作的时候 可以选择性的切换到其他任务上
# 在微观上 是一个任务一个任务的进行切换  切换条件一般就是IO操作
# 在宏观上 我们能看到的其实是多任务一起在执行
# 上方所讲的一切 都是在单线程的条件下

import asyncio
import time
# async def func():
#     print("你好")
#
# if __name__ == '__main__':
#     g = func()  #此时的函数是异步协程函数 此时函数执行得到的是一个协程对象
#     asyncio.run(g)  #协程运行需要asyncio模块支持
async def func1():
    print('你好呀 潘金莲1')
    # time.sleep(3)
    await asyncio.sleep(3) #异步操作代码 程序挂起  切换其他的
    print('你好呀 潘金莲2')
async def func2():
    print('你好呀 川建国1')
    await asyncio.sleep(2)
    print('你好呀 川建国2')
async def func3():
    print('你好呀 胖揍宕1')
    await asyncio.sleep(1)
    print('你好呀 胖揍宕2')

# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [
#         f1,f2,f3
#     ]
#
#     # 一次性启动多个任务（协程）
#     asyncio.run(asyncio.wait(tasks))  #多个任务
async def main():
    tasks = [
        func1(),func2(),func3()
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
