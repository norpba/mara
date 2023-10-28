# PaRR - Python Arranger

import PySimpleGUI as sg

# Welcome-window

welcomewindow_layout = [[sg.Text("Welcome to Python Arranger v0.1.0 !")], [sg.Button("Ok", expand_y=True)]]
sg.Window(title="Python Arranger v0.1.0", layout = welcomewindow_layout, margins=(0, 15)).read()