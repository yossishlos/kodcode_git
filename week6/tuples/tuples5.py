def swap_pairs(nums: tuple):
    result = list(nums)
    for i in range(0, len(nums), 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return tuple(result)

print(swap_pairs((1, 2, 3, 4, 5, 6)))