'''
模拟文件上传，键盘输入上传文件时的名称（abc.jpg）,
判断文件名abc是否大于6位以上，
扩展名是否是： jpg,gif,png格式
如果不是则提示上传失败，
如果名字不满足条件，
而扩展名满足条件则随机生成一个6位数字组成的文件名，
打印成功上传xxxxxx.png
'''
import random

file = input('请输入文件名称')
# 获取.的下标，帮助判断文件名是否满足条件   使用右侧查找，以防左侧文件名加.
dian = file.rindex('.')

# 获取文件名长度 使用切片 stop = dian
length = len(file[: dian])

end = file[dian: ]

if end == '.jpg' or '.gif' or '.png':
    if length < 6:
            ran=random.randint(100000, 999999)
            file =str(ran)+end
            print('文件名：',(file))
    else:
        print('成功上传：', file)
else:
    print('上传失败')

#   修改

file2 = input('请输入文件名称')
s = 'abcdefg1234567890'

# 获取后缀，帮助判断是否满足条件
if file2.endswith('.jpg') or file2.endswith('.gif') or file2.endswith('png'):
    dian2 = file2.rindex('.')
    name2 = file2[ :dian2]
    newFile = ''
    if len(name2) < 6:
        print('长度不满足6个，自动创建文件名')
        for i in range(6):
            ind=random.randint(0,len(s)-1)
            newFile += s[ind]

        file2 = newFile + file2[dian2: ]
        print('文件名：',(file2))
else:
    print('文件后缀不正确，上传失败')




