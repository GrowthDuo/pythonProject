'''

center(number,"要添加的字符或其他，可不加") ，只是指定number个数，后面不加默认是添加空格
center(20,"*")
'''

# 移除字符串首、尾字母
s = ' hello '
print(s.strip())

a = 'a b c'
s=a.strip()
print(s)
# 只去除左侧空格 lstrip( )
print(s.lstrip())

# 只去除右侧空格 rstrip( )




# center   左右添加内容
'''
    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass
        
 返回一个长宽居中的字符串。

填充是使用指定的填充字符（默认为空格）完成的。
        
'''
print(s.center(20,"*"))

print(s.center(15))


print(s.ljust(3," "))


