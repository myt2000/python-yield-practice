class Stack(object):
    """栈"""
    def __init__(self):
        # 顺序表
        self.__items = []
        # 链表
        # self.__items = SingleList()

    def is_empty(self):
        """判断是否为空"""
        return self.__items == []

    def push(self, item):
        """加入元素"""
        self.__items.append(item)   # O(1)
        # self.__items.insert(0, item)   # O(n)

    def pop(self):
        """弹出元素"""
        return self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.__items[-1]
        # return self.__items[len(self.__items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.__items)

if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())