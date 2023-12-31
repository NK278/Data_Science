import threading,time

def p_time():
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        time.sleep(5)
time_t=threading.Thread(target=p_time)
time_t.start()
while True:
    if input()=='q': break
