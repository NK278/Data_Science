import logging
logging.basicConfig(filename="t7.log",level=logging.INFO)
uin=int(input("Enter x:"))
logging.info("User input: %s",uin)
rev= lambda n:list(map(int,str(n)))[::-1]
ANS=rev(uin)
logging.info("Reverse : %s",ANS)
