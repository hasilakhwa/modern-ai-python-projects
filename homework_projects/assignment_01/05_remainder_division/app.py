def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division and modulo operation
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Remainder (modulus)

    # Display the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# This provided line is required at the end of the Python file
# to call the main() function
if __name__ == '__main__':
    main()
