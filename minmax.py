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
    blue: bool = False #Blue = Player 1 victory -- Red = Player 2 victory

class mmTree:
    
    def __init__(self, root: mmNode):
        self.root = root
        self.keyI = root.key

    def addNode(self, node: mmNode, parentNode: mmNode = None) -> None:
        if not parentNode:
            parentNode = self.root
        if len(parentNode.children) < 3:
            parentNode.children.append(node)

    def depth(self, node):
        count = 0
        while node != self.root:
            count += 1
            node = node.father
        return count - 1

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
        if NodeL.value > 0:
            self.calculateMinMax(nodeL)
        if NodeC and NodeC.value > 0:
            self.calculateMinMax(nodeC)
        if NodeR and NodeR.value > 0:
            self.calculateMinMax(nodeR)

        if node.value == 0:
            depth = self.depth(node)
            # Player 1 will have even depth
            # For example... first turn beans equal to node on height 0
            # This means player 2 will have the odd depths
            if depth % 2 != 0:
                # This means player 2 has no beans to grab, which means
                # Player 1 grabbed the last one, victory for Player 2
                # Long live PLayer 2
                node.blue = False
            else:
                node.blue = True
