'''
查找
find    ： 从左开始查找， 找不到为 -1
rfind   ： 从右开始查找， 找不到为 -1

index  ： 从左开始查找 ， 找不到报错ValueError
rindex ： 从右开始查找 ， 找不到报错ValueError

count ： 统计指定字符的个数
'''

path = 'https://www.bilibili.com/video/BV1R7411F7JV?p=32&spm_id_from' \
       '=pageDriver&vd_source=61a8ee86e65fe9c687841f6936393d11'

'''
find
1、 从左往右查找,当有多个时，找到第一个停止查找
2、 当未找到返回-1

底层代码
find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        
        翻译为 ：
        S.find（sub[，start[，end]]）->int
返回S中找到子串sub的最低索引，
使得sub包含在S[start:end]内。可选择的
参数start和end被解释为切片表示法。
故障时返回-1。
        """
'''
# 查找 video位置
index =path.find('video')
print(index)
print(path[25 : 30])



'''
rfind
1、 从右往左查找,当有多个时，找到第一个停止查找
2、 当未找到返回-1

 def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        
        翻译 ：
        S.rfind（sub[，start[，end]]）->int


返回S中找到子串sub的最高索 引，

使得sub包含在S[start:end]内。可选择的

参数start和end被解释为切片表示法。


故障时返回-1。 
        """
        return 0
'''
# 查找vd_source
index2 = path.rfind('vd_source')
print(index2) # 72
print(path[72 : 81])


'''
查找

index
底层 ：
  def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        
        翻译：
        “”“

S.index（sub[，start[，end]]）->int


返回S中找到子串sub的最低索引，

使得sub包含在S[start:end]内。可选择的

参数start和end被解释为切片表示法。


未找到子字符串时引发ValueError。

“”“
        """
        return 0
        
        
        
        
rindex

   def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        翻译：
返回S中找到子串sub的最高索引，

使得sub包含在S[start:end]内。可选择的

参数start和end被解释为切片表示法。


未找到子字符串时引发ValueError。
        """
        return 0
'''
print(path.index('/'))

print(path.rindex('/'))


'''
count ： 统计指定字符的个数

   def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
   

返回中子字符串sub的非重叠出现次数

字符串S[开始：结束]。可选参数开始和结束为

被解释为切片表示法。         
        """
        return 0
'''
# 统计 / 出现的次数 4
print(path.count('/'))