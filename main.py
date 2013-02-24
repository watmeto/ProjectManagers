from tkinter import *
from theMenu import *

if __name__ == '__main__':
    
    root= Tk()
    root.title("Project Manager")
    Menus(root)
    frame = Frame(width=768, height=576, bg="", colormap="new")
    frame.pack()
    mainloop()    
#end
