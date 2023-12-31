try:
    # Prompt user for a list of integers
    num_list = [int(num) for num in input("Enter a list of integers (separated by spaces): ").split()]

    # Calculate the average of the list
    avg = sum(num_list) / len(num_list)
    print("Average of the list:", avg)

    # Raise a ValueError if the list is empty
    if not num_list:
        raise ValueError("List is empty")
except ValueError as e:
    print("Error:", e)