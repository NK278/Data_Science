# Prompt user for input
n = int(input("Enter a positive integer: "))

# Initialize the factorial variable to 1
factorial = 1

# Loop through all integers from 1 to n
i = 1
while i <= n:
    # Multiply the current value of the factorial variable with i
    factorial *= i

    # Update the loop counter
    i += 1

# Print the final factorial value
print(factorial)