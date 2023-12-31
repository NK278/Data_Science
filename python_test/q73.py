from multiprocessing import Process,Queue
def calculate_sum(numbers, q):
    """
    This function takes a list of numbers and calculates the sum of them.
    The result is put into a queue to be returned to the main process.
    """
    result = sum(numbers)
    q.put(result)
if __name__ == '__main__':
    # Define the list of numbers to be summed
    numbers = [1, 2, 3, 4, 5]

    # Create a queue to communicate between processes
    q = Queue()

    # Create a process to calculate the sum of the numbers
    p = Process(target=calculate_sum, args=(numbers, q))
    p.start()

    # Wait for the result to be put in the queue and retrieve it
    result = q.get()

    # Print the result
    print(f"The sum of the numbers {numbers} is {result}.")
