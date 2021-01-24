#############################Program-01#########################
# # Balance
# count = 1000
# # Withdrawal
# money = int(input("Please input withdrawal:\n"))
# # Judge whether the balance is sufficient
# if money <= count:
#     count = count - money
#     print("Successful! The count is", count)
# else:
#     print("Insufficient!")
#############################Program-02#########################
# """
# multiple-branching constructuon
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 E
# Less than 0 or more than 100 is illegal data
# """
# score = int(input("Please input a grade:\n"))
# if score <= 100 and score >= 90:
#     print("Level A")
# elif score >= 80 and score <= 89:
#     print("Lever B")
# elif score >= 70 and score <= 79:
#     print("Level C")
# elif score >= 60 and score <= 69:
#     print("Level D")
# elif score >= 0 and score <= 59:
#     print("Level E")
# else:
#     print("Illegal Data")
#############################Program-03#########################
# """
# Compare the size of two integers
# """
# num_a = int(input("Please input the first integer:\n"))
# num_b = int(input("Please input the second integer:\n"))
# print( str(num_a)+">="+str(num_b) if num_a >= num_b else str(num_a)+"<"+str(num_b))
#############################Program-04#########################
# Style one
# r1 = range(10)
# print(r1)
# print(list(r1))
# # Style two
# r2 = range(1, 10)
# print(r2)
# print(list(r2))
# # style three
# r3 = range(1, 10, 2)
# print(r3)
# print(list(r3))
# print(10 in r3)
# print(10 not in r3)
#############################Program-05#########################
# sum = 0
# a = 1
# while a <= 10:
#     sum += a
#     a += 1
# print("Sum of 1-10 is", sum)
#
# sum1 = 0
# start1 = 2
# while start1 <= 100:
#     sum1 += start1
#     start1 += 2
# print("Sum of even in 1-100", sum1)
#
# sum2 = 0
# start2 = 1
# while start2 <= 100:
#     if start2 % 2 == 0:
#         # if not bool(start2%2):
#         sum2 += start2
#     start2 += 1
# print("Sum of even in 1-100", sum2)
#############################Program-06#########################
# for item in "Python":
#     print(item, end="")
# print("\n")
#
# for item in range(1, 10):
#     print(item, end=" ")
# print("\n")
#
# sum = 0
# for item in range(1, 101):
#     if item % 2 == 0:
#         sum += item
# print(sum)
#
# for item in range(100, 1000):
#     # single digit
#     position_01 = item % 10
#     # tens digit
#     position_02 = item // 10 % 10
#     # hundreds digit
#     position_03 = item // 100
#     # judge whether the number is Narcissistic number
#     if position_01 ** 3 + position_02 ** 3 + position_03 ** 3 == item:
#         print(item, end=" ")
#############################Program-07#########################
# for item in range(3):
#     passw = str(input("Please input your password:\n"))
#     if passw == "123456":
#         print("Correct!")
#         break
#     elif item == 2:
#         print("Log out!")
#     else:
#         print("Please try again")
#
# flag = 1
# while flag <= 3:
#     passw = str(input("Please input your password:\n"))
#     if passw == "123456":
#         print("Correct!")
#         break
#     elif flag == 3:
#         print("Log out!")
#     else:
#         print("Please try again")
#     flag += 1
#############################Program-08#########################
# for item in range(1, 51):
#     if item % 5 == 0:
#         print(item, end=" ")
# print("\n")
# for item in range(1, 51):
#     if item % 5 != 0:
#         continue
#     print(item, end=" ")
#############################Program-09#########################
# for item in range(3):
#     passw = input("Please input your password:\n")
#     if passw == "123456":
#         print("Correct!")
#         break
#     else:
#         print("Invalid password! Please try again!")
# else:
#     print("Log out!")
#
# flag = 0
# while flag < 3:
#     passw = input("Please input your password:\n")
#     if passw == "123456":
#         print("Correct!")
#         break
#     else:
#         print("Invalid password! Please try again!")
#     flag += 1
# else:
#     print("Log out!")
#############################Program-10#########################
# # Set up the number of row
# for i in range(3):
#     # Set up the number of column
#     for j in range(5):
#         print("*", end=" ")
#     print("\n")
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(str(j) + "x" + str(i) + "=" + str(j * i), end="  ")
#     print("\n")
#############################Program-11#########################
# # The first way to create a list
# list_01 = ["element-01", "element-02", 95, "element-01"]
# # The second way to create a list
# list_02 = list(["element-01", "element-02", 96])
# list_03 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list_04 = list_03[1:6:1]
# print(list_01)
# print(list_01[0], list_01[-3])
# print(list_01.index("element-01"))
# print(list_01.index("element-01", 0, 4))
# print(id(list_01))
# print(list_04)
# print(id(list_04))
# print(list_03[::2])
# print(list_03[:0:-1])
#############################Program-12#########################
# list_01 = [10, 20, 30, 40, 50, 60, 70]
# print(10 in list_01)
# print(100 in list_01)
# print(10 not in list_01)
# print(list_01, id(list_01))
# list_01.append(100)
# print(list_01, id(list_01))
# list_02 = ["hello", "world"]
# list_01.append(list_02)
# print(list_01, id(list_01))
# list_01.extend(list_02)
# print(list_01, id(list_01))
# list_01.insert(40, "20")
# print(list_01, id(list_01))
# list_01[20::] = list_02
# print(list_01)
# list_01.remove(100)
# print(list_01)
# list_01.pop(4)
# print(list_01, id(list_01))
# # list_01.clear()
# # del list_01
#############################Program-13#########################
# list_01 = [10, 20, 30, 40, 50, 60, 70]
# print(id(list_01))
# list_01[2] = 100
# print(list_01, id(list_01))
# list_01[1:3] = [400, 400, 500]
# print(list_01)
#############################Program-14#########################
# list_01 = [10, 20, 300, 400, 500, 60, 70]
# print(list_01, id(list_01))
# list_01.sort()
# print(list_01, id(list_01))
# list_01.sort(reverse=True)
# print(list_01, id(list_01))
# list_02 = sorted(list_01)
# print(list_02, id(list_02))
# list_03 = sorted(list_02, reverse=True)
# print(list_03, id(list_03))
# list_04 = [i for i in range(1, 10)]
# print(list_04)
# list_05 = [i * 2 for i in range(1, 6)]
# print(list_05)
#############################Program-15#########################
# The first way to create a dictionary by {}
# scores = {"Jerry": 40, "Tommy": 50, "Tom": 60}
# print(scores)
# print(scores["Jerry"])
# print(scores.get("Jerry"))
# print(type(scores))
# # The second way to create a dictionary, build-in function dict()
# student = dict(name="Jack", age=20)
# print(student)

