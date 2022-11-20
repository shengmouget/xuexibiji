# coding: utf-8 
# @Time    : 2022/11/13 下午6:54
a = []
n = int(input())
while n > 0:
    b = int(input())
    a.append(b)
    n = n - 1
a.sort()
print(a[0] - a[n-1])
