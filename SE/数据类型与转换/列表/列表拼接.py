'''
列表拼接两种方式
1、 使用 + 号拼接
2、 使用 extend  （会将列表拆开，一一取出里面元素添加到另一个列表, 相当于是以元素的形式添加，不是列表）
'''

list1 =[]

# 向 list1 列表中添加一些动物
list1.append('狗')
list1.append('狗')
list1.append('狗')
list1.append('狗')
list1.append('狗')

print(list1)

list2 = ['zoo']


# list1 = list1.extend(list2) # 结果为 None
'''
可能是因为 list1.extend(list2) 方法没有返回值（或者说返回了 None）。所以在赋值语句 list1=list1.extend(list2) 中，
    list1 实际上被赋值为 None，而不是被扩展后的列表。

解决 ：
list1 = [...]
list2 = [...]

list1.extend(list2)  # 不需要赋值，直接扩展即可
print(list1)
或者修改原来的方法，将两行代码合并为一行：

list1 += list2  # 等价于 list1.extend(list2)
print(list1)
'''
print(list1+list2) #['狗', '狗', '狗', '狗', '狗', 'zoo']
print(list1)
