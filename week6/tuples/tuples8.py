def join_tuples(tuple1: tuple, tuple2: tuple):
    new = []
    for i in tuple1:
        new.append(i)
    for j in tuple2:
        new.append(j)
    new.sort()
    return tuple(new)

print(join_tuples((3, 1, 4), (1, 5, 9)))
