# Iterables - An iterable in any object that can be looped over using a loop.

numbers = [1, 2, 3]
name = "Python"
student = {"name": "Rahul", "age": 25}

for item in numbers:
    print(item)

# list, tuple, string dictionary

# Iterables vs Iterators

numbers = [10, 20, 30] # iterable
iterator = iter(numbers) # iterator

print(next(iterator))
print(next(iterator))
print(next(iterator))


# __iter__() - return iterator object
# __next__() - return the next value

numbers = [10, 20, 30]
iterator = iter(numbers)
print(iterator.__next__())
print(iterator.__next__())

# StopIteration - if you trying to access more than iterators exist then This will be occured



# Generators are a simple way to create iterators

def count_up_to(limit):
    current = 1

    while current <= limit:
        yield current # pauses the function and returns a value and its continues from where you stopped
        current += 1

for num in count_up_to(3):
    print(num)


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # StopIteration

# Generators are memory efficient
# They produce value one at a time

numbers = [x*x for x in range(1000000)]

squares = [x * x for x in range(5)]
print(squares)
# Generator Expressions
squares = (x * x for x in range(5))
print(squares)
print(next(squares))
print(next(squares))


# map() applies a function to every item in an iterable
numbers = [1, 2, 3, 4]
squares = map(lambda x : x * x, numbers)
print(list(squares))

def square(x):
    return x * x
numbers = [1, 2, 3, 4]
square = map(square, numbers)
print(list(squares))

# filter() keeps only the items that match a condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x:x % 2 == 0, numbers)

print(list(even_numbers))

# reduce()

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)