'''
遍历 查询
列表  list.index()   lise.count()   in

get ：获取     未指定可设默认值，返回结果可自定，默认为None
value = books['name']  未找到会报 keyError错误
'''
books ={'book' :'多少', 'money' : 15, '出版社' : '古'}
b=books.get('book')
b2=books.get('book1')
b3=books.get('book1','自定义')
print(b)  # 多少

print(b2) # None

print(b3) # 自定义

# value = books['name'] #KeyError: 'name'

# 遍历
# 如果使用 for in 直接遍历，取出的是字典的key
for key in books:
    print(key)
# book
# money
# 出版社
print("\n")
for varlue in books.values():
    print(varlue)

print('---------------------')
# 获取value值
# 获取字典中所有的value值 ：字典.values（）

print(books.values())

print(books.keys())
# dict_values(['多少', 15, '古'])

print("\n")

# 按一对一对取出
print(books.items())

print("\n")

# 遍历取出
for k,v in books.items():
    print(k,v)

print("\n")
for k,v in books.items():
    print(k)
    print(v)