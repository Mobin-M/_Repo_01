# Async Basics
import time
from collections import deque
import heapq

class Scheduler:
  def __init__(self):
    self.ready = deque()
    self.sleeping = []
    self.sequence= 0    #just for prioritizing of heappush in case deadline is the same 
   
  def call_next(self, func):
    self.ready.append(func)
   
  def call_later(self, delay, func):
    self.sequence += 1
    deadline = time.time() + delay
    #priority queue
    heapq.heappush(self.sleeping, (deadline, self.sequence, func))
   
  def run(self):
    while self.ready or self.sleeping:
      if not self.ready:
        #fine nearest deadling
        deadline, _,func = heapq.heappop(self.sleeping)
        delta = deadline - time.time()
        if delta > 0:
          time.sleep(delta)
        self.ready.append(func)
     
      while self.ready:
        func = self.ready.popleft()
        func()

def countDown(n):
  if n > 0:
    print ("Down", n)
    sched.call_later(2, lambda: countDown(n-1))         #run next countDown in 4 sec  
   
def countUp(stop, x=0):
  if x < stop:
    print("Up", x)
    sched.call_later(0.5, lambda: countUp(stop, x+1))   #run next countUp in 1 sec
   

sched = Scheduler()
sched.call_next(lambda: countDown(5))
sched.call_next(lambda: countUp(20))
sched.run()