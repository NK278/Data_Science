import logging
logging.basicConfig(filename="t9.log",level=logging.INFO)
uin=int(input("Enter x:"))
isleap= lambda yr:(yr%4==0 and yr%100==0) or (yr%400==0)
ans=isleap(uin)
logging.info("leap year or not: %s",ans)