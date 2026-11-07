print("Hello World")

# Python Identifiers

# Identifiers are the names give to variables, classes, methods.
language = "Python"

# Keywords
# Keywords are predefined, reserved words used in python programming that have special meanings to the compiler.
# continue = 'Hello' # Can't be used as define an identifier

# Rules for naming Identifier

# 1. Identifiers cannot be a keyword
# 2. Identifiers are case sensitive score 
# 3. It can have a sequence of letter and digits, However, it must always begin with a letter or _. The first letter of an identifier cannot be a digit
# 4. Whitespace are not allowed
# 5. We cannot use special symbols like ! @ # $ and so on..

# Variables: 
language_name = "python"
print(language_name)

language_name = "java"
print(language_name)

language_name = 1
print(language_name)

a, b, c = 5, 3.2, "Hello"
print(a) # 5
print(b) # 3.2 
print(c) # Hello

site1 = site2 = 'This is the end!!!!'
print("--------------------------------")
print(site1)
print(site2)

# Constant
PI = 3.14
result = True

# Python DataTypes
# Data types specify the type of data that can be stored inside a variable.

# 1. Numeric
# 2. String
# 3. Sequence -> list, tuple, range
# 4. Mapping -> dict
# 5. Boolean -> bool (True/False)
# 6. Set -> set, frozenset

print("--------------------------------------")
num1 = 5
print(type(num1))
num2 = 5.0
print(type(num2))

# Python List data type
# List is an ordered collection of similer or different types of items seperated by commas and enclosed within brackets [].

languages = ['C++', 'Java', 'Python']
print('--------------------------------------')
# You can access value by its indexed
print(languages[0])


# Tuple data type
# Tuple is an ordered sequence of items same as a list. The only difference is that tuples are not immutable. Tuples once created cannot be modified.
# Access via indexed

products = ('abc', 100)
print(products[0])

# String data type
# String is a sequence of characters represented by either single or double quotes.

name = "Python"
print(name)

message = "Python is a beginer friendly language"
print(message)

# Set data type
# Set is an unordered collection of unique elements. Set is defined by values seperated by comma inside braces {}.

student_ids = {1, 2, 3, 4, 5}

print(student_ids)


# Python dictionary data type
# Dictionary is an ordered collection of items. It stores elements in key/value pairs.
# Keys are unique identifiers that are associated with each value.

capitals = {'Nepal': 'Kathmandu', 'India': 'New Delhi', 'Italy': 'Rome'}
print(capitals)

# Keys -> Nepal, India, Italy
# Values -> Kathmandu, New Delhi, Rome
print(capitals['India']) # access via key



# Type Conversion
# It is a process of converting data of one type to another.

# 1. Implicit  -> Automatic type conversion
# 2. Explicit  -> Manual type conversion

# Implicit Type conversion
int_number = 123
float_number = 1.23

# Addition forces implicit conversion
val = int_number + float_number
print(val)



# Explicit Type conversion
num_string = '12'
num_integer = 12

print(type(num_string))
num_string = int(num_string)
print(type(num_string))

# Python Input and Output
a = 5
print(a)

print('Python is ' + 'awesome')

x = 5
y = 10 
print('The value of x is {} and y is {}'.format(x, y))

# Python Input
prompt = 'Hello'
input(prompt)

num = input("Enter a number: ")
print(num)