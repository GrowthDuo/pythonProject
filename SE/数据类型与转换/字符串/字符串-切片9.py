'''
  字符串，列表

   格   式 ：字符串变量 [start ：end]
'''

s = 'ABCDEF'
print('长度：',len(s))

# BCDE
print(s[1 :len(s)-1])
print(s[1 : -1])

# ABCD
print(s[ : 4])

# DEF
print(s[-3 : ])
print(s[3 : ])

# ABCDEF
home = print()
# 判断是否与s地址一致
print(id(s))
print(id(s[ : ]))

print(s is s[ : ])

# BDF
# star 1  stop 6-1(实际到len-1)  步长 2 （增量）
print(s[1 : 6 : 2])

# 使用步长倒着取
# FEDCBA
print(s[ : : -1])

# 步长为负数时,起点到终点也应该反着走[-1 : ] ,否则没有结果
# 同一方向 ABCD
print(s[6 :0 -2])

# 不同一方向 空
print(s[0 :6 -2])