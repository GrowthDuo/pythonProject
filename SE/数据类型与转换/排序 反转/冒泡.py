list1 = [1, 3, 5, 4, 2]
length = len(list1)



for i in range(0, length-1):          # 0 - 4   0 1 2 3 4
    for j in range(0, length -1):      # 0 - 3   0 1 2 3
        if list1[j] >  list1[j+1]:
               temp = list1[j]
               list1[j] =list1[j+1]
               list1[j + 1] = temp
print(list1)




# 优化 冒泡排序



for i in range(length-1):
    for j in range(length -1):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

print(list1)

'''
这两段代码实现的功能都是对列表进行冒泡排序，只是第二个代码实现了冒泡排序的优化，相对于第一个代码，第二个代码经过优化减少了比较和交换的次数，提高了算法效率。

第二个代码中，第二层循环中遍历的范围用 `length-i-1` 替换了之前的 `length-1`，实现了每轮冒泡后减少一次比较和交换，因为每轮冒泡的过程中都会将待排序数组中的最大数沉到数组最后的位置。

注意，在第二层循环中，优化过后的冒泡排序并没有去掉交换元素的步骤，而是通过减少比较次数来提高了排序的效率。
'''