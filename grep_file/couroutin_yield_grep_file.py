import os
import fnmatch
import sys
import asyncio


def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return wrapper

@asyncio.coroutine
@decorator
def find_files(target):
    while True:
        topdir, pattern = (yield)
        for path, dirname, filelist in os.walk(topdir):
            for name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    target.send(os.path.join(path, name))


import gzip, bz2


@asyncio.coroutine
@decorator
def opener(target):
    while True:
        name = (yield)
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        target.send(f)


@asyncio.coroutine
@decorator
def cat(target):
    while True:
        f = (yield)
        for line in f:
            target.send(line)


@asyncio.coroutine
@decorator
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@asyncio.coroutine
@decorator
def printer():
    while True:
        line = (yield)
        sys.stdout.write(line)




if __name__ == "__main__":
    # finder = find_files(opener(cat(grep(None, printer()))))
    finder = find_files(opener(cat(grep("python", printer()))))
    # finder.send()
    finder.send(("d:/", "*"))
    # finder.send(("oterwww", "access-log*"))
