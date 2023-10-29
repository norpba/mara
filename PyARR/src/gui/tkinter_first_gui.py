from tkinter import *
from tkinter import ttk
from tkinter import messagebox

## main window

# creating the main window
root = Tk()
root.title("PyARR v0.1.0")
root.geometry("600x600")

# create frames
top_frame = Frame(root, width=580, height=190, bg="red")
top_frame.grid(row=0, column=0, padx=10, pady=5)

middle_frame = Frame(root, width=580, height=190, bg="green")
middle_frame.grid(row=1, column=0, padx=10, pady=5)

example = Tk()
bottom_frame = Frame(root, width=580, height=160, bg="blue")
bottom_frame.grid(row=2, column=0, padx=10, pady=5)

# create frames and labels inside the first frames



# welcome window -popup
welcome = Tk()
welcome.title("Welcome!")
welcome.attributes('-topmost', True)
info4 = ttk.Label(welcome, text="Welcome to Python Arranger!")
b1 = ttk.Button(welcome, text="Close", command=welcome.destroy)

root.mainloop()
