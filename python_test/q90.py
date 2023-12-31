try:
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Divide the number by 2
    result = 2 / num

    # Print the result
    print("Result:", result)
except ValueError:
    # Handle the case where the user did not enter a valid number
    print("Error: You must enter a valid number")
except ZeroDivisionError:
    # Handle the case where the user entered 0 as the number
    print("Error: You cannot divide by zero")
finally:
    # Clean up resources or run some final code
    print("Thank you for using this program!")