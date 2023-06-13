'''
运算符
    赋值运算符 ： +  -  /  %  //（整除） **（幂次方）
    赋值运算符 ： = +=  -=
    比较运算符 ： > < >= <= == !=
    逻辑      ： and(两边都为true则true)  or  not
'''
from asyncio import sleep
import random
# random.randint(0, 3) 可以生成从 0 到 3（包括 0 和 3）之间的整数。
# a = 5
# b = 2
# print(a//b)
# print(b//a)
# print(b/a)
# print(b%a) # 2
#
# 输入三位数，求出各个位数
num = int (input('输入'))
print('个位' , num % 10)
print('十位', num //10 %10)
print('百位', num//100)
s = 'abcdefg1234567890'
print(len(s))
name =''

for i in range(6):
    ran2 = random.randint(0, len(s)-1)
    name += s[ran2]
print(name)
