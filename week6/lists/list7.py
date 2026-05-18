def join_lists(list1: list, list2: list):
    new = []
    for i in list1:
        new.append(i)
    for j in list2:
        new.append(j)
    new.sort()
    return new

print(join_lists([1, 3, 5], [2, 4, 6]))