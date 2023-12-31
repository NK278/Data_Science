# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Prompt user for input
n = int(input("Enter a positive integer: "))

# Loop through all numbers up to n and print prime numbers
for i in range(2, n+1):
    if is_prime(i):
        print(i)