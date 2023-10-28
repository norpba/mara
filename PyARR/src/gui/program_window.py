# PyARR - Python Arranger

import PySimpleGUI as sg

# Welcome-window
def welcome_window():

    layout = [[sg.Text('Welcome to Python Arranger!', justification='center',size=(100,1))]
              ]
    
    button = [
        [[sg.Button('Ok',size=(100,1))]]
        ]

    window = sg.Window("PyARR v0.1.0", layout, button, size=(400, 100))

    while True:
        event, values = window.read()
        print(event, values)
        if event == None or event == button:
            break
        if event == 'Button':
            break
        window.close()
if __name__ == "__main__":
    welcome_window()
        #main()