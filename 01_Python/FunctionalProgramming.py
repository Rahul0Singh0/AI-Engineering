# functions can be stored in variables
# passed as arguments
# returns from other functions
# used inside data transformations

def sq(x):
    return x * x

operation = sq
print(operation(5))

# HOF - higher Order function
# accept another function as argument or it returns a function

def apply_operation(func, value):
    return func(value)

def sq(x):
    return x*x

print(apply_operation(sq, 5))


#Closure - a closer is when an inner function remember variables from the outer functions even after the outer function is finished

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))


# functools provides tools for working with functions 
# reduce, partial, lru_cache, wraps
# functools.partial - partial() lets us create a new function by fixing some arguments of and existing function

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent = 2)
cube = partial(power, exponent = 3)

print(square(5))
print(cube(5))


# itertools provides efficient tools for working with iterators

# chain() - combines multiple iterables into one sequence
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = chain(list1, list2)
print(list(combined))

# combinations() - gives possible selections using repeating order 
from itertools import combinations

items = ["A", "B", "C"]
result = combinations(items, 2)

print(list(result))