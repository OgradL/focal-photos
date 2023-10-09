
import ctypes
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import os
import sys
import random
from random import *
import math
from math import cos, sin, tan, pi as PI, sqrt, pow, ceil, floor
import time
import tkinter
import tkinter.filedialog
import copy

Builder.load_file("focal.kv")

# class layout(GridLayout):
#     pass

class home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    3
    dark_theme = {
        "back1": (30 / 255, 30 / 255, 30 / 255, 1),    # (30, 30, 30)
        "back2": (38 / 255, 38 / 255, 38 / 255, 1),    # (38, 38, 38)
        "main1": (218 / 255, 218 / 255, 218 / 255, 1), # (218, 218, 218)
        "main2": (225 / 255, 225 / 255, 225 / 255, 1), # (225, 225, 225)
    }
    
    color_palette = dark_theme
    
    def calculate_hyper_distance(self):
        fs = self.ids.f_in.text
        Fs = self.ids.F_in.text
        if not fs.isnumeric():
            fs = "0"
        if not Fs.isnumeric():
            Fs = "1"
        f = int(fs)
        F = int(Fs)
        pvc = self.ids.pvc_in.active
        if pvc:
            f *= 1.5
        hyper_distance = f*f / (F*0.033)
        self.ids.iperfocal_distance_label.text = str(round(hyper_distance) / 1000) + " m"
        pass


runTouchApp(home())

# if __name__ == '__main__':
#     home().run()