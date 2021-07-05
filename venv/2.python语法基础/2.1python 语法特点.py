# -*- coding:utf-8 -*-
"""
作者： Cutesk
日期：2021/4/6

"""

# 充值业务
# print("欢饮使用XXX充值业务，请输入充值金额：")
#
# value = float(input("请输入充值金额："))
# print(value)
#
# print("充值成功，您本次充值{}元。".format(value))

# 预测儿子的身高
# father_high = float(input("请输入父亲的身高（单位：m）："))
#
# mather_high = float(input("请输入母亲的身高（单位：m）："))
#
# son_high = (father_high + mather_high ) * 0.54
#
# print("预测儿子的身高为：", son_high)


# 消耗的热量
number = float(input("请输入步数（单位：步）："))

cal = float(number / 28)

# print('%.2f' % cal)
print("今天共消耗卡路里（单位：千卡）：", '%.2f' % cal)

