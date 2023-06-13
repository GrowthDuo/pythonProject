'''
    目录 ：
     数据类型
    保留输出格式
'''

"""
 数据类型
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；**

    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。**

    此外还有一些高级的数据类型，如: 字节数组类型(bytes)。**

#### Number（数字）

Python3 支持 **int、float、bool、complex（复数）**。

        int
        float
        string
        boolean
"""

money = '1万'
# <class 'str'>字符串
print(type(money))


# isinstance 和 type 的区别在于：
#
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))








# 保留输出格式
shi = '''
    苏轼——《水调歌头》

　　明月几时有，把酒问青天。

　　不知天上宫阙，今夕是何年?

　　我欲乘风归去，又恐琼楼玉宇，高处不胜寒。

　　起舞弄清影，何似在人间!

　　转朱阁，低绮户，照无眠。

　　不应有恨，何事长向别时圆?

　　人有悲欢离合，月有阴晴圆缺，此事古难全。

　　但愿人长久，千里共婵娟。
'''
print(shi)