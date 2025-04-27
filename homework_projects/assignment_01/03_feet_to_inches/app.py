"""
An example program with constants
"""

# Constant value: Number of inches in one foot
INCHES_IN_FOOT: int = 12

def main():
    # Get the number of feet from user
    feet: float = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT
    
    # Output the result
    print("That is", inches, "inches!")

# Required to call the main() function
if __name__ == '__main__':
    main()
