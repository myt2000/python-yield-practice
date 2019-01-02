from bisect import *

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    print(i)
    return grades[i]

if __name__ =="__main__":
    a = [grade(score) for score in [33, 99, 77, 89, 90, 100]]
    print(a)