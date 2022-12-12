# producer-consumer problem in concurrency
# How to produce and to consume what is ready at the same time without using thread?

import time
from collections import deque
import heapq


#-----------------------------------------------#
class Scheduler:
  def __init__(self):
    self.ready = deque()
    self.sleeping = []
    self.sequence= 0    #just for prioritizing of heappush in case deadline is the same 
   
  def call_next(self, func):   # Ready to call functions
    self.ready.append(func)
   
  def call_later(self, delay, func):  # functions in queue to be called prioritized by their deadline
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

#-----------------------------------------------#
class AsyncQueue:
    def __init__(self):
        self.item = deque()     #items are the numbers being produced and consumed
        self.waiting = deque()  #waitings are functions (getters) 
        self._closed = False    
    
    def close(self):
        self._closed = True
        if self.waiting and not self.item:
          for func in self.waiting:
            sched.call_next(func)

    def put(self, item):            # appends a number to the item list.
        if self._closed:
          print("XXXXXXXXXXXXXXXXXXX")    # the main never passes this part
          raise QueueClosed() 

        self.item.append(item)
        print("New item is produced - is there any one ready to consume?")
        time.sleep(1)   # just for better understanding. must be removed later
        if self.waiting:
            print("Yes! There is one waiting, I call him...")
            func = self.waiting.popleft()
            sched.call_next(func)
        else:       # This part should be removed. just for understanding better is added
            print("No response.......")
            time.sleep(1)
            print("No response.......")
            time.sleep(1)
            print("No response.......")
            time.sleep(1)
            print("No response.......")

    def get(self, callback):
        print("Hey! I am a consumer, is there something to consume?")
        if self.item:
            print("Yes, I am here to be consumed")
            callback(Result(value = self.item.popleft()))
        else:
            # No items available (must wait)
            if self._closed:
              print("No, Production is finished!")
              callback(Result(exc=QueueClosed()))
            else:
              print("No item to consume, you should wait ")
              self.waiting.append(lambda: self.get(callback))

#-----------------------------------------------#
class Result:
    def __init__(self, value=None, exc=None):
      self.value = value
      self.exc = exc
    
    def result(self):
      if self.exc:
        raise self.exc
      else:
        return self.value

#-----------------------------------------------#
class QueueClosed(Exception):
  pass

#-----------------------------------------------#
def producer(q, count):
    def _produce(n):
        if n < count:
            print("producing ", n)
            q.put(n)
            sched.call_later(1, lambda: _produce(n+1))
        else: 
            print("Producer Done!")
            q.close()
    _produce(0)

#-----------------------------------------------#
def consumer(q):
    def _consume(result):
        try:
          item = result.result()
          print("Consuming ", item)
          sched.call_later(0,lambda: consumer(q))  #Or call_next()
        except QueueClosed:
          # How to check and error here 
          print("Consumer Done!")
    q.get(callback=_consume)





#----------------main---------------------------#
sched = Scheduler()
q = AsyncQueue()
sched.call_next(lambda: producer(q,5))
sched.call_next(lambda: consumer(q))
sched.run()