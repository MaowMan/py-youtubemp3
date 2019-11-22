from tkinter import *

class Main(object):
    def __init__(self):
        self.Root=Tk()
        self.Root.title("py-youtubemp3")
        self.Setup()
        self.Loop()
    def Setup(self):
        self.Topbar=Menu(self.Root)
        self.Root.config(menu=self.Topbar)
    def Loop(self):
        self.Root.mainloop()

if __name__=="__main__":
    Main()