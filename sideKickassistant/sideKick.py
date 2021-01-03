import tkinter as tk
from tkinter import * # https://memegenerator.net/img/instances/67862979/wildcard.jpg # will un-wildcard down the road: just for WIP atm 
from sideKickassistant import commands
import os 

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Big brain side kick')
        # Width*Height

# there is never enough time in a day