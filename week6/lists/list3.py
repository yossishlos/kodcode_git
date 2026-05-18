def counyt_value(values: list, a_value: any):
    tmp = 0
    for value in values:
        if value == a_value:
            tmp += 1
    return tmp

print(counyt_value([1, 2, 3, 2, 4, 2], 2))