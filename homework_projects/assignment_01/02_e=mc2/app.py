# Constant value for the speed of light in meters per second
C: int = 299_792_458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the process and result
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# Required to call the main() function
if __name__ == '__main__':
    main()
