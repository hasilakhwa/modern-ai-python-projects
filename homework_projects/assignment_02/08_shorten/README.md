List Shortener Program

Description
This program takes a list of user-inputted values and shortens it to a predefined maximum length (MAX_LENGTH). If the list exceeds the maximum length, the program removes elements from the end of the list and prints each element as it is removed. If the list is already shorter than the maximum length, it remains unchanged.

Features
Prompts the user to enter elements into a list one at a time.
Removes elements from the end of the list until it reaches the MAX_LENGTH.
Prints each element removed from the list.
If the list is already shorter than MAX_LENGTH, it doesn't change.

How It Works
User Input: The program continuously asks the user to input values. The user can press enter without typing anything to stop the input process.

Shortening the List: Once the input is finished, the program checks the length of the list. If the list is longer than the MAX_LENGTH (default is 3), it starts removing items from the end and prints each one.

Result: Finally, the program will display the items removed from the list, if any.

Requirements
Python 3.x

Usage
Run the program.

Enter values when prompted. You can stop entering values by pressing "Enter" without typing anything.

The program will print any elements removed from the list.