import threading ,random
def sort_l(v,s,e):
    v[s:e]=sorted(v[s:e])
v=[random.randint(1, 100) for _ in range(10)]
print("original list: ",v)
t1=threading.Thread(target=sort_l,args=(v,0,len(v)//2))
t2=threading.Thread(target=sort_l,args=(v,len(v)//2,len(v)))
t1.start()
t2.start()
t1.join()
t2.join()
s_l=sorted(v)
print("sorted list: ",s_l)

