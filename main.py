from tkinter import *
from tkinter import ttk

def nothing():
    print("Nothing")

root = Tk()

root.title("Practice")

mainFrame = ttk.Frame(root, padding="3 3 12 12")

mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainFrame, text="Button 1", command=nothing).grid(column=0, row=3, sticky=E)
ttk.Button(mainFrame, text="Button 2", command=nothing).grid(column=1, row=3, sticky=E)
ttk.Button(mainFrame, text="Button 3", command=nothing).grid(column=2, row=3, sticky=E)


root.mainloop()


#from tkinter import *
#window = Tk()
#
#lbl=Label(window, text="Welcome to our Bean Game", fg="purple", font=("Helvetica", 16))
#lbl.place(x=200, y=100)
#btn=Button(window, text="Start", fg="black")
#btn.place(x=270, y=300)
#
#window.title("Bean Game")
#window.geometry("600x400+10+20")
#window.mainloop()
