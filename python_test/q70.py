import threading
def sum_num():
    res=sum(range(1,101))
    print("sum is:",res)
th=threading.Thread(target=sum_num)
th.start()
th.join()