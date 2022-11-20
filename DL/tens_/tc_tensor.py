# coding: utf-8 
# @Time    : 2022/11/15 下午10:26
import torch
# 张量类型转换
data = torch.tensor([10,20,30])
data.to('cuda:0')
