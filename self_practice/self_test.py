class Test_(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}:({!r}, {!r})'.format(class_name, *self)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def test(*self):
        print(self)

    def test2(self):
        print(self)

if __name__ == "__main__":
    dd = Test_(2, 3)
    dd.test()
    dd.test2()

'''
(Test_:(2, 3),)
Test_:(2, 3)
'''




