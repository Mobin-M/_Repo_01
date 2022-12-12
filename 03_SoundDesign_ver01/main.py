################################################
##################SOUND DESIGN####################
################################################
## IMPORTING GENERAL STUFF
from sinusoid import Discrete_Real_Sinusoid_1 as Dsin
from scipy.io.wavfile import write
from playsound import playsound
from threading import Thread
from time import sleep

## GLOBAL VARIABLE
f_comm = 0
f_play = 1
f_query = 0
int_req = 0

## FUCNTIONS
# function to continuously playing when f_play == 1
def play():
    while True:
        if (f_play == 1):
            try:
                playsound('./03_SoundDesign_ver01/testWav.wav')
                sleep(3)
            except:
                if (f_comm == 1): print("Nothing to play")
                sleep(3)

# function asking for a task and modifying global var based on request
def query():
    global int_req
    int_req = 0
    print("Request a task:")
    print("(1)      build/modify sinusoid")
    print("(2)      add harmonics")
    print("(3)      add/modify ADSR")
    print("(4)      add filer")
    print("(5)      save data")
    print("(99)     Exit without save")
    int_req = int(input())
    if (int_req != 0):
        global f_play
        global f_query
        f_query = 1
        f_play = 0
        print(f"Task {int_req} requested")
        # This thread dies here, next time it should be run/started again
        sleep(1)
    sleep(1)

# function recieving task number and performing the task
def tasks():
    global int_req
    global f_play
    
    if (int_req != 0):  
        # add a switch case for every request
        print(f"starting  task {int_req}")
        sleep(5)
        print("task done")
        f_play = 1



print("###############################################")
print ("########### Sound design program ##############")
print("###############################################")

t_play = Thread(target=play, daemon=True)
t_play.start()

while (int_req != 99):
    query()
    tasks()







