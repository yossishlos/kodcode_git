def count_items(items: tuple):
    new = {}
    for item in items:
        if item not in new:
            new[item] = 0
    for i in new:
        for j in items:
            if i == j:
                new[i] += 1

    return tuple(new.items())

print(count_items(("a", "b", "a", "c", "b", "a",)))