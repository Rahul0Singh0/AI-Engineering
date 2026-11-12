# Object Oriented Programming Paradigm

# is a way of organizing code around objects
# An object represents a real-world entity that has 

# Attributes -- data/properties > store data about object 
# Methods -- Behaviour/actions > are functions which are defined inside the class


class Student:
    pass

student1 = Student()

# classes is a blueprint
# An object is an actual instance created from that blueprint

class Student:
    # __init__ is special method that runs automatically when a object is created.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, I am a {self.name} and {self.age} years old")

# student1 = Student("Rahul", 25)
# student1.introduce()

# self > refers to the current object

# student1 = Student()

# student1.set_name("Rahul") # Python understand this line as it -> Student.set_name("student1", "Rahul")


# instance attributes vs class attributes

# Instance attr. belong to individual objects
# class attr. shared by all the objects of a class

class Student:
    school = "abc"

    def __init__(self, name):
        self.name = name

student1 = Student("Rahul")
student2 = Student("Rohan")

print(student1.name)
print(student2.name)

print(student1.school)
print(student2.school)

# Method Overriding

# Method Overriding means a class provide its own version of a method already defined in parent class

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

# super() is used to call methods from the parent class

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __str__(self):
        return f"Student name is {self.name}"
        

student1 = Student("Rahul", "Python")
print(student1)
print(student1.name)
print(student1.course)

# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

# name : pulic
# _name : protected
# __name : private

# Dunder/magic methods

# special methods that start and end with double unnderscores

# __init__
# __str__    --> used to print the object if called it
# __len__   
# __eq__
# __add__

class Course:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

course = Course(["Rahul", "Roli"])

print(len(course))

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value

student1 = Student(90)

print(student1.marks)

student1.marks = 95

print(student1.marks)

# class method associated with class only not particular object

class Student:
    school = "abc"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("xyz")
student1 = Student("Rahul")

print(student1.school)

# static methods -- utility methods inside a class for logical grouping
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))

# difference between class and static method
# Class method uses cls and work with class data
# Static method uses neither self nor cls

# NOTE: cls is a conventional name for first argumemt for class method


# Data Classes --> help us to create classes mainly used for storing data

# They reduce boilerplate code like writing __init__ manually.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: str
    course: str = "Python"

student1 = Student("rahul", 25, "C++")

print(student1)