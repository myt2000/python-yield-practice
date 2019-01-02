def foo():
    while True:
        x = yield
        print("value:",x)

if __name__ == "__main__":
    g = foo()
    next(g)
    g.send(1)
    g.send(2)