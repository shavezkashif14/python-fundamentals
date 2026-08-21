numA = float(input("Enter the first number: "))
numB = float(input("Enter the second number: "))
operator = input("Choose operator: ")

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if operator == "/":
    result = divide(numA, numB)

elif operator == "*":
    result = multiply(numA, numB)

elif operator == "+":
    result = add(numA, numB)

elif operator == "-":
    result = subtract(numA, numB)

else:
    result = "Syntax Error"
    
print("Result:", result)