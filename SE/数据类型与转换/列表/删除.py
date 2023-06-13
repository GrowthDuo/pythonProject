'''
删除

根据下标删除,  不添加下标默认从后往前删除
pop( ) 默认形式

根据变量名（value）删除
remove( )  默认情况下是删除第一个，从左到右  如果使用remove删除有多个一样的挨着的value值, 可能会漏删。

clear( ) 清空元素

del 列表名    删除列表
del 元素      删除元素




'''

# pop  默认形式  ['🐏', '🐱', '🐕']

list1 = ['🐏', '🐱', '🐕', '驴']
list1.pop()
print(list1)

# pop  指定下标   ['🐏', '🐕', '驴']

list2 = ['🐏', '🐱', '🐕', '驴']
list2.pop(1)
print(list2)

# remove  根据变量名删除
list3 = ['一', '二', '三', '四', '五', '三']

# 删除 '三'  默认情况下是删除第一个，从左到右    可以通过循环实现删除多个
list3.remove('三')
print(list3)  # ['一', '二', '四', '五', '三']

# remove通过循环实现删除多个
'''
如果有多个一样的value值，默认情况下是删除第一个，从左到右 。

ps : 如果使用remove删除有多个一样的挨着的value值, 可能会漏删。
     如 下面例1。
'''
li = ['你好', '天才', 'hh', 'hh', '呀！']
# 将 ‘hh’ 都删除
for i in li:
    if i == 'hh':
        li.remove(i)
print(li)  # ['你好', '天才', 'hh', '呀！']

'''
range() 函数来倒序遍历列表 li，从最后一个元素开始遍历，到第 0 个元素结束（不包含第 0 个元素）。在遍历的过程中，如果当前元素是 'hh'，我们使用 remove() 方法将其从列表中删除。

需要注意的是，在循环中修改列表的操作可能会引发问题，因为修改列表之后，列表的长度和索引会发生改变。为了避免这种问题，我们使用倒序的方式遍历列表，这样删除元素时就不会影响到后面的元素。

'''
for i in range(len(li) - 1, -1, -1):

    if li[i] == 'hh':
        li.remove('hh')

print(li)

for i in li[:: -1]:
    if li == 'hh':
        li.remove(i)

print(li)

# 使用while实现
length = len(li)
i = 0
# length-1 为最后一个值的下标
while i < length:
    if li[i] == 'hh':
        li.remove(li[i])  # 如果是删除后还停留在原位判断
    else:
        i += 1  # 如果不是则往后判断
print(li)

# clear 清空
list4 = [1, 2, 3]
list4.clear()
print(list4)

# del
list5 = [1, 2, 3, 4, 5, 6]
# 根据下标删除
del list5[1]
print(list5)
# 删除列表
list6 = [1, 2, 3, 4, 5, 6]
del  list6
print(list6)
