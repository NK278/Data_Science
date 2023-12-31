while True:
    try:
        # Prompt user for list of strings
        string_list = input("Enter a list of strings separated by commas: ").split(",")

        # Sort list in alphabetical order
        sorted_list = sorted(string_list)

        # Check if any string contains non-alphabetic characters
        for string in sorted_list:
            if not string.isalpha():
                raise TypeError("Error: list contains non-alphabetic characters.")

        # Print sorted list
        print("Sorted list:", sorted_list)
        break
    except TypeError as e:
        print(e)
