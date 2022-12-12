# Using Async Await syntax; Hiding yield
# how to sleep in a better way; not locking with time.sleep()
import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.current = None
        self.sleeping = []
        self.sequence = 0

    def new_task(self, coro):
        self.ready.append(coro)

    async def sleep(self, delay, name: str):  #how to put a task in the sleeping list of the scheduler 
        deadline = time.time() + delay 
        self.sequence += 1
        heapq.heappush(self.sleeping, (deadline, self.sequence, self.current))      #heappush also sorts by deadline,...
        self.current = None
        await yield_control(name)


    
    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:  #nothing is ready to run. see if anything in sleeping tasks
                deadline, _, coro = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(coro)
            
            self.current = self.ready.popleft()
            try:
                self.current.send(None)
                if self.current:  
                    self.ready.append(self.current)
            except StopIteration:
                print("Counting Done!") 

class Awaitable:
    def __init__(self, name):
        self.name = name
    def __await__(self):
        print(self.name, "yields control")
        yield

def yield_control(name: str):
    return Awaitable(name)



# Coroutines
async def countDown(n):
    while n > 0:
        print('Down,', n)
        await sched.sleep(1, "countDown")
        n -= 1
async def countUp(stop):
    n = 0
    while n < stop:
        print('Up,', n)
        await sched.sleep(0.4, "countUp")
        n += 1


# main
sched = Scheduler()
sched.new_task(countDown(5))
sched.new_task(countUp(5))
sched.run()