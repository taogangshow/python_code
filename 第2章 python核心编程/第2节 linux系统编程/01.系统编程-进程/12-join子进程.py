from multiprocessing import Process
import time,random

def test():
    for i in range(random.randint(1,5)):
        print("---%d---"%i)
        time.sleep(1)

p = Process(target=test)
p.start()
p.join(1)

print("---main---")
