def dfsRecursive(n):
    if n is None:
        return Node
    # #preorder
    # print(n.val)
    # dfsRecursive(n.left)
    # dfsRecursive(n.right)
    # #inorder
    # dfsRecursive(n.left)
    # print(n.val)
    # dfsRecursive(n.right)
    # #postorder
    dfsRecursive(n.left)
    dfsRecursive(n.right)
    print(n.val)

def dfsIterative(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Driver Code
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(4)
    root.right = Node(17)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    # root.right.right = Node(22)
    # root.right.right.left = Node(20)
    k = 18
    print(dfsIterative(root))
