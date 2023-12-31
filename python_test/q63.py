import threading
balance=0
lock=threading.Lock()
def deposit():
    global balance
    for i in range(10):
        lock.acquire()
        balance+=100
        print("Deposited $100, balance is now $" + str(balance))
        lock.release()
def withdraw():
    global balance
    for i in range(10):
        lock.acquire()
        balance-=50
        print("Withdrawn $50, balance is now $" + str(balance))
        lock.release()
deposit_t=threading.Thread(target=deposit)
withdraw_t=threading.Thread(target=withdraw)
deposit_t.start()
withdraw_t.start()
deposit_t.join()
withdraw_t.join()