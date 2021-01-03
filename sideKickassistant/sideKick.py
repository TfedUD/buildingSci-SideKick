import tkinter as tk
from tkinter import * # https://memegenerator.net/img/instances/67862979/wildcard.jpg
import commands
import os 

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Big brain side kick')
        # Width*Height
