import threading,time
from random import randint

'''
有一类线程需要满足条件之后才能够继续执行，
Python提供了threading.Condition 对象用于条件变量线程的支持，
它除了能提供RLock()或Lock()的方法外，
还提供了 wait()、notify()、notifyAll()方法。
wait([timeout]):线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）
才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
调用wait()会释放Lock，直至该线程被Notify()、NotifyAll()或者超时线程又重新获得Lock.

notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，
默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，
否则会触发RuntimeError。notify()不会主动释放Lock。

notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程（这个一般用得少）
lock_con=threading.Condition([Lock/Rlock])： 锁是可选选项，
默认创建一个RLock(),一般都用默认。
'''

class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0,100)
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            print('生产者', self.name, ' Append'+str(val), L)
            if lock_con.acquire():   # 获取底层锁
                L.append(val)
                lock_con.notify()  # 生产者 通知（唤醒）
                lock_con.release()   # 释放底层锁
            time.sleep(3)


class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()  # 条件变量加锁
            if len(L) == 0:
                lock_con.wait()  # 消费者等待
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('消费者', self.name, 'Delete'+str(L[0]), L)
            del L[0]
            lock_con.release()
            time.sleep(0.5)


if __name__ == '__main__':
    L = []
    lock_con = threading.Condition()
    threads = []
    for i in range(5):
        threads.append(Producer(args=(1, )))
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()


'''
class Condition
条件变量允许一个或多个线程等待，直到另一个线程通知它们。

如果给出了lock参数而不是None，则它必须是Lock或RLock对象，并且它被用作底层锁。 
否则，将创建一个新的RLock对象并将其用作基础锁。
'''