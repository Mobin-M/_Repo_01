# Case of sound design application, meaning that sinusoid is already generated for a defined duration t_sec.
# input to adsr is x_n.

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from playsound import playsound




adsr_list = {
    1:  "adsr_linear",
    2:  "adsr_exponential",
    3:  "adsr_P",
    4:  "adsr_PI",
    5:  "adsr_PID",
    6:  "adsr_remove"
}


fs = 44100
def adsr_linear():
    x_n = np.load('./03_SoundDesign_ver01/x_n.npy')
    adsr = np.zeros(len(x_n))
    attack = np.linspace(0, 1, 11100)
    adsr[0:11100] = attack
    adsr[11100:88199] = 1
    x_n_mod = adsr*x_n
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





