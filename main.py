from tkinter import *
window = Tk()

lbl=Label(window, text="Welcome to our Bean Game", fg="purple", font=("Helvetica", 16))
lbl.place(x=200, y=100)
btn=Button(window, text="Start", fg="black")
btn.place(x=270, y=300)

window.title("Bean Game")
window.geometry("600x400+10+20")
window.mainloop()