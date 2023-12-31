import threading

shared_variable = 0
lock = threading.Lock()

def increment_variable():
    global shared_variable
    lock.acquire()
    shared_variable += 1
    lock.release()

num1 = threading.Thread(target=increment_variable)
num2 = threading.Thread(target=increment_variable)

num1.start()
num2.start()

num1.join()
num2.join()

print("Shared variable value: ", shared_variable)
