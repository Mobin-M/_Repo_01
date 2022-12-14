import matplotlib.pyplot as plt
import numpy as np
from Sinusoids import Discrete_Real_Sinusoid_1
from scipy.io.wavfile import write
from playsound import playsound


f0 = 440
A   = [0.6, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0]
phi = [0, 0 , 0, 0, 0, 0, 0]
f0  = [f0, f0*2, f0*3, f0*4, f0*5, f0*6, f0*7]
fs  = 44100

[N, m, x_n] = Discrete_Real_Sinusoid_1(A, phi, f0, fs, 1)

#Plot one period: lowest in f0[] ---> T0 = 1/min(f0) ---(T0/Ts = N0)---> N0 = fs/min(f0)

N0 = (int) (fs/f0[0])

plt.plot(np.arange(N0), x_n[0:N0])
plt.show()


# play the sinusoid constructed
#write('./DSP/testWav.wav', fs, x_n)
#playsound('./DSP/testWav.wav')



