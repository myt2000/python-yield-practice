# -*- coding: utf-8 -*-
"""模拟:grep -rl 'root' /etc"""
import os
# 用来开启协程
def deco(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        next(res)  # res.seng(None)
        return res
    return wrapper
@deco
def search(target):
    while True:
        PATH = yield
        # 获取PATH目录下的文件，文件夹
        g = os.walk(PATH)
        # 迭代解包,取出当前目录路径和文件名
        for par_dir, _, files in g:
            for file in files:
                file_path = r'%s\%s' %(par_dir,file)  # 拼接文件的绝对路径
                target.send(file_path)  # 给下一个
@deco
def opener(target, pattern=None):
    while True:
        file_path = yield
        with open(file_path, encoding='utf-8') as f:
            # 将文件路径和文件对象一起传递给下一个函数的yield，因为在打印路径时候，需要打印出文件路径，只有从这里传递下去
            target.send((file_path, f))
@deco
def cat(target):
    while True:
        # 这里接收opener传递进来的路径和文件对象
        filepath, f = yield
        for line in f:
            # 同样，也要传递文件路径,并且获取下一个函数grep的返回值，从而判断该文件是否重复读取了
            tag = target.send((filepath, line))
            # 如果为真，说明该文件读取过了，则执行退出循环
            if tag:
                break
@deco
def grep(target, pattern):
    tag = False
    while True:
        # 接受两个值，并且设置返回值，這个返回值要传递给发送消息的send()，也就是cat()函数send
        filepath, line = yield tag
        tag = False
        # 如果待匹配字符串在该行
        if pattern in line:
            # 把文件路径传递给priter
            target.send(filepath)
            # 设置tag
            tag = True
@deco
def printer():
    while True:
        filename = yield
        print(filename)

if __name__ == "__main__":
    PATH1 = r'D:\python'
    search(opener(cat(grep(printer(), 'python')))).send(PATH1)