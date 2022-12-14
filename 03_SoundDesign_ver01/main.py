################################################
##################SOUND DESIGN####################
################################################
## IMPORTING GENERAL STUFF
from playsound import playsound
from threading import Thread
from time import sleep
from tasks import *

## GLOBAL VARIABLE
f_comm = 0
f_play = 1
int_req = 0
task_list = {
    0:  "nothing",
    1:  "build_sinusoid",
    2:  "add_harmonics",
    3:  "add_adsr",
    4:  "add_filter",
    5:  "save_data",
    99: "to_exit"
}

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
    try:
        int_req = int(input())
    except:
        int_req = 0
    if (int_req != 0):
        #global f_play
        #f_play = 0
        pass

# function recieving task number and performing the task
def tasks():
    global int_req
    global f_play
    
    func_name = task_list.get(int_req, "nothing")
    print(f"starting task: {func_name}")
    eval(func_name+"()")
    print(f"{func_name} is done!")
    #f_play = 1  reset if in query( ) isset to 0

    

# MainThread
print()
print("###############################################")
print ("########### Sound design program ##############")
print("###############################################")
print()

#Run play() on a new thread
t_play = Thread(target=play, daemon=True)
t_play.start()

while (int_req != 99):
    query()
    tasks()







