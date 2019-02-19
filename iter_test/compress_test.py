# from itertools import compress

def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    # a = zip(data, selectors)
    # for m,n in a:
    #     if n:
    #         yield (m)

    return (d for d, s in zip(data, selectors) if s)


if __name__ == '__main__':
    a = 'ABCEDF'
    s = [1,0,1,0,1,1]
    for i in compress(a, s):
        print(i)