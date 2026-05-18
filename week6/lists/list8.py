def rotate_a_list(a_list: list, num: int):
        num = num % len(a_list)
        return a_list[-num:] + a_list[:-num]

print(rotate_a_list([1, 2, 3, 4, 5], 5))