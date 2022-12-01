def foo(x: int):
    return False


def bar(x: foo):
    return True


def baz(x, y=1, *, z, u=1, v, r=1):
    pass


if __name__ == '__main__':
    print(int)
    print(int(3.5))

    print(bar(3))
