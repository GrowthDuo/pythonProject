'''
替换 replace
replace(old,       new ,  count)
    要替换的内容     新内容   次数（如：出现多个要替换掉内容，默认是全体换, 可以指定数量）


底层 ：
   def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass


def-replace（self，*args，**kwargs）：#真实签名未知

“”“

返回一个副本，其中所有出现的子字符串old都被new替换。


计数

要替换的最大出现次数。

-1（默认值）表示替换所有出现的项。


如果给定了可选参数计数，则仅出现第一次计数

已更换。

“”“

通过
'''

s = 'wzd like look blue bird very like look blue bird'

# 将 blue bird 替换成 ***
print(s.replace('blue bird', '***'))

# 将 第一个 blue bird 替换成 ***
print(s.replace('blue bird', '***', 1))



