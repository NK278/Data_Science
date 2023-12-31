import math

while True:
    try:
        # Prompt user for number
        num = float(input("Enter a number: "))

        # Check if number is negative
        if num < 0:
            raise ValueError("Error: number cannot be negative.")

        # Calculate square root
        result = math.sqrt(num)
        print("The square root of", num, "is", result)
        break
    except ValueError as e:
        print(e)
