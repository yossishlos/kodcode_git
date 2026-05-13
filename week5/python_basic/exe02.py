def test1(a,/,b,c):
    print(a, b, c)

def test2(*items):
    print(items)


def test3(a,/,b,*,c,):
    print(a, b, c)

test3("A", c="B", b="C")
