import logging
logging.basicConfig(filename="t10.log",level=logging.INFO)
sum_t= lambda t:( lambda res:(logging.info("input t: %s",t),logging.info("sum of t ele: %s",res)))(sum(map(int,t)))
uin=input("Enter tupule:")
ut=tuple(map(int,uin.split()))
res=sum_t(ut)