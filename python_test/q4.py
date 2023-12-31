import logging
def swap(a,b,c):
    logging.info(f"Before swapping: a = {a}, b = {b}, c = {c}")
    a=a^b^c
    b=a^b^c
    c=a^b^c
    a=a^b^c
    logging.info(f"After swapping: a = {a}, b = {b}, c = {c}")
logging.basicConfig(filename="t3.log",level=logging.INFO)
a=5
b=8
c=9
swap(a, b, c)

