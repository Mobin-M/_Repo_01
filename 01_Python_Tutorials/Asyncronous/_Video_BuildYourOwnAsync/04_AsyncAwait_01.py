# Using Async Await syntax; Hiding yield
import time
from collections import deque

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.current = None

    def new_task(self, coro):
        self.ready.append(coro)
    
    def run(self):
        while self.ready:
            self.current = self.ready.popleft()
            try:
                self.current.send(None)
                #if self.current:  #try runnin without this line since it will go to exception is self.current != 1
                self.ready.append(self.current)
            except StopIteration:
                pass 

sched = Scheduler()

class Awaitable:
    def __await__(self):
        yield
def yield_control():
    return Awaitable()


async def countDown(n):
    while n > 0:
        print('Down,', n)
        time.sleep(1)
        await yield_control()
        n -= 1

async def countUp(stop):
    n = 0
    while n < stop:
        print('Up,', n)
        time.sleep(1)
        await yield_control()
        n += 1

sched.new_task(countDown(5))
sched.new_task(countUp(5))
sched.run()