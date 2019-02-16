# from itertools import accumulate
import operator
# 类似于itertools.accumulate
def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total

if __name__ == '__main__':
    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    print(list(accumulate(data, operator.mul)))
