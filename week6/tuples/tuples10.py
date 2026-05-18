def rotate_a_tupel(a_list: tuple, num: int):
        num = num % len(a_list)
        return a_list[-num:] + a_list[:-num]

print(rotate_a_tupel((1, 2, 3, 4, 5), 2))