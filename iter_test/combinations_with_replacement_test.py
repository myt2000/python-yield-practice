# from itertools import combinations_with_replacement


def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        a = reversed(range(r))
        print(list(a))
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        print(i)
        yield tuple(pool[i] for i in indices)


if __name__ == '__main__':
    a = 'ABC'
    for i in combinations_with_replacement(a, 2):
        print(i)