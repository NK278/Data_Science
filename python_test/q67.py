import threading as s
import time

def countdown():
  for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
  print("Blastoff!")

threada = s.Thread(target=countdown())
threada.start()