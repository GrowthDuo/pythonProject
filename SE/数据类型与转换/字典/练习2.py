'''
books =【】 框 能放多本书
书 { }
书名
作者
价钱

添加三本书
1、添加书

'''

# 错误代码
# books =[ ]
# for i in range(3):
#     name=input('书名：')
#     if i>=1:
#         if books[0: :3].count(1):
#             while True :
#                 names = input('此书已存在，请输入书名：')
#                 if name.center(0):
#                     name=names
#                     break
#     book={'name': name}
#     zuo = input('作者 ：')
#     zuozhe ={'作者 ： ': zuo}
#     money = input('价钱：')
#     m ={'价钱 ： ':money}
#     books.append(book)
#     books.append(zuozhe)
#     books.append(m)
# print(books)


# Ai改错
books = []
for i in range(3):
    name = ''
    while name == '':
        name = input('书名：')
        if i >= 1:
            #如果 books 列表中的某个字典中包含 name 这个键，并且其值与输入的书名 name 相同，那么就认为输入的书名已经存在于 books 列表中了。
            if name in [book['name'] for book in books if 'name' in book]:
                print('此书已存在，请重新输入书名：')
                name = ''
    book = {'name': name}
    zuo = input('作者：')
    zuozhe = {'作者：': zuo}
    money = input('价格：')
    m = {'价格：': money}
    books.append(book)
    books.append(zuozhe)
    books.append(m)
print(books)





