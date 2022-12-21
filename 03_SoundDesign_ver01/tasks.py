from time import sleep
from sinusoid import Discrete_Real_Sinusoid_1 as Dsin
from scipy.io.wavfile import write
from adsr import query_adsr

def nothing():
    print("Nothing!")
    sleep(2)

def to_exit():
    print("closing the application...")

def build_sinusoid():
    print("Building a new sinusoid...")
    
    f0 = float(input("insert frequency (default 440): ") or "440")
    A = float(input("insert amplitude (default 0.8): ") or "0.8")
    phi= float(input("insert phase (default 0): ") or "0")
    fs = int(input("insert sampling frequency (default 44100): ") or "44100")
    t_len = int(input("time length of the sound (default 2): ") or "2")
    
    [N, m, x_n] = Dsin(A, phi, f0, fs, t_len)
    
    write('./03_SoundDesign_ver01/testWav.wav', fs, x_n)

def add_adsr():
    query_adsr()
