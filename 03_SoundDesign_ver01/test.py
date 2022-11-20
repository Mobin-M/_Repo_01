# Global variable
f_comment = 0       # global flag to show flow comments
# imports
from sinusoid import Discrete_Real_Sinusoid_1 as Dsin
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from playsound import playsound

# Get sinusoid parameter from the user with default values
def get_sin_param():
    if f_comment: print("inside get_sin_param")
    freq = float(input("Please enter the frequency: ") or '0')
    amp = float(input("Please enter the amplitude: ") or '0.8')
    phi = float(input("Please enter the phase: ") or '0')
    return freq, amp, phi

f0, A, phi = get_sin_param()
fs = 10000
t_sec = 1
N,m,x_n = Dsin([A], [phi], [f0], fs, t_sec)

# play the sinusoid constructed
write('./03_SoundDesign/testWav.wav', fs, x_n)
playsound('./03_SoundDesign/testWav.wav')

plt.plot(np.arange(N),x_n)
plt.show()