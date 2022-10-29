# Cooperative Multitasking:
# How to use coroutines for a simple concurrency scheme
from collections import deque

def scheduler(coros):
    ready = deque(coros)
    while ready:
        try:
            coro_to_run = ready.popleft()
            coro_to_run.send(None)
            ready.append(coro_to_run)
        except StopIteration:
            pass
def coro1():
    print("coro1 doing some work")
    yield       #yield simply gives back control to its caller
    print("coro1 doing some work")
    yield

def coro2():
    print("coro2 doing some work")
    yield
    print("coro2 doing some work")
    yield



scheduler([coro1(), coro2()])