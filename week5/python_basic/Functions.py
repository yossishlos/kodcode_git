
# 1

def is_even(n):
    return n % 2 ==0

# print(is_even(6))

# 2

def factorial(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
    return tmp

# print(factorial(4))

# 3

def count_vowels(s):
    cnt = 0
    for i in s:
        if i in "aeiouAEIOU":
            cnt += 1
    return cnt

# print(count_vowels("aaasdfgaaa"))

# 4

