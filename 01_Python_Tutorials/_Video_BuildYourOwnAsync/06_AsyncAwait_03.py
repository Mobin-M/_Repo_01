# Producer-Consumer solution without callbacks using coroutines (with async await)
import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()    # waiting list of ready coroutines to be executed
        self.current = None     # current coroutines being executed
        self.sleeping = []      # sleeping coroutines
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
                pass 

class Awaitable:
    def __init__(self, name):
        self.name = name
    def __await__(self):
        print(self.name, "yields control")
        yield

class AsyncQueue:
    def __init__(self):
        self.items = deque()        # waiting items to be consumed
        self.waiting = deque()      # waiting consumers
        self._closed = False
    
    def close(self):
        self._closed = True
        if self.waiting and not self.items:
            sched.ready.append(self.waiting.popleft())      #re-scheduling

    def put(self, item):
        if self._closed:
            raise QueueClosed()
        self.items.append(item)
        if self.waiting:
            sched.ready.append(self.waiting.popleft())

    async def get(self):
        while not self.items:
            if self._closed:
                raise QueueClosed()
            self.waiting.append(sched.current)
            sched.current = None
            await yield_control("consumer")
        return self.items.popleft()

class QueueClosed(Exception):
    pass

def yield_control(name: str):
    return Awaitable(name)



# ------------tasks---------------

async def producer(q, count):
    for n in range(count):
        print('Producing,', n)
        q.put(n)
        await sched.sleep(1, "Producer")
    print('Produce done!')
    q.close()

async def consumer(q):
    try:
        while True:
            item = await q.get()
            print("Consuming,",item)
    except QueueClosed:
        print('Consumer done!')



# ---------------main-------------
sched = Scheduler()
q = AsyncQueue()

sched.new_task(producer(q, 5))
sched.new_task(consumer(q))
sched.run()