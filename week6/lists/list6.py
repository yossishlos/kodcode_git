def the_second_max_num(nums: list):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    second_num = 0
    for num in nums:
        if max_num > num > second_num:
            second_num = num
    if second_num == 0:
        return None
    return second_num
print(the_second_max_num([4, 1, 7, 7, 3, 5]))