# Define the list of strings
string_list = ["hello", "world", "python", "programming"]

# Loop through each string in the list and print it in reverse order
for string in string_list:
    index = len(string) - 1
    while index >= 0:
        print(string[index], end="")
        index -= 1
    print()