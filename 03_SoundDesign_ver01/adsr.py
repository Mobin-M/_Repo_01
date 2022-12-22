# Case of sound design application, meaning that sinusoid is already generated for a defined duration t_sec.
# input to adsr is x_n.

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from playsound import playsound
from time import sleep


adsr_list = {
    1:  "adsr_linear",
    2:  "adsr_exponential",
    3:  "adsr_P",
    4:  "adsr_PI",
    5:  "adsr_PID",
    6:  "adsr_remove"
}



def nothing():
    print("Nothing!")
    sleep(2)

def adsr_linear():
    fs = int(np.load('./03_SoundDesign_ver01/fs.npy'))
    x_n = np.load('./03_SoundDesign_ver01/x_n.npy')
    length = len(x_n)
    
    l_attack = int(length*(int((input("attack length[%]: (default = 20)") or 20))/100))
    h_attack = float(input("attack height[ ]: (default = 1)") or 1)
    attack = np.linspace(0, h_attack, l_attack)

    l_decay = int(length*(int(input("decay length[%]: (default = 10)") or 10))/100)
    h_decay = float(input("decay height[ ]: (default = 0.8)") or 0.8)
    decay = np.linspace(h_attack, h_decay, l_decay)

    l_sustain = int(length*(int(input("sustain length[%]: (default = 50)") or 50))/100)
    sustain = np.linspace(h_decay, h_decay, l_sustain)

    l_release = length - (l_attack + l_decay + l_sustain)
    release = np.linspace(h_decay, 0, l_release)

    adsr = np.append(attack, decay)
    adsr = np.append(adsr, sustain)
    adsr = np.append(adsr, release)

    x_n_mod = adsr * x_n

    write('./03_SoundDesign_ver01/testWav.wav', fs, x_n_mod)  

def adsr_exponential():
    print("performing exponential adsr...")



# choosing the type of the adsr and run the related function
def query_adsr():
    int_adsr = 0
    print("Request a task:")
    print("(1)      linear adsr")
    print("(2)      exponential adsr")
    print("(3)      (P)ID")
    print("(4)      (PI)D")
    print("(5)      (PID)")
    print("(99)    Cancel")
    try:
        int_adsr = int(input())
    except:
        int_adsr = 0
    if (int_adsr != 0):
        func_name = adsr_list.get(int_adsr, "nothing")
        print(f"starting task: {func_name}")
        eval(func_name+"()")
        print(f"{func_name} is done!")





