# import threading
# import time
#
# lock = threading.Lock()
# l = []
#
#
# def test1(n):
#     lock.acquire()
#     l.append(n)
#     time.sleep(1)
#     print(l)
#     lock.release()
#
# '''
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# '''
# def test(n):
#     l.append(n)
#     time.sleep(1)
#     print(l)
# '''
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# '''
#
#
# def main():
#     for i in range(0, 10):
#         th = threading.Thread(target=test1, args=(i,))
#         th.start()
#
#
# if __name__ == '__main__':
#     main()


# import threading
# import time
#
# # 定义一个全局变量
# g_num = 0
#
#
# def test1(num):
#     global g_num
#
#     for i in range(num):
#         mutex.acquire()  # 上锁 注意了此时锁的代码越少越好
#         g_num += 1
#         mutex.release()  # 解锁
#
#     print("-----in test1 g_num=%d----" % g_num)
#
#
# def test2(num):
#     global g_num
#     for i in range(num):
#         mutex.acquire()  # 上锁
#         g_num += 1
#         mutex.release()  # 解锁
#     print("-----in test2 g_num=%d=----" % g_num)
#
#
# # 创建一个互斥锁，默认是没有上锁的
# mutex = threading.Lock()
#
#
# def main():
#     t1 = threading.Thread(target=test1, args=(1000000,))
#     t2 = threading.Thread(target=test2, args=(1000000,))
#
#     t1.start()
#     t2.start()
#
#     # 等待上面的2个线程执行完毕....
#     time.sleep(2)
#
#     print("-----in main Thread g_num = %d---" % g_num)
#
#
# if __name__ == "__main__":
#     main()


'''
-----in main Thread g_num = 1794024---
-----in test1 g_num=1910832----
-----in test2 g_num=2000000=----
'''

# dead lock 死锁
import threading
import time


def test1(num):
    print("---test1---")
    mutex1.acquire()
    print("test1 请求 mutex1")
    time.sleep(1)
    print("test1 获得 mutex1")
    print("test1 请求 mutex2")
    mutex2.acquire()


def test2(num):
    print("---test2---")
    print("test2 请求 mutex2")
    mutex2.acquire()
    print("test2 获得 mutex2")
    time.sleep(1)
    print("test2 请求 mutex1")
    mutex1.acquire()


mutex1 = threading.Lock()
mutex2 = threading.Lock()
threading.RLock()

def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
