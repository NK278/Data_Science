import threading

def print_numbers(start, end):
    for i in range(start, end+1):
        print(i)

# create two threads
thread1 = threading.Thread(target=print_numbers, args=(1, 10))
thread2 = threading.Thread(target=print_numbers, args=(1, 10))

# start the threads
thread1.start()
thread2.start()

# wait for the threads to finish
thread1.join()
thread2.join()
