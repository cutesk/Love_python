# -*- coding:utf-8 -*-
"""
作者： Cutesk
日期：2021/6/21

"""


# while 循环

none = True
number = 0

while none:
    number += 1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("该值是:", number)
        none = False   # 注意该值，否则会产生死循环

