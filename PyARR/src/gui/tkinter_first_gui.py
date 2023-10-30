
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class WelcomeWindow(Toplevel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.title("Welcome!")
        info4 = ttk.Label(self, text="Welcome to Python Arranger!")
        b1 = ttk.Button(self, text="Close", command=self.destroy)

        # call the function center_window
        self.center_window()

        # making a function to ensure that the window opens in the middle of the screen
    def center_window(self):
        w = 100 # width of the welcome window
        h = 100 # height of the welcome window

            # get the screen width and height
        screen_x = self.winfo_screenwidth()
        screen_y= self.winfo_screenheight()

            # calculate the x and y positions for centering the window
        x = (screen_x - w) // 2
        y = (screen_y - h) // 2

        self.geometry(f'{w}x{h}+{x}+{y}')
        self.geometry("100x100")

class MainWindow(Tk):
    ## main window
    # creating the main window and doing some configuration
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            # load icon from disk
        self.iconbitmap("C:\\Users\\norppa\\myCode\\mara\\PyARR\\src\\titlebar_icon.ico")
            # note that it will only change the windows taskbar after
            # compiling the code and running the program from the executable
        self.title("PyARR v0.1.0")
        self.configure(bg="snow")
        self.center_window()


            # create frames
        top_frame = Frame(self, width=580, height=170, bg="PaleVioletRed1")
        top_frame.grid(row=0, column=0, padx=10, pady=5)

        middle_frame = Frame(self, width=580, height=190, bg="PaleVioletRed1")
        middle_frame.grid(row=1, column=0, padx=10, pady=5)

        bottom_frame = Frame(self, width=580, height=190, bg="PaleVioletRed1")
        bottom_frame.grid(row=2, column=0, padx=10, pady=5)

        info_frame = Frame(self, width=580, height=15, bg="purple4")
        info_frame.grid(row=3, column=0, padx=10, pady=0)

            # create frames and labels inside the first frames

    def center_window(self):
        w = 600 # width of the welcome window
        h = 600 # height of the welcome window

            # get the screen width and height
        screen_x = self.winfo_screenwidth()
        screen_y= self.winfo_screenheight()

            # calculate the x and y positions for centering the window
        x = (screen_x - w) // 2
        y = (screen_y - h) // 2

        self.geometry(f'{w}x{h}+{x}+{y}')

if __name__ == ("__main__"):
    main_window = MainWindow()
    welcome_window = WelcomeWindow(main_window)
    main_window.mainloop()