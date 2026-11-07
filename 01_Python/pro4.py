# for loop
languages = ['Java', 'C++', 'Python', 'C#']

for language in languages:
    print(language)


values = range(4) # 0 to 3
print(values)
for i in values:
    print(i)

# while loop
i = 1
n = 5

while(i <= n):
    print(i)
    i = i + 1

# NOTE - Python does not have built in functionality to create do while loop like other languages
# But we can simulate the structure of do while loop in other way

# Break and continue statements
# Break statement is used to terminate the loop immediately when it is encountered.

for i in range(5):
    if i == 3:
        break
    print(i)

# Continue statement is used to skip the current iteration of the loop and the control the flow of the program
for i in range(5):
    if i == 3:
        continue
    print(i)


# python switch statements - introduces after python 3.10
lang = 'Java'
match lang:
    case 'Javascript':
        print("let's start js")
    case 'Python':
        print('Python it is')
    case _:
        print('the language does not matter')


# Functions
# A block of code that performs a specific task.
# Standard library functions
# User defined functions

def greet():
    print("Hello World")

greet()

def add_numbers(num1, num2):
    sum = num1 + num2
    print(sum)

add_numbers(2, 3)

def find_square(num):
    result = num * num
    return result

sq = find_square(3)
print(sq)

# Benifits 
# 1. Code reusable
# 2. Code readability

# Python List
# used to store multiple data at once.
numbers = [1, 2, 3]
print(numbers)

my_list = []
my_list = [1, "hello", 3.15]
print(my_list)

languages = ['Java', 'C++', 'Python', 'C#']

print(languages[0])
print(languages[3])
print(languages[-2]) # indexing from end to start

# Access the particular section of items in list via slice operator in list
print(languages[1:3])
print(languages[2:])
print(languages[:])

languages.append('swift')
print(languages)

prime_numbers = [2, 3, 5]
even_numbers = [4, 6, 8]

prime_numbers.extend(even_numbers)
print(prime_numbers)

# languages[2] = 'C'
# print(languages)

# del languages[2]
print(languages)

languages.remove('Java')
print(languages)

print('Python' in languages)
print(len(languages))

