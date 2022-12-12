import time
from collections import deque

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.current = None     # Currently executing generator

    def new_task(self, gen):
        self.ready.append(gen)

    def run(self):
        while self.ready:
            self.current = self.ready.popleft()
            try:
                next(self.current)
                print(self.current)
                if self.current:
                    self.ready.append(self.current)
            except StopIteration:
                    print("Iteration stops here")
    
sched = Scheduler()


def countDown(n):       #Returning generators
    while n > 0:
        print('Down,',n)
        time.sleep(1)
        yield
        n -= 1

def countUp(stop):      #Returning generator
    x = 0
    while x < stop:
        print("Up,",x)
        time.sleep(1)
        yield
        x += 1


sched.new_task(countDown(2))
sched.new_task(countUp(2))
sched.run()
