from playsound import playsound
import time
while True:
    try:
        playsound('./03_SoundDesign_ver01/testWav.wav')
        time.sleep(3)
    except:
        print("Nothing to play")
        time.sleep(3)
        