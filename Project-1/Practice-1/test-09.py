#############################Program-01#########################
# import keyword
# from decimal import Decimal
# print(keyword.kwlist)
# # try to write a annotation
# print("Hello! World!")
# # fp = open('/home/ai-xll/PycharmProjects/test-06.txt', 'a+')
# # print('This is just a test!', file=fp)
# # fp.close()
# print(r'http:\\www.baidu.com''\\')
# print(ord('乘'))
# name = "Tony Stark"
# # output the address of memory
# print(id(name))
# # output the type of object
# print(type(name))
# # output the object
# print(name)
# print(1.1 + 2.2)
# print(Decimal('1.1') + Decimal('2.2'))
#############################Program-02#########################
# c = "".join(["ab", "c"])
# print(c, type(c))
# str_01 = "Hello!Human!"
# print(str_01.index("lo"))
# print(str_01.find("lo"))
# print(str_01.find("k"))
# print(str_01.rindex("ma"))
# print(str_01.rfind("ma"))
# print(str_01.rfind("k"))
# print(str_01, id(str_01))
# # After being converted to uppercase or lowercase, the string is gonna get a new address
# print(str_01.lower(), id(str_01.lower()))
# print(str_01.upper(), id(str_01.upper()))
# print(str_01.swapcase())
# print("hello!python".title())
# str_02 = "I don't wanna work!"
# print(str_02.center(40, "*"))
# print(str_02.ljust(40, "*"))
# print(str_02.rjust(40, "*"))
# print(str_02.zfill(40))
# str_03 = "Hello|World|Python|Java|Program"
# print(str_03.split(sep="|"))
# print(str_03.rsplit(sep="|"))
# print(str_03.split(sep="|", maxsplit=3))
# print(str_03.rsplit(sep="|", maxsplit=3))
# print("1.", "hello,".isidentifier())
# print("2.", "   ".isspace())
# print("3.", "abc1234".isalpha())
# print("4.", "abc".isalpha())
# print("5.", "123456".isdecimal())
# print("6.", "123四".isdecimal())
# print("7.", "123".isnumeric())
# print("8.", "123abc".isalnum())
# str_04 = "Hello!Python!Python!Python!Python!Java!C++"
# print(str_04.replace("Hello", "Get out"))
# print(str_04.replace("Python", "World", 2))
# list_01 = ["Hello", "Python", "Java"]
# print("|".join(list_01))
# tuple_01 = ("Hello", "Python", "Java")
# print("|".join(tuple_01))
# print("*".join("Python"))
# print(">", "apple" > "app")
# print("<", "apple" < "app")
# print(ord("a"), chr(97))
# str_05 = str_04[0:7]
# str_06 = str_04[7:]
# str_07 = str_04[7::2]
# print(str_05)
# print(str_06)
# print(str_07)
#############################Program-03#########################
name = "konglong"
age = 20
print("My name is %s, I'm %d" % (name, age))
print("my name is {0}, I'm {1}, my name is {0}".format(name, age))
print(f"my name is {name}, I'm {age}")
str_01 = "海上生明月"
# Encode
print(str_01.encode(encoding="GBK"))
print(str_01.encode(encoding="utf-8"))
# Decode
byte_01 = str_01.encode(encoding="GBK")
print(byte_01.decode(encoding="GBK"))