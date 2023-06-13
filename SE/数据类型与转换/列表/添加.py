'''
使用 append   将列表以整体的形式添加
使用 extend  （会将列表拆开，一一取出里面元素添加到另一个列表, 相当于是以元素的形式添加，不是列表）
'''
list1 = []

# 向 list1 列表中添加一些动物
list1.append('狗')
list1.append('狗')
list1.append('狗')
list1.append('狗')
list1.append('狗')

print(list1)

list2 = []
list2.extend('猫')
print(list2)

# 添加时差别

# append
l1 = [0]
l2 = [1, 2, 3]
l1.append(l2)
# l1[0, [1, 2, 3]]
print(l1)

# extend
l3 = [5]
l4 = [6, 7, 8, 9]
l3.extend(l4)
print(l3)  # [5, 6, 7, 8, 9]
