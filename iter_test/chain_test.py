# from itertools import chain

def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


if __name__ == '__main__':
    a = 'ABC'
    b = 'DEF'
    print(list(chain(a,b)))