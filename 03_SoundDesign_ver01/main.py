################################################
##################SOUND DESIGN####################
################################################
## IMPORTING GENERAL STUFF

## IMPORTING CUSTOM SCHEDULER AND RELATED STUFF
from scheduler import Scheduler, Awaitable, yield_control

## DEFINING COROUTINES/TASK NEEDED (SEE IF CAN BE PUT TOGETHER IN ANOTHER FILE)

# coroutine: test
async def test(scheduler, n):
    while n > 0:
        print('Down,', n)
        await scheduler.sleep(1, "countDown")
        n -= 1

# coroutine: playing the sound





## START OF THE PROGRAM
print("######################\n### Program starts ### \n######################")
sched = Scheduler()
sched.new_task(test(sched, 5))
sched.run()



