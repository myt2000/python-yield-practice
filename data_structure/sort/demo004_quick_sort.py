def quick_sort(alist, start, end):
    """快速排序"""
    print("原始数据:" , alist, start, end)
    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        print("high指向的元素放到low的位置上:", alist, low, high)
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
        print("将low指向的元素放到high的位置上:", alist, low, high)
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    print("将基准元素放到该位置:%s %s %s %s" % (alist, low, high, mid))

    # 对基准元素左边的子序列进行快速排序
    print("---------对基准元素左边的子序列进行快速排序---------------")
    print(start, low-1)
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    print("---------对基准元素右边的子序列进行快速排序---------------")
    print(start, low - 1)
    quick_sort(alist, low+1, end)

# def quick_sort2(alist, start, end):
#
#
#     mid = alist[start]
#     left = start
#     right = end
#
#     while left < right:
#         while left < right and alist[right] > mid:
#             right -= 1
#         alist[left] = alist[right]
#         while left < right and alist[right] < mid:
#             left += 1
#         alist[right] = alist[left]
#
#     alist[left] = mid
#     quick_sort2(alist, start, left-1)
#     quick_sort2(alist, left+1, end)


if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    quick_sort(alist,0,len(alist)-1)
    print(alist)

