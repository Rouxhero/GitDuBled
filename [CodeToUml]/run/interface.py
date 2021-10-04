import tkinter as tk
import tkinter.ttk as tkk
from interface.frames import *


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Uml to Code")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in FramesList:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.showMenu()
        self.show_Main()
        

    def showMenu(self):
        self.menubar = Menu(self)
        menu1 = Menu(self.menubar, tearoff=0)
        menu1.add_command(label="Generate Code", command=self.show_Main)
        menu1.add_command(label="Generate UML", command=self.show_uML)
        self.menubar.add_cascade(label="UML", menu=menu1)
        menu2 = Menu(self.menubar, tearoff=0)
        menu2.add_command(label="Generate Test", command=self.show_Main)
        self.menubar.add_cascade(label="Test", menu=menu2)
        self.config(menu=self.menubar)

    def show_Main(self):
        frame = self.frames[MainPage]
        frame.tkraise()

    def show_uML(self):
        frame = self.frames[UmlPage]
        frame.tkraise()

    


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
