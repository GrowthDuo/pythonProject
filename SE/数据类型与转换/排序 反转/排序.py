'''
排序
sort  从小到大排序，默认是升序，参数为（reverse=False）可不加
       但可以通过参数调整成 从大到小排序

    def sort(self, *args, **kwargs): # real signature unknown
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        pass

按升序对列表进行排序，然后返回None。


排序是适当的（即列表本身被修改）和稳定的（即

维持两个相等元素的顺序）。


如果给定了一个键函数，则将其应用于每个列表项一次并对其进行排序，

根据函数值升序或降序。


反向标志可以设置为按降序排序。
'''

list1 = [1,4,6,23,54,2]
# 默认情况
list1.sort()
print(list1)

# 默认加参 从小到大
list2 = [3,4,6,23,54,2]
list2.sort(reverse=False)
print(list2)

# 调参 从大到小
list3 = [3,4,6,23,54,2]

list2.sort(reverse=True)
print(list3)

'''
结果
[1, 2, 4, 6, 23, 54]
[2, 3, 4, 6, 23, 54]
[3, 4, 6, 23, 54, 2]

'''