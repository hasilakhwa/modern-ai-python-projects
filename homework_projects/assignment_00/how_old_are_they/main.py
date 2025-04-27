# How Old Are They

from datetime import datetime

def calculate_age():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    calculate_age()
