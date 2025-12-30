class  Node:
    def __init__(self,d):
        self.val = d
        self.left = None
        self.right = None

#In-Order-Traversal, from left-subtree -> root-node-right-subtree using Recursion.
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.val, end=" ")
    inOrderTraversal(node.right)

#Pre-Order-Traversal, from Root-node -> Left-subtree -> Right-subtree
def preOrderTraversal(node):
    if node is None:
        return 
    print(node.val,end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

#Post-Order-Traversal, from Left-subtree -> Right-subtree -> Root-node
def postOrderTraversal(node):
    if node is None:
        return 
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.val,end=" ")
    
#EXAMPLE
firstNode  = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)
fifthNode = Node(5)

# Build full example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5


firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
secondNode.right = fifthNode

print("\nPreorder Traversal:")
preOrderTraversal(firstNode)

print("\nInorder Traversal:")    
inOrderTraversal(firstNode)

print("\nPostorder Traversal:")    
postOrderTraversal(firstNode)