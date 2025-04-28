def get_last_element(lst):
    """
    Prints the last element of the provided list.

    Args:
    lst (list): A non-empty list whose last element will be printed.
    """
    # Two correct ways to access the last element
    print(lst[len(lst) - 1])
    # OR simply: print(lst[-1])

def get_lst():
    """
    Prompts the user to enter elements one at a time to form a list.

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
    Main function that collects user input into a list and prints the last element.
    """
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
