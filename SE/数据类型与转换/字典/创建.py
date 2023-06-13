'''
字典由 一对一对键值对组成，其中键（key）是唯一的，不可重复的，不可改变的

新建
添加
修改
'''

zidian = {}
print(type(zidian))  # <class 'dict'>

# 添加

# 分行添加各个键值对
zidian['name'] = '李'
zidian['age'] = 12

print(zidian)

# 直接添加
zidian2 = {'id': 1, 'Username': 'xzd', 'password': 123456}
print(zidian2)

# 修改
zidian['name'] = '张'
zidian['age'] = 14
print('修改后 ： ', zidian)

# 删除
# pop删除 ：根据key实现删除，删除的是键值对，返回key对应的value
zidian2.pop('Username')
print(zidian2 )

# 删除方法popitem 从后往前删
'''
  def popitem(self, *args, **kwargs): # real signature unknown
        """
        Remove and return a (key, value) pair as a 2-tuple.
        
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        pass
        
移除（键，值）对并将其作为2元组返回。
 
对按后进先出顺序返回。

如果dict为空，则引发KeyError。        
'''
zidian2.popitem()

# del删除键值对
del zidian['name']

# 删除字典
del zidian

book ={}

# 添加 setdefault
'''
 def setdefault(self, *args, **kwargs): # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        """
        pass
如果关键字不在字典中，请插入具有默认值的关键字。


如果关键字在字典中，则返回关键字的值，否则为默认值。        
'''
#   只能做添加键值对元素使用
book.setdefault('出版社','cd')

# 尝试使用setdefault修改value值、
book.setdefault('出版社','充电线')

print(book)    # {'出版社': 'cd'}

# 使用常规修改
book['出版社']='地方v发'
print(book)

# update  合并
'''
 def update(self, E=None, **F): # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass
        
如果E存在并且有.keys（）方法，则执行：对于E:D[k]=E[k]中的k

如果E存在并且缺少.keys（）方法，则执行：对于E:D[k]=v中的k，v

在任何一种情况下，后面跟着：对于F:D[k]=F[k]中的k        
'''
# 合并字典
zoo ={'name':'天天动物园'}
zoo.update(book)
print(zoo)

# 尝试使用 + 号
# print(zoo+book)
# 报错 TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# fromkeys新建字典 属于类，可以直接使用字典类调用
# fromkeys新建字典的值是一个整体 key value共享一个
""" 
Create a new dictionary with keys from iterable and values set to value. 

创建一个新的字典，其中键来自iterable，值设置为value。

"""
s=dict.fromkeys(['id','name'])
print(s)

t =dict.fromkeys(['D','P'],1)
print(t)