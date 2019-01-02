# -*- coding:utf-8 -*-

# def create_counter():
#     def increase():
#         n = 0
#         while True:
#             n = n + 1
#             yield n
#     it = increase()
#
#     def counter():
#         return next(it())
#     return counter()
#
# counter_ = create_counter()
# print(counter_(), counter_(), counter_())'

class Counter(object):
    def __init__(self, start=0):
        self.num = start
    def count(self):
        self.num += 1
        return self.num

