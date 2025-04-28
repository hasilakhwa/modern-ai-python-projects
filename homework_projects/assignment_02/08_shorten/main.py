MAX_LENGTH = 3  # Maximum length of the list

def shorten(lst):
    # Continue removing elements from the end of the list until it reaches MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)  # Print the element that was removed

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    shorten(lst)  # Shorten the list to MAX_LENGTH and print removed elements

if __name__ == '__main__':
    main()
