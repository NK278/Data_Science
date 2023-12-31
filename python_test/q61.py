import threading
def even():
    for i in range(0,11,2): print(i)
def odd():
    for i in range(1,10,2): print(i)

# threads
t1=threading.Thread(target=even)
t2=threading.Thread(target=odd)

# start threads
t1.start()
t2.start()
# wait for threads ti finish
t1.join()
t2.join()