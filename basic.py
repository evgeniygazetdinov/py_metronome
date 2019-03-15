from abc import ABC,abstractmethod
from tkdisplay import Application
import pyaudio as pa
from time import sleep
import tkinter as tk

class Metronome(Application):

    def __init__(self):

        bpm = 0


    def play(self):
        p = pa.PyAudio()
        stream = p.open(format = p.get_format_from_width(width=2),channels = 2,rate = 44100 ,output = True)
        stream.write('H#8',8)


    def play_tempo(self):
        while True:
            sleep(1)
            self.play()
            sleep(1)



    def run_program(self):
        root =tk.Tk()
        app = Application(master = root,command = self.play_tempo)
        app.mainloop()

if __name__ == "__main__":
    Metronome().run_program()
