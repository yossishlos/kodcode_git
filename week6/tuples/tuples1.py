def sum_nums(nums: tuple):
    the_sum = 0
    for num in nums:
        the_sum += num
    return the_sum

print(sum_nums((1, 2, 3, 4, 5)))