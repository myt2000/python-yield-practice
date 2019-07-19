#
# from  multiprocessing import Pool
# import time
#
# def Foo(i):
#     time.sleep(2)
#     return i + 100
#
# def Bar(arg):
#     print(arg)
#
#
# if __name__ == '__main__':
#     t_start = time.time()
#     pool = Pool(5)  # 每次只能并发5个
#
#     for i in range(10):
#         pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#         # 先执行Foo，在执行Bar，参数共用
#
#     pool.close()
#     pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
#     pool.terminate()
#     t_end = time.time()
#     t = t_end-t_start
#     print('the program time is :%s' % t)

'''
同步并发每次5个进程
102
100
101
103
104
105
107
106
108
109
the program time is :7.337979078292847
'''


# from multiprocessing import Process, Pool
# import time
#
#
# def Foo(i):
#     time.sleep(1)
#     print(i + 100)
#
#
# if __name__ == '__main__':
#     t_start = time.time()
#     pool = Pool(5)
#
#     for i in range(10):
#         pool.apply(Foo, (i,))
#
#     pool.close()
#     pool.join()  # 进程池中每个进程执行完毕后再关闭，如果注释，那么程序直接关闭。
#     t_end = time.time()
#     t = t_end-t_start
#     print('the program time is :%s' %t)

'''
单独每个并发
100
101
102
103
104
105
106
107
108
109
the program time is :12.6555495262146
'''
# from  multiprocessing import Process, Pool
# import time
#
# def Foo(i):
#     time.sleep(2)
#     return i + 100
#
# def Bar(arg):
#     return arg
#
# if __name__ == '__main__':
#     t_start = time.time()
#     pool = Pool(5)
#
#     for i in range(10):
#         res = pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#         a = res.get()
#         print(res.get())   # 错误使用get()用例
#
#     pool.close()
#     pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
#     pool.terminate()
#     t_end = time.time()
#     t = t_end-t_start
#     print('the program time is :%s' %t)

'''
100
101
102
103
104
105
106
107
108
109
the program time is :22.676316022872925
'''

from  multiprocessing import Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100

def Bar(arg):
    return arg

if __name__ == '__main__':
    res_list = []
    t_start = time.time()
    pool = Pool(5)

    for i in range(10):
        res = pool.apply_async(func=Foo, args=(i,), callback=Bar)
        res_list.append(res)   # 将进程放入列表，然后在get()返回值

    pool.close()
    pool.join()
    for res in res_list:
        print(res.get())
    t_end = time.time()
    t = t_end-t_start
    print('the program time is :%s' %t)

'''
100
101
102
103
104
105
106
107
108
109
the program time is :7.268125057220459
'''