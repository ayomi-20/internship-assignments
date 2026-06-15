def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if (b == 0):
        return "cannot divide by zero."
    else:
        return a / b


number1 = float(input("enter your first number: "))
choice = input("choose an operation {\n1: addition\n2: subtraction\n3: multiplication\n4: division}: ")
number2 = float(input("Enter your second number: "))

if (choice == "1"):
    print(addition(number1, number2))
elif(choice == "2"):
    print(subtraction(number1, number2))
elif(choice == "3"):
    print(multiplication(number1, number2))
elif(choice == "4"):
    print(division(number1, number2))
else:
    print("Invalid Input!")