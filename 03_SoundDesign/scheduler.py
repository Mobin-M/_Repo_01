import time
from collections import deque
import heapq

# Scheduler class to schedule and run tasks
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
        await yield_control(name)       # executing await method of class Awaitable

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


# Awaitable class to yielding resource control of the current task running
class Awaitable:
    def __init__(self, name):
        self.name = name
    def __await__(self):
        print(self.name, "yields control")
        yield

# Function call  to yield control
def yield_control(name: str):
    return Awaitable(name)
