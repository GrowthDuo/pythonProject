'''
单个 for循环
列表推导式（List comprehension）是Python中一种方便且简洁的创建列表的方法。它们被用来快速的从一个可迭代对象（例如列表、元组、集合、字典、生成器等）中生成新的列表。

列表推导式的语法形式为：
  [i for i in  可迭代的]

 格式2 if： [i for i in  可迭代的  if 条件]
 格式3 if-else： [i.结果1（成立）  i.筛选条件   else i.结果2（筛选条件不成立） i for i in  可迭代的  if 条件]


```python
[expression for item in iterable if condition]
```

其中 `expression` 是要生成的新列表的元素表达式，`item` 是要迭代的可迭代对象中的元素，`iterable` 是要迭代的可迭代对象，`if condition` 是一个可选的条件，只有满足条件时才会生成符合条件的新元素。

例如，以下是一个简单的列表推导式，它从一个列表中生成一个新的平方数列表：

```python
old_list = [1, 2, 3, 4, 5]
new_list = [x**2 for x in old_list]
print(new_list) #[1, 4, 9, 16, 25]
```

你也可以添加一个可选的条件来过滤输入列表中的元素，例如：

```python
old_list = [1, 2, 3, 4, 5]
new_list = [x**2 for x in old_list if x % 2 == 0]
print(new_list) #[4, 16]
```

这个列表推导式只生成输入列表中的偶数的平方数列表。
'''

'''
isinstance()是Python中的一个内置函数，用于判断一个对象是否是指定类型（或者指定类型的子类）。

isinstance()的语法如下：

```
isinstance(object, classinfo)
```

其中，object表示待检测的对象，classinfo表示待检测的类型（或者类型元组）。

当对象object的类型是classinfo（或者是classinfo中的一个子类）时，该函数返回True，否则返回False。

下面是一个isinstance()的例子：

```
a = 5
b = 'hello'
print(isinstance(a, int))   # True
print(isinstance(b, str))   # True
print(isinstance(a, str))   # False
```

以上代码输出结果为：

```
True
True
False
```

在第一个isinstance()中，我们检测a是否是int类型，由于a是整型，因此返回True。

在第二个isinstance()中，我们检测b是否是str类型，由于b是字符串，因此返回True。

在第三个isinstance()中，我们检测a是否是str类型，由于a是整型而不是字符串，因此返回False。
'''

# 格式1： [i for i in  可迭代的]

# 输出1-20
list1 =[i for i in range(21)]
print(list1)

# 输出1-20的偶数
list2 =[i for i in range(0,21,2)]
print(list2)

# 格式2： [i for i in  可迭代的  if 条件]

# 筛选1-20的偶数
list3 = [i for i in range(21) if i%2 == 0]


# 打印是字母的
list4 =[21, 'hello', 34,'dit',45]
list5 =[i for i in list4 if isinstance(i,str)]
print(list5) # ['hello', 'dit']

# list4 =[21, 'hello', 34,'dit',45] 都转为字符串
list6 = [str(i) for i in  list4]
print(list6) # ['21', 'hello', '34', 'dit', '45']

# 打印是字母的
# 如果i 是 int类型转为字符串，如果不是则输出
zifu=[]
list = [str(i)  if type(i)==int  else zifu.append(i) for i in list4]
print(zifu)


# 如果是h开头的转为全部大写，如果不是则将首字母转为大写
list7 = ['dfg', 'hello', 'dfd','dit','hi']
list8 =[i.upper() if i.startswith('h') else i.title() for i in list7 ]
print(list8)


'''
for嵌套
如果需要在列表推导式中使用两个 `for` 嵌套，我们可以使用以下语法：

```python
[(i, j) for i in range(3) for j in range(2)]
```

这会产生如下输出：

```python
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

这个推导式使用两个 `for` 循环，将第一个循环的变量 `i` 与第二个循环的变量 `j` 组合起来产生新的元组 `(i,j)`，并加入列表中。

如果需要使用三个 `for` 嵌套，我们可以使用以下语法：

```python
[(i, j, k) for i in range(3) for j in range(2) for k in range(4)]
```

这会产生如下输出：

```python
[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 1, 3)]
```

这个推导式使用了三个 `for` 循环，将三个循环的变量 `i`、`j`、`k` 组合起来生成新的元组 `(i, j, k)`，并添加到列表中。

注意，在实际使用中，使用多个循环的列表推导式可能会导致程序难以理解。我们应该根据具体情况来决定是否使用多个循环。

'''