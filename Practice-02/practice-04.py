# # Reading
# file = open("test_01.txt", "r")
# print(file.readlines())
# file.close()
# # Writing
# file = open("test_02.txt", "w")
# file.write("Hello!I wanna date with you!\nThis is the second line!")
# file.close()
# # With
# with open("test_01.txt", "r") as file:
#     print(file.readlines())
import os

print(os.path.abspath("test_01.txt"))
path_01 = os.getcwd()
print(path_01)
list_01 = os.listdir(path_01)
for filename in list_01:
    if filename.endswith(".py"):
        print(filename)
list_02=os.walk(path_01)
for dirpath,dirname,filename in list_02:
    print(dirpath)
    print(dirname)
    print(filename)