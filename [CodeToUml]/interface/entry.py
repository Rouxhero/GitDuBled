import tkinter as tk


class entry(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.returnValue = "" 
        self.wm_title("Entry")
        tk.Label(self, text="Enter Text :",width=45).pack(pady=15)
        self.entree = tk.Entry(self,width=30)
        self.entree.pack()
       
        tk.Button(self,text="Done",command=self.done).pack(pady=15)      



    def done(self):
        self.returnValue = self.entree.get()
        self.destroy()
        