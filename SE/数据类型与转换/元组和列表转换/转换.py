'''
元组 转为 列表 tuple(列表)
列表 转为  元组 list(元组)
'''
# list转换为tuple:

list1=[1,2,3]

tupl=tuple(list1)
print(type(tupl), tupl)


# tuple转换为list：
t3 = (1, 2, 3, 4, 5)
t3 = list(t3)
print(type(t3))
print(t3)
'''
<class 'tuple'> (1, 2, 3)
<class 'list'>
[1, 2, 3, 4, 5]
    '''