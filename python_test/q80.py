import multiprocessing
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def factorial_worker(n):
    return factorial(n)
def main():
    n = 10
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(factorial_worker, range(1, n+1))
    pool.close()
    pool.join()
    print(f"The factorials of the numbers 1 to {n} are: {results}")
if __name__ == "__main__":
    main()