#############################Program-01#########################
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def show(self):
#         print(self.name, self.__age)
#
#
# student_01 = Student("Jim", 30)
# student_01.show()
# print(dir(student_01))
# print(student_01._Student__age)
#############################Program-02#########################
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print("name:{0},age:{1}".format(self.name, self.age))
#
#
# class Student(Person):
#     def __init__(self, name, age, score):
#         super().__init__(name, age)
#         self.score = score
#
#     def info(self):
#         super().info()
#         print(self.score)
#
#
# class Teacher(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school
#
#     def info(self):
#         super().info()
#         print(self.school)
#
#
# student_01 = Student("Jerry", 20, 1001)
# student_01.info()
# teacher_01 = Teacher("Tom", 40, "Beijing")
# teacher_01.info()
#############################Program-03#########################
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "My name is {0}, I'm {1} years old.".format(self.name, self.age)
#
#
# student_01 = Student("Jack", 30)
# print(dir(student_01))
# print(student_01)
#############################Program-04#########################
# class Animal():
#     def show(self):
#         print("This is an animal.")
#
#
# class Dog(Animal):
#     def show(self):
#         print("This is a dog")
#
#
# class Cat(Animal):
#     def show(self):
#         print("This is a cat")
#
#
# class Person:
#     def show(self):
#         print("This is a Person")
#
#
# def fun(something):
#     something.show()
#
#
# fun(Dog())
# fun(Cat())
# fun(Person())
# print(dir(object))
# print(object.__dict__)
#############################Program-05#########################
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name + other.name
#
#
# student_01 = Student("Terry")
# student_02 = Student("Jack")
# student_03 = student_01 + student_02
# print(student_01.name)
# print(student_02.name)
# print(student_03)
# print(type(student_03))
#############################Program-06#########################
# """
# Two special BIFs
# __new__(): To create a object
# __init__(): To initialize the new object
# """
#
#
# class Person:
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__ is called, the id of cls is {0}".format(id(cls)))
#         obj = super().__new__(cls)
#         print("The id of created object is {0}".format(id(obj)))
#         return obj
#
#     def __init__(self, name, age):
#         print("__init__ is called, the id of self is {0}".format(id(self)))
#         self.name = name
#         self.age = age
#
#
# print("The id of object is {0}".format(id(object)))
# print("The id of Person is {0}".format(id(Person)))
# p1 = Person("Jack", 230)
# print("The id of p1 is {0}".format(id(p1)))
#############################Program-07#########################
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# Variable assignments
cpu_01 = CPU()
cpu_02 = cpu_01
print(cpu_01)
print(cpu_02)
# Shallow Copy
disk = Disk()
computer = Computer(cpu_01, disk)
import copy

computer_01 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer_01, computer_01.cpu, computer_01.disk)
# Deep Copy
computer_02 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer_02, computer_02.cpu, computer_02.disk)
