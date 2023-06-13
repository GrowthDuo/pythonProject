'''
for
输入账号和密码，输错三次账号被锁
for -- else
'''

'''
for 变量名  in range (start, stop[, step])
start : 起始值，默认为 0
stop  ： 尾部（end-1）
[, step] ： 步长（增量）

   range(stop) -> range object
    range(start, stop[, step]) -> range object
'''

# 输入账号和密码，输错三次账号被锁
# 方法1：
flag = False
# 次数
count = 0
for i in range(3):
    name = input('用户名')
    pw = input('密码')
    if name == 'admin' and pw == '1234':
        flag = True
        print('登录成功')
        break
    count += 1
    print('账户或密码错误，剩余' + str(3 - count) + '次！')

if not flag:
    print('账户锁定')

# 方法2 ： for -- else
# 次数
count2 = 0
for i in range(3):
    name2 = input('用户名')
    pw2 = input('密码')
    if name2 == 'admin' and pw2 == '1234':

        print('登录成功')
        break
    count2 += 1
    print('账户或密码错误，剩余' + str(3 - count2) + '次！')
else:
    print('账户锁定')