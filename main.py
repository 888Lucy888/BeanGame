import tkinter as tk
from tkinter.ttk import Combobox


LARGE_FONT= ("Verdana", 12)


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
        label = tk.Label(self, text="Welcome to our Bean Game", font=LARGE_FONT)
        label.pack(pady=40,padx=10)
        label1 = tk.Label(self, text="Rules:", font=LARGE_FONT)
        label1.pack(pady=5,padx=10)
        label2 = tk.Label(self, text="Each player will have a turn, in that turn")
        label2.pack(pady=5,padx=10)
        label3 = tk.Label(self, text="they can choose to pick 1 to 3 beans.")
        label3.pack(pady=5,padx=10)
        label4 = tk.Label(self, text="Whoever picks up the last bean loses.")
        label4.pack(pady=5,padx=10)
        button = tk.Button(self, text="Start", font=LARGE_FONT,
                            command=lambda: controller.show_frame(PageOne))
        button.pack(pady=40,padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label0 = tk.Label(self, text="Number of Starting Beans")
        label0.pack(pady=10,padx=10)
        data0=(21,22,23,24,25)
        cb = Combobox(self, values=data0)
        cb.pack(pady=10,padx=10)
        label1 = tk.Label(self, text="Player 1 CPU Difficulty")
        label1.pack(pady=10,padx=10)
        data=(1,2,3,4,5,6,7,8,9,10)
        cb1 = Combobox(self, values=data)
        cb1.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="Player 2 CPU Difficulty")
        label2.pack(pady=10,padx=10)
        cb2 = Combobox(self, values=data)
        cb2.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Continue",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack(pady=10,padx=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="# Beans Remaining", font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        label1 = tk.Label(self, text="Player1's Turn", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="How many beans will you take?")
        label2.pack(pady=10,padx=10)
        data=(1,2,3)
        cb = Combobox(self, values=data)
        cb.pack(pady=10,padx=10)
        button2 = tk.Button(self, text="Continue",  #IF NO BEANS SHOW EndPage
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20,padx=10)
        

class EndPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Congratulations", font=LARGE_FONT)
        label.pack(pady=30,padx=10)
        label1 = tk.Label(self, text="Player ", font=LARGE_FONT)
        label1.pack(pady=20,padx=10)
        label2 = tk.Label(self, text="YOU WIN", font=LARGE_FONT)
        label2.pack(pady=20,padx=10)
        button = tk.Button(self, text="Play Again", font=LARGE_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button.pack(pady=40,padx=10)


app = menu()
app.mainloop()
