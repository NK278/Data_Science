import logging
def nature(x):
    return "Positive" if x>0 else "Negative" if x<0 else "Zero"
logging.basicConfig(filename="t4.log",level=logging.INFO)
logging.info("nature of number %s",nature(87))