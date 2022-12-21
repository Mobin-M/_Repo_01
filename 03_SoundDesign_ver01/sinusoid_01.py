# Complete explanation is in this article: https://python.plainenglish.io/making-a-synth-with-python-oscillators-2cb8e68e9c3b

# In case of a synth application, we don’t want to generate all the samples at once (we want generating samples as key being pressed for example) 
# When next is called to the generator next sample is generated and put into the array of samples

# This method takes longer than the normal np.sin() method generating samples for lets say 2 second, but it seems necessary for creating a synthesizer app rather than a sound design tool

# Later we see in action how this will help to run a synthesizer

#

import itertools, math, time
from abc import ABC, abstractclassmethod


SAMPLE_RATE= 44100

def get_sin_oscillator(freq, amp=1, phase=0, sample_rate=SAMPLE_RATE):
    phase = (phase / 360) * 2 * math.pi
    increment = (2 * math.pi * freq)/ sample_rate
    return (math.sin(phase + v) * amp for v in itertools.count(start=0, step=increment))
    # returns a generator


t_sec = 2   # or instead of this, as long as the key is pressed
t0 = time.time()
num_sample = SAMPLE_RATE * t_sec
osc = get_sin_oscillator(freq=440)
samples = [next(osc) for i in range(num_sample)]
t1= time.time()
print(t1-t0)




osc = get_sin_oscillator(freq=1)
print(type(osc))
sample0 = next(osc)
sample1 = next(osc)
print(sample0)
print(sample1)
print(type(sample1)) 