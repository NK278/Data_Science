import logging
logging.basicConfig(filename="t6.log",level=logging.INFO)
uin=input("Enter x:")
logging.info("user_ip: %s",uin)
try:
    x=int(uin)
    s= lambda n: sum(map(int,str(n)))
    res=s(x)
    logging.info("sum of digits is %s",res)
except ValueError:
    logging.error("Invalid number")

