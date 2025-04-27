# Square a Number

def square_number():
    try:
        number = float(input("Enter a number to square: "))
        squared = number ** 2
        print(f"The square of {number} is {squared}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    square_number()
