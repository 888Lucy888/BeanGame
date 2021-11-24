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

        print("UWU")
        print(self.root.blues)
        print(self.root.reds)


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

        print("AAAA")
        print(node.value)

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
frijoles= 21 #a 25
turno= False

print("Elige el numero de frijoles")
frijoles= int(input())

#Crear arbol
arbol= mmTree(mmNode(frijoles))

print("Jugador 1 ->  Dificultad del 1 al 10")
dificultad1= int(input())
print("Jugador 2 ->  Dificultad del 1 al 10")
dificultad2= int(input())

actualNodo= arbol.root #Nodo hijo de la raiz

while True:
  if frijoles == 0:
    if turno:
      print("Gana jugador 2")
    else:
      print("Gana jugador 1")
    break

  print(frijoles)

  camino= 0

  print("Seleccione 1 si quiere que que la maquina escoja y 0 si usted quiere elegir")
  auto= input()

  #Modo Maquina
  if int(auto) == 1:
    if turno:
      dificultad= dificultad1
    else:
      dificultad= dificultad2

    probabilidad= randint(1,10)
    if frijoles == 1:
      camino= 1
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
      
    else:
      print("Eligio bien")
      if actualNodo.children[0].blue == turno:
        print("Toma camino correcto" + str(actualNodo.children[1].blue) + str(actualNodo.children[1].value))
        camino= 1
        actualNodo= actualNodo.children[0]
      elif actualNodo.children[1] and actualNodo.children[1].blue == turno:
        print("Toma camino correcto")
        camino= 2
        actualNodo= actualNodo.children[1]
      elif actualNodo.children[2] and actualNodo.children[2].blue == turno:
        print("Toma camino correcto")
        camino= 3
        actualNodo= actualNodo.children[2]
      else:
        print("Toma camino incorrecto")
        camino= 1
        actualNodo= actualNodo.children[0]

  #Modo jugador
  else:
    if frijoles >= 3:
      print("Escoge entre 1 y 3 frijolitos")
    elif frijoles >= 2:
      print("Escoge entre 1 y 2 frijolitos")
    else:
      print("Toma tu frijol")
    camino= input() #Decision del jugador

  frijoles-= int(camino)
  #Intercambiar jugadores
  turno = not turno