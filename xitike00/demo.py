import math
# print(math)
'''
# ceil()向上取整
print(math.ceil(5.01))
print(math.ceil(5.9))

# floor()向下取整操作
print(math.floor(5.01))
print(math.floor(5.9))


# 查看系统保留关键字，不可以用来当作变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入操作 python内置函数
print(round(5.01))
print(round(5.5))


# sqrt() 开平方 返回浮点数
print(math.sqrt(4))
print(math.sin(0.5))
print(math.sqrt(3))


# pow() 与幂运算差不多，计算一个数的几次方，有底数和指数两个概念
print(math.pow(4,3)) #4的3次方
# 幂运算 函数返回浮点型，幂运算返回整型
print(4**3)



# fabs() 对一个数值获取他的绝对值 返回的也是浮点数
print(math.fabs(-1))
print(math.fabs(0))



# abs() 获取绝对值操作 不是数学模块当中，属于python内置函数 返回值由本身类型而定
print(abs(-1))
print(abs(1.8))



# fsum() 对整个序列求和
print(math.fsum([2,5,3,2]))
# sum() python 内置求和
print(sum([2,5,3,2]))



# math.modf() 将一个浮点数拆分为整数部分和小数部分组成元组,小数部分在前，整数部分在后
print(math.modf(3.7))
print(math.modf(3))



# copysign() 将第二个数的符号（正负号）传给第一个数, 返回第一个数值的浮点数
print(math.copysign(1,-5.32))
print(math.copysign(-1,5.32))

# 打印自然对数和pi的值
print(math.e)
print(math.pi)
'''

# 随机数模块

# 获取0-1之间的随机整数，包含0不包含1
import random
'''
for i in range(10):
    print(random.random())
    # 取边界具体F4看代码
    print(random.randint(1,5))
# random.randrange() 获取指定开始和结束之间的值，可以指定间隔值

print(random.randrange(1,4))

# choice() 随机获取列表中的值

print(random.choice([1,6,5,8,2.5,16151,32.3]))


# shuffle() 随机打乱序列 返回值是None

list1 = [2,6.32,545,312]
print(list1)
random.shuffle(list1)
print(list1)

'''

# uniform() 随机获取指定范围内的值（包括小数）