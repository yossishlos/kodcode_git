# # 1

# age = int(input("please enter your age: "))

# if age >= 0 and age <= 120:
#     if age <= 12:
#         print("child")

#     elif age <= 17:
#         print("teen")

#     else:
#         print("adult")

# else:
#     print("invalid")

# # 2

# cher = input("please enter a cher: ")

# if not cher.isalpha():
#     print("invalid")

# elif cher in "aeiou":
#     print("vowel")

# else:
#     print("Consonant")

# # 3

# age = int(input("please enter your age: "))
# has_vip = input("do you have a vip card? (y/n): ")

# if age < 16:
#     print("access denied")

# elif age < 22:
#     print("welcome")

# elif age > 21 and has_vip == "y":
#     print("welcome")

# else:
#     print("access denied")

# # 4

# password = input("please enter the password: ")

# if password == "123456789":
#     print("acces granted")

# elif len(password) < 8:
#     print("too short")

# else:
#     print("worng password")

# # 5

# x = int(input("please enter your x number: "))
# y = int(input("please enter your y number: "))

# if 50 > x > 10 and 80 > y > 20:
#     print("Inside the rectangle")

# elif x == 50 or x == 10 or y == 80 or y == 20:
#     print("on the edge")

# else:
#     print("outside the rectangle")

# # 6

# name = input("please enter your name: ")
# print(f"your name is {name or "anonymous"}")

# # 7

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
# print(bool(num1) + bool(num2) + bool(num3))

# # 8 

# score = int(input("Enter your score: "))

# grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# print(grade)