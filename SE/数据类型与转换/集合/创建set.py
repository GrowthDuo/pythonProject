'''
集合：
set
特点 ：没有重复，无序的    没有下标    如果添加重复元素就添加不上


集合和字典的区别 :
集合 是单个的出现的
字典 需要成对出现 key,values

符号：
{}   {元素, 元素, 元素}            集合
{}   {key:value , key :value}   字典
'''

# 空子典
z ={}
print(type(z))  #<class 'dict'>

# 空集合
s = set()
print(type(s)) #<class 'set'>

# 非空集合
f = {'hello'}
print(type(f), f) #<class 'set'> {'hello'}

# 添加
# 方式1 ：add
s.add('盗墓笔记')
print(s)

s.add('三体')
print(s)

# 方式2 ：
# append 末尾追加  extend合并 ----》 列表
# add             update     ----> 集合

s2 = ('爱情公寓', '菜鸟教程')

# 将 s 与 s2 合并
s.update(s2)
print(s, type(s))      # {'三体', '爱情公寓', '盗墓笔记', '菜鸟教程'}


