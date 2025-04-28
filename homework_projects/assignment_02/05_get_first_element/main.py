def get_first_element(lst):
    """
    Prints the first element of a provided list.

    Args:
    lst (list): A non-empty list whose first element will be printed.
    """
    print(lst[0])

def get_lst():
    """
    Prompts the user to enter elements one by one to form a list.
    
    Returns:
    list: A list containing the user-entered elements.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    """
    Main function that creates the list and prints its first element.
    """
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
