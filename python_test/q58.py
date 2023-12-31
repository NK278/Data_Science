# Prompt user for input
n = int(input("Enter a positive integer: "))

# Initialize variables for the first two Fibonacci numbers
fib1 = 0
fib2 = 1

# Print the first Fibonacci number (0)
print(fib1)

# Print the second Fibonacci number (1)
print(fib2)

# Loop through all remaining Fibonacci numbers up to n
while fib2 <= n:
    # Compute the next Fibonacci number and print it
    fib3 = fib1 + fib2
    print(fib3)

    # Update variables for the next iteration
    fib1 = fib2
    fib2 = fib3