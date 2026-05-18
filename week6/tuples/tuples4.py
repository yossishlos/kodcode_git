def reverse(nums: tuple):
    new = []
    list(nums)
    for num in nums:
        new.insert(0, num)
    return tuple(new)

print(reverse((1, 2, 3, 4)))