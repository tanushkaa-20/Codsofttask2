import random
import string

def generate_password(length, complexity):
    characters = ""

    if '1' in complexity:
        characters += string.ascii_lowercase
    if '2' in complexity:
        characters += string.ascii_uppercase
    if '3' in complexity:
        characters += string.digits
    if '4' in complexity:
        characters += string.punctuation

    if not characters:
        return "Complexity options not selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Hey ! that's Password Generator")

    while True:
        length = int(input("Enter the length of the password that you want : "))
        complexity = input("Enter complexity you want (1: lowercase, 2: uppercase, 3: digits, 4: special characters): ")

        password = generate_password(length, complexity)

        if password != "Complexity options not selected.":
            print("Generated Password:", password)
        else:
            print("Please select at least one complexity option.")

        another = input("Do you want to Generate another password? (yes/no): ")
        if another != "yes":
            break

    print("Thank You, See You Again  !!")

if __name__ == "__main__":
    main()
