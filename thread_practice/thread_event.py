import threading
import time
'''
class Event
事件管理一个标志，可以使用set（）方法设置为true，并使用clear（）方法重置为false。 wait（）方法将阻塞，直到该标志为true。 该标志最初是假的。
'''

def do(event):
    print('start')
    event.wait()  # 红灯，所有线程执行都这里都在等待
    print('end')


if __name__ == "__main__":
    event_obj = threading.Event()  # 创建一个事件
    for i in range(10):  # 创建10个线程
        t = threading.Thread(target=do, args=(event_obj,)) # 把事件传给do函数，并让事件的内部标志变为False
        t.start()

    time.sleep(5)

    event_obj.clear()  # 让灯变红，默认也是红的，阻塞所有线程运行
    data = input('请输入要：')
    if data == 'True':
        event_obj.set()  # 变绿灯   把事件的内部标志变为True