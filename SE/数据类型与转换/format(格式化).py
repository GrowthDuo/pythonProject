name = '李'
age = 18
result = '美女你姓{}, 今年{}'.format(name, age)
print(result)

# 使用数字填充  从0开始
result2 = '美女你姓{0}, 今年{1}'.format(name, age)
print(result2)

# 变量名填充
result3 = '美女你姓{name}, 今年{age}'.format(name='邓', age=12)
print(result3)