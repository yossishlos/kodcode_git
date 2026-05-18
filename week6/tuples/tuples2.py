def the_max(nums: tuple):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(the_max((3, 7, 2, 8, 5)))