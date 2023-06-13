'''
分割

split(sep, 'maxcount')  sep作为分隔符字符串, 返回字符串中子字符串的列表   maxcount可加 分割几刀
rsplit(sep, 'maxcount')


splitlines()


'''


'''


    def split(self): # real signature unknown; restored from __doc__
        """
        Return a list of the substrings in the string, using sep as the separator string.

          sep
            The separator used to split the string.

            When set to None (the default value), will split on any whitespace
            character (including \\n \\r \\t \\f and spaces) and will discard
            empty strings from the result.
          maxsplit
            Maximum number of splits (starting from the left).
            -1 (the default value) means no limit.

        Note, str.split() is mainly useful for data that has been intentionally
        delimited.  With natural text that includes punctuation, consider using
        the regular expression module.
        """
        pass

“”“

返回字符串中子字符串的列表，使用sep作为分隔符字符串。


九月

用于分隔字符串的分隔符。


当设置为None（默认值）时，将在任何空白处拆分

字符（包括\\n\r\\t\\f和空格），并将丢弃

结果中的空字符串。

最大分割

最大拆分次数（从左侧开始）。

-1（默认值）表示没有限制。


注意，str.split（）主要适用于有意

定界。对于包含标点符号的自然文本，请考虑使用

正则表达式模块。

“”“
'''

s = 'www.baidu.com'
l = s.split('.')
print(l)

# 按行分割
s2 = '''s = 'www.baidu.com'
l = s.split('.')
'''

print(s2.splitlines())
