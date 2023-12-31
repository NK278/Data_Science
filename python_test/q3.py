import logging
def prime():
    return [n for n in range(2,51) if all(n%i!=0 for i in range(2,int(n**0.5)+1))]
logging.basicConfig(filename="t2.txt",level=logging.INFO)
prime_num=prime()
logging.info("prime numbers from 2 to 50: %s",prime_num)