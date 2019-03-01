import random
import math

'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数，则输出这个三位数的个位\十位\百位
如果等于程序随机数，则提示中奖，记100分
如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后八个是数字）
'''

def line():
    # 定义一个空字符串用于拼接字符
    str_num = ''
    # 循环前四个随机字母（用ASCII对应的值来随机再转化为字母）
    for i in range(4):
        num = random.randrange(97,123) # 65-90大写字母 97-122小写字母
        str_s = chr(num) #将ASCII码值转为对应字母
        str_num = str_num + str_s # 依次拼接得到的随机字母
    # 循环后8个随机数
    for i in range(8):
        num = random.randrange(0,10)
        str_num += str(num)
    return str_num
# 输入函数
num = input("请输入一个三位数")

random_num = random.randrange(100,1000)
# 输入函数输入的是字符类型，不强制转化会报错
if num.isdigit() and 100 <= int(num) <= 999:    # 输入函数返回的是字符类型，不能与整型直接比较，需要强制类型转换
    # 判断输入的数与系统随机数比较大小。
    if int(num) > int(random_num):
        # 求百位数字方法是地板除100或者用floor()函数
        bai = int(num)//100
        # 求十位数字方法是先取100的余数再地板除10
        shi = int(num)%100//10
        ge = int(num)%10
        print('这个数的百位是{}，十位是{}，个位是{}'.format(bai,shi,ge))
    if int(num) == int(random_num):
        pass
    if int(num) < int(random_num):
        # 由于120个字符每行12个可知只需存入10行就可以
        for i in range(10):
            str_line = line()
            # print(str_line)
            # 执行文件存入操作
            with open('str_num.txt', 'a') as f:
                f.write(str_line + '\n')
else:
    print("请按规定输入")

