import tkinter as tk


class Application(tk.Frame):
    def __init__(self,master = None,command = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(command)

    def create_widgets(self,command):
        self.but_start = tk.Button(text = 'start',command = command).pack()
        self.but_quit = tk.Button(text = "quit",command = self.master.destroy).pack(side = "bottom")


