import threading
import time

g_nums = [1, 2]

# 不同函数多个线程传参数

def test1(temp):
    temp.append(33)
    print("-----in test1 temp=%s-----" % str(temp))


def test2(temp):
    print("-----in test2 temp=%s-----" % str(temp))


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))  # 加上要传递的参数，元组类型
    t2 = threading.Thread(target=test2, args=(g_nums,))  # args 元组类型

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("-----in main temp=%s-----" % str(g_nums))


if __name__ == '__main__':
    main()
