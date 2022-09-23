from inspect import currentframe, getframeinfo
import pathlib
from time import sleep
import os
#pip install playsound==1.2.2
from playsound import playsound

Me = getframeinfo(currentframe()).filename
FileFolder = pathlib.Path(Me).resolve().parent
OutroMusic = pathlib.Path(FileFolder).joinpath("Outro-Music.mp3")

MsgWarning = "The PC Will Shutdown In "

def Countdown():
    SecondsLeft = 15
    while SecondsLeft > 0:
        print(MsgWarning + str(SecondsLeft))
        SecondsLeft -= 1
        sleep(1)

playsound(str(OutroMusic), False)

Countdown()

print("The PC Will Shutdown In 0")

os.system('shutdown /f -s -t 1 -c " "')

sleep(5)