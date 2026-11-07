# Operators
# Symbols used to perform operations on values and variables.

a = 10
b = 5

print(a + b)

# Arithmetic Operators
a = 10 
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) # division
print(a // b) # floor 
print(a % b) # modulo
print(a ** b) # power

# Assignment Operators
x = 10

x += 5
print(x)

x -= 2
print(x)

# Comparision Operators
a = 10
b = 5

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Logical Operators
age = 25
has_id = True

print(age >= 18 and has_id) # both conditions are true
print(age >= 18 or has_id) # atleast one condition is true
print(not has_id) # not operator

# Membership Operators
# check whether a value exists inside a sequence
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)
print("grapes" not in fruits)

# Identity Operators
# Check whether two variables refer to the same object in memory

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True -> check objects are same or not
print(a is c) # False -> check objects are same or not
print(a == c) # Check values

# Operator precedence
result = 10 + 5 * 2
print(result)
result = (10 + 5) * 2
print(result)
