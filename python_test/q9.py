import logging
logging.basicConfig(filename="t8.log",level=logging.INFO)
uin=int(input("Enter x:"))
logging.info("User input: %s",uin)
isams= lambda n:n==sum(int(d)**len(str(n)) for d in str(n))
res=isams(uin)
logging.info("amstrong no or not: %s",res)