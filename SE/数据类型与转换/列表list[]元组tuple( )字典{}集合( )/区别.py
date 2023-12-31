'''

列表list[]     允许重复，有序，有下标
元组tuple( )   允许重复，有序，不能增删改，只能查看
字典dict{}     键值对存在， 键 ：唯一的，值： 允许重复
集合set( )       不允许存在，无序，无下标

类型转换：
list ----》tuple,set(长度可能发生改变)
tuple -----> list,set
set -------->list,tuple

dict------->list  tuple  set  只会把键key 提出来。

list------>dict  需要特定格式  list = [('a',10),('b',20),('c',[12,34,45])] 成对出现才可以且key是唯一的,value可以是多个

运算符：
+  合并  支持 ： 字符串 列表 元组
* 复制   支持 ： 字符串 列表 元组
in   判断       字符串 列表 元组 字典
not in          字符串 列表 元组 字典

'''
'''
AI:
列表（List）: 有序序列，可变，用中括号[]表示。示例：my_list = [1, 2, 'apple']

元组（Tuple）: 有序序列，不可变，用圆括号()表示。示例：my_tuple = (1, 2, 'apple')

字典（Dictionary）: 无序映射，由键值对组成，key是唯一的，用花括号{}表示。示例：my_dict = {'apple': 2, 'banana': 1, 'orange': 3}

集合（Set）: 一组无序、不重复元素的集合，用花括号{}或set()函数表示。示例：my_set = {1, 2, 3, 'apple'}

需要注意的是，元素的可变性是指元素本身是否可以被修改，而不是元素中的对象是否可变，
例如一个元素是一个列表，那么这个列表可以继续修改。此外，虽然字典是无序的，但是在Python 3.7及以后版本，字典保证元素存储的顺序是稳定的。
'''

'''
AI 运算符
好的，以下是具体列举：

1. 列表支持的运算符

- `+`：连接两个列表。
- `*`：重复列表元素。
- `in`：判断元素是否在列表中。
- `not in`：判断元素是否不在列表中。
- `[]`：通过索引获取元素。
- `[:]`：切片操作，获取列表的子序列。
- `[i:j:k]`：扩展切片操作，根据步长获取列表的子序列。
- `len()`：获取列表的长度。
- `list()`：将其他类型转换为列表。
- `max()`：获取列表中最大的元素。
- `min()`：获取列表中最小的元素。
- `sorted()`：对数组进行排序。
- `sum()`：求列表元素的和。

2. 元组支持的运算符

- `+`：连接两个元组。
- `*`：重复元组元素。
- `in`：判断元素是否在元组中。
- `not in`：判断元素是否不在元组中。
- `[]`：通过索引获取元素。
- `[:]`：切片操作，获取元组的子序列。
- `[i:j:k]`：扩展切片操作，根据步长获取元组的子序列。
- `len()`：获取元组的长度。
- `tuple()`：将其他类型转换为元组。
- `max()`：获取元组中最大的元素。
- `min()`：获取元组中最小的元素。

3. 字典支持的运算符

- `[]`：通过键获取值。
- `in`：判断键是否在字典中。
- `not in`：判断键是否不在字典中。
- `len()`：获取字典中键值对的数量。
- `dict()`：将key-value列表转换为字典。
- `items()`：返回包含所有（key,value）对元组的列表。
- `keys()`：返回包含所有键的列表。
- `values()`：返回包含所有值的列表。

4. 集合支持的运算符

- `&`：求交集。
- `|`：求并集。
- `-`：求差集。
- `^`：求对称差集（即两个集合的并集减去交集）。
- `in`：判断元素是否在集合中。
- `not in`：判断元素是否不在集合中。
- `len()`：获取集合中元素个数。
- `set()`：将其他类型转换为集合。

需要注意的是，每种类型的运算符支持的操作不完全相同，
例如元组不支持修改元素，字典和集合不支持切片操作等，
因此在使用时要注意操作的正确性和合理性。
'''

'''
AI:常用方法
好的，以下是它们常用的方法：

1. 列表常用的方法

- `append(x)`：在列表末尾添加元素x。
- `extend(iterable)`：在列表末尾添加迭代对象iterable中所有元素。
- `insert(i,x)`：在列表的第i位置插入元素x。
- `remove(x)`：从列表中删除第一个值为x的元素。
- `pop(i)`：删除列表中第i个元素并返回该元素。
- `index(x)`：返回列表中第一个值为x的元素所在的索引位置。
- `count(x)`：统计列表中值为x的元素出现的次数。
- `sort()`：将列表按升序排序。
- `reverse()`：将列表反转。
- `copy()`：复制列表。

2. 元组常用的方法

元组是不可变序列，因此只能使用基本的序列操作，其常见方法只有`count()`和`index()`。

- `count(x)`：统计元组中值为x的元素出现的次数。
- `index(x)`：返回元组中值为x的元素所在的索引位置。

3. 字典常用的方法

- `clear()`：清空字典，删除所有元素。
- `copy()`：复制字典。
- `keys()`：返回包含所有键的列表。
- `values()`：返回包含所有值的列表。
- `items()`：返回包含所有（key,value）对元组的列表。
- `get(key, default=None)`：根据key获取相应的value，如key不存在则返回None或指定的default。
- `pop(key, default=None)`：删除指定key的元素，并返回其值，如key不存在则返回None或指定的default。
- `popitem()`：弹出字典中任意一对键值，并以元组形式返回键和其对应值，用于随机删除元素。

4. 集合常用的方法

- `add(elem)`：添加元素elem到集合中。
- `remove(elem)`：删除集合中指定元素elem。
- `copy()`：复制集合。
- `clear()`：清空集合。
- `pop()`：删除集合中任意一个元素，并返回该元素。
- `union(other)`或`|`：返回并集。
- `intersection(other)`或`&`：返回交集。
- `difference(other)`或`-`：返回差集。
- `symmetric_difference(other)`或`^`：返回对称差集。

需要注意的是，每种类型的方法不完全相同，有些方法只适用于某个特定类型，
例如元组只有`count()`和`index()`方法，
因此在具体使用时需要仔细查看文档或手册，以确定相应类型的具体方法和用法。
'''