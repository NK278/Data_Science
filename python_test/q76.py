import multiprocessing

def my_function():
    print("This is a child process.")

if __name__ == '__main__':
    p = multiprocessing.Process(target=my_function)
    p.start()