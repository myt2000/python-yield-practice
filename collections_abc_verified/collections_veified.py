# -*- coding: utf-8 -*-
from collections.abc import Set

class ListBasedSet(Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

if __name__ == '__main__':
    s1 = ListBasedSet('abcdef')
    print(list(s1))
    s2 = ListBasedSet('defghi')
    print(s2)
    overlap = s1 & s2
    print(overlap)