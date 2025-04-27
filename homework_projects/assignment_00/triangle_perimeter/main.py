# Triangle Perimeter

def triangle_perimeter():
    try:
        a = float(input("Enter length of side A: "))
        b = float(input("Enter length of side B: "))
        c = float(input("Enter length of side C: "))
        
        perimeter = a + b + c
        print(f"The perimeter of the triangle is: {perimeter}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    triangle_perimeter()
