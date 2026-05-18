def reverse_list(a_list: list):
    new_list = []
    for i in a_list:
        new_list.insert(0, i)
    return new_list

print(reverse_list([1, 2, 3, 4, 5]))