print("\n\nWelcome to the simple calculator\n")
choice="c"
while choice == "c":
    print("Here you have to first enter the operator and then two numbers to perform the operation\n")
    operator=(input("Enter the operator to perform the operation\n1. Enter + for addition\n2. Enter - for subtraction\n3. Enter * for multiplication\n4. Enter / for division\n5. Enter % for modulus\n6. Enter ^ or ** for power\n"))
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    if operator=="+":
        print(int(num1)+int(num2))
    elif operator=="-":
        print(int(num1)-int(num2))
    elif operator=="*":
        print(int(num1)*int(num2))
    elif operator=="/":
        print(int(num1)/int(num2))
    elif operator=="%":
        print(int(num1)%int(num2))
    elif operator=="^" or operator=="**":
        print(int(num1)**int(num2))
    else:
        print("\nInvalid operator\n")
    choice=input("\nEnter c to continue or any other key to quit\n")
print("Thank you for using the calculator")