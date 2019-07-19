# 上下文和启动方法
# import multiprocessing as mp
#
# def foo(q):
#     q.put('hello')
#
# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()   # 消息队列
#     p = mp.Process(target=foo, args=(q,))   # 创建进程
#     p.start()
#     print(q.get())
#     p.join()


import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()