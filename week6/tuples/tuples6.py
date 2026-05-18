def min_and_max(nums: tuple):
    the_min = nums[0]
    the_max = 0
    for num in nums:
        if num <the_min:
            the_min = num
        elif num > the_max:
            the_max = num
    return (the_min, the_max)

print(min_and_max((4, 1, 7, 3, 5)))