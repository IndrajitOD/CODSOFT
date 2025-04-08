print("\n\nWelcome to the simple calculator\n")
choice = "c"
while choice == "c":
    print("Here you have to first enter the operator and then two numbers to perform the operation\n")
    print("1. Enter + for addition")
    print("2. Enter - for subtraction")
    print("3. Enter * for multiplication")
    print("4. Enter / for division")
    print("5. Enter % for modulus division")
    print("6. Enter ^ or ** for power")
    operator = input("\nEnter the operator to perform the operation :  ")
    num1 = input("\nEnter first number: ")
    num2 = input("Enter second number: ")
    if (operator == "+"):
        print("Result is = ",int(num1) + int(num2))
    elif (operator == "-"):
        print("Result is = ",int(num1) - int(num2))
    elif (operator == "*"):
        print("Result is = ",int(num1) * int(num2))
    elif (operator == "/"):
        if (int(num2) != 0):
            print("Result is = ",int(num1) / int(num2))
        else:
            print("Error: Division by zero is not allowed")
    elif (operator == "%"):
        print("Result is = ",int(num1) % int(num2))
    elif (operator == "^" or operator == "**"):
        print("Result is = ",int(num1) ** int(num2))
    else:
        print("\nError : Please enter a valid operator\n")
    choice = input("\nEnter c to continue or any other key to quit\n")
    print("--------------------------------------------------------")
print("Thank you for using the calculator")