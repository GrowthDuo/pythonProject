'''
判断

'''

path = 'https://www.bilibili.com'
# startswith 判断是否以 http 开头
'''
   def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        
如果S以指定前缀开头，则返回True，否则返回False。

在可选启动的情况下，从该位置开始测试S。

对于可选端，停止在该位置比较S。

前缀也可以是要尝试的字符串元组。        
        """
        return False
'''

b =  path.startswith('http')
print(b) # True

# endswith 判断结尾是否以某某某结尾
'''
    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """

“”“

S.endswitch（后缀[，start[，end]]）->布尔


如果S以指定后缀结尾，则返回True，否则返回False。

在可选启动的情况下，从该位置开始测试S。

对于可选端，停止在该位置比较S。

后缀也可以是一个字符串元组来尝试。

“”“         
        return False
'''
end = path.endswith('.com')
print(end) # True