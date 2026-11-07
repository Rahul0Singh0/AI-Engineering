# Exceptions are errors that occur while the program is running.
# If they are not handled, the program stops execution

# num = int('abc')

# ValueError
# FileNotFoundError
# IndexError
# KeyError
# TypeError
# ZeroDivisionError
# Traceback

# A traceback shows where the error happend and what type of error occured

# def divide(a, b):
#     return a / b

# divide(10, 0)

# try except

# try is used to write risky code. except handle the error if something goes wrong

try:
    # num = int(input("Enter a number: "))
    # print(num)
    result = 10 / 0
except ValueError:
    print("Invalid input. Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Conversion successful: ", num)
finally:
    print("this always runs")


try:
    result = 10 / 0
except Exception as e:
    print("Something went wrong: ", e)


# raise
# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient Balance")

#     return balance - amount

# print(withdraw(1000, 15000))


# Custom Exceptions helps us to create meaningful errors for our own application

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    return balance - amount

try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(e)

# Exception chaining is used when one exception happens because of another exception

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise ValueError("Failed to convert value to integer") from e

convert_to_int("abc")


# finally 
# finally  --- cleanup
file = None
try: 
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print('file not found')

finally:
    if file:
        file.close()