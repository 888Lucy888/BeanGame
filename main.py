import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL, VERTICAL
from tkinter.ttk import Combobox


class menu(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, EndPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Welcome to our Bean Game")
        label["font"] = "TkHeadingFont"
        label.pack(pady=40,padx=10)
        label1 = ttk.Label(self, text="Rules:")
        label1["font"] = "TkHeadingFont"
        label1.pack(pady=5,padx=10)
        label2 = tk.Label(self, text="Each player will have a turn, in that turn")
        label2.pack(pady=5,padx=10)
        label3 = tk.Label(self, text="they can choose to pick 1 to 3 beans.")
        label3.pack(pady=5,padx=10)
        label4 = tk.Label(self, text="Whoever picks up the last bean loses.")
        label4.pack(pady=5,padx=10)
        button = ttk.Button(self, text="Start", command=lambda: controller.show_frame(PageOne))
        button.pack(pady=40,padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        settingFrame = ttk.Frame(self)

        label = ttk.Label(settingFrame, text="Settings")
        label["font"] = "TkHeadingFont"
        label0 = ttk.Label(settingFrame, text="Number of Starting Beans")

        label.grid(row=0, column=1)
        label0.grid(row=1, column=1)

        sliderBeans = ttk.Scale(settingFrame, from_=21, to=25, orient=HORIZONTAL)

        sliderBeans.grid(row=2, column=1)

        label1 = ttk.Label(settingFrame, text="Player 1 CPU Difficulty")
        label2 = ttk.Label(settingFrame, text="Player 2 CPU Difficulty")
        sliderPlayer1 = ttk.Scale(settingFrame, from_=1, to=10, orient=VERTICAL)
        sliderPlayer2 = ttk.Scale(settingFrame, from_=1, to=10, orient=VERTICAL)

        label1.grid(row=0, column=0)
        label2.grid(row=0, column=2)

        sliderPlayer1.grid(row=1, column=0)
        sliderPlayer2.grid(row=1, column=2)


        button1 = ttk.Button(settingFrame, text="Continue",
                            command=lambda: controller.show_frame(PageTwo))

        button1.grid(row=3, column=1)

        settingFrame.pack(padx=10, pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="# Beans Remaining")
        label["font"] = "TkHeadingFont"
        label.pack(pady=20,padx=10)
        label1 = ttk.Label(self, text="Player1's Turn")
        label1["font"] = "TkHeadingFont"
        label1.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="How many beans will you take?")
        label2.pack(pady=10,padx=10)

        buttonFrame = ttk.Frame(self)

        button1Bean = ttk.Button(buttonFrame, text="1")
        button2Bean = ttk.Button(buttonFrame, text="2")
        button3Bean = ttk.Button(buttonFrame, text="3")

        button1Bean.state(['disabled'])
        button2Bean.state(['disabled'])
        button3Bean.state(['disabled'])

        button1Bean.grid(row=0, column=0)
        button2Bean.grid(row=0, column=1)
        button3Bean.grid(row=0, column=2)

        buttonFrame.pack(pady=10, padx=10)

        #data=(1,2,3)
        #cb = Combobox(self, values=data)
        #cb.pack(pady=10,padx=10)
        button2 = ttk.Button(self, text="Continue",  #IF NO BEANS SHOW EndPage
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20,padx=10)
        

class EndPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Congratulations")
        label["font"] = "TkHeadingFont"
        label.pack(pady=30,padx=10)
        label1 = ttk.Label(self, text="Player ")
        label["font"] = "TkHeadingFont"
        label1.pack(pady=20,padx=10)
        label2 = ttk.Label(self, text="YOU WIN")
        label2["font"] = "TkHeadingFont"
        label2.pack(pady=20,padx=10)
        button = tk.Button(self, text="Play Again", command=lambda: controller.show_frame(StartPage))
        button.pack(pady=40,padx=10)


app = menu()
app.mainloop()
