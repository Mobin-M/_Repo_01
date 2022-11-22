################################################
##################SOUND DESIGN####################
################################################
## IMPORTING GENERAL STUFF
from sinusoid import Discrete_Real_Sinusoid_1 as Dsin
from scipy.io.wavfile import write
from playsound import playsound

## GLOBAL VARIABLE
f_comment = 0
f_query = 0

## IMPORTING CUSTOM SCHEDULER AND RELATED STUFF
from scheduler import Scheduler, Awaitable, yield_control


## DEFINING FUNCTIONS/COROUTINES/TASK NEEDED (SEE IF CAN BE PUT TOGETHER IN ANOTHER FILE)
# coroutine: test
async def test(scheduler, n):
    while n > 0:
        print('Down,', n)
        await scheduler.sleep(1, "countDown")
        n -= 1
    
# coroutine: change query
async def changeRequest(scheduler):
    response_query = str(input("any query? (S or M)" or 'n'))
    if response_query is 'S':
        print('request to make new sinusoid')
        scheduler.ready.append(make_sinusoid())
    elif response_query is 'M':
        print("request to modify the sinusoid")
    else:
        print("no query")

# function: read parameters of the sinusoid
def get_sin_param():
    if f_comment: print("inside get_sin_param")
    freq = float(input("Please enter the frequency: ") or '0')
    amp = float(input("Please enter the amplitude: ") or '0.8')
    phi = float(input("Please enter the phase: ") or '0')
    return freq, amp, phi

# coroutine: make the sinusoid
async def make_sinusoid():
    f0, A, phi = get_sin_param()
    fs = 10000
    t_sec = 1
    N, m, x_n = Dsin([A], [phi], [f0], fs, t_sec)
    write('./03_SoundDesign_ver01/testWav.wav', fs, x_n)


# coroutine: modification     
    


# coroutine: playing the sound
async def play_sound(scheduler):
    while True:
        try:
            playsound('./03_SoundDesign_ver01/testWav.wav')
            scheduler.ready.append(changeRequest(sched))
            await scheduler.sleep(3, "Play routine")
        except:
            print("Nothing to play")
            scheduler.ready.append(changeRequest(sched))
            await scheduler.sleep(3, "Play routine") 






## START OF THE PROGRAM
print("######################\n### Program starts ### \n######################")
sched = Scheduler()
sched.new_task(play_sound(sched))
sched.new_task(changeRequest(sched))
sched.run()



