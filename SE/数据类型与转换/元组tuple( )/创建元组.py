# 如果元组只要一个元素时，后面要加 , 号
tuple1 =('yuan',)
print(type(tuple1)) # <class 'tuple'>



t2 = ('yuan')
print(type(t2))  # <class 'str'>

# 查看元组元素  切片 和 下标
t3 = (1, 2, 3, 4, 5)
print(t3[1])
print(t3[2: ])
