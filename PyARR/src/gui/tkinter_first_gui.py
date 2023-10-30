
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

## main window

# creating the main window and doing some configuration
root = Tk()
# load icon from disk
icon = tk.PhotoImage(file="C:\\Users\\norppa\\myCode\\mara\\PyARR\\src\\icon.png")
# set image above as the window icon
    # note that it will only change the windows taskbar after
    # compiling the code and running the program from the executable
root.iconphoto(True, icon)
root.title("PyARR v0.1.0")
root.geometry("600x600")
root.configure(bg="snow")
root.eval("tk::PlaceWindow . center")

# create frames
top_frame = Frame(root, width=580, height=170, bg="PaleVioletRed1")
top_frame.grid(row=0, column=0, padx=10, pady=5)

middle_frame = Frame(root, width=580, height=190, bg="PaleVioletRed1")
middle_frame.grid(row=1, column=0, padx=10, pady=5)

bottom_frame = Frame(root, width=580, height=190, bg="PaleVioletRed1")
bottom_frame.grid(row=2, column=0, padx=10, pady=5)

info_frame = Frame(root, width=580, height=15, bg="purple4")
info_frame.grid(row=3, column=0, padx=10, pady=0)
# create frames and labels inside the first frames
root.mainloop()


# welcome window -popup
welcome = Tk()
welcome.title("Welcome!")
welcome.attributes('-topmost', True)
info4 = ttk.Label(welcome, text="Welcome to Python Arranger!")
b1 = ttk.Button(welcome, text="Close", command=welcome.destroy)


