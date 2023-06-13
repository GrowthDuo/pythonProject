# 先死后活
# 打印 1-50之间被3整除的
'''
while
商品购物
while  --- else
'''

i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1

n = 3
while n <= 50 and n % 3 == 0:
    print(n)
    n += 3

x = int(input('起点'))
p = int(input('终点'))
t = int(input('除数'))
# 总个数
count = 0
while x <= p and t != 0:
    # 判断x能否被t整数
    if x % t == 0:
        print(x)
        count += 1
    # x滴加
    x += 1
print(count)

# 商品购物
# 个数
counts = 0
# 单价

money = 0
# 未购物
flag = False

print('开始结算')
print('点击0000结算')
while True:

    ge = float(input('单价 : '))
    if ge == 0000:
        break
    counts += 1
    print('数量x1')
    money += ge
print('总价:%.2f  个数%d' % (money, counts))


'''
while  --- else
'''
n = 1
while n <= 10 :
    print(n, end=' ')
    n += 1

    if n == 3 :
        continue

else:
    print('over')
