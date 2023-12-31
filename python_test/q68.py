import threading

def fib(n):
    """
    Print the Fibonacci sequence up to n.
    """
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b

# Prompt the user for the value of n
n = int(input("Enter a number: "))

# Create a thread to print the Fibonacci sequence
t = threading.Thread(target=fib, args=(n,))
t.start()

# Wait for the thread to finish before exiting
t.join()