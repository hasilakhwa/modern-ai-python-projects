# Agreement Bot

def agreement_bot():
    response = input("Do you agree? (yes/no): ").strip().lower()
    
    if response in ["yes", "y"]:
        print("Great! Let's proceed.")
    elif response in ["no", "n"]:
        print("Okay, maybe next time.")
    else:
        print("Sorry, I didn’t understand your response.")

if __name__ == "__main__":
    agreement_bot()
