# Functions are reusable block of code to perform a specific task.
# They help reduce repetition and make code modular.

def greet(): # define the function
    print("Hello")

greet() # call the function

def introduce(name, age):
    print(f"{name} is {age} years old")

introduce("Rahul", 25)

# Keyword arguments passes using parameter names, so the order does not matter

introduce(age = 25, name = "rahul")

# default arguments are used when no value is passed for a parameter
def greet(name = "student"):
    print(f"Hello, {name}")


greet()
greet("Rahul")

# *args allow a function to accept any no of positional arguments. It stores them as a tuple

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20, 30))

# *keyargs allow a function to accept any number of keyword arguments. It stores them as a dictionary
def show_profiles(**kwargs):
    print(kwargs)

show_profiles(name= "Rahul", age= 25)

# the return keyword sends a value back from a function to the place where it is called 

def square(num):
    return num * num

result = square(5)

print(result)

# multiple return values, seperated by commas
def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)

print(add, sub, mul)

# Scope in Python
# Local > A variable created inside a function is local abd can only used inside that function

def greet():
    message = "Hello"
    print(message)

# Global > A varibale created outside all functions is global and can be accessed inside function

name = "Rahul"
def greet():
    print(name)

greet()

# global keyword is used when we want to modify a global variable inside a function
count = 0
def increment():
    global count
    count += 1

increment()
print(count)

# nonlocal keyword is used in nested functions to modify a variable from outer function
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)

outer()

# Lambda expressions are small anonymous functions used for short one-line operations
square = lambda x: x * x

print(square(3))

add = lambda a, b : a + b
print(add(2,3))

is_even = lambda num: num % 2 == 0

to_upper = lambda text: text.upper()

# Docstring used to describe what a function does. They are usually written inside triple quotes
def add(a, b):
    """
    Adds to numbers and return result.
    """
    return a + b


# Type Annotations describe the expected input and output types of a function
def add(a: int, b: int) -> int:
    return a + b