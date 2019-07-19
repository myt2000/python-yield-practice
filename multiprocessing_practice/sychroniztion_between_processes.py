# 进程间同步
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()  # 获取锁
    try:
        print('hello world', i)
    finally:
        l.release()  # 释放锁

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()