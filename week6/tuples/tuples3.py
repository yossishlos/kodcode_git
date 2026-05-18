def count_value(values: tuple, a_value: any):
    result = 0
    for value in values:
        if value == a_value:
            result += 1
    return result

print(count_value((1, 2, 3, 2, 4, 2), 2))