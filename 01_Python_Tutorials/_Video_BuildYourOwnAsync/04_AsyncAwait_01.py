import time

class Awaitable:
    def __await__(self):
        yield

def switch():
    return Awaitable()




async def countUp(stop):      #Returning generator
    x = 0
    while x < stop:
        print("Up,",x)
        time.sleep(1)
        await switch()
        x += 1

a = countUp(5)
a.send(None)
a.send(None)
a.send(None) 