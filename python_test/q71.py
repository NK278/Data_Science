from multiprocessing import Process

def num(s,e):
    for i in range(s,e+1): print(i)
if __name__=='__main__':
        p1=Process(target=num,args=(1,5))
        p2=Process(target=num,args=(6,10))
        p1.start()
        p1.join()
        p2.start()
        p2.join()