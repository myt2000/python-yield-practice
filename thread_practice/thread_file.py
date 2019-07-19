# b = Barrier(2, timeout=5)
#
# def server():
#     start_server()
#     b.wait()
#     while True:
#         connection = accept_connection()
#         process_server_connection(connection)
#
# def client():
#     b.wait()
#     while True:
#         connection = make_connection()
#         process_client_connection(connection)


import time
import threading
from datetime import datetime
import logging

def f0():
    pass


def f1(a1, a2):
    time.sleep(5)  # 多个线程同时睡5秒
    print('start thread')
    f0()
    print('end thread')

if __name__ == "__main__":
    '''下面代码是直接运行下去的，不会等待函数里面设定的sleep'''
    a = datetime.now().strftime('%H-%M-%S')
    print(a)
    t = threading.Thread(target=f1, args=(111, 112))  # 创建线程
    t.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
    t.start()  # 开启线程
    print(t.name)

    t = threading.Thread(target=f1, args=(111, 112))
    t.start()
    print(t.name)
    t = threading.Thread(target=f1, args=(111, 112))
    t.start()
    print(t.name)
    # 默认情况下程序会等线程全部执行完毕才停止的，不过可以设置更改为后台线程，使主线程不等待子线程，主线程结束则全部结束
    b = datetime.now().strftime('%H-%M-%S')
    print(b)

    '''
    15-07-10
    Thread-6
    Thread-7
    Thread-8
    15-07-10
    start thread
    end thread
    start threadstart thread
    end thread
    
    end thread
    '''