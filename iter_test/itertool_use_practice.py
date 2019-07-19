import itertools
import operator

test_list1 = [1,2,3,4,5]
test_list2 = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
test_list3 = [1000, -90, -90, -90, -90]
test_str = 'ABCDE'

def itertools_function(iterable):
    a1 = list(itertools.accumulate((test_list1, operator.mul)))
    print(a1)