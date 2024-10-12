#exception handling
#1. try 2. except 3. else 4. finally


#Zero division error handle(example1):
num1 = int(input("enter a first number:"))#10
num2 = int(input("enter a second number:"))#0
try:
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("divide by zero is not possible")
print("rest of code")

#Name Error and zero division error(example 2):
num1 = int(input("enter a first number:"))#10,10
num2 = int(input("enter a second number:"))#0,4
try:
    div = num1 / num2 #first exception handle always
    print(di)
except ZeroDivisionError: #exception have a built in class
    print("divide by zero is not possible")
except NameError:
    print("variable name is wrong")
print("rest of code")

#(Example 3):
num1 = int(input("enter a first number:"))#10,10
num2 = int(input("enter a second number:"))#0,4
try:
    div = num1 / num2 #first exception handle always
    print(di)
except(ZeroDivisionError,NameError) as obj:
    print(obj)
print("rest of code")

#if you not know which error occured(example4):
num1 = int(input("enter a first number:"))#10,10
num2 = int(input("enter a second number:"))#0,4
try:
    div = num1 / num2 #first exception handle always
    print(di)
except:
    print("something went wrong")
print("rest of code")

#else and finally block(example5):
num1 = int(input("enter a first number:"))#10,10
num2 = int(input("enter a second number:"))#0,4
try:
    div = num1 / num2
    print(div)
except:
    print("something went wrong")
else:
    print("an exception is not occured")
finally:
    print("always executed")
print("rest of code")

#exection is a built in class
import sys
num1 = int(input("enter a num1:"))
num2 = int(input("enter a num2:"))
try:
    div = num1 / num2 #those exception which occurred first can handled
    print("divison is:",div)
except:
    print(sys.exc_info()[0]) #to see class
    print(sys.exc_info()[1]) #to see information
print("rest of code")

# to create an exception we need to follow these steps:
#     1.call class
#     2.constructor
#     3.raise statement

#raise:
#for built in excption(example1):
try:
    age = int(input("enter your age:")) #-10
    if age<0:
        raise ValueError
    print("your age is:",age)
except ValueError:
    print("enter valid age")
print("rest of code")

# statement in valuerror
try:
    age = int(input("enter your age:")) #-10
    if age<0:
        raise ValueError("invalid age")
    print("your age is:",age)
except ValueError as var:
    print(var)
print("rest of code")

# #user defined exception:
class FiveDivisionError(Exception):
    "this is exception class called when five division error happens"
    pass
try:
    n1 = int(input("enter a 1st number:"))
    n2 = int(input("enter a 2nd number:"))
    if n2 == 5:
        raise FiveDivisionError("cannot divide by five")
    div = n1 / n2
    print("division is",div)
except(FiveDivisionError,ZeroDivisionError) as var:
    print(var)
print("rest of code")




