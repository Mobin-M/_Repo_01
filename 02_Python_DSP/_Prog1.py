from Sinusoids import Discrete_Real_Sinusoid_1
from scipy.io.wavfile import write
from playsound import playsound


def get_freq():
    pass
def get_amp():
    pass

#[N, m, x_n] = Discrete_Real_Sinusoid_1(A, 0, f0, 44100, 0)

# Method 1
try:
    while(True):
       print("Program running")
except KeyboardInterrupt:
    print ("\nProgram closed")


"""
## Method 2 :not that keyboard module must be installed in root (sudo pip insta...) and python program as well run with sudo this way!
import keyboard
while True:
    print("Program running")
    if keyboard.is_pressed('q'):
        print("program closed")
        break
"""


