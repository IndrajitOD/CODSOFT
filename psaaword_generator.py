import random

def password(length, level):

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%&*()_+-=;:,.?/~"

    if level == 1:
        chars = alphabets
    elif level == 2:
        chars = alphabets + digits
    elif level == 3:
        chars = alphabets + digits + symbols
    else:
        print("\nPlease enter a valid choice.")
        chars = alphabets

    p = ""
    for i in range(length):
        p = p + random.choice(chars)
    return p

def main():
    print("\nWelcome to my simple Password Generator\n")
    while True:
        print("-----------------------------------------------------")
        print("Choose how secure your password will be :")
        print("1. Only Alphabets (A-Z, a-z)")
        print("2. Alphabets and Numbers (A-Z, a-z, 0-9)")
        print("3. Alphabets, Numbers and Symbols")
        print("4. Exit the program")
        level = int(input("\nEnter your choice (1, 2, 3 or 4) : "))
        if level == 4:
            print("\nThank you for using my simple Password Generator!")
            print("Exiting the Password Generator\n")
            break
        length = int(input("Enter the length of password: "))
        pas = password(length, level)

        print("\nYour Generated Password is :: ", pas)
        print("-----------------------------------------------------\n")

if __name__ == "__main__":
    main()
