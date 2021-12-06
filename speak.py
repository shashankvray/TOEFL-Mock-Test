from time import sleep
from playsound import playsound
from scipy.io.wavfile import write
import wavio, threading, pyttsx3, os, sounddevice as sd

class Speaking:
    '''
    --help = This class provides the technical working of TOEFL Speaking section. 
    '''
    
    def __init__(self):
        pass
    
    def qnNumber(self, number):
        global PREP_TIME
        global SPEAKER_DURATION
        engine = pyttsx3.init()
        engine.setProperty("rate", 95)
        sleep(.8)
        if number == 1:
            PREP_TIME = 15
            SPEAKER_DURATION = 45
            text = input(f"Paste the listening question #{number} now or Press ENTER to skip:\n") or ""
        else:
            PREP_TIME = 30
            SPEAKER_DURATION = 60
        
        engine.say(text)
        engine.runAndWait()
    
    def record(self):
        freq = 48000
        recording = sd.rec((int(SPEAKER_DURATION) * freq), samplerate = freq, channels = 2)
        sd.wait()
        write("SpeakingRec.wav", freq, recording)
    
    def countdown(self):
        for i in range(int(SPEAKER_DURATION),0,-1):
            sleep(0.99)
            print(i, end = ' ', flush = True)
        playsound(os.getcwd() + "\\files\\beep.mp3")


if __name__ == '__main__':
    S = Speaking()
    S.qnNumber(1)
    #for i in range(1,5):
    print("\nPrepare your speech now")
    playsound(os.getcwd() + r"\files\prepare_speech.mp3")
    sleep(0.7)
    playsound(os.getcwd() + r"\files\beep.mp3")
    # sleep(15)
    for i in range(int(PREP_TIME),0,-1):
        sleep(0.99)
        print(i, end = ' ', flush = True)
    print()
    playsound(os.getcwd() + r"\\files\\speak_now.mp3", True)
    print("\nStart speaking your answer now")
    sleep(0.4)
    playsound(os.getcwd() + r"\\files\\beep.mp3")

    t1 = threading.Thread(target = S.record)
    t2 = threading.Thread(target = S.countdown)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    ch = input("\n\nDo you want to hear your answer recording?(y/n) - ")
    if ch.lower() == 'y':
        print("Playing your answer ")
        PlaySound(os.getcwd() + r"\\SpeakingRec.wav", SND_NODEFAULT)
        print()