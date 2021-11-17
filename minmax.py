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

    def caclulateMinMax(self, node: mmNode = None):
        if not node:
            node = self.root
        nodeL = mmNode(self.key+1, node.value-1, node)
        nodeC = mmNode(self.key+2, node.value-2, node)
        nodeR = mmNode(self.key+3, node.value-3, node)
        self.key += 3
        self.addNode(nodeL, node)
        self.addNode(nodeC, node)
        self.addNode(nodeR, node)
        self.caclulateMinMax(nodeL)
        self.caclulateMinMax(nodeC)
        self.caclulateMinMax(nodeR)
