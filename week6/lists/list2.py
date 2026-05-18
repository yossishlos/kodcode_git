def the_max_num(nums: list):
    tmp = 0
    for num in nums:
        if num > tmp:
            tmp = num
    return tmp

print(the_max_num([3, 7, 2, 8, 5]))