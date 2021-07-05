# -*- coding:utf-8 -*-
"""
作者： Cutesk
日期：2021/6/21
项目：打印乘法表

"""

for i in range(1, 10):   # 表示行数
    for j in range(1, i+1):   # 输出与行数相同的列
        result = j * i
        print(str(j)+"x"+str(i)+"=" + str(result)+"\t", end="")
    print("")
