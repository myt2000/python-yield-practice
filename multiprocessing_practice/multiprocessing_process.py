# from multiprocessing import Process
#
# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

'''
输出
hello bob
'''



# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

'''
输出
main line
module name: __main__
parent process: 12080
process id: 10156
function f
module name: __mp_main__
parent process: 10156
process id: 17448
hello bob
'''

# from multiprocessing import Process
# import threading
# import time
#
#
# def foo(i):
#     print('say hi', i)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=foo, args=(i,))
#         p.start()


from multiprocessing import Process
import time

# run()里面可以执行需要的函数，不需要target
class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg

    def run(self):
        print('say hi', self.arg)
        time.sleep(1)


if __name__ == '__main__':

    for i in range(10):
        p = MyProcess(i)
        p.start()