import multiprocessing

def my_function(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.starmap(my_function, [(2, 3), (4, 5)])
    print(results)