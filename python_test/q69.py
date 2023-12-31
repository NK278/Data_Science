import threading,random,time

class Add(threading.Thread):
    def __init__(self,var):
        super().__init__()
        self.var=var
    def run(self):
        for i in range(10):
            n=random.randint(1, 10)
            self.var+=n
            print("added",n,"to var")
            time.sleep(0.1)
class Subtract(threading.Thread):
    def __init__(self,var):
        super().__init__()
        self.var=var
    def run(self):
        for i in range(10):
            n=random.randint(1, 10)
            self.var-=n
            print("subtracted",n,"to var")
            time.sleep(0.1)
var=0
add_t=Add(var)
sub_t=Subtract(var)
add_t.start()
sub_t.start()
add_t.join()
sub_t.join()
print("final val:",var)