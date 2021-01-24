#############################Program-01#########################
# def fun(arg1, arg2):
#     print("arg1=", arg1)
#     print("arg2=", arg2)
#     arg1 = 100
#     arg2.append(10)
#     print("arg1=", arg1)
#     print("arg2=", arg2)
#
#
# n1 = 10
# n2 = [22, 33, 44]
# print("n1=", n1)
# print("n2=", n2)
# fun(n1, n2)
# print("n1=", n1)
# print("n2=", n2)
#############################Program-02#########################
# def fun(num):
#     odd = []
#     even = []
#     for i in num:
#         if i % 2:
#             odd.append(i)
#         else:
#             even.append(i)
#     return odd, even
#
#
# list_01 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# print(fun(list_01))
#############################Program-03#########################
# def show(name, age, height):
#     print(name, age, height)
#
#
# show(age=20, name="suibian", height=168)
# def test_01(x, y, *args):
#     res = x + y
#     print(x, y, args)  # *args-->多于的参数，位置参数传入，以元组的形式接收
#
#
# test_01(1, 2, 7, 8, 6)
# test_01(2, 3, {"name": "alex"})  # 即使传入字典，字典当成整体也会以元组的方式被接收
# test_01(3, 4, ["alex", "James"], "hello world")
# test_01(3, 4, *["alex", "James"])  # 相当于该列表遍历，逐个添加至列表并且转为元组
# test_01(3, 4, *"alex")
#
#
# def test_02(x, y, **kwargs):
#     res = x + y
#     # print(x,y)
#     print(x, y, kwargs)  # **kwargs-->位置参数传入，以字典的形式接收
#     return res
#
#
# test_02(x=1, y=3, name="alex")
# test_02(1, 2, **{"name": "Amanda"})
# def fun(a, b, c):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#
#
# fun(10, 20, 30)
# list_01 = [11, 22, 33]
# fun(*list_01)
# dic_01 = {"a": 111, "b": 222, "c": 333}
# fun(**dic_01)
#
#
# def fun_01(a, b, *, c, d):
#     print(a, b, c, d)
#
#
# fun_01(10, 20, c=30, d=40)
#############################Program-04#########################
# def fac(n):
#     if n != 1:
#         return n * fac(n - 1)
#     else:
#         return 1
#
#
# print(fac(6))
# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))
# for i in range(1, 7):
#     print(fib(i))
