import logging
def isEO(x):
    return "Even" if x%2==0 else "ODD"
logging.basicConfig(filename="t5.log",level=logging.INFO)
logging.info("Even or odd: %s",isEO(98))