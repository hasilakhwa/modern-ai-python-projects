# Add Two Numbers

def add_two_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    add_two_numbers()
