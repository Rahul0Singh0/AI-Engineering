# Sets 
# A set is a unique collection of data. That  is elements of a set cannot be duplicate. for eg:

student_ids = {112, 113, 114, 115, 116}

print(student_ids)

print(type(student_ids))

numbers = {2, 4, 6, 6, 2, 8}

print(numbers) # automatically remove those duplicates 

numbers.add(32)
print(numbers)

num = [23, 24, 25]
numbers.update(num)

print(numbers)

numbers.discard(2) # remove from set
print(numbers)
print(len(numbers))