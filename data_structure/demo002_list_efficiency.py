import timeit

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li = li + [i]

def t3():
    li = [i for i in range(10000)]

def t4():
    li = list(range(10000))

def t5():
    li = []
    for i in range(10000):
        li.insert(0, i)
    
timer1 = timeit.Timer("t1()", "from __main__ import t1")
timer2 = timeit.Timer("t2()", "from __main__ import t2")
timer3 = timeit.Timer("t3()", "from __main__ import t3")
timer4 = timeit.Timer("t4()", "from __main__ import t4")
timer5 = timeit.Timer("t5()", "from __main__ import t5")

print("append: %f" % timer1.timeit(number=100))
print("[]+[]: %f" % timer2.timeit(number=100))
print("[i for]: %f" % timer3.timeit(number=100))
print("list(): %f" % timer4.timeit(number=100))
print("insert(): %f" % timer5.timeit(number=100))

'''
append: 0.120588
[]+[]: 10.108985
[i for]: 0.042463
list(): 0.015909
insert(): 1.651315
'''

'''
# ('concat ', 1.7890608310699463, 'seconds')
# ('append ', 0.13796091079711914, 'seconds')
# ('comprehension ', 0.05671119689941406, 'seconds')
# ('list range ', 0.014147043228149414, 'seconds')
'''

# 可以看出，两个列表相加最慢，第二慢的是insert插入的方式，其次是一个一个元素添加到列表尾部， 列表表达式相对快，迭代器转换为列表最快

# if __name__ == "__main__":
    
