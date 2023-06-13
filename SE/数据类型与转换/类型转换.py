# 类型转换
# str --> int
str = 'hello'
print(str, type(str) )

# str --> int
print('请输入')
sting = input()
print(sting, type(sting),end="\n" )
sting = int(sting)
print(sting, type(sting) )

# float->int 精度丢失(向下取整)
f = 3.14
at = 3.7
f = int(f)
at = int(at)
print(f)
print(at)

# 布尔bool --> int
f = True
l = False
# 查看类型
print(f, type(f))
print(l, type(l))

# 转换为 int 与 float
print(int(f))
print(int(l))

print(float(f))
print(float(l))

# 思考
a = 5
# 能否将a转为bool
print(bool(a)) # True
# 变量是0或空字符串转布尔为false，其他值则为true
