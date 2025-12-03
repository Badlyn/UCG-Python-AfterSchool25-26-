# Her is a function called add(a, b) is created where
# any given two numbers are added together.

#Creating the function called add which has two parameters a & b.
def add (a,b):
    return a + b

# Recieving tw no.s from the user and converting it to
# float for smooth addition
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Calling the add function and printing the result.

print(f"The number {num1} and {num2} added together = {add(num1, num2)}")

#Subractcion Function
def sub(a,b):
    return a - b

#Multiplication Function
def mul(a,b):
    return a * b

#Division Function
def div(a,b):
    return a / b

#Modulus Function
def mod(a,b):
    return a % b

#Print Statements
print(f"The numbers {num1} and {num2} subtracted together = {sub(num1, num2)}")
print(f"The numbers {num1} and {num2} multiplied together = {mul(num1, num2)}")
print(f"The numbers {num1} and {num2} divided together = {div(num1, num2)}")
print(f"The numbers {num1} and {num2} modulo together = {mod(num1, num2)}")
