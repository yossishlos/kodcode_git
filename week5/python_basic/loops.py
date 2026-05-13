# # 1

# for i in range(10):
#     if i % 2 == 0:
#         continue

#     if i == 7:
#         break

# print(i)

# # 2

# while True:
#     password = input("please enter the password: ")

#     if password == "1234":
#         break

#     else:
#         print("try again")

# print("Welcome!")

# # 3

# products = []

# while True:
#     product = input("enter your product: ")

#     if product == "done":

#         break
#     else:
#         products.append(product)

# print(products)

# # 3.1

# for i in range(1, 4):
#     for j in range(1, 4):
#         if j == 2:
#             break
#     print(i, j)

# # 4

# tmp = 0
# string = input("enter string: ")

# for i in string:
#     if i in "aeiouAEIOU":
#         tmp += 1
# print(tmp)

# # 5

# result = 0
# for i in range(1, 6):
#     for j in range(1, 6):
#         result = i * j
#         print(f"{i} x {j} = {result}")

# print("1  2  3  4  5\n2  4  6  8 10\n3  6  9 12 15\n4  8 12 16 20\n5 10 15 20 25")

# # 6

# string = "yossi"
# new = ""
# for i in string:
#     new = i + new
# print(new)

# # 7

# num = "2345678"
# lengs = len(num)
# cnt = 0
# result = 0
# while lengs:
#     if int(num[cnt]) % 2 == 0:
#         result += 1
#     cnt += 1
#     lengs -= 1

# print(result)

# # 8

# string = "abc"
# new = ""
# for i in string:
#     new += i * 2
# print(new)

# # 9

# tmp = 0
# while True:
#     num = int(input("enter number: "))
#     if num == 0:
#         break
#     if num > tmp:
#         tmp = num
# print(tmp)

# # 10

# string = "hello123"

# for i in string:
#     if i.isalpha() or i in "0123456789":
#         continue
#     else:
#         print(False)
#         break
# else:
#     print(True)

# # 11

# num = 123
# tmp = 0
# while True:
#     tmp += num % 10
#     num = num // 10
#     if num == 0:
#          break
#     tmp *= 10
# print(tmp)