# from itertools import count

# 无限循环递增的计数器，生成连续的数据点
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


if __name__ == '__main__':
    for i in count(10, 1):
        print(i)