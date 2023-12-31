import logging
import math
def sqrt_x(x):
    return x**0.5 
logging.basicConfig(filename="t1.txt",level=logging.INFO)
logging.info("sqrt of 625: %f",sqrt_x(625))