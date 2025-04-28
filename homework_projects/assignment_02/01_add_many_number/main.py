def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes a list of numbers and returns their sum.
    
    Args:
        numbers (list[int]): List of integers to sum.
    
    Returns:
        int: The sum of all numbers in the list.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far


def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Example list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)
    print(f"The sum of the numbers is: {sum_of_numbers}")


if __name__ == '__main__':
    main()
