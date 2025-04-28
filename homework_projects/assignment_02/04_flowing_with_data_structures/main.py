def add_three_copies(my_list, data):
    """
    Adds three copies of the given data into the provided list.

    Args:
    my_list (list): The list to which data will be appended.
    data (any): The data to copy into the list.
    """
    for _ in range(3):
        my_list.append(data)

def main():
    """
    Main function that takes user input, displays the list before and after modification.
    """
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
