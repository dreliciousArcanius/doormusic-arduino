from pygame import mixer
import serial
import time
import multiprocessing
a = True;
arduino = serial.Serial('COM3', 9600)
mixer.init()
def Measure():
    distance = arduino.readline()
    return float(distance)

while True:
    output = Measure()
    if output < 29.00:
        if a:
            mixer.music.load('never.mp3')
            mixer.music.play()
            a = False
    else:
        a = True
        mixer.music.stop()
