# Nested coroutines
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
                print('Waiting any courotine....')
                time.sleep(deadline - time.time())
            ready.append(coro)
            
        try:                
            coro = ready.popleft()
            result = coro.send(None)
            # the case of a coro that wants to be put to sleep
            if len(result) == 2 and result[0] == "sleep":
                deadline = time.time() + result[1]
                time.sleep(0.001)       #This is needed atleast in Windows PC of ZF but no issue without it in ubuntu
                heapq.heappush(sleeping, (deadline, coro))
            else:
                print(f"Got: {result}")
                ready.append(coro)      #in this case adding it just result in passing to exception
        except StopIteration:
            pass
 #       print(f"Time elapsed: {time.time()-start:.3}s")



def get_page():
    print("Starting to download page")
    yield ("sleep", 1)
    print("Done downloading page")
    return "<html> !! DATA IS HERE BITCHES !!</html>"

def write_db(data):
    print("Starting to write data to db")
    yield ("sleep", 0.5)
    print("Connected to db")
    yield ("sleep", 1)
    print("Done writing data to db")

def worker():
    page = yield from get_page()
    print(page)
    yield from write_db(page)

scheduler([worker(), worker(), worker()])