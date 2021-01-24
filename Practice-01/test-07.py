# import time
#
# print("---RUNOOB EXAMPLE ： Loading 效果---")
# print("Loading", end="")
# for i in range(20):
#     print(".", end='', flush=True)
#     time.sleep(0.5)

# str1 = input("Please input a string:")
# print(str1, type(str1))

# Operators in Python
# Chained assignment
a = b = c = 4
print(a, type(a), b, type(b), c, type(c))
# Parameter assignment
a = 20
a += 10
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 4
print(a)
a //= 3
print(a)
a %= 2
print(a)
# unpack assignment
a, b, c = 10, 20, 30
print(a, b, c)
a, b, c = c, b, a
print(a, b, c)
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1))
print(id(list2))
# boolean operator
a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 or b == 3)
str2 = "Hello"
print("H" in str2)
print("K" in str2)
print("K" not in str2)
print(4 & 8)
print(4 | 8)
print(4 << 1)
print(4 >> 10)
