import multiprocessing

def square_sum(numbers, result):
    """Calculate the sum of squares of numbers and store the result in the given shared array."""
    total = 0
    for num in numbers:
        total += num**2
    result.value = total

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = multiprocessing.Value('i')  # shared integer value
    p = multiprocessing.Process(target=square_sum, args=(nums, result))
    p.start()
    p.join()
    print(f"Sum of squares of {nums} is {result.value}")
