def main():
    """
    Doubles each element in a list of numbers and prints the updated list.
    """
    numbers: list[int] = [1, 2, 3, 4]  # Initial list of numbers

    for i in range(len(numbers)):  # Loop through each index
        numbers[i] = numbers[i] * 2  # Double the value at each index

    print(f"Doubled list: {numbers}")


if __name__ == '__main__':
    main()
