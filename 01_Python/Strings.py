# String is a sequence of characters used to store text

name = "Rahul"

message = "Python is fun"

# Strings are immutable, meaning they cannot be changed directly after creation

s1 = "Hello"
s2 = "Hello"
s3 = """This is a multi-line strings"""

sentence = "I'm learning python"
quote = 'He said, "Python is easy"'

text = "Python"

# strings are indexed from 0.
print(text[0])
print(text[-1])

# slicing
print(text[0:3])
print(text[:4])
print(text[2:])
print(text[::-1]) # from last indexed to first

# slicing does not modified the original string
  
name = "python"
print(name.upper())
print(name.capitalize()) # makes only the first character of entire string uppercase
print(name.title()) # first character of every word uppercase

text = "I love python"
print(text.find("python")) # return indexed start from in string
print("python" in text)

email = "     test@gmail.com     "
print(email.strip())

print(email)

sentence = "Python is powerful"

words = sentence.split()
print(words)

joined = "-".join(words)

print(joined)

text = "I like Java"
print(text.replace("Java", "Python"))

# string formatting
name = "Rahul"
age = 25
print(f"My name is {name} and i am {age} years old")
print("My name is {} and i am {} years old".format(name, age))
print("My name is %s and I am %d years old" % (name, age))

message = """Hello,
Welcome to Python Strings.
Let's Lear!"""

print(message)

# Use raw strings when working with file paths or regular expressions
path = r"C:\Users\rahul\Documents"
print(path)

# Escape Sequences
print("Hello\nWorld")
print("She said, \"Python is easy\"")
print("C:\\Users\\Rahul")

# \n > newline
# \t > tab
# \\ backslash
# \" double quote
# \' single quote

# Python strings support unicode by default
text = "Hello "
print(text)
print(ord("A"))
print(chr(65))

# Python string > bytes using UTF-8 encoding
text = "Python" # normal string
encoded = text.encode("utf-8")
print(encoded) # Output b'Python' > the b before the python means this is a pyhton object, not a normal string