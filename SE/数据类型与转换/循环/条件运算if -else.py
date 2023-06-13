name = input('用户名')
pw = input('密码')

flat = False
if name == 'admin' and pw == '1234':
    print('登录成功')
    loGin= input('是否记住账号密码（y/n）')
    if loGin =='y':
        flat=True
        print('已记住用户%s与密码%s',(name,'***'))
    else:
        print('下次记住')
else:
    print('检查用户与密码是否输错')