from multiprocessing import Process,Value
def n_sum(s,e,t):
    for i in range(s,e+1):
        with t.get_lock(): t.value+=i
if __name__=='__main__':
    t=Value('i',0)
    p1=Process(target=n_sum,args=(1,250,t))
    p2=Process(target=n_sum,args=(251,500,t))
    p3=Process(target=n_sum,args=(501,750,t))
    p4=Process(target=n_sum,args=(751,1000,t))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join() 
    p2.join()
    p3.join()
    p4.join()

    print("total val:",t.value)
