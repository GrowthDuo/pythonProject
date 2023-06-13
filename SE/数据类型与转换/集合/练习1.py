'''
产生 5 组（不允许重复），字母和数字组成4位验证码

'''
import random

s = 'abcderdfigidofvkdsmmfskopi1234567890'
yzm =set()

for t in range(5):
    for i in range(4):
         index = random.randint(0, len(s)-1)
         yz =set(s[index])
         yzm.update(yz)


    print()
print(yzm)

# AI

s = 'abcderdfigidofvkdsmmfskopi1234567890'
result = []

for t in range(5):
    yzm = ''
    used_chars = set() # 用一个集合来存储已经生成过的字符
    for i in range(4):
        while True:
            index = random.randint(0, len(s)-1)
            c = s[index]
            if c not in used_chars: # 如果生成的字符没有出现过，则将其加入验证码中
                yzm += c
                used_chars.add(c) # 将该字符加入已使用的字符集合
                break
    result.append(yzm)

for y in result:
    print('{}{}{}{}'.format(y[0], y[1], y[2], y[3]))