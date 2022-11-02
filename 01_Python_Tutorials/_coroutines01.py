# Cooperative Multitasking:
# How to use coroutines for a simple concurrency scheme
# Simulating I/O with time.sleep().
import time
from collections import deque
import heapq

def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []
    while True:
        if not ready and not sleeping:
            break
            
        # wait for nearest sleeper,
        # if no coro can be executed immediately right now
        if not ready:
            deadline, coro = heapq.heappop(sleeping)
            if deadline > time.time():
                time.sleep(deadline - time.time())
            ready.append(coro)
            
        try:                
            coro = ready.popleft()
            result = coro.send(None)
            # the case of a coro that wants to be put to sleep
            if len(result) == 2 and result[0] == "sleep":
                deadline = time.time() + result[1]
                time.sleep(0.001)       # Needed at least in windows PC (ZF PC), no problem observed in ubuntu
                heapq.heappush(sleeping, (deadline, coro))
            else:
                print(f"Got: {result}")
                ready.append(coro)      #in this case adding it just result in passing to exception
        except StopIteration:
            pass
        print(f"Time elapsed: {time.time()-start:.3}s")


def get_page():
    print("Starting to download page")
    yield ("sleep", 1.2)
    print("Done downloading page")
    yield "<html>Hello</html>"

def read_db():
    print("Starting to retrieve data from db")
    yield ("sleep", 0.5)
    print("Connected to db")
    yield ("sleep", 1)
    print("Done retrieving data from db")
    yield "db-data"



#scheduler([get_page(), read_db()])
scheduler([get_page() if i%2 == 0 else read_db() for i in range(1000)])
