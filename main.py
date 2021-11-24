import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL, VERTICAL
from tkinter.ttk import Combobox
from dataclasses import dataclass
from random import randint

@dataclass
class mmNode:
    pass

@dataclass
class mmNode:
    value: int
    parent: mmNode = None
    children: list = None
    blue: bool = False #Blue = Player 1 victory -- Red = Player 2 victory
    blues: int = 0
    reds: int = 0

class mmTree:
    
    def __init__(self, root: mmNode):
        self.root = root

        self.calculateMinMax()
        self.redPriority()
        self.bluePriority()


    def addNode(self, node: mmNode, parentNode: mmNode = None) -> None:
        if not parentNode:
            parentNode = self.root
        if not parentNode.children:
            parentNode.children = []
        parentNode.children.append(node)

    def depth(self, node):
        count = 0
        while node != self.root:
            count += 1
            node = node.parent
        return count - 1

    def calculateMinMax(self, node: mmNode = None):
        if not node:
            node = self.root

        NodeR = None
        NodeC = None
        NodeL = None

        value = int(node.value)

        if value > 2:
            NodeR = mmNode(value-3, node)
        if int(value) > 1:
            NodeC = mmNode(value-2, node)
        NodeL = mmNode(value-1, node)
        if int(NodeL.value) > 0:
            self.addNode(NodeL, node)
        if NodeC:
            self.addNode(NodeC, node)
        if NodeR:
            self.addNode(NodeR, node)
        if int(NodeL.value) > 0:
            self.calculateMinMax(NodeL)
        if NodeC and int(NodeC.value) > 0:
            self.calculateMinMax(NodeC)
        if NodeR and int(NodeR.value) > 0:
            self.calculateMinMax(NodeR)

        if value == 1:
            depth = self.depth(node)
            # Player 1 will have even depth
            # For example... first turn beans equal to node on height 0
            # This means player 2 will have the odd depths
            if depth % 2 == 0:
                # This means player 1 has to grab the last one, which means
                # victory for Player 2
                # Long live PLayer 2
                self.convertRed(node)
            else:
                self.convertBlue(node)

    # TODO we can add a priority function that counts blues and reds of each subtree
    # To give each branch a given priority

    def convertBlue(self, node: mmNode):
        while True:
            node.blue = True
            node = node.parent
            if node == self.root: break

    def convertRed(self, node: mmNode):
        while True:
            node.blue = False
            node = node.parent
            if node == self.root: break

    def redPriority(self, node:mmNode = None):
        if not node:
            node = self.root

        priority = 0

        if not node.blue: priority += 1

        if node.children: 
            for nodes in node.children:
                priority += self.redPriority(nodes)

        node.reds = priority

        return priority

    def bluePriority(self, node:mmNode = None):
        if not node:
            node = self.root

        priority = 0

        if node.blue: priority += 1

        if node.children:
            for nodes in node.children:
                priority += self.bluePriority(nodes)

        node.blues = priority

        return priority

dificultad= 0
turno= False
totalBeans = 21
cpu1 = int()
cpu2 = int()
actualNodo = None
turn = 1
arbol = None

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

    def set_settings(self, cont, beans, p1Dif, p2Dif):
        global totalBeans, cpu1, cpu2, totalBeans, arbol, actualNodo
        frame = self.frames[cont]
        frame.tkraise()
        totalBeans = beans
        cpu1 = p1Dif
        cpu2 = p2Dif
        arbol= mmTree(mmNode(totalBeans))
        actualNodo= arbol.root

    def pick_beans(self, button, number, cont):
        frame = self.frames[cont]
        frame.tkraise()
        global totalBeans, turn , turno
        if totalBeans-1<number:
            button.state(["disabled"])
        totalBeans = totalBeans - number
        turno = not turno
        if turn == 1: turn = 2
        if turn == 2: turn = 1

    
    def cpu(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        global cpu1, cpu2, totalBeans, actualNodo
        if turno:
            dificultad= cpu2
        else:
            dificultad= cpu1
        probabilidad= randint(1,10)
        if totalBeans == 1:
            camino = 1
        elif probabilidad > dificultad:
            print("Eligio mal")
        if actualNodo.children[0].blue != turno:
            print("Toma camino incorrecto")
            camino= 1
            actualNodo= actualNodo.children[0]
        elif actualNodo.children[1] and actualNodo.children[1].blue != turno:
            print("Toma camino incorrecto")
            camino= 2
            actualNodo= actualNodo.children[1]
        elif actualNodo.children[2] and actualNodo.children[2].blue != turno:
            print("Toma camino incorrecto")
            camino= 3
            actualNodo= actualNodo.children[2]
        else:
            print("Toma camino correcto")
            camino= 1
            actualNodo= actualNodo.children[0]
        


        
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

        sliderBeans = tk.Scale(settingFrame, from_=21, to=25, orient=HORIZONTAL, resolution=1)

        sliderBeans.grid(row=2, column=1)

        label1 = ttk.Label(settingFrame, text="Player 1 CPU Difficulty")
        label2 = ttk.Label(settingFrame, text="Player 2 CPU Difficulty")
        sliderPlayer1 = tk.Scale(settingFrame, from_=1, to=10, orient=VERTICAL, resolution=1)
        sliderPlayer2 = tk.Scale(settingFrame, from_=1, to=10, orient=VERTICAL, resolution=1)

        label1.grid(row=0, column=0)
        label2.grid(row=0, column=2)

        sliderPlayer1.grid(row=1, column=0)
        sliderPlayer2.grid(row=1, column=2)


        button1 = ttk.Button(settingFrame, text="Continue",
                            command=lambda: controller.set_settings(PageTwo, sliderBeans.get(), sliderPlayer1.get(), sliderPlayer2.get()))
        button1.grid(row=3, column=1)

        settingFrame.pack(padx=10, pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=str(totalBeans)+" Beans Remaining")
        label["font"] = "TkHeadingFont"
        label.pack(pady=20,padx=10)
        label1 = ttk.Label(self, text="Player"+str(turn)+"'s Turn")
        label1["font"] = "TkHeadingFont"
        label1.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="How many beans will you take?")
        label2.pack(pady=10,padx=10)

        buttonFrame = ttk.Frame(self)

        button1Bean = ttk.Button(buttonFrame, text="1", command=lambda: controller.pick_beans(self, 1, PageTwo))
        button2Bean = ttk.Button(buttonFrame, text="2", command=lambda: controller.pick_beans(self, 2, PageTwo))
        button3Bean = ttk.Button(buttonFrame, text="3", command=lambda: controller.pick_beans(self, 3, PageTwo))


        button1Bean.grid(row=0, column=0)
        button2Bean.grid(row=0, column=1)
        button3Bean.grid(row=0, column=2)

        buttonFrame.pack(pady=10, padx=10)

        buttonCPU = ttk.Button(self, text="Let the CPU decide",
                            command=lambda: controller.cpu(PageTwo))
        buttonCPU.pack(pady=20,padx=10)

        #data=(1,2,3)
        #cb = Combobox(self, values=data)
        #cb.pack(pady=10,padx=10)
        button2 = ttk.Button(self, text="Continue",  #IF NO BEANS SHOW EndPage
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20,padx=10)

        # if totalBeans == 0:
        #     button2.state(["!disabled"])
        # else:
        #     button2.state(["disabled"])
        
    

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
