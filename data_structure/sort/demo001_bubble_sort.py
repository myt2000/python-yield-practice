def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        # range(start, stop[, step])
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def bubble_sort2(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            break


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    bubble_sort(li)
    # bubble_sort2(li)
    print(li)