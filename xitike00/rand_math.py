import random
import math

# 输入函数
num = input("请输入一个三位数")
# 输入函数输入的是字符类型，不强制转化会报错
if num.isdigit() and 100 <= int(num) <= 999:
    # 判断输入的数与系统随机数比较大小。
    pass
else:
    print("请按规定输入")