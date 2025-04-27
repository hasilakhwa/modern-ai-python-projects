# Fahrenheit to Celsius Converter

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    fahrenheit_to_celsius()
