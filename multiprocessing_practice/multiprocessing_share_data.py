# from multiprocessing import Process
# li = []
#
# def foo(i):
#     li.append(i)
#     print('say hi', li)
# if __name__ == '__main__':
#
#     for i in range(10):
#         p = Process(target=foo, args=(i,))
#         p.start()
#
#     print('ending', li)

'''
say hi [0]
say hi [1]
say hi [2]
say hi [3]
say hi [4]
say hi [5]
say hi [6]
say hi [7]
ending []
say hi [8]
'''

# 使用Array共享数据
from multiprocessing import Process, Array

def f(a):
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    arr = Array('i', range(10))
    p = Process(target=f, args=(arr,))
    p.start()
    p.join()

    print(arr[:])

# 使用Manages共享数据