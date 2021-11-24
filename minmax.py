from dataclasses import dataclass

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

        print(node.value)

        NodeR = None
        NodeC = None
        NodeL = None

        if node.value > 3:
            NodeR = mmNode(node.value-3, node)
        if node.value > 2:
            NodeC = mmNode(node.value-2, node)
        NodeL = mmNode(node.value-1, node)
        if NodeL.value > 0:
            self.addNode(NodeL, node)
        if NodeC:
            self.addNode(NodeC, node)
        if NodeR:
            self.addNode(NodeR, node)
        if NodeL.value > 0:
            self.calculateMinMax(NodeL)
        if NodeC and NodeC.value > 0:
            self.calculateMinMax(NodeC)
        if NodeR and NodeR.value > 0:
            self.calculateMinMax(NodeR)

        if node.value == 1:
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

mmTree(mmNode(4))