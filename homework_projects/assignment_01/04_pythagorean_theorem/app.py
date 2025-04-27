# Import the math library so we can use the sqrt function
import math

def main():
    # Get the two side lengths from the user
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)
    
    # Print the hypotenuse
    print("The length of BC (the hypotenuse) is: " + str(bc))

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
