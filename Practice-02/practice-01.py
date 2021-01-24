class Student:
    native_place = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Student is eating......")

    def drink(self):
        print("Student is drinking......")

    @staticmethod
    def method():
        print("This is a static method")

    @classmethod
    def cm(cls):
        print("This is a class method")


student_01 = Student("Terry", 20)
print(id(student_01))
print(type(student_01))
print(student_01)
student_01.eat()
student_01.drink()
print(student_01.name)
print(student_01.age)
# Student.native_place = "USA"
print(student_01.native_place)
student_01.method()
student_01.cm()
student_01.gender = "male"
print(student_01.gender)
def show():
    print("Dynamically binding method")
student_01.show=show()
student_01.show