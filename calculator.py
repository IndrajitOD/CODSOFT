def display_menu():
    print("--------------------------------------------------------")
    print("1. Enter + for addition")
    print("2. Enter - for subtraction")
    print("3. Enter * for multiplication")
    print("4. Enter / for division")
    print("5. Enter % for modulus division")
    print("6. Enter ^ or ** for power")
    print("7. Enter E or e to exit the calculator")

def perform_operation(operator, num1, num2):
    if operator == "+":
        print("Result is =",num1 + num2)
    elif operator == "-":
        print("Result is =",num1 - num2)
    elif operator == "*":
        print("Result is =",num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result is =",num1 / num2)
        else:
            return "Error: Division by zero is not allowed"
    elif operator == "%":
        print("Result is =",num1 % num2)
    elif operator == "^" or operator == "**":
        print("Result is =",num1 ** num2)
    else:
        print("Error! Please enter a valid operator") 

def main():
    print("\n\nWelcome to the simple calculator\n")
    print("Here you have to first enter the operator and then two numbers to perform the operation\n")

    while True:
        display_menu()
        operator = input("\nEnter the operator to perform the operation: ")
        if operator == "E" or operator == "e":
            print("Exiting the calculator. Thank you for using the simple calculator!")
            break
        num1 = input("\nEnter first number: ")
        num2 = input("Enter second number: ")
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            perform_operation(operator, num1, num2)
        else:
            print("\nInvalid input. Please enter valid numbers.\n")

if __name__ == "__main__":
    main()