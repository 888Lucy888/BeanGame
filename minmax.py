from dataclasses import dataclass

@dataclass
class mmNode:
    pass

@dataclass
class mmNode:
    key: int
    value: int
    parent: mmNode = None
    children: list = None
    blue: bool = False

class mmTree:
    
    def __init__(self, root: mmNode):
        self.root = root
        self.keyI = root.key

    def addNode(self, node: mmNode, parentNode: mmNode = None) -> None:
        if not parentNode:
            parentNode = self.root
        if len(parentNode.children) < 3:
            parentNode.children.append(node)

    def calculateMinMax(self, node: mmNode = None):
        if not node:
            node = self.root

        NodeR = None
        NodeC = None
        NodeL = None

        if node.value > 2:
            nodeR = mmNode(self.keyI+3, node.value-3, node)
        if node.value > 1:
            nodeC = mmNode(self.keyI+2, node.value-2, node)
        nodeL = mmNode(self.keyI+1, node.value-1, node)
        self.keyI += 3
        self.addNode(nodeL, node)
        if NodeC:
            self.addNode(nodeC, node)
        if NodeR:
            self.addNode(nodeR, node)
        if NodeL > 0:
            self.calculateMinMax(nodeL)
        if NodeC and NodeC.value > 0:
            self.calculateMinMax(nodeC)
        if NodeR and NodeR.value > 0:
            self.calculateMinMax(nodeR)
