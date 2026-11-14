# First class functions - functions are first class objects.

def greet():
    return "Hello"

message = greet
print(message())

def shout(text):
    return text.upper()

def process(func, value):
    return func(value)

print(process(shout, "Python"))

def outer():
    def inner():
        print("Inside inner functions")

    return inner

func = outer()
func()


# Decorators - A decorator is a function that takes another function and extra behaviour to it and returns a new function

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_hello():
    print("Hello")

# decorated_function = my_decorator(say_hello)
# decorated_function()

say_hello()

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

print(add(10, 20))


# Timing Decorator

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)

#         end = time.time()

#         print(f"{func.__name__} tool {end - start} second")

#         return result
#     return wrapper


# @timer
# def slow_function():
#     time.sleep(2)
#     print("Done")


# slow_function()


# functools.wraps 

from functools import wraps

# def timer(func):
#     def wrapper(*args, **kwargs):
#        return func(*args, **kwargs)
#     return wrapper

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hello")

print(greet.__name__)
print(greet.__doc__)


# A class decorator is a function that takes a class, modifies it, and returns it
def add_greeting(cls):
    cls.greet = lambda self: "Hello from decorated class"

    return cls

@add_greeting
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Rahul")
print(student.name)
print(student.greet())


#Introspection - means inspecting object at run time
# So python allows us to check what attribute and method and object has

class Student:
    school = "Algocamp"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


student = Student("Rahul")
print(dir(student))
print(getattr(student, "name"))
print(getattr(student, "age", "Age not found"))

setattr(student, "age", 25)
print(student.age)


print(hasattr(student, "marks"))