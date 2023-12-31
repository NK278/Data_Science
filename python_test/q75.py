import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5]
        result = pool.map(square, numbers)
        print(result)
