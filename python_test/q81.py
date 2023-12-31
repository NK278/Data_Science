while True:
    try:
        x = int(input("Enter the first integer: "))
        y = int(input("Enter the second integer: "))
        result = x / y
        print("Result: ", result)
        break
    except ValueError:
        print("Please enter integers only.")
    except ZeroDivisionError:
        print("Error: division by zero. Please enter a non-zero value for the second integer.")

