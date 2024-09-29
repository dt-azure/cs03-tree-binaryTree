class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findDepth(root, node):
    if root == None:
        return -1
    
    depth = -1
    
    if root == node:
        return depth + 1
    
    depth = findDepth(root.left, node)
    if depth >= 0:
        return depth + 1
    
    depth = findDepth(root.right, node)
    if depth >= 0:
        return depth + 1
    
    return depth

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')

nodeA.left = nodeB
nodeA.right = nodeC

nodeB.left = nodeD
nodeB.right = nodeE

nodeC.left = nodeF
nodeC.right = nodeG

print("Depth of node A (root): ", findDepth(nodeA, nodeA))
print("Depth of node B: ", findDepth(nodeA, nodeB))
print("Depth of node F: ", findDepth(nodeA, nodeF))